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
	"net/rpc"

	"github.com/hashicorp/go-plugin"
	"go.opentelemetry.io/collector/model/pdata"
	"go.opentelemetry.io/collector/receiver/pluginreceiver/proto"
)

type ReceiverRPC struct{ client *rpc.Client }

func (g *ReceiverRPC) Start() {
	err := g.client.Call("Plugin.Start", new(interface{}), nil)
	if err != nil {
		panic(err)
	}
}

// Here is the RPC server that ReceiverRPC talks to, conforming to
// the requirements of net/rpc
type ReceiverRPCServer struct {
	// This is the real implementation
	Impl Receiver
}

type ReceiverPlugin struct {
	Impl Receiver
}

func (p *ReceiverPlugin) Server(*plugin.MuxBroker) (interface{}, error) {
	return &ReceiverRPCServer{Impl: p.Impl}, nil
}

func (ReceiverPlugin) Client(b *plugin.MuxBroker, c *rpc.Client) (interface{}, error) {
	return &ReceiverRPC{client: c}, nil
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

func (c *SerializingSignalConsumer) ConsumeLogs(ctx context.Context, logs pdata.Logs) {
	bytes, _ := c.logsMarshaller.MarshalLogs(logs)
	resp := &proto.PluginResponse{
		Type: proto.PluginResponse_LOG,
		Data: bytes,
	}
	c.out.Send(resp)
}

func (c *SerializingSignalConsumer) ConsumeMetrics(ctx context.Context, metrics pdata.Metrics) {
	bytes, _ := c.metricsMarshaller.MarshalMetrics(metrics)
	resp := &proto.PluginResponse{
		Type: proto.PluginResponse_METRIC,
		Data: bytes,
	}
	c.out.Send(resp)
}

func (c *SerializingSignalConsumer) ConsumeTraces(ctx context.Context, traces pdata.Traces) {
	bytes, _ := c.tracesMarshaller.MarshalTraces(traces)
	resp := &proto.PluginResponse{
		Type: proto.PluginResponse_TRACE,
		Data: bytes,
	}
	c.out.Send(resp)
}
