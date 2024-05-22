# Benchmarks for Minio and ReductStore with Python client

The benchmarks write and read 1 Gb of random data from [Minio](https://min.io)
and [ReductStore](https://www.reduct.store).

## Results

| Blob Size | Operation | Minio, blob/s | ReductStore, blob/s | ReducStore, % |
|-----------|-----------|---------------|---------------------|---------------|
| 1 KB      | Write     | 548           | 1518                | 176 %         |
|           | Read      | 1028          | 6868                | 568 %         |  
| 10 KB     | Write     | 533           | 1480                | 177 %         |
|           | Read      | 1030          | 8386                | 714 %         | 
| 100 KB    | Write     | 360           | 1289                | 258 %         |
|           | Read      | 844           | 6561                | 677 %         |
| 1 MB      | Write     | 97            | 568                 | 486 %         |
|           | Read      | 528           | 944                 | 79 %          |
| 10 MB     | Write     | 21            | 97                  | 361 %         |
|           | Read      | 94            | 103                 | 10 %          |
