import grpc
import storage_pb2
import storage_pb2_grpc

from concurrent import futures

class StorageServicer(storage_pb2_grpc.StorageServicer):
    def __init__(self) -> None:
        super().__init__()
    
    def Store(self, request, context):
        print(request)
        return storage_pb2.StorageResponse(status=200, message='buna')

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    storage_pb2_grpc.add_StorageServicer_to_server(StorageServicer(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
