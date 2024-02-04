# Benchmarks for Minio and ReductStore with Python client

The benchmarks write and read 1 Gb of random data from [Minio](https://min.io)
and [ReductStore](https://www.reduct.store).

## Results

| Chunk                  | Operation | Minio   | ReductStore |
|------------------------|-----------|---------|-------------|
| 10.0 Mb (100 requests) | Write     | 8.39 s  | 2.65 s      | 
|                        | Read      | 2.13 s  | 1.4s        |   
| 1.0 Mb (1000 requests) | Write     | 16.38 s | 3.78 s      | 
|                        | Read      | 3.13 s  | 1.16 s      |   
| .1 Mb (10000 requests) | Write     | 35.3 s  | 11.25 s     | 
|                        | Read      | 14.51 s | 2.24 s      |   
