#!/usr/bin/env python3

import time
from opentelemetry.collector import plugin

class ExamplePlugin(plugin.Plugin):
    def run(self, config, builder):
        i = 0 
        while True:
            i += 1
            yield builder.metrics.gauge(f"example.python.{config['metric_name']}", "An example metric", i, units='{loops}')
            time.sleep(1)

if __name__ == '__main__':
    ExamplePlugin().execute() 