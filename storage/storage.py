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


class StorageEngineServicer(Engine, storage_pb2_grpc.StorageServicer):
    def __init__(self, network: Network, sync_queue: Queue) -> None:
        super().__init__(network, sync_queue)

    def Store(self, request, context):
        logger.debug(f'serviceName={request.serviceName} traceid={request.traceID} spanid={request.spanID}')
        
        self._network.add_span(request.serviceName, request.traceID, request)
        self._queue.put(request.serviceName)

        return storage_pb2.StorageResponse(status=200, message='DEBUG')

if __name__ == '__main__':
    config_path = 'storage/config/storage.yml'
    fo = open(config_path, 'r')
    config = yaml.load(fo.read(), yaml.SafeLoader)
    fo.close()

    network = Network()
    sync_queue = Queue()

    storage_engine = StorageEngineServicer(network, sync_queue)
    
    snapshot_engine = SnapshotEngine(network, sync_queue, config['snapshot']['path'])
    snapshot_engine.start()

    host = config['server']['host']
    port = int(config['server']['port'])
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    storage_pb2_grpc.add_StorageServicer_to_server(storage_engine, server)
    server.add_insecure_port(f'{host}:{port}')
    
    logger.debug(f'Starting gRPC server on {host}:{port}')
    server.start()
    server.wait_for_termination()
