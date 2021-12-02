package simple_go

import (
	"context"
	"time"

	"go.opentelemetry.io/collector/model/pdata"
	"go.opentelemetry.io/collector/receiver/pluginreceiver/plugindef"
)

type SimplePlugin struct{}

func (s *SimplePlugin) Run(sink plugindef.SignalConsumer) {
	for i := 0; true; i++ {
		ms := pdata.NewMetrics()
		rm := ms.ResourceMetrics()
		ilm := rm.AppendEmpty().InstrumentationLibraryMetrics()
		m := ilm.AppendEmpty().Metrics().AppendEmpty()
		m.SetDataType(pdata.MetricDataTypeSum)
		m.SetName("a.metric.example")
		m.SetUnit("1")
		sum := m.Sum()
		sum.SetIsMonotonic(true)
		dp := sum.DataPoints().AppendEmpty()
		dp.SetIntVal(int64(i))
		sink.ConsumeMetrics(context.Background(), ms)
		time.Sleep(2 * time.Second)
	}
}

func (s *SimplePlugin) Start() {

}
