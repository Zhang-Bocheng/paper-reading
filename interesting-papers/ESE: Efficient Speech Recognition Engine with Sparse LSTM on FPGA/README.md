# ESE: Efficient Speech Recognition Engine with Sparse LSTM on FPGA
[paper link](https://arxiv.org/pdf/1612.00694) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2017 | This paper describes a hardware gas pedal called ESE (Efficient Speech Recognition Engine) for long short-term memory networks (LSTM) in speech recognition          | Model Compression         |

## Methodology

### 1. Abstract
  Since large models require a lot of computational and memory resources, the researchers proposed ways to compress the model size and improve energy efficiency. The authors used a load-balancing-aware pruning method to compress the model size by a factor of 20 and further reduced it by a factor of 2 through quantization. In addition, they designed a scheduler to encode and assign the compressed model to multiple PEs for parallel processing and to schedule complex LSTM data streams. Finally, a hardware architecture called ESE to work directly on sparse LSTM models. Experimental results show that ESE is 43x and 3x faster than CPU and GPU implementations, while having higher energy efficiency.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/d900cdae-e36d-40e1-91d4-42b5b26823bf)

### 2. Method Description 
  This thesis proposes a long short-term memory (LSTM) neural network model based on FPGA acceleration for speech recognition task. The system adopts a CPU+FPGA heterogeneous architecture and divides the whole system into three parts: **hardware gas pedal, software program and external memory**. Among them, the hardware gas pedal includes modules such as ESE Accelerator, ESE Controller, PCI-E Controller, MEM Controller, and On-chip Buffers; the software program consists of CPU and host memory, which is responsible for communicating with FPGA and transferring parameters and results; and the external memory is used for storing the vector data.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/fd72e67a-5951-402e-8d93-b4a0eb5b4b51)

### 3. Key concepts
  _Load Balance-Aware Pruning_: A technique used in distributed computing environments to optimize the performance of parallel processing systems by efficiently distributing computational tasks among nodes while considering load balancing constraints. In a distributed system, computational tasks are divided into smaller sub-tasks and assigned to different nodes for parallel execution. Load imbalance can occur when certain nodes have heavier workloads than others, leading to inefficient resource utilization and longer processing times.

Load Balance-Aware Pruning addresses this issue by dynamically adjusting the task distribution among nodes based on their current workload or processing capabilities. This optimization technique aims to achieve a more balanced distribution of tasks across the system, ensuring that each node operates at its optimal capacity and overall system performance is improved.

### 4. Methodological improvements
  The system achieves efficient speech recognition performance by optimizing the computational process in the LSTM network. Specifically, the system decomposes the LSTM network into two basic operations: **sparse matrix vector multiplication (SpMV) and elemental multiplication (ElemMul)**, and realizes concurrent execution among multiple computational units by controlling the operation flow through a state machine. And, the system is designed with a double-buffering mechanism to realize the overlapping of data transmission and computation, which further improves the efficiency of the system.
  
### 5. Issues addressed 
  The system solves the problem of latency due to high computational complexity in real-time speech recognition, enabling real-time response in speech recognition. Also, the system provides scalability and flexibility and can be applied to other similar deep learning tasks.
  
## Experiments
  This paper presents the authors' evaluation of the performance of the hardware system and the results of comparative experiments. First, the authors used the TIMIT speech dataset to evaluate the performance of model compression and a large private speech recognition dataset for testing. Then, they compared the hardware resource utilization with the results of the combined experiments.

For the experiments, the authors used an XCKU060 FPGA as the hardware platform, two external DDR3 memory modules, and a host program to send parameters and vectors to the programmable logic section and collect the corresponding results. The authors also used library functions such as MKL BLAS/cuBLAS and MKL SPARSE/cuSPARSE for the implementation of dense matrix operations and sparse matrix operations.

In terms of resource utilization, the authors found that the ESE gas pedal design almost completely utilizes the hardware resources of the FPGA. Each channel is configured with 32 PEs to balance between computation and data transfer. By adjusting the FIFO depth, the authors found that the highest utilization was achieved when the FIFO depth was 8. In addition, the authors measured the power consumption of CPU, GPU and ESE and derived the corresponding power consumption values.

In terms of speed and energy efficiency, the authors compared ESE with CPU and GPU. The authors found that ESE is 43 times faster than CPU and 3 times faster than GPU when processing LSTM models. Considering both performance and power consumption, ESE is 197.0x (dense) and 40.0x (sparse) more energy efficient than CPU and 14.3x (dense) and 11.5x (sparse) more energy efficient than GPU. Also, the sparse LSTM makes the CPU and GPU more energy efficient, which shows the advantage of the authors' pruning technique.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/511c3deb-6a01-48c6-a38b-b8a2b18555f4)

## Conclusion

### 1. Advantages of the Thesis
  1. Firstly, a method that can compress the LSTM model to 20 times of its original size without loss of prediction accuracy is proposed;
  
  2. Secondly, a scheduler is designed to efficiently map and parallelize complex LSTM operations on FPGAs;
  
  3. Finally, a hardware architecture that can efficiently handle the irregular computational patterns generated by the compression is proposed.
  
  Experimental results show that ESE achieves 282 GOPS on a Xilinx XCKU060 FPGA board, which is 43 and 3 times faster than Core i7 CPU and Pascal Titan X GPU, respectively, while its energy efficiency is 40 and 11.5 times higher than that of CPU and GPU.
  
### 2. Innovative points
 1. The main contribution of this paper is to propose an effective LSTM model compression algorithm that includes both pruning and quantization.
 
 2. The authors also particularly emphasize their proposed load-balancing-aware pruning and automatic process dynamic accuracy data quantization.

 3. In addition, they design a scheduler capable of efficiently scheduling complex LSTM operations and realizing memory references with computational overlap.
 
 4. Finally, the authors design a hardware architecture that can work directly on sparse models to improve computational and storage efficiency.

### 3. Future Works
  1. Coming research can further explore how to extend this approach to other types of RNNs, and more in-depth studies can be conducted to discover additional optimization strategies to further improve computational and storage efficiency.
  
  2. In addition, consideration can be given to how this approach can be applied to resource-constrained environments such as mobile devices to enable features such as real-time speech recognition.
