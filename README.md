# Benchmarks for Minio and ReductStore with Python client

The benchmarks write and read 1 Gb of random data from [Minio](https://min.io)
and [ReductStore](https://www.reduct.store).

## Results

| Blob Size | Operation | Minio, blob/s | ReductStore, blob/s | ReducStore, % |
|-----------|-----------|---------------|---------------------|---------------|
| 1 KB      | Write     | 614           | 9256                | 1400 %        |
|           | Read      | 724           | 60159               | 8310 %        |
| 10 KB     | Write     | 570           | 9290                | 1629 %        |
|           | Read      | 632           | 38996               | 6170 %        |
| 100 KB    | Write     | 422           | 5434                | 1288 %        |
|           | Read      | 690           | 10703               | 1552 %        |
| 1 MB      | Write     | 104           | 975                 | 936 %         |
|           | Read      | 474           | 1380                | 291 %         |
