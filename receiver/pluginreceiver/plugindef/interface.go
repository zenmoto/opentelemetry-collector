package plugindef

import "go.opentelemetry.io/collector/consumer"

type SignalConsumer interface {
	consumer.Logs
	consumer.Metrics
	consumer.Traces
}

type Receiver interface {
	// Start()
	Run(sink SignalConsumer, config map[string]string)
}
