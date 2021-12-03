package simplereceiverhelper

import (
	"go.opentelemetry.io/collector/config"
)

type Config struct {
	config.ReceiverSettings `mapstructure:",squash"`
	// TODO: this is a placeholder for a real config
	Values map[string]string `mapstructure:"config"`
}

func createDefaultConfigProducer(typeStr string) func() config.Receiver {
	return func() config.Receiver {
		return &Config{
			ReceiverSettings: config.NewReceiverSettings(config.NewComponentID(config.Type(typeStr))),
			Values:           make(map[string]string),
		}
	}
}
