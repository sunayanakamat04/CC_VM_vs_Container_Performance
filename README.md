VM vs Container Performance Analysis
====================================

Comparative performance evaluation of a Virtual Machine and a Docker Container using CPU, Memory, Disk I/O, and Network workloads.

1. Project Overview
-------------------

This project performs a practical performance comparison between a Virtual Machine and a Docker Container.

The experiment was designed to observe how virtualization and containerization behave under different system workloads.

Four major performance areas were tested:

| Performance Area | Benchmark Tool | Measurement |
|------------------|----------------|-------------|
| CPU Performance | Sysbench | Events per second |
| Memory Performance | Sysbench | MiB/sec |
| Disk Performance | FIO | KiB/sec |
| Network Performance | iPerf3 | Gbits/sec |

The benchmark results were collected separately for the VM and Docker Container, stored as raw output files, converted into structured CSV files, and visualized using Python.

2. Aim
-------

To experimentally compare the performance characteristics of Virtual Machines and Docker Containers using standardized CPU, memory, disk, and network workloads.

3. Objectives
-------------

| No. | Objective |
|-----|-----------|
| 1 | Configure a Virtual Machine environment for benchmarking |
| 2 | Configure a Docker Container environment |
| 3 | Perform CPU benchmarking |
| 4 | Perform memory benchmarking |
| 5 | Perform disk I/O benchmarking |
| 6 | Perform network benchmarking |
| 7 | Store the raw benchmark outputs |
| 8 | Process benchmark results into CSV files |
| 9 | Generate graphical comparisons |
| 10 | Analyze the measured performance of VM and Container |

4. Experimental Setup
---------------------

The experiments were performed inside an Ubuntu virtual machine using VMware. Docker was configured inside the same environment for container-based benchmarking.

| System Component | Configuration |
|------------------|---------------|
| Operating System | Ubuntu 22.04.5 LTS |
| Architecture | amd64 |
| CPU Cores | 4 |
| Python Version | 3.10.12 |
| Hypervisor | VMware |
| Container Platform | Docker |
| CPU Benchmark | Sysbench |
| Memory Benchmark | Sysbench |
| Disk Benchmark | FIO |
| Network Benchmark | iPerf3 |
| Data Processing | Python / Pandas |
| Graph Generation | Matplotlib |

5. Experimental Methodology
----------------------------

The following procedure was followed during the experiment.

| Step | Work Performed |
|------|----------------|
| 1 | Collected system and environment information |
| 2 | Prepared the VM environment |
| 3 | Prepared the Docker environment |
| 4 | Created the required benchmark workload |
| 5 | Executed CPU tests |
| 6 | Executed memory tests |
| 7 | Executed disk read/write tests |
| 8 | Executed network throughput tests |
| 9 | Stored raw benchmark outputs |
| 10 | Converted the results into CSV format |
| 11 | Generated performance graphs |
| 12 | Compared VM and Container results |

6. CPU Benchmark
----------------

CPU performance was tested using Sysbench.


At 8 threads, the VM produced 3371.46 events/sec and the Container produced 3362.75 events/sec.

The measurements become very close at higher thread counts.
![CPU Performance](results/figures/cpu_performance.png)

7. Memory Benchmark
-------------------

Memory performance was tested using Sysbench.
Test configuration:

|-----------|-------|
| Block size | 1 KiB |
| Total size | 10 GiB |
| Operation | Write |
| Threads | 1 |
| Measurement | MiB/sec |

Memory Comparison

| Environment | Memory Throughput |
|-------------|------------------:|
| VM | 5102.12 MiB/sec |
| Container | 4641.70 MiB/sec |

Memory Interpretation

The VM produced a measured memory throughput of 5102.12 MiB/sec.

The Container produced a measured memory throughput of 4641.70 MiB/sec.

These values represent the measurements obtained from the configured experimental environment.

Memory Performance Graph

![Memory Performance](results/figures/memory_performance.png)

8. Disk I/O Benchmark
---------------------

Disk performance was tested using FIO.

Both read and write workloads were measured for 30 seconds.

Disk Comparison

| Operation | VM | Container |
|-----------|---:|----------:|
| Read | 8709 KiB/sec | 9519 KiB/sec |
| Write | 8663 KiB/sec | 9454 KiB/sec |

Disk Interpretation

For the read workload, the measured VM bandwidth was 8709 KiB/sec and the Container bandwidth was 9519 KiB/sec.

For the write workload, the measured VM bandwidth was 8663 KiB/sec and the Container bandwidth was 9454 KiB/sec.

Disk Performance Graph

![Disk Performance](results/figures/disk_performance.png)

9. Network Benchmark
--------------------

Network performance was tested using iPerf3.

Test configuration:

| Parameter | Value |
|-----------|-------|
| Protocol | TCP |
| Test duration | 30 seconds |
| Test type | Local network throughput |
| Measurement | Gbits/sec |

Network Comparison

| Environment | Throughput |
|-------------|-----------:|
| VM | 38.7 Gbits/sec |
| Container | 38.7 Gbits/sec |

Network Interpretation

The VM and Container produced approximately the same measured network throughput of 38.7 Gbits/sec in the local iPerf3 test.

Network Performance Graph



|-----------|--------|----:|----------:|
| CPU - 4 Threads | Events/sec | 3364.15 | 3305.75 |
| CPU - 8 Threads | Events/sec | 3371.46 | 3362.75 |
| Memory | MiB/sec | 5102.12 | 4641.70 |
| Disk Read | KiB/sec | 8709 | 9519 |
| Disk Write | KiB/sec | 8663 | 9454 |
11. Benchmark-wise Comparison
| Network | 38.7 Gbits/sec | 38.7 Gbits/sec | Approximately equal measured throughput |

