proto_storage:
	@python -m grpc_tools.protoc -Ibtrace-idl/proto/v2 --python_out=storage --grpc_python_out=storage btrace-idl/proto/v2/storage.proto

client_test_proto:
	@python -m grpc_tools.protoc -Ibtrace-idl/proto/v2 --python_out=storage/tests --grpc_python_out=storage/tests btrace-idl/proto/v2/storage.proto

run:
	@python storage/storage.py

