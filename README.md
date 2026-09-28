VM vs Container Performance Analysis

Comparative performance evaluation of a Virtual Machine and a Docker Container using CPU, memory, disk I/O, and network workloads.


1. Project Overview

This project performs a practical performance comparison between a Virtual Machine and a Docker Container.

The experiment evaluates four major performance areas:

| Performance Area | Benchmark Tool | Measurement |
|---|---|---|
| CPU | Sysbench | Events per second |
| Memory | Sysbench | MiB/sec |
| Disk I/O | FIO | KiB/sec |
| Network | iPerf3 | Gbits/sec |

The benchmark results were collected separately for the VM and Docker Container. The raw outputs were stored, processed into CSV files, and visualized using Python.


2. Aim

To experimentally compare the performance characteristics of a Virtual Machine and a Docker Container using CPU, memory, disk I/O, and network workloads.


3. Objectives

| No. | Objective |
|---|---|
| 1 | Configure the Virtual Machine environment |
| 2 | Configure the Docker Container environment |
| 3 | Perform CPU benchmarking |
| 4 | Perform memory benchmarking |
| 5 | Perform disk I/O benchmarking |
| 6 | Perform network benchmarking |
| 7 | Store raw benchmark results |
| 8 | Process results into CSV files |
| 9 | Generate performance graphs |
| 10 | Compare VM and Container results |


4. Experimental Setup

| Component | Configuration |
|---|---|
| Operating System | Ubuntu 22.04.5 LTS |
| Architecture | amd64 |
| CPU Cores | 4 |
| Python | 3.10.12 |
| Hypervisor | VMware |
| Container Platform | Docker |
| CPU Benchmark | Sysbench |
| Memory Benchmark | Sysbench |
| Disk Benchmark | FIO |
| Network Benchmark | iPerf3 |
| Data Processing | Python |
| Visualization | Matplotlib |


5. Experimental Methodology

The experiment was performed in the following stages:

1. Collected system and environment information.
2. Prepared the Virtual Machine environment.
3. Prepared the Docker Container environment.
4. Executed CPU benchmarks.
5. Executed memory benchmarks.
6. Executed disk read and write benchmarks.
7. Executed network throughput benchmarks.
8. Stored raw benchmark outputs.
9. Converted benchmark results into CSV files.
10. Generated comparison graphs.
11. Compared the measured results.


6. CPU Benchmark

CPU performance was measured using Sysbench.

Test configuration:

| Parameter | Value |
|---|---|
| Test duration | 30 seconds |
| Threads | 1, 2, 4, 8 |
| Measurement | Events per second |

CPU Results:

| Threads | VM | Container |
|---:|---:|---:|
| 1 | 743.36 | 781.03 |
| 2 | 1670.49 | 1655.96 |
| 4 | 3364.15 | 3305.75 |
| 8 | 3371.46 | 3362.75 |

The CPU measurements were collected using increasing numbers of threads. At higher thread counts, the measured VM and Container results were relatively close.

CPU Performance Graph

![CPU Performance](results/figures/cpu_performance.png)


7. Memory Benchmark

Memory performance was measured using Sysbench.

Test configuration:

| Parameter | Value |
|---|---|
| Block size | 1 KiB |
| Total size | 10 GiB |
| Operation | Write |
| Threads | 1 |
| Measurement | MiB/sec |

Memory Results:

| Environment | Memory Throughput |
|---|---:|
| VM | 5102.12 MiB/sec |
| Container | 4641.70 MiB/sec |

Memory Performance Graph

![Memory Performance](results/figures/memory_performance.png)


8. Disk I/O Benchmark

Disk performance was measured using FIO.

The experiment measured both read and write bandwidth.

Disk Results:

| Operation | VM | Container |
|---|---:|---:|
| Read | 8709 KiB/sec | 9519 KiB/sec |
| Write | 8663 KiB/sec | 9454 KiB/sec |

Disk Performance Graph

![Disk Performance](results/figures/disk_performance.png)


9. Network Benchmark

Network performance was measured using iPerf3 with a 30-second TCP test.

Network Result:

| Environment | Throughput |
|---|---:|
| VM | 38.7 Gbits/sec |
| Container | 38.7 Gbits/sec |

The measured network throughput was approximately equal for the VM and Container in the performed test.

Network Performance Graph

![Network Performance](results/figures/network_performance.png)


10. Overall Comparison

