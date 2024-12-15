# Infinite-LLM: Efficient LLM Service for Long Context with DistAttention and Distributed KVCache
[paper link](https://arxiv.org/pdf/2401.02669) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a novel language modelling service system called Infinite-LLM, which is designed to effectively deal with the dynamic context length problem.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The system achieves flexible and independent resource scheduling by separating the attention layer from the reasoning process and exploiting GPU memory policies in the cluster, optimising computational performance and improving memory utilisation. Experimental results show that when tested on a dataset containing several to 2 million token context lengths, Infinite-LLM improves throughput by 1.35-3.4 times over existing approaches, enabling efficient and resilient language model deployment.

![image](https://github.com/user-attachments/assets/26b2746f-da14-4357-a6e4-2038fa4b11de)

### 2. Method Description 
The paper presents a system called Infinite-LLM, which aims to improve the performance of large-scale natural language processing models such as GPT-4. The system employs distributed attention computing techniques and is optimised for the computational and memory resource allocation problems that exist in traditional LSTM models.

Specifically, Infinite-LLM splits a long text task into multiple short text tasks, each of which is processed in parallel by different GPU instances. During processing, Infinite-LLM uses a distributed attention computation technique to spread the attention computation to different GPU instances, thus reducing the computational pressure on a single GPU instance. In addition, Infinite-LLM further improves the performance by dynamically adjusting the memory resource allocation among different GPU instances.

![image](https://github.com/user-attachments/assets/cb583809-b6ae-4e05-9c46-24d73965e528)

### 3.  Methodological improvements
Compared with the traditional LSTM model, Infinite-LLM adopts a more flexible memory resource allocation strategy, which can better adapt to text requests of different lengths. At the same time, Infinite-LLM also introduces distributed attention computation technology, which enables long text tasks to be processed more efficiently.

![image](https://github.com/user-attachments/assets/3a58205e-bb62-44cf-a5a6-52800e020fa8)

### 4. Issues addressed 
The traditional LSTM model suffers from insufficient computational and memory resources when processing long text tasks, resulting in performance degradation. Infinite-LLM, however, solves these problems and improves the performance of large-scale natural language processing models by means of distributed attention computing techniques and dynamic memory resource allocation strategies.

## Experiments
This paper focuses on the performance of Infinite-LLM in different scenarios and compares it with static model parallelism and resource planning methods. Specifically, the following comparison experiments are conducted in this paper:

**Context Length Performance:** this experiment compares the performance difference between Infinite-LLM and vLLM-multi and vLLM-single. The experiment uses six different context length ranges and three different model sizes and tests the maximum throughput for each data point. The results show that Infinite-LLM maintains high throughput for short sequences while supporting longer context lengths, providing better performance relative to vLLM-multi and vLLM-single.

![image](https://github.com/user-attachments/assets/095999a2-971e-4b87-adf0-459efb59cb3f)

**End-to-end Serving Performance:** This experiment compares the performance difference between Infinite-LLM and vLLM-multi and vLLM-single. The experiment uses three different request rates and two different request distributions to compare the impact of different numbers of instances on performance. The results show that Infinite-LLM performs better relative to vLLM as the number of instances increases and the unevenness of the request distribution increases.

![image](https://github.com/user-attachments/assets/824ced0e-db03-4082-8102-fe7f8781fc85)

**Micro-benchmarks:** This experiment compares the performance difference between different long sequence attention computation methods such as DistAttention, RingAttention and TP. The experiment uses the LLaMA2-13B model on four GPUs and tests the performance over a range of contexts. The results show that DistAttention has better communication efficiency relative to TP and higher performance advantage relative to RingAttention.

![image](https://github.com/user-attachments/assets/a668ff87-5fab-4e18-a9d9-a298e786333e)
 
## Conclusion

### 1. Advantages of the Thesis
  1. A system called Infinite-LLM is proposed to solve the highly dynamic request length problem.
  2. Efficient scheduling strategies are designed that are able to utilise both the computational and bandwidth resources of the GPU.
  3. Extensive evaluations are performed on representative real datasets and show significant performance improvements.

### 2. Innovative points
  1. Efficient processing of requests of different lengths is achieved using a novel system architecture.
  2. Introduced attention allocation techniques to improve computational efficiency and reduce memory requirements.
  3. Developed a scalable architecture for LLM services that supports large-scale deployment and high-performance computing.

### 3. Future Works
  1. Possible further optimisation of scheduling strategies for more efficient resource utilisation.
  2. Further investigate how to adjust the parameter settings of the system in different application scenarios.
  3. Explore applying the concept of infinite length requests to other types of deep learning models.  
