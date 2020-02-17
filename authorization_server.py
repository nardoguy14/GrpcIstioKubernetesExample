from concurrent import futures
import logging
import grpc
import auth_service_pb2_grpc
from auth_service_pb2 import Out
from grpc_status import rpc_status
from oslash import Right
from google.rpc import code_pb2, status_pb2

logging.basicConfig()
logger = logging.getLogger('authorization_service')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('../application.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class AuthorizationServerImpl(auth_service_pb2_grpc.AuthorizationServiceServicer):


    def ValidateOneLoginTokens(self, request, context):
        print("yo")
        logger.info(f"Version 2 -- {request}")
        return Out(value="version2")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_service_pb2_grpc.add_AuthorizationServiceServicer_to_server(AuthorizationServerImpl(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    print("started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
