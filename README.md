# Benchmarks for Minio and Reduct Storage with Python client

I write and read 1 Gb of random data from [Minio](https://min.io) and [Reduct Storage](https://reduct-storage.dev).

## Results

**Chunk size=10.0 Mb, count=100**

Write 1000.0 Mb to Minio: 8.690120697021484 s
Read 1000.0 Mb from Minio: 1.1872284412384033 s
Write 1000.0 Mb to Reduct Storage: 0.5293519496917725 s
Read 1000.0 Mb from Reduct Storage: 0.5725595951080322 s

**Chunk size=1.0 Mb, count=1000**

Write 1000.0 Mb to Minio: 12.656668424606323 s
Read 1000.0 Mb from Minio: 2.044912099838257 s
Write 1000.0 Mb to Reduct Storage: 1.3007972240447998 s
Read 1000.0 Mb from Reduct Storage: 1.3807475566864014 s

**Chunk size=0.1 Mb, count=10'000**

Write 1000.0 Mb to Minio: 61.86865258216858 s
Read 1000.0 Mb from Minio: 13.731996774673462 s
Write 1000.0 Mb to Reduct Storage: 9.385319471359253 s
Read 1000.0 Mb from Reduct Storage: 15.022344589233398 s