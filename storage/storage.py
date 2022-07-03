import json
import grpc
import storage_pb2
import storage_pb2_grpc
import yaml

from concurrent import futures
from engine import Engine
from loguru import logger
from network import Network
from queue import Queue
from snapshot import SnapshotEngine
from threading import Event


class StorageEngineServicer(Engine, storage_pb2_grpc.StorageServicer):
    def __init__(self, network: Network, sync_queue: Queue) -> None:
        super().__init__(network, sync_queue)

    def Store(self, request, context):
        logger.debug(f'serviceName={request.serviceName} traceid={request.traceID} spanid={request.spanID}')
        
        self._network.add_span(request.serviceName, request.traceID, request)
        self._queue.put(request.serviceName)

        return storage_pb2.StorageResponse(status=200, message='DEBUG')

    def GetServices(self, request, context):
        logger.debug('GetServices')
        for service_name in self._network._services.keys():
            yield storage_pb2.ServiceName(name=service_name)

    def GetServiceData(self, request, context):
        service_data = self._network.get_service_data(request.name)

        service_processed = {}
        span_list = list(filter(lambda data: data['tag'] == 2, service_data['nodes']))
        data_with_spans = {}
        for span in span_list:
            trace_id = span['data']['traceID']
            span_id = span['id']

            if trace_id not in data_with_spans:
                data_with_spans[trace_id] = {span_id: span['data']}
            else:
                data_with_spans[trace_id][span_id] = span['data']

            if trace_id not in service_processed:
                service_processed[trace_id] = [span['data']]
            else:
                service_processed[trace_id].append(span['data'])

        with open('service_data.json', 'w') as fo:
            json.dump(service_processed, fo, indent=4)

        for trace_id, spans in service_processed.items():
            logs = [storage_pb2.StorageKeyValue(type=log['type'], value=log['value']) for log in span['data']['logs']]
            spans = [storage_pb2.StorageSpan(logs=logs, spanID=span['spanID'], spanName=span['spanName'], parentSpanID=span['parentSpanID']) for span in spans]
            yield storage_pb2.ServiceResponse(traceId=trace_id, spans=spans)

    def GetMultipleServicesData(self, request_iterator, context):
        return super().GetMultipleServicesData(request_iterator, context)

    def GetData(self, request, context):
        return super().GetData(request, context)

if __name__ == '__main__':
    config_path = 'storage/config/storage.yml'
    fo = open(config_path, 'r')
    config = yaml.load(fo.read(), yaml.SafeLoader)
    fo.close()

    network = Network()
    event, sync_queue = Event(), Queue()

    storage_engine = StorageEngineServicer(network, sync_queue)
    snapshot_engine = SnapshotEngine(network, sync_queue, event, config['snapshot']['path'])
    snapshot_engine.start()

    host = config['server']['host']
    port = int(config['server']['port'])
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    storage_pb2_grpc.add_StorageServicer_to_server(storage_engine, server)
    server.add_insecure_port(f'{host}:{port}')
    
    try:
        logger.debug(f'Starting gRPC server on {host}:{port}')
        server.start()
        server.wait_for_termination()
    except:
        event.set()
        snapshot_engine.join()
