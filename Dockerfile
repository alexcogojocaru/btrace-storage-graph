FROM python:3.8-slim-buster

WORKDIR /storage_graph
COPY storage storage
COPY requirements.txt .
COPY btrace-idl/proto/v2/storage.proto .

RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I. --python_out=storage --grpc_python_out=storage storage.proto
RUN rm -rf storage.proto

CMD [ "python", "storage/storage.py" ]
