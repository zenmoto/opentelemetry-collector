package simplereceiverhelper

import (
	"context"

	"go.opentelemetry.io/collector/component"
	"go.opentelemetry.io/collector/config"
	"go.opentelemetry.io/collector/consumer"
	"go.opentelemetry.io/collector/receiver/pluginreceiver"
	"go.opentelemetry.io/collector/receiver/pluginreceiver/plugindef"
	"go.opentelemetry.io/collector/receiver/receiverhelper"
)

func NewSimpleReceiverFactory(typeString string, p plugindef.Receiver) component.ReceiverFactory {
	r := NewPluginReceiverManager(p)
	return receiverhelper.NewFactory(
		config.Type(typeString),
		createDefaultConfigProducer(typeString),
		receiverhelper.WithLogs(r.createLogReceiver),
		receiverhelper.WithMetrics(r.createMetricsReceiver),
		receiverhelper.WithTraces(r.createTracesReceiver))
}

// TODO: Currently just recreating the receiver for every pipeline, should be combined like in oltp receiver
func (p *combinedPluginReceiverManager) createLogReceiver(ctx context.Context, settings component.ReceiverCreateSettings, c config.Receiver, sink consumer.Logs) (component.LogsReceiver, error) {
	r, err := p.getOrCreateReceiver(c)
	if err != nil {
		return nil, err
	}
	r.consumer.Logs = sink
	return r, nil
}

func (p *combinedPluginReceiverManager) createTracesReceiver(ctx context.Context, settings component.ReceiverCreateSettings, c config.Receiver, sink consumer.Traces) (component.TracesReceiver, error) {
	r, err := p.getOrCreateReceiver(c)
	if err != nil {
		return nil, err
	}
	r.consumer.Traces = sink
	return r, nil
}

func (p *combinedPluginReceiverManager) createMetricsReceiver(ctx context.Context, settings component.ReceiverCreateSettings, c config.Receiver, sink consumer.Metrics) (component.MetricsReceiver, error) {
	r, err := p.getOrCreateReceiver(c)
	if err != nil {
		return nil, err
	}
	r.consumer.Metrics = sink
	return r, nil
}

type combinedPluginReceiverManager struct {
	plugin    plugindef.Receiver
	receivers map[config.ComponentID]*combinedPluginReceiver
}

func (m *combinedPluginReceiverManager) getOrCreateReceiver(c config.Receiver) (*combinedPluginReceiver, error) {
	r, found := m.receivers[c.ID()]
	if !found {
		r = newCombinedPluginReceiver(m.plugin, c)
		m.receivers[c.ID()] = r
	}
	return r, nil
}

func newCombinedPluginReceiver(p plugindef.Receiver, baseConfig config.Receiver) *combinedPluginReceiver {
	c := baseConfig.(*Config)
	return &combinedPluginReceiver{plugin: p, config: c, consumer: &pluginreceiver.ReceiverSignalConsumer{}}

}

type combinedPluginReceiver struct {
	plugin   plugindef.Receiver
	config   *Config
	consumer *pluginreceiver.ReceiverSignalConsumer
}

func (r *combinedPluginReceiver) Shutdown(ctx context.Context) error {
	// TODO: Plugin should support lifecycle commands, I've built this prototype so it cantstopwontstop
	return nil
}

func (r *combinedPluginReceiver) Start(ctx context.Context, host component.Host) error {
	go r.plugin.Run(r.consumer, r.config.Values)
	return nil
}

func NewPluginReceiverManager(p plugindef.Receiver) *combinedPluginReceiverManager {
	return &combinedPluginReceiverManager{plugin: p, receivers: make(map[config.ComponentID]*combinedPluginReceiver)}
}
