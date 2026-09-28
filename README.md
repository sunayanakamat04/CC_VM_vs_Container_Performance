CC Experiment: VM vs Container Performance Benchmark

Project Overview

This project is a Cloud Computing experiment that compares the performance of a Virtual Machine and a Docker container using CPU, memory, disk I/O, and network benchmarks.

The objective is to understand the performance overhead and differences between traditional virtualization and containerization.

The experiments were performed on Ubuntu 22.04.5 LTS running inside VMware Workstation.

Environment Details

Host/VM Operating System: Ubuntu 22.04.5 LTS
Kernel: Linux 6.8.0-138-generic
Architecture: x86_64
CPU: 12th Gen Intel Core i5-12500H
Allocated CPU Cores: 4
Allocated Memory: 7.7 GiB
Storage: 60 GB virtual disk
Hypervisor: VMware Workstation
Container Runtime: Docker 29.1.3

Benchmark Tools

Sysbench 1.0.20
FIO 3.28
iperf3 3.9
Python 3.10.12
Git 2.34.1
Docker 29.1.3

Experiment Structure

vm-vs-container-performance/

    analysis/
    api/
    docker/
    docs/
    results/
        figures/
        processed/
        raw/
    scripts/
    vm/
    workloads/
        cpu/
        memory/
        disk/
        network/
    .gitignore
    README.md

Experiments Performed

CPU Benchmark

CPU performance was measured using Sysbench with a prime-number calculation workload.

Test parameters:

CPU max prime: 20000
Test duration: 30 seconds
Threads: 1, 2, 4 and 8

Memory Benchmark

Memory performance was measured using Sysbench.

Test parameters:

Block size: 1 KiB
Total size: 10 GiB
Operation: Write
Threads: 1

Disk Benchmark

Disk performance was measured using FIO using read and write workloads.

Test duration: 30 seconds

Network Benchmark

Network performance was measured using iperf3.

Test duration: 30 seconds
Protocol: TCP

Performance Comparison

CPU Performance

| Threads | VM Events/sec | Container Events/sec |
|--------:|--------------:|---------------------:|
| 1       | 743.36 / 847.21 | 781.03 |
| 2       | 1670.49 | 1655.96 |
| 4       | 3364.15 | 3305.75 |
| 8       | 3371.46 | 3362.75 |

Memory Performance

| Environment | Memory Speed (MiB/sec) |
|-------------|------------------------:|
| VM          | 5102.12 |
| Container   | 4641.70 |

Disk Performance

| Environment | Operation | Bandwidth (KiB/sec) |
|-------------|-----------|--------------------:|
| VM          | READ      | 8709 |
| VM          | WRITE     | 8663 |
| Container   | READ      | 9519 |
| Container   | WRITE     | 9454 |

Network Performance

The network benchmark was performed using iperf3 for 30 seconds. The container test used host networking so that the container could be compared with the VM without introducing Docker bridge-network overhead.

The detailed raw and processed network results are available under:

results/raw/network/
results/processed/network_results.csv

Performance Graphs

CPU Performance

![CPU Performance](results/figures/cpu_performance.png)

Memory Performance

![Memory Performance](results/figures/memory_performance.png)

Disk Performance

![Disk Performance](results/figures/disk_performance.png)

Network Performance

![Network Performance](results/figures/network_performance.png)

Results Summary

The experiments demonstrate that VM and container performance can differ depending on the workload.

CPU performance was broadly similar between the VM and container, with both environments scaling from 1 to 4 threads and showing limited additional throughput at 8 threads.

The VM achieved higher memory throughput in the measured test.

The container achieved higher measured disk read and write bandwidth in the FIO test.

Network performance was measured using iperf3, with host networking used for the container experiment.

The complete raw benchmark outputs, processed CSV files, Python analysis scripts, and generated graphs are included in the repository.

Reproducibility

CPU benchmark:

sysbench cpu --cpu-max-prime=20000 --threads=1 --time=30 run

sysbench cpu --cpu-max-prime=20000 --threads=2 --time=30 run

sysbench cpu --cpu-max-prime=20000 --threads=4 --time=30 run

sysbench cpu --cpu-max-prime=20000 --threads=8 --time=30 run

Memory benchmark:

sysbench memory --memory-block-size=1K --memory-total-size=10G --threads=1 run

Container benchmark example:

docker run --rm cc-benchmark:latest sysbench cpu --cpu-max-prime=20000 --threads=4 --time=30 run

Network benchmark:

iperf3 -s

iperf3 -c 127.0.0.1 -t 30

Docker network benchmark:

docker run --rm --network host cc-benchmark:latest iperf3 -c 127.0.0.1 -t 30

Analysis Scripts

CPU:

scripts/analyze_cpu.py

Memory:

scripts/analyze_memory.py

Disk:

scripts/analyze_disk.py

Network:

scripts/analyze_network.py

Generated Results

Raw benchmark outputs are stored in:

results/raw/

Processed benchmark data is stored in:

results/processed/

Performance graphs are stored in:

results/figures/

Documentation

System information and environment details are available in:

docs/cpu-info.txt
docs/memory-info.txt
docs/storage-info.txt
docs/kernel-info.txt
docs/docker-info.txt

Conclusion

This experiment provides a practical comparison between virtual machines and containers across CPU, memory, disk, and network workloads.

The collected benchmark data can be used to study how virtualization and containerization affect resource utilization and application performance.
