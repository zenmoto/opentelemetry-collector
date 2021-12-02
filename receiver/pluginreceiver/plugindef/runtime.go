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

package plugindef

import (
	"context"

	"github.com/hashicorp/go-plugin"
	"go.opentelemetry.io/collector/receiver/pluginreceiver/proto"
	"google.golang.org/grpc"
)

type ReceiverGRPCPlugin struct {
	plugin.NetRPCUnsupportedPlugin
	Impl Receiver
}

func (p *ReceiverGRPCPlugin) GRPCServer(broker *plugin.GRPCBroker, s *grpc.Server) error {
	proto.RegisterPluginServiceServer(s, &GRPCServer{Impl: p.Impl})
	return nil
}

func (p *ReceiverGRPCPlugin) GRPCClient(ctx context.Context, broker *plugin.GRPCBroker, c *grpc.ClientConn) (interface{}, error) {
	return NewGRPCClient(proto.NewPluginServiceClient(c)), nil
}

var HandshakeConfig = plugin.HandshakeConfig{
	ProtocolVersion:  1,
	MagicCookieKey:   "ReceiverPlugin",
	MagicCookieValue: "1",
}
