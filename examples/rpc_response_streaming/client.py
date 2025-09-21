import grpc
import numbers_pb2
import numbers_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = numbers_pb2_grpc.NumberGeneratorStub(channel)
        responses = stub.GenerateNumbers(numbers_pb2.NumberRequest(max=5))
        
        for response in responses:
            print("Got number:", response.number)

if __name__ == "__main__":
    run()
