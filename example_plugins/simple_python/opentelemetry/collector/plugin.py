import grpc

import grpc_health.v1.health_pb2_grpc as health_pb2_grpc
import grpc_health.v1.health_pb2 as health_pb2
from grpc_health.v1.health import HealthServicer
from concurrent import futures
import opentelemetry.collector.plugin_pb2_grpc as plugin_grpc
import opentelemetry.collector.plugin_pb2 as pbplugin
import sys
import opentelemetry.proto.metrics.v1.metrics_pb2 as pmetrics

import debugpy
debugpy.listen(5678)

def build_response(metric):
    resp = pbplugin.PluginResponse()
    resp.type = resp.METRIC
    resp.data = metric.SerializeToString()
    return resp

class MetricsBuilder(object):
    def gauge(self, name, description, value, units="1"):
        m = pmetrics.Metric()
        m.name = name
        m.description = description
        dp = pmetrics.NumberDataPoint()
        dp.as_int = value
        m.gauge.data_points.append(dp)
        ilm = pmetrics.InstrumentationLibraryMetrics()
        ilm.metrics.append( m )
        rm = pmetrics.ResourceMetrics()
        rm.instrumentation_library_metrics.append( ilm )
        md = pmetrics.MetricsData()
        md.resource_metrics.append( rm )
        return md


class Builder(object):
    def __init__(self) -> None:
        self.metrics = MetricsBuilder()

class PluginServicer(plugin_grpc.PluginServiceServicer):
    def __init__(self, plugin):
        self.plugin = plugin

    def run(self, request, context):
        return ( build_response(m) for m in self.plugin.run(request.config.values, Builder()) )

    def start(self):
        pass


class Sink(object):
    def __init__(self):
        pass
        
    def add_gauge(self, name, description, value):
        dp = pmetrics.IntDataPoint()
        dp.value = value
        g = pmetrics.IntGauge()
        g.data_points = [dp]
        m = pmetrics.Metric()
        m.name = name
        m.description = description
        m.int_gauge = g
        ilm = pmetrics.InstrumentationLibraryMetrics()
        ilm.metrics = [m]
        rm = pmetrics.ResourceMetrics()
        rm.instrumentation_library_metrics = [ilm]
        md = pmetrics.MetricsData()
        md.resource_metrics = [rm]




class Plugin(object):
    def run(self, config, sink):
        raise NotImplementedError('Method not implemented!')

    def execute(self):
        health = HealthServicer()
        health.set(
            "plugin", health_pb2.HealthCheckResponse.ServingStatus.Value('SERVING'))

        # Start the server.
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        plugin_grpc.add_PluginServiceServicer_to_server(
            PluginServicer(self), server)
        health_pb2_grpc.add_HealthServicer_to_server(health, server)
        server.add_insecure_port('127.0.0.1:1234')
        server.start()

        # Output information
        print("1|1|tcp|127.0.0.1:1234|grpc")
        sys.stdout.flush()
        server.wait_for_termination()
