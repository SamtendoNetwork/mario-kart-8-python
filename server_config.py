from nintendo.nex import settings
from dotenv import load_dotenv
import os

load_dotenv()

GAME_SERVER_ID = 0x1010EB00
ACCESS_KEY = "25dbf96a"
NEX_VERSION = 30504

# NEX_SETTINGS = settings.load("friends")
NEX_SETTINGS = settings.default()
NEX_SETTINGS.configure(ACCESS_KEY, NEX_VERSION)
NEX_SETTINGS["prudp.resend_timeout"] = 1.5
NEX_SETTINGS["prudp.resend_limit"] = 3
NEX_SETTINGS["prudp.version"] = 1
NEX_SETTINGS["prudp.max_substream_id"] = 1


def readEnv(key: str, default: str = None) -> str:
    value = os.environ.get("PN_MK8_" + key)
    if value is None:
        if default is None:
            raise Exception("Missing environment variable: PN_MK8_" + key)
        return default
    return value


class NEXConfig:
    def __init__(self):
        self.nex_host = readEnv("NEX_HOST", "0.0.0.0")
        self.nex_auth_port = int(readEnv("NEX_AUTH_PORT", "1223"))
        self.nex_secure_port = int(readEnv("NEX_SECURE_PORT", "1224"))
        self.nex_secure_user_password = readEnv("NEX_SECURE_USER_PASSWORD")
        # Your external IP, for external clients to connect.
        self.nex_external_address = readEnv("NEX_EXTERNAL_ADDRESS")

        self.friends_grpc_host = readEnv("FRIENDS_GRPC_HOST")
        self.friends_grpc_port = int(readEnv("FRIENDS_GRPC_PORT"))
        self.friends_grpc_api_key = readEnv("FRIENDS_GRPC_API_KEY")

        self.account_grpc_host = readEnv("ACCOUNT_GRPC_HOST")
        self.account_grpc_port = int(readEnv("ACCOUNT_GRPC_PORT"))
        self.account_grpc_api_key = readEnv("ACCOUNT_GRPC_API_KEY")

        # These gRPC credentials are for the server we're implementing
        self.mario_kart_8_grpc_host = readEnv("MARIO_KART_8_GRPC_HOST", "0.0.0.0")
        self.mario_kart_8_grpc_port = int(readEnv("MARIO_KART_8_GRPC_PORT", "50051"))
        self.mario_kart_8_grpc_api_key = readEnv("MARIO_KART_8_GRPC_API_KEY")

        self.game_db_connection_string = readEnv("MONGO_DB_CONNECTION_STRING")

        self.game_database = readEnv("MONGO_DB_NAME", "mariokart8")

        # Rebuild Redis ranking leaderboards from MongoDB on startup.
        self.rebuild_rankings_on_start = readEnv("REBUILD_RANKINGS_ON_START", "false").lower() == "true"

        self.sequence_collection = "counters"
        self.gatherings_collection = "gatherings"
        self.sessions_collection = "sessions"
        self.tournaments_collection = "tournaments"
        self.tournaments_score_collection = "tournaments_scores"
        self.ranking_common_data_collection = "commondata"
        self.rankings_score_collection = "rankings"
        self.secure_reports_collection = "secure_reports"
        self.datastore_collection = "datastore"
        self.restriction_collection = "restrictions"

        self.s3_endpoint_domain = readEnv("S3_ENDPOINT_DOMAIN", "s3.pretendo.cc")
        self.s3_endpoint = "https://" + self.s3_endpoint_domain
        self.s3_access_key = readEnv("S3_ACCESS_KEY")
        self.s3_secret = readEnv("S3_SECRET_KEY")
        self.s3_region = readEnv("S3_REGION", "us-east-1")
        self.bucket_name = readEnv("S3_BUCKET_NAME", "pn-amkj-d1")

        self.redis_uri = readEnv("REDIS_URI", "redis://127.0.0.1:6379")

        self.health_http_host = readEnv("HEALTH_HTTP_HOST", "0.0.0.0")
        self.health_http_port = int(readEnv("HEALTH_HTTP_PORT", "8080"))
        self.health_udp_host = readEnv("HEALTH_UDP_HOST", "0.0.0.0")
        self.health_udp_port = int(readEnv("HEALTH_UDP_PORT", "8081"))


NEX_CONFIG = NEXConfig()
