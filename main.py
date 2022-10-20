import io
import random
import time
import asyncio

from minio import Minio
from reduct import Client as ReductClient

CHUNK_SIZE = 100000
CHUNK_COUNT = 10000
BUCKET_NAME = "test"

CHUNK = random.randbytes(CHUNK_SIZE)

minio_client = Minio("127.0.0.1:9000", access_key="minioadmin", secret_key="minioadmin", secure=False)
reduct_client = ReductClient("http://127.0.0.1:8383")


def write_to_minio():
    count = 0
    for i in range(CHUNK_COUNT):
        count += CHUNK_SIZE
        minio_client.put_object(BUCKET_NAME, f"data/{str(int(time.time_ns() / 1000))}.bin", io.BytesIO(CHUNK),
                                CHUNK_SIZE)
    return count


def read_from_minio(t1, t2):
    count = 0

    t1 = str(int(t1 * 1000_000))
    t2 = str(int(t2 * 1000_000))

    for obj in minio_client.list_objects("test", prefix="data/"):
        if t1 <= obj.object_name[5:-4] <= t2:
            resp = minio_client.get_object("test", obj.object_name)
            count += len(resp.read())

    return count


async def write_to_reduct():
    count = 0
    bucket = await reduct_client.create_bucket("test", exist_ok=True)
    for i in range(CHUNK_COUNT):
        await bucket.write("data", CHUNK)
        count += CHUNK_SIZE
    return count


async def read_from_reduct(t1, t2):
    count = 0
    bucket = await reduct_client.get_bucket("test")
    async for rec in bucket.query("data", int(t1 * 1000000), int(t2 * 1000000)):
        count += len(await rec.read_all())
    return count


if __name__ == "__main__":
    print(f"Chunk size={CHUNK_SIZE/1000_000} Mb, count={CHUNK_COUNT}")
    ts = time.time()
    size = write_to_minio()
    print(f"Write {size / 1000_000} Mb to Minio: {time.time() - ts} s")

    ts_read = time.time()
    size = read_from_minio(ts, time.time())
    print(f"Read {size / 1000_000} Mb from Minio: {time.time() - ts_read} s")

    loop = asyncio.new_event_loop();
    ts = time.time()
    size = loop.run_until_complete(write_to_reduct())
    print(f"Write {size / 1000_000} Mb to Reduct Storage: {time.time() - ts} s")

    ts_read = time.time()
    size = loop.run_until_complete(read_from_reduct(ts, time.time()))
    print(f"Read {size / 1000_000} Mb from Reduct Storage: {time.time() - ts_read} s")
