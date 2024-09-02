# Efficient Memory Management for Large Language Model Serving with PagedAttention
[paper link](https://arxiv.org/pdf/2309.06180) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper focuses on the memory management problem in Large Language Model (LLM) services and proposes an algorithm called PagedAttention and a system called vLLM to solve this problem.           |  LLM        |

## Methodology

### 1. Abstract
In existing systems, each request requires the use of a large amount of cached memory that grows and shrinks dynamically, leading to memory waste and limiting batch sizes. To address this problem, the authors, inspired by operating system virtual memory and paging techniques, designed an algorithm based on the attention mechanism and built on top of it an LLM service system, vLLM, which is able to share cache memory flexibly and achieve zero wastage. Experimental results show that, compared to the current state-of-the-art systems, vLLM can significantly improve the throughput, especially when dealing with longer sequences, larger models and more complex decoding algorithms. In addition, the source code of vLLM has been publicly released for others' reference.

### 2. Method Description 
This paper proposes the implementation of various decoding algorithms using three key methods: **fork, append and free**. Among these methods, fork method is used to create a new sequence, append method is used to append new tokens to the sequence and free method is used to delete the sequence. These methods are used in different decoding algorithms such as parallel sampling, bundle search and prefix sharing.
![image](https://github.com/user-attachments/assets/e480d318-b9b9-4474-81b5-0857f61764a2)

### 3. Methodological improvements
By using these methods, vLLM can easily support multiple decoding algorithms and can flexibly switch between different algorithms. For example, in parallel sampling, vLLM uses the fork method to create multiple output sequences and uses the append method to add new tokens to these sequences in each iteration. When the stop condition is met, it removes these sequences using the free method. Similarly, bundle search and prefix sharing use this method strategy.
![image](https://github.com/user-attachments/assets/1b8b041c-1452-4be6-ba1e-6f1490e30335)

### 4. Issues addressed 
The decoding algorithm approach proposed in this paper can help improve the performance of NLP models, especially in cases where multiple possible solutions need to be considered simultaneously. In addition, the method can help researchers better understand the differences between different decoding algorithms and provide a basis for future research.

## Experiments
This paper focuses on vLLM, a multi-model heterogeneous computing platform based on a shared cache mechanism, and evaluates and optimises its performance through several comparative experiments.

First, the authors used the OPT model (with parameters 13B, 66B, and 175B, respectively) and LLaMA52 (with parameter 13B), as well as the NVIDIA A100 GPU on the A2 instance, in their experiments on the Google Cloud Platform. They used the ShareGPT51 and Alpaca50 datasets to synthesise workloads to measure performance under different models and system configurations.

Next, the authors compare vLLM's basic sampling (one sample per request) with different sampling methods such as parallel sampling and bundle search. The results show that vLLM is able to efficiently manage memory usage to achieve higher request rates than Orca and FasterTransformer while maintaining similar latency. In addition, the authors investigate the performance impact of factors such as dynamic block mapping and block size selection in PagedAttention, and compare the efficiency differences between two recovery mechanisms, recomputation and swapping. 
![image](https://github.com/user-attachments/assets/bed5f5aa-68fe-4da8-a023-3423b7015ad7)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new attention algorithm, PagedAttention, and applies it to a high throughput LLM service system, vLLM. pagedAttention uses virtual memory and paging techniques to manage the KV cache of requests in order to improve memory utilisation and reduce memory fragmentation.
  
  2. And, vLLM uses techniques such as block-level memory management and pre-request scheduling to further improve the performance of the system. Experimental results show that vLLM achieves 2-4 times throughput improvement compared to existing systems under various models and workloads without affecting model accuracy.
 
### 2. Innovative points
  1. The main contributions of the paper are the proposed PagedAttention algorithm and the vLLM system. pagedAttention divides the requested KV cache into fixed-size blocks and allows these blocks to be stored in non-contiguous page space, thus making better use of GPU memory resources.
  
  2. vLLM, on the other hand, through techniques such as block-level memory management and pre-request scheduling, further optimises memory allocation and task scheduling, enabling the system to efficiently handle multiple requests and maintain high performance.
     
### 3. Future Works
In the future, it can further explore how to combine other techniques and algorithms, such as distributed computing and dynamic planning, to further improve the performance and scalability of LLM services. In addition, it can be considered how to implement similar solutions on different types of hardware devices to meet the needs of more application scenarios.
