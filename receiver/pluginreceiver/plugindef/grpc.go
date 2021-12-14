package plugindef

import (
	"context"
	"io"

	"go.opentelemetry.io/collector/model/otlp"
	"go.opentelemetry.io/collector/receiver/pluginreceiver/proto"
)

func NewGRPCClient(client proto.PluginServiceClient) *GRPCClient {
	return &GRPCClient{
		client:       client,
		unmarshaller: NewSignalUnmarshaller(),
	}

}

type GRPCClient struct {
	client       proto.PluginServiceClient
	unmarshaller SignalUnmarshaller
}

func (c *GRPCClient) Run(sink SignalConsumer, config map[string]string) {
	runClient, _ := c.client.Run(context.Background(), &proto.PluginRequest{Config: &proto.Config{Values: config}})
	for {
		msg, err := runClient.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			panic(err)
		}
		ctx := context.Background()
		switch msg.Type {
		case proto.PluginResponse_METRIC:
			m := c.unmarshaller.UnmarshalMetrics(msg.GetData())
			// x := m.ResourceMetrics().At(0).InstrumentationLibraryMetrics().At(0).Metrics().At(0)
			// fmt.Printf("%+v (%+v): %+v\n", x.Name(), x.DataType(), x.Sum().DataPoints().At(0).IntVal())
			sink.ConsumeMetrics(ctx, m)
		case proto.PluginResponse_LOG:
			sink.ConsumeLogs(ctx, c.unmarshaller.UnmarshalLogs(msg.Data))
		case proto.PluginResponse_TRACE:
			sink.ConsumeTraces(ctx, c.unmarshaller.UnmarshalTraces(msg.Data))
		}
	}
}

type GRPCServer struct {
	proto.UnimplementedPluginServiceServer
	Impl Receiver
}

func (s *GRPCServer) Run(in *proto.PluginRequest, out proto.PluginService_RunServer) error {
	consumer := &SerializingSignalConsumer{
		out:               out,
		logsMarshaller:    otlp.NewProtobufLogsMarshaler(),
		tracesMarshaller:  otlp.NewProtobufTracesMarshaler(),
		metricsMarshaller: otlp.NewProtobufMetricsMarshaler(),
	}
	s.Impl.Run(consumer, in.Config.Values)
	return nil
}