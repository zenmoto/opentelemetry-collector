// Copyright  The OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package plugindef

import (
	"context"
	"io"

	"github.com/hashicorp/go-plugin"
	"go.opentelemetry.io/collector/consumer"
	"go.opentelemetry.io/collector/model/otlp"
	"go.opentelemetry.io/collector/model/pdata"
	"go.opentelemetry.io/collector/receiver/pluginreceiver/proto"
)

type GRPCClient struct {
	client          proto.PluginServiceClient
	unmarshaller    SignalUnmarshaller
	metricsConsumer consumer.Metrics
	logsConsumer    consumer.Logs
	tracesConsumer  consumer.Traces
}

func (c *GRPCClient) Run() {
	runClient, _ := c.client.Run(context.Background(), &proto.PluginRequest{})
	for {
		msg, err := runClient.Recv()
		if err == io.EOF {
			break
		}
		ctx := context.Background()
		switch msg.Type {
		case proto.PluginResponse_METRIC:
			c.metricsConsumer.ConsumeMetrics(ctx, c.unmarshaller.UnmarshalMetrics(msg.Data))
		case proto.PluginResponse_LOG:
			c.logsConsumer.ConsumeLogs(ctx, c.unmarshaller.UnmarshalLogs(msg.Data))
		case proto.PluginResponse_TRACE:
			c.tracesConsumer.ConsumeTraces(ctx, c.unmarshaller.UnmarshalTraces(msg.Data))
		}
	}
}

type SignalUnmarshaller struct {
	logs    pdata.LogsUnmarshaler
	traces  pdata.TracesUnmarshaler
	metrics pdata.MetricsUnmarshaler
}

func (u *SignalUnmarshaller) UnmarshalMetrics(data []byte) pdata.Metrics {
	metrics, _ := u.metrics.UnmarshalMetrics(data)
	return metrics
}

func (u *SignalUnmarshaller) UnmarshalTraces(data []byte) pdata.Traces {
	traces, _ := u.traces.UnmarshalTraces(data)
	return traces
}

func (u *SignalUnmarshaller) UnmarshalLogs(data []byte) pdata.Logs {
	logs, _ := u.logs.UnmarshalLogs(data)
	return logs
}

type GRPCServer struct {
	proto.UnimplementedPluginServiceServer
	Impl Receiver
}

func (s *GRPCServer) Run(in *proto.PluginRequest, out *proto.PluginService_RunServer) {
	consumer := &SerializingSignalConsumer{
		out:               *out,
		logsMarshaller:    otlp.NewProtobufLogsMarshaler(),
		tracesMarshaller:  otlp.NewProtobufTracesMarshaler(),
		metricsMarshaller: otlp.NewProtobufMetricsMarshaler(),
	}
	s.Impl.Run(consumer)
}

var HandshakeConfig = plugin.HandshakeConfig{
	ProtocolVersion:  1,
	MagicCookieKey:   "ReceiverPlugin",
	MagicCookieValue: "1",
}

type SerializingSignalConsumer struct {
	logsMarshaller    pdata.LogsMarshaler
	tracesMarshaller  pdata.TracesMarshaler
	metricsMarshaller pdata.MetricsMarshaler
	out               proto.PluginService_RunServer
}

func (c *SerializingSignalConsumer) Capabilities() consumer.Capabilities {
	return consumer.Capabilities{MutatesData: false}
}

func (c *SerializingSignalConsumer) ConsumeLogs(ctx context.Context, logs pdata.Logs) error {
	bytes, err := c.logsMarshaller.MarshalLogs(logs)
	if err != nil {
		return err
	}
	resp := &proto.PluginResponse{
		Type: proto.PluginResponse_LOG,
		Data: bytes,
	}
	c.out.Send(resp)
	return nil
}

func (c *SerializingSignalConsumer) ConsumeMetrics(ctx context.Context, metrics pdata.Metrics) error {
	bytes, err := c.metricsMarshaller.MarshalMetrics(metrics)
	if err != nil {
		return err
	}
	resp := &proto.PluginResponse{
		Type: proto.PluginResponse_METRIC,
		Data: bytes,
	}
	c.out.Send(resp)
	return nil
}

func (c *SerializingSignalConsumer) ConsumeTraces(ctx context.Context, traces pdata.Traces) error {
	bytes, err := c.tracesMarshaller.MarshalTraces(traces)
	if err != nil {
		return err
	}
	resp := &proto.PluginResponse{
		Type: proto.PluginResponse_TRACE,
		Data: bytes,
	}
	c.out.Send(resp)
	return nil
}
