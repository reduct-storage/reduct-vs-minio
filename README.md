# Benchmarks for Minio and Reduct Storage with Python client

The benchmarks write and read 1 Gb of random data from [Minio](https://min.io)
and [Reduct Storage](https://reduct-storage.dev).

## Results

| Chunk                  | Operation | Minio   | Reduct Storage |
|------------------------|-----------|---------|----------------|
| 10.0 Mb (100 requests) | Write     | 8.69 s  | 0.53 s         | 
|                        | Read      | 1.19 s  | 0.57 s         |   
| 1.0 Mb (1000 requests) | Write     | 12.66 s | 1.30 s         | 
|                        | Read      | 2.04 s  | 1.38 s         |   
| .1 Mb (10000 requests) | Write     | 61.86 s | 13.73 s        | 
|                        | Read      | 9.39 s  | 15.02 s        |   
