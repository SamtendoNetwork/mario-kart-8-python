# Mario Kart 8 NEX server (The python variant)

This is the currently hosted version of Mario Kart 8 on Samtendo Network.

# Cloning and building

```shell
git clone --recursive https://www.github.com/SamtendoNetwork/mario-kart-8-python.git
```

You need:

- S3 instance
- MongoDB server 6.0+
- Redis server 7.0+

Install Python3 and these libs:

- [NintendoClients](https://github.com/kinnay/NintendoClients)
- `python -m pip install aioconsole requests pymongo redis grpcio-tools minio`

```shell
python -m grpc_tools.protoc --proto_path=grpc --python_out=. --grpc_python_out=. grpc/amkj_service.proto
```

# Configuration

The server is configured entirely through environment variables, all prefixed
with `PN_MK8_`. Variables without a default are **required** - the server
exits on startup if one is missing.

| Variable                           | Default                  | Description                                                               |
| ---------------------------------- | ------------------------ | ------------------------------------------------------------------------- |
| `PN_MK8_NEX_HOST`                  | `0.0.0.0`                | Address the NEX auth/secure servers bind to                               |
| `PN_MK8_NEX_AUTH_PORT`             | `1223`                   | NEX authentication server port                                            |
| `PN_MK8_NEX_SECURE_PORT`           | `1224`                   | NEX secure server port                                                    |
| `PN_MK8_NEX_SECURE_USER_PASSWORD`  | _required_               | Password for the NEX `guest`/secure user                                  |
| `PN_MK8_NEX_EXTERNAL_ADDRESS`      | _required_               | External IP address clients connect to                                    |
| `PN_MK8_FRIENDS_GRPC_HOST`         | _required_               | Hostname of the friends gRPC service                                      |
| `PN_MK8_FRIENDS_GRPC_PORT`         | _required_               | Port of the friends gRPC service                                          |
| `PN_MK8_FRIENDS_GRPC_API_KEY`      | _required_               | API key for the friends gRPC service                                      |
| `PN_MK8_ACCOUNT_GRPC_HOST`         | _required_               | Hostname of the account gRPC service                                      |
| `PN_MK8_ACCOUNT_GRPC_PORT`         | _required_               | Port of the account gRPC service                                          |
| `PN_MK8_ACCOUNT_GRPC_API_KEY`      | _required_               | API key for the account gRPC service                                      |
| `PN_MK8_MARIO_KART_8_GRPC_HOST`    | `0.0.0.0`                | Address this server's own gRPC service binds to                           |
| `PN_MK8_MARIO_KART_8_GRPC_PORT`    | `50051`                  | Port for this server's own gRPC service                                   |
| `PN_MK8_MARIO_KART_8_GRPC_API_KEY` | _required_               | API key required to call this server's gRPC service                       |
| `PN_MK8_MONGO_DB_CONNECTION_STRING` | _required_              | MongoDB connection string (e.g. `mongodb://user:pass@host:27017`)         |
| `PN_MK8_MONGO_DB_NAME`             | `mariokart8`             | MongoDB database name                                                     |
| `PN_MK8_S3_ENDPOINT_DOMAIN`        | `s3.pretendo.cc`         | S3 endpoint domain (scheme is always `https`)                             |
| `PN_MK8_S3_ACCESS_KEY`             | _required_               | S3 access key                                                             |
| `PN_MK8_S3_SECRET_KEY`             | _required_               | S3 secret key                                                             |
| `PN_MK8_S3_REGION`                 | `us-east-1`              | S3 region                                                                 |
| `PN_MK8_S3_BUCKET_NAME`            | `pn-amkj-d1`             | S3 bucket used for DataStore objects                                      |
| `PN_MK8_REDIS_URI`                 | `redis://127.0.0.1:6379` | Redis connection URI                                                      |
| `PN_MK8_REBUILD_RANKINGS_ON_START` | `false`                  | Rebuild the Redis ranking leaderboards from MongoDB on startup (see below) |
| `PN_MK8_HEALTH_HTTP_HOST`          | `0.0.0.0`                | Address the HTTP health check binds to                                    |
| `PN_MK8_HEALTH_HTTP_PORT`          | `8080`                   | HTTP health check port (any request returns `200 {"status":"ok"}`)        |
| `PN_MK8_HEALTH_UDP_HOST`           | `0.0.0.0`                | Address the UDP echo health check binds to                                |
| `PN_MK8_HEALTH_UDP_PORT`           | `8081`                   | UDP health check port (echoes received datagrams back to the sender)      |

## Rebuilding the ranking leaderboards

Redis holds the leaderboards as a cache of MongoDB's `rankings` collection and is
never rehydrated on its own, so a fresh or flushed Redis leaves them empty.

Set `PN_MK8_REBUILD_RANKINGS_ON_START=true` for one startup to rebuild them from
MongoDB, then unset it. The rebuild is read-only on MongoDB and safe to re-run.

Credits to Pretendo for original repo.
