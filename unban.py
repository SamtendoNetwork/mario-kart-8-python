import sys, os, grpc
from dotenv import load_dotenv
import amkj_service_pb2 as pb
import amkj_service_pb2_grpc as pbg

load_dotenv()
stub = pbg.AmkjServiceStub(grpc.insecure_channel("localhost:56751"))
md = [("x-api-key", os.environ["PN_MK8_MARIO_KART_8_GRPC_API_KEY"])]

stub.ClearBan(pb.ClearBanRequest(pid=int(sys.argv[1])), metadata=md)