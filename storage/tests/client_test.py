import grpc
import storage_pb2
import storage_pb2_grpc


if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = storage_pb2_grpc.StorageStub(channel)

        empty = storage_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        services = stub.GetServices(empty)
        for service in services:
            print(service.name)
