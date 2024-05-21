# Benchmarks for Minio and ReductStore with Python client

The benchmarks write and read 1 Gb of random data from [Minio](https://min.io)
and [ReductStore](https://www.reduct.store).

## Results

| Blob Size | Operation | Minio, blob/s | ReductStore, blob/s | ReducStore, % |
|-----------|-----------|---------------|---------------------|---------------|
| 1 KB      | Write     | 347           | 1078                | 210 %         |
|           | Read      | 739           | 7059                | 855 %         |  
| 10 KB     | Write     | 378           | 889                 | 235 %         |
|           | Read      | 612           | 6440                | 952 %         |  
| 100 KB    | Write     | 259           | 916                 | 255 %         |
|           | Read      | 629           | 4571                | 628 %         |
| 1 MB      | Write     | 75            | 343                 | 367 %         |
|           | Read      | 383           | 518                 | 35 %          |
| 10 MB     | Write     | 15            | 60                  | 300 %         |
|           | Read      | 72            | 42                  | -41 %         |
