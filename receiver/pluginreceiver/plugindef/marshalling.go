package plugindef

import (
	"context"
	"fmt"

	"go.opentelemetry.io/collector/consumer"
	"go.opentelemetry.io/collector/model/otlp"
	"go.opentelemetry.io/collector/model/pdata"
	"go.opentelemetry.io/collector/receiver/pluginreceiver/proto"
)

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
	fmt.Printf("xx: %+v", bytes)
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

type SignalUnmarshaller struct {
	logs    pdata.LogsUnmarshaler
	traces  pdata.TracesUnmarshaler
	metrics pdata.MetricsUnmarshaler
}

func NewSignalUnmarshaller() SignalUnmarshaller {
	return SignalUnmarshaller{
		logs:    otlp.NewProtobufLogsUnmarshaler(),
		traces:  otlp.NewProtobufTracesUnmarshaler(),
		metrics: otlp.NewProtobufMetricsUnmarshaler(),
	}
}

func (u *SignalUnmarshaller) UnmarshalMetrics(data []byte) pdata.Metrics {
	metrics, err := u.metrics.UnmarshalMetrics(data)
	if err != nil {
		panic(err)
	}
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
