package main

import (
	"github.com/hashicorp/go-plugin"

	"go.opentelemetry.io/collector/example_plugins/simple_go"
	"go.opentelemetry.io/collector/receiver/pluginreceiver/plugindef"
)

func main() {
	plugin.Serve(&plugin.ServeConfig{
		HandshakeConfig: plugindef.HandshakeConfig,
		Plugins: map[string]plugin.Plugin{
			"receiver": &plugindef.ReceiverGRPCPlugin{Impl: &simple_go.SimplePlugin{}},
		},

		// A non-nil value here enables gRPC serving for this plugin...
		GRPCServer: plugin.DefaultGRPCServer,
	})
}