12. Result Processing
---------------------

The benchmark outputs were organized into three stages.

Raw Results


    results/raw/
Processed Results

The required values were extracted and stored as CSV files under:

    results/processed/

Figures

The processed data was used to generate comparison graphs stored under:

    results/figures/

13. Result Files
----------------

| Benchmark | Raw VM Result | Raw Container Result | Processed Result |
|-----------|---------------|----------------------|------------------|
| CPU | vm_cpu_results.txt | docker_cpu_results.txt | cpu_results.csv |
| Memory | vm_memory_results.txt | docker_memory_results.txt | memory_results.csv |
| Disk | vm_disk_results.txt | docker_disk_results.txt | disk_results.csv |
| Network | vm_network_results.txt | docker_network_results.txt | network_results.csv |

14. Analysis Scripts
--------------------

Python scripts were created to process the benchmark data and generate the corresponding graphs.

| Script | Purpose |
|--------|---------|
| analyze_cpu.py | Processes CPU results and generates CPU graph |
| analyze_memory.py | Processes memory results and generates memory graph |
| analyze_disk.py | Processes disk results and generates disk graph |
| analyze_network.py | Processes network results and generates network graph |

15. Generated Graphs
--------------------

The project contains four performance graphs.

CPU Performance

![CPU Performance](results/figures/cpu_performance.png)

Memory Performance

![Memory Performance](results/figures/memory_performance.png)

Disk Performance

![Disk Performance](results/figures/disk_performance.png)

Network Performance

![Network Performance](results/figures/network_performance.png)

16. Project Structure
---------------------

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
    |       |   |-- docker_cpu_results.txt
    |       |   |-- vm_cpu_results.txt
    |       |
    |       |-- memory/
    |       |   |-- docker_memory_results.txt
    |       |   |-- vm_memory_results.txt
    |       |
    |       |-- disk/
    |       |   |-- docker_disk_results.txt
    |       |   |-- vm_disk_results.txt
    |       |
    |       |-- network/
    |           |-- docker_network_results.txt
    |           |-- vm_network_results.txt
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

17. Technologies Used
---------------------

| Technology | Role in Project |
|------------|-----------------|
| Ubuntu Linux | Experimental operating system |
| VMware | Virtual Machine environment |
| Docker | Container environment |
| Sysbench | CPU and memory benchmarking |
| FIO | Disk I/O benchmarking |
| iPerf3 | Network benchmarking |
| Python | Data processing and analysis |
| Pandas | CSV processing |
| Matplotlib | Performance visualization |
| Git | Version control |
| GitHub | Repository management |

18. Key Findings
----------------

| Benchmark | Observation |
|-----------|-------------|
| CPU | VM and Container produced closely related results at higher thread counts |
| Memory | Different throughput values were measured between VM and Container |
| Disk | Different read and write bandwidth values were measured |
| Network | Both environments produced approximately 38.7 Gbits/sec |

The results demonstrate that the performance difference between a VM and Container depends on the type of workload and the configuration of the underlying environment.

19. Conclusion
--------------

This project experimentally evaluated Virtual Machine and Docker Container performance using CPU, memory, disk I/O, and network workloads.

The experiment involved collecting raw benchmark outputs, organizing the results, processing them into CSV files, generating graphical representations, and comparing the measured values.

The CPU measurements were relatively close between the two environments, especially at higher thread counts. Memory throughput showed different measured values. Disk benchmarking produced different read and write bandwidth measurements, while the network benchmark produced approximately equal throughput for both environments.

The results are specific to the experimental hardware, operating system, VM configuration, Docker configuration, and benchmark parameters used in this project.

20. Author
----------

By

Sunayana Kamat
The original outputs generated by the benchmark tools were stored under:
| Disk Write | 8663 KiB/sec | 9454 KiB/sec | Different measured bandwidth |
| CPU | 743.36 to 3371.46 events/sec | 781.03 to 3362.75 events/sec | Similar measurements at higher thread counts |
| Disk Read | 8709 KiB/sec | 9519 KiB/sec | Different measured bandwidth |
| Memory | 5102.12 MiB/sec | 4641.70 MiB/sec | Different measured throughput |

|------|-----------|------------------|----------------------|
| Area | VM Result | Container Result | Measured Observation |
-----------------------------

| Network | Gbits/sec | 38.7 | 38.7 |
| CPU - 2 Threads | Events/sec | 1670.49 | 1655.96 |
| CPU - 1 Thread | Events/sec | 743.36 | 781.03 |
| Benchmark | Metric | VM | Container |
The following table combines the main measurements obtained from all experiments.
![Network Performance](results/figures/network_performance.png)

10. Overall Comparison
----------------------
| Parameter | Value |


CPU Performance Graph

At 4 threads, the VM produced 3364.15 events/sec and the Container produced 3305.75 events/sec.
At 2 threads, the VM produced 1670.49 events/sec and the Container produced 1655.96 events/sec.
At 1 thread, the VM produced 743.36 events/sec and the Container produced 781.03 events/sec.

The CPU results were collected for increasing numbers of threads.

| Parameter | Value |


CPU Interpretation
| 4 | 3364.15 | 3305.75 |
| 8 | 3371.46 | 3362.75 |
|-----------|-------|
| 2 | 1670.49 | 1655.96 |
| Prime limit | 20000 |
| 1 | 743.36 | 781.03 |
| Threads | VM | Container |
|---------|----:|----------:|

| Test duration | 30 seconds |
CPU Comparison
| Threads | 1, 2, 4, 8 |

| Measurement | Events per second |

Test configuration:

