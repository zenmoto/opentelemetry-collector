package plugindef

import "go.opentelemetry.io/collector/consumer"

type SignalConsumer interface {
	consumer.Logs
	consumer.Metrics
	consumer.Logs
}

type Receiver interface {
	Start()
	Run(sink SignalConsumer)
}