| Benchmark | Metric | VM | Container |
|---|---|---:|---:|
| CPU - 1 Thread | Events/sec | 743.36 | 781.03 |
| CPU - 2 Threads | Events/sec | 1670.49 | 1655.96 |
| CPU - 4 Threads | Events/sec | 3364.15 | 3305.75 |
| CPU - 8 Threads | Events/sec | 3371.46 | 3362.75 |
| Memory | MiB/sec | 5102.12 | 4641.70 |
| Disk Read | KiB/sec | 8709 | 9519 |
| Disk Write | KiB/sec | 8663 | 9454 |
| Network | Gbits/sec | 38.7 | 38.7 |


11. Benchmark Comparison

| Area | VM Result | Container Result | Observation |
|---|---|---|---|
| CPU | 743.36–3371.46 events/sec | 781.03–3362.75 events/sec | Results become relatively close at higher thread counts |
| Memory | 5102.12 MiB/sec | 4641.70 MiB/sec | Different measured throughput |
| Disk Read | 8709 KiB/sec | 9519 KiB/sec | Different measured bandwidth |
| Disk Write | 8663 KiB/sec | 9454 KiB/sec | Different measured bandwidth |
| Network | 38.7 Gbits/sec | 38.7 Gbits/sec | Approximately equal measured throughput |


12. Result Organization

The benchmark results were organized into three categories.

Raw Results

The original benchmark outputs are stored under:

results/raw/

Processed Results

The extracted benchmark values are stored as CSV files under:

results/processed/

Graphs

The generated performance graphs are stored under:

results/figures/


13. Result Files

| Benchmark | VM Result | Container Result | Processed Result |
|---|---|---|---|
| CPU | vm_cpu_results.txt | docker_cpu_results.txt | cpu_results.csv |
| Memory | vm_memory_results.txt | docker_memory_results.txt | memory_results.csv |
| Disk | vm_disk_results.txt | docker_disk_results.txt | disk_results.csv |
| Network | vm_network_results.txt | docker_network_results.txt | network_results.csv |


14. Analysis Scripts

| Script | Purpose |
|---|---|
| analyze_cpu.py | Generates CPU performance graph |
| analyze_memory.py | Generates memory performance graph |
| analyze_disk.py | Generates disk performance graph |
| analyze_network.py | Generates network performance graph |


15. Project Structure

CC_VM_vs_Container_Performance/
|
|-- README.md
|-- .gitignore
|
|-- docker/
|   |-- Dockerfile
|
|-- docs/
|   |-- cpu-info.txt
|   |-- docker-info.txt
|   |-- kernel-info.txt
|   |-- memory-info.txt
|   |-- storage-info.txt
|
|-- results/
|   |
|   |-- figures/
|   |   |-- cpu_performance.png
|   |   |-- memory_performance.png
|   |   |-- disk_performance.png
|   |   |-- network_performance.png
|   |
|   |-- processed/
|   |   |-- cpu_results.csv
|   |   |-- memory_results.csv
|   |   |-- disk_results.csv
|   |   |-- network_results.csv
|   |
|   |-- raw/
|       |-- cpu/
|       |-- memory/
|       |-- disk/
|       |-- network/
|
|-- scripts/
|   |-- analyze_cpu.py
|   |-- analyze_memory.py
|   |-- analyze_disk.py
|   |-- analyze_network.py
|
|-- vm/
|-- api/
|
|-- workloads/
    |-- cpu/
    |-- memory/
    |-- disk/
    |-- network/


16. Technologies Used

| Technology | Purpose |
|---|---|
| Ubuntu Linux | Operating system |
| VMware | Virtual Machine environment |
| Docker | Container environment |
| Sysbench | CPU and memory benchmarking |
| FIO | Disk I/O benchmarking |
| iPerf3 | Network benchmarking |
| Python | Data processing |
| Pandas | CSV processing |
| Matplotlib | Graph generation |
| Git | Version control |
| GitHub | Repository hosting |


17. Key Findings

| Benchmark | Measured Result |
|---|---|
| CPU | VM and Container produced relatively close results at higher thread counts |
| Memory | Different throughput values were measured |
| Disk | Different read and write bandwidth values were measured |
| Network | Both environments produced approximately 38.7 Gbits/sec |

The results depend on the experimental hardware, operating system, VM configuration, Docker configuration, and benchmark parameters.


18. Conclusion

This project experimentally evaluated Virtual Machine and Docker Container performance using CPU, memory, disk I/O, and network workloads.

The experiment involved collecting raw benchmark outputs, organizing the results, processing the results into CSV files, generating graphical representations, and comparing the measured values.

The CPU measurements were relatively close between the two environments, especially at higher thread counts. Memory throughput showed different measured values. Disk benchmarking produced different read and write bandwidth measurements, while the network benchmark produced approximately equal throughput for both environments.

The results are specific to the experimental hardware, operating system, VM configuration, Docker configuration, and benchmark parameters used in this project.


19. Author

By Sunayana Kamat
