import grpc
import storage_pb2
import storage_pb2_grpc


if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = storage_pb2_grpc.StorageStub(channel)

        timestamp = storage_pb2.Timestamp(started=1, ended=2, duration=2)
        span = storage_pb2.Span(serviceName='filter', traceID='', spanID='', parentSpanID='', spanName='', timestamp=timestamp)

        response = stub.Store(span)
        print(response)