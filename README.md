VM VS CONTAINER PERFORMANCE ANALYSIS

Comparative Performance Evaluation of Virtual Machines and Docker Containers


PROJECT OVERVIEW

This project presents an experimental performance comparison between a Virtual Machine and a Docker Container.

The evaluation covers four major workload categories:

| Workload | Benchmark Tool | Main Metric |
|---|---|---|
| CPU | Sysbench | Events/sec |
| Memory | Sysbench | MiB/sec |
| Disk I/O | FIO | KiB/sec |
| Network | iPerf3 | Gbits/sec |

The experiment includes environment setup, benchmark execution, raw data collection, result processing, CSV generation, graph generation, and comparative analysis.


AIM

To experimentally compare the performance of a Virtual Machine and a Docker Container across CPU, memory, disk I/O, and network workloads.


OBJECTIVES

| Objective |
|---|
| Configure the Virtual Machine environment |
| Configure the Docker Container environment |
| Collect system and environment information |
| Execute CPU benchmark workloads |
| Execute memory benchmark workloads |
| Execute disk I/O benchmark workloads |
| Execute network benchmark workloads |
| Store raw benchmark results |
| Process benchmark results into CSV files |
| Generate performance graphs |
| Compare VM and Container measurements |
| Document the complete experimental setup and results |


SYSTEM ARCHITECTURE

The experiment uses a host system containing a Virtual Machine and Docker-based Container environment.

```text
                         HOST SYSTEM
                              |
               +--------------+--------------+
               |                             |
               v                             v
       VMware Virtualization            Docker Engine
               |                             |
               v                             v
      +-------------------+          +-------------------+
      |   Virtual Machine |          | Docker Container  |
      |                   |          |                   |
      | Ubuntu Linux      |          | Linux Environment |
      |                   |          |                   |
      | CPU Workload      |          | CPU Workload      |
      | Memory Workload   |          | Memory Workload   |
      | Disk Workload     |          | Disk Workload     |
      | Network Workload  |          | Network Workload  |
      +---------+---------+          +---------+---------+
                |                              |
                +--------------+---------------+
                               |
                               v
                    Benchmark Measurements
                               |
                               v
                       Raw Result Files
                               |
                               v
                     Processed CSV Files
                               |
                               v
                       Python Analysis
                               |
                               v
                      Performance Graphs
                               |
                               v
                    VM vs Container Results
```


EXPERIMENTAL WORKFLOW

```text
System Information Collection
             |
             v
Virtual Machine Configuration
             |
             v
Docker Configuration
             |
             v
Benchmark Environment Preparation
             |
             +-------------------+-------------------+
             |                   |                   |
             v                   v                   v
            CPU               Memory               Disk
             |                   |                   |
             +-------------------+-------------------+
                                 |
                                 v
                              Network
                                 |
                                 v
                         Raw Measurements
                                 |
                                 v
                         Result Processing
                                 |
                                 v
                            CSV Files
                                 |
                                 v
                         Python Analysis
                                 |
                                 v
                       Graph Generation
                                 |
                                 v
                     Performance Comparison
```


EXPERIMENTAL SETUP

| Component | Configuration |
|---|---|
| Operating System | Ubuntu 22.04.5 LTS |
| Architecture | amd64 |
| Python Version | 3.10.12 |
| CPU Cores | 4 |
| Virtualization Platform | VMware |
| Container Platform | Docker |
| CPU Benchmark | Sysbench |
| Memory Benchmark | Sysbench |
| Disk Benchmark | FIO |
| Network Benchmark | iPerf3 |
| Data Processing | Python |
| Visualization | Matplotlib |
| Version Control | Git |
| Repository Hosting | GitHub |


SYSTEM INFORMATION COLLECTED

| Information | File |
|---|---|
| CPU Information | docs/cpu-info.txt |
| Docker Information | docs/docker-info.txt |
| Kernel Information | docs/kernel-info.txt |
| Memory Information | docs/memory-info.txt |
| Storage Information | docs/storage-info.txt |


