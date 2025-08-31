<!-- Compile the proto file -->

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto
