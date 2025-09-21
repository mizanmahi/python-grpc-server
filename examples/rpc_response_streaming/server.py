import time
import grpc
from concurrent import futures
import numbers_pb2
import numbers_pb2_grpc

class NumberGeneratorServicer(numbers_pb2_grpc.NumberGeneratorServicer):
    def GenerateNumbers(self, request, context):
        # request.max tells how many numbers
        for i in range(1, request.max + 1):
            yield numbers_pb2.NumberResponse(number=i)
            time.sleep(0.5)  # simulate delay (like streaming)
            
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    numbers_pb2_grpc.add_NumberGeneratorServicer_to_server(NumberGeneratorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
