run: bin/example_plugin
	../../bin/cmd-otelcol --config ./collector.yml

../../bin/cmd-otelcol:
	pushd ../../ && make build-binary-cmd-otelcol && popd

bin/example_plugin: ../../bin/cmd-otelcol
	mkdir -p bin
	go build -o bin/example_plugin ./cmd/example.go

.PHONY = build
build: bin/example_plugin

.PHONY = cleanup
clean:
	rm -rf bin/
