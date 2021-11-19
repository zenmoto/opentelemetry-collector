// Copyright The OpenTelemetry Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package pluginreceiver // import "go.opentelemetry.io/collector/receiver/otlpreceiver"

import (
	"fmt"

	"go.opentelemetry.io/collector/config"
)

// Config defines configuration for OTLP receiver.
type Config struct {
	config.ReceiverSettings `mapstructure:",squash"` // squash ensures fields are correctly decoded in embedded struct
	// Protocols is the configuration for the supported protocols, currently gRPC and HTTP (Proto and JSON).
	Executable string `mapstructure:"executable"`
}

var _ config.Receiver = (*Config)(nil)

// Validate checks the receiver configuration is valid
func (cfg *Config) Validate() error {
	if cfg.Executable == "" {
		// TODO: Ensure plugin exists
		return fmt.Errorf("executable not specified")
	}
	return nil
}
