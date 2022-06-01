import sys
import grpc
import storage_pb2
import storage_pb2_grpc

from concurrent import futures
from loguru import logger

class StorageServicer(storage_pb2_grpc.StorageServicer):
    def __init__(self) -> None:
        super().__init__()
    
    def Store(self, request, context):
        logger.debug(f'traceid={request.traceID} spanid={request.spanID}')
        return storage_pb2.StorageResponse(status=200, message='buna')

if __name__ == '__main__':
    logger.debug('Starting server on port 50051')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    storage_pb2_grpc.add_StorageServicer_to_server(StorageServicer(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
