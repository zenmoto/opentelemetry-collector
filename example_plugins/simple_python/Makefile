bin/open_telemetry_collector:
	mkdir -p bin/open_telemetry_collector

bin/open_telemetry_collector/plugin_pb2.py bin/open_telemetry_collector/plugin_pb2_grpc.py: bin/open_telemetry_collector
	python3 -m grpc_tools.protoc -I ../../receiver/pluginreceiver/proto --python_out=bin/open_telemetry_collector --grpc_python_out=bin/open_telemetry_collector ../../receiver/pluginreceiver/proto/plugin.proto

build: bin/open_telemetry_collector/plugin_pb2_grpc.py

.PHONY=run
run: build
	../../bin/cmd-otelcol --config collector.yml