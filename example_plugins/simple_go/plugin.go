package simple_go

import (
	"context"

	"go.opentelemetry.io/collector/model/pdata"
	"go.opentelemetry.io/collector/receiver/pluginreceiver/plugindef"
)

type SimplePlugin struct{}

func (s *SimplePlugin) Run(sink plugindef.SignalConsumer) {
	ms := pdata.NewMetrics()
	rm := ms.ResourceMetrics()
	ilm := rm.AppendEmpty().InstrumentationLibraryMetrics()
	m := ilm.AppendEmpty().Metrics().AppendEmpty()
	m.SetName("a.metric.example")
	m.SetUnit("1")
	sum := m.Sum()
	sum.SetIsMonotonic(true)
	dp := sum.DataPoints().AppendEmpty()
	dp.SetIntVal(1)
	sink.ConsumeMetrics(context.Background(), ms)
}

func (s *SimplePlugin) Start() {

}
