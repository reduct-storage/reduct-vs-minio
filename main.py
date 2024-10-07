import io
import random
import time
import asyncio

from minio import Minio
from reduct import Client as ReductClient, Batch

BLOB_SIZE = 1000_000

BATCH_MAX_SIZE = 8_000_000
BATCH_MAX_RECORDS = 80

BLOB_COUNT = min(1000, 1_000_000_000 // BLOB_SIZE)
BUCKET_NAME = "test"

CHUNK = random.randbytes(BLOB_SIZE)

minio_client = Minio(
    "127.0.0.1:9000", access_key="minioadmin", secret_key="minioadmin", secure=False
)




def write_to_minio():
    count = 0
    for i in range(BLOB_COUNT):
        count += BLOB_SIZE
        minio_client.put_object(
            BUCKET_NAME,
            f"data/{str(int(time.time_ns() / 1000))}.bin",
            io.BytesIO(CHUNK),
            BLOB_SIZE,
        )
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
    async with ReductClient(
        "http://127.0.0.1:8383", api_token="reductstore"
    ) as reduct_client:
        count = 0
        bucket = await reduct_client.get_bucket("test")
        batch = Batch()
        for i in range(0, BLOB_COUNT):
            batch.add(timestamp=time.time(), data=CHUNK)
            await asyncio.sleep(0.000001)  # To avoid time collisions
            count += BLOB_SIZE

            if  batch.size >= BATCH_MAX_SIZE or len(batch) >= BATCH_MAX_RECORDS:
                await bucket.write_batch("data", batch)
                batch.clear()

        if len(batch) > 0:
            await bucket.write_batch("data", batch)

        return count


async def read_from_reduct(t1, t2):
    async with ReductClient("http://127.0.0.1:8383") as reduct_client:
        count = 0
        bucket = await reduct_client.get_bucket("test")
        async for rec in bucket.query("data", int(t1 * 1000000), int(t2 * 1000000)):
            count += len(await rec.read_all())
        return count


if __name__ == "__main__":
    print(f"Chunk size={BLOB_SIZE / 1000_000} Mb, count={BLOB_COUNT}")
    ts = time.time()
    size = write_to_minio()
    print(f"Write {size / 1000_000} Mb to Minio: {BLOB_COUNT / (time.time() - ts)} blob/s")

    ts_read = time.time()
    size = read_from_minio(ts, time.time())
    print(f"Read {size / 1000_000} Mb from Minio: {BLOB_COUNT / (time.time() - ts_read)} blob/s")

    loop = asyncio.new_event_loop()
    ts = time.time()
    size = loop.run_until_complete(write_to_reduct())
    print(f"Write {size / 1000_000} Mb to ReductStore: {BLOB_COUNT / (time.time() - ts)} blob/s")

    ts_read = time.time()
    size = loop.run_until_complete(read_from_reduct(ts, time.time()))
    print(f"Read {size / 1000_000} Mb from ReductStore: {BLOB_COUNT / (time.time() - ts_read)} blob/s")
