# Efficient LLM inference solution on Intel GPU
[paper link](https://arxiv.org/pdf/2401.05391) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper presents an efficient large-scale language model (LLM) reasoning solution, implemented on Intel GPUs and publicly released.         | large-scale language model (LLM)         |

## Methodology

### 1. Abstract
Traditional LLMs have a complex structure with many operations and reason in autoregressive mode, making the design of an efficient system a challenging task. The authors propose an approach to simplify the LLM decoder layer by fusing data movement and elemental operations to reduce the frequency of memory accesses and decrease system latency. In addition, they propose a segment key-value caching strategy for efficiently managing request and response tokens/values in the device memory to scale up the runtime batch size and improve system throughput. Finally, they design a customised Scaled-Dot-Product-Attention kernel that matches their fusion strategy.

### 2. Method Description 
The paper presents an efficient solution for LLM inference and implements it on Intel GPUs. The solution includes measures such as simplifying the model structure, optimising data access operations and designing a segmented KV caching algorithm.
First, to address the complexity of the LLM model structure, which contains a large number of operations, the authors simplify the structure of the Transformer decoding layer by reducing data movement operations and applying custom kernel fusion strategies. Second, to better manage device memory and improve throughput, the authors propose a shared hint key-value technique based on the segmented KV caching algorithm. Finally, the authors also designed a customised SDPA kernel to support their fusion policy and the segmented KV cache algorithm.

![image](https://github.com/user-attachments/assets/b10a7f36-e706-40cc-ad75-eba19ba9a8c2)

### 3. Methodological improvements
  1. Simplified the MHA structure by removing unnecessary data movement operations and reducing the computational complexity.
  2. Incorporated multiple operations, such as those in the RMSNorm, RoPE, and SDPA modules, reducing the number of computational steps.
  3. Applies the segmented KV cache algorithm to dynamically adjust the cache size to avoid excessive memory fragmentation and save memory space.
     
![image](https://github.com/user-attachments/assets/11963d64-6b0d-4e2d-b75a-9b56ddd276de)

### 4. Issues addressed 
  1. Multiple and time-consuming data movement operations due to the complex model structure;
  2. Large memory footprint of the device, which limits the batch size and system throughput;
  3. A large number of memory fragments in the KV cache, which affects memory utilisation.

## Experiments
This paper describes the authors' implementation of an LLM inference solution on Intel GPUs and performs several performance evaluation experiments. 

Firstly, the authors conducted an efficiency evaluation of the customised SDPA kernel, comparing the effect of using two different data layout approaches, batch and serialisation. The results show that using batch layout results in higher memory bandwidth utilisation and better performance efficiency at larger batch sizes.

![image](https://github.com/user-attachments/assets/341a3bbc-07f2-416c-8ce3-d988c0a41be3)

Next, the authors conducted system latency evaluation experiments to compare the latency performance of the standard HuggingFace scheme and the authors' proposed solution under different cue lengths. The results show that the latency of the standard scheme gradually increases as the length of the cue sequence increases, while the authors' proposed solution can achieve lower latency with higher hardware resource usage. In addition, the authors also compare the latency performance of the two schemes under different batch widths (BW) and find that the batch width has less impact on the scheme proposed by the authors, whereas the scheme proposed by the authors can significantly reduce the latency at high batch widths.

![image](https://github.com/user-attachments/assets/850c7191-cb3a-4de0-a3fd-89c4cceba326)

Finally, the authors conducted throughput evaluation experiments to compare the throughput performance of the standard HuggingFace scheme and the authors' proposed scheme under different batch widths. The results show that the authors' proposed scheme has a significant advantage in terms of throughput, which can achieve 8x to 27x improvement. This is mainly due to the segment-level KV caching approach proposed by the authors, which can save device memory and improve hardware resource utilisation. 

![image](https://github.com/user-attachments/assets/494bbed0-18ff-4015-8ad8-90f4154d270f)

## Conclusion

### 1. Advantages of the Thesis
The solution employs several innovative approaches to improve efficiency, including simplifying the decoding layer structure to reduce data movement overhead, designing a deep fusion strategy to combine matrix multiplication and scalar operations as much as possible, and proposing an efficient SDPA kernel based on a segmented KV caching strategy. 

### 2. Innovative points
  1. **Simplified decoding layer structure:** by merging data movement and scalar operations, the frequency of memory accesses is reduced, thus improving efficiency.
  
  2. **Deep fusion strategy:** combining GeMM and scalar operations as much as possible, further reducing the number of memory accesses.
  
  3. **Segmented KV caching strategy:** the key values of the cue and response are stored in the discrete device memory, which allows the key values of the cue to be shared by different response tokens and avoids memory waste.
  
  4.**Efficient SDPA kernel:** based on the above strategies and methods, an efficient SDPA kernel is designed to combine all computational steps with a possible index selection process for bundle search.

### 3. Future Works
  1. **Cross-platform optimisation:** extend the solution proposed in this study to other GPU or CPU platforms to achieve efficient reasoning in different hardware environments.
  
  2. **More complex models:** exploring how these optimisation techniques can be applied to more complex and deeper LLM models to further improve inference performance.
 
  3. **Real-time reasoning:** apply the solutions proposed in this study to real-time reasoning scenarios, such as speech recognition, machine translation, and other tasks, to meet real-time requirements.
  
  4. **Adaptive Optimisation:** Adaptively adjust the decoding layer structure, fusion strategy, and caching strategy according to the requirements of specific application scenarios to achieve the best inference results. 
