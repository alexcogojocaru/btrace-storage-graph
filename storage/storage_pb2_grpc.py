# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import storage_pb2 as storage__pb2


class StorageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Store = channel.unary_unary(
                '/Storage/Store',
                request_serializer=storage__pb2.StorageSpan.SerializeToString,
                response_deserializer=storage__pb2.StorageResponse.FromString,
                )
        self.GetServices = channel.unary_stream(
                '/Storage/GetServices',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=storage__pb2.ServiceName.FromString,
                )
        self.GetServiceData = channel.unary_unary(
                '/Storage/GetServiceData',
                request_serializer=storage__pb2.ServiceName.SerializeToString,
                response_deserializer=storage__pb2.ServiceResponse.FromString,
                )
        self.GetMultipleServicesData = channel.stream_unary(
                '/Storage/GetMultipleServicesData',
                request_serializer=storage__pb2.ServiceName.SerializeToString,
                response_deserializer=storage__pb2.ServiceResponse.FromString,
                )
        self.GetData = channel.unary_stream(
                '/Storage/GetData',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=storage__pb2.ServicePair.FromString,
                )


class StorageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Store(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMultipleServicesData(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StorageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Store': grpc.unary_unary_rpc_method_handler(
                    servicer.Store,
                    request_deserializer=storage__pb2.StorageSpan.FromString,
                    response_serializer=storage__pb2.StorageResponse.SerializeToString,
            ),
            'GetServices': grpc.unary_stream_rpc_method_handler(
                    servicer.GetServices,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=storage__pb2.ServiceName.SerializeToString,
            ),
            'GetServiceData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceData,
                    request_deserializer=storage__pb2.ServiceName.FromString,
                    response_serializer=storage__pb2.ServiceResponse.SerializeToString,
            ),
            'GetMultipleServicesData': grpc.stream_unary_rpc_method_handler(
                    servicer.GetMultipleServicesData,
                    request_deserializer=storage__pb2.ServiceName.FromString,
                    response_serializer=storage__pb2.ServiceResponse.SerializeToString,
            ),
            'GetData': grpc.unary_stream_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=storage__pb2.ServicePair.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Storage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Storage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Store(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Storage/Store',
            storage__pb2.StorageSpan.SerializeToString,
            storage__pb2.StorageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Storage/GetServices',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            storage__pb2.ServiceName.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Storage/GetServiceData',
            storage__pb2.ServiceName.SerializeToString,
            storage__pb2.ServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMultipleServicesData(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Storage/GetMultipleServicesData',
            storage__pb2.ServiceName.SerializeToString,
            storage__pb2.ServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Storage/GetData',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            storage__pb2.ServicePair.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)