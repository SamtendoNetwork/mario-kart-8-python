import os, grpc, datetime, sys
from dotenv import load_dotenv
from google.protobuf.timestamp_pb2 import Timestamp
import amkj_service_pb2 as pb
import amkj_service_pb2_grpc as pbg

load_dotenv()
API_KEY = os.environ["PN_MK8_MARIO_KART_8_GRPC_API_KEY"]

stub = pbg.AmkjServiceStub(grpc.insecure_channel("localhost:56751"))
md = [("x-api-key", API_KEY)]

start = Timestamp(); start.GetCurrentTime()
end = Timestamp(); end.FromDatetime(datetime.datetime.utcnow() + datetime.timedelta(days=7))

stub.IssueBan(pb.IssueBanRequest(pid=int(sys.argv[1]), reason=sys.argv[2],
                                 start_time=start, end_time=end), metadata=md)