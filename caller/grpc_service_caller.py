from auth_service_pb2_grpc import AuthorizationServiceStub
from auth_service_pb2 import In
import grpc
import time

channel = grpc.insecure_channel('192.168.64.2:32129')
stub = AuthorizationServiceStub(channel)
print(stub)
while True:
    try:
        print("sleep")
        time.sleep(2)

        resp = stub.ValidateOneLoginTokens(In(value="hello"))
        print(resp)

    except grpc.RpcError as rpc_error:
        print(rpc_error)


# from vmd_grpc.vmdgrpc.domain.onelogin_pb2 import OidcAuthenticationTokens
# from vmd_grpc.vmdgrpc.domain.auth_pb2 import IdToken, AccessToken
#
# bad_tokens = OidcAuthenticationTokens(accessToken=AccessToken(value="hi"), idToken=IdToken(value="yo"))
# validity_response = stub.ValidateOneLoginTokens(bad_tokens)
# print(validity_response.valid)
# print(validity_response.reason)

# token = AccessToken(value='thisisthetoken')
# resp = stub.MintVmdAccessTokenForOneLoginAccessToken.with_call(
#     Empty(),
#     metadata=(
#         ('assertion', resp.accessToken.value),
#         ('grant_type', "urn:ietf:params:oauth:grant-type:jwt-bearer"),
#         ('initial-metadata-1', 'The value should be str'),
#         ('binary-metadata-bin',
#          b'With -bin surffix, the value can be bytes')
#     ))
#
# print(resp)
