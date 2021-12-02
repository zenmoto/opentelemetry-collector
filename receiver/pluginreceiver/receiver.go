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

package pluginreceiver

import (
	"context"
	"fmt"
	"os/exec"

	"github.com/hashicorp/go-plugin"

	"go.opentelemetry.io/collector/component"
	"go.opentelemetry.io/collector/consumer"
	"go.opentelemetry.io/collector/receiver/pluginreceiver/plugindef"
)

type receiverSignalConsumer struct {
	consumer.Logs
	consumer.Metrics
	consumer.Traces
}

func (p *receiverSignalConsumer) Capabilities() consumer.Capabilities {
	return consumer.Capabilities{}
}

func newPluginReceiver(cfg *Config, settings component.ReceiverCreateSettings) *pluginReceiver {
	return &pluginReceiver{config: cfg, settings: settings, consumer: &receiverSignalConsumer{}}
}

type pluginReceiver struct {
	config   *Config
	settings component.ReceiverCreateSettings
	consumer *receiverSignalConsumer
	// logsConsumer    consumer.Logs
	// tracesConsumer  consumer.Traces
	// metricsConsumer consumer.Metrics
}

func (p *pluginReceiver) registerLogsConsumer(c consumer.Logs) error {
	p.consumer.Logs = c
	return nil
}

func (p *pluginReceiver) registerTraceConsumer(c consumer.Traces) error {
	p.consumer.Traces = c
	return nil
}

func (p *pluginReceiver) registerMetricsConsumer(c consumer.Metrics) error {
	p.consumer.Metrics = c
	return nil
}

func (p *pluginReceiver) Start(ctx context.Context, host component.Host) error {
	// We're a host! Start by launching the plugin process.
	client := plugin.NewClient(p.buildClientConfig())
	defer client.Kill()

	// Connect via RPC
	rpcClient, err := client.Client()
	if err != nil {
		panic(err)
	}

	// Request the plugin
	raw, err := rpcClient.Dispense("receiver")
	if err != nil {
		fmt.Println("Error in dispense")
		panic(err)
	}

	plugin := raw.(plugindef.Receiver)
	plugin.Run(p.consumer)
	return nil
}

func (p *pluginReceiver) buildClientConfig() *plugin.ClientConfig {
	return &plugin.ClientConfig{
		HandshakeConfig: plugindef.HandshakeConfig,
		Plugins:         pluginMap,
		Cmd:             exec.Command(p.config.Executable),
		AllowedProtocols: []plugin.Protocol{
			plugin.ProtocolGRPC},
	}
}

func (p *pluginReceiver) Shutdown(ctx context.Context) error {
	return nil
}

var pluginMap = map[string]plugin.Plugin{
	"receiver": &plugindef.ReceiverGRPCPlugin{},
}
