# FP6-LLM: Efficiently Serving Large Language Models Through FP6-Centric Algorithm-System Co-Design
[paper link](https://arxiv.org/pdf/2401.14112) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This thesis focuses on how to improve the performance and efficiency of Large Language Models (LLMs) through FP6 quantisation techniques.          |  Large Language Models (LLMs)        |

## Methodology

### 1. Abstract
Existing systems have problems such as unfriendly GPU memory access and high weight dequantisation runtime when supporting FP6 quantisation. To address these issues, the authors propose a TC-FPx full-stack GPU kernel design solution and integrate it into an existing inferencing system to provide new end-to-end support (called FP6-LLM) for quantised LLM inferencing. Experimental results show that FP6-LLM is able to achieve higher inferencing throughput while maintaining consistent model quality.

![image](https://github.com/user-attachments/assets/2e7876a9-f95c-40b3-a1c9-942ca6e7e7e7)

### 2. Method Description 
This paper presents a GPU kernel called TC-FPx for accelerating the computation of quantised Low-Latency Matrix Multiplication (LLM). The kernel combines memory prefetching, optimised data layout and efficient SIMT-Efficient GPU runtime techniques to reduce computation time and memory access time and improve model accuracy without adding extra overhead.

The TC-FPx kernel uses a customised data storage format that splits the quantisation weight matrix into multiple 2-bit or 4-bit chunks with a pre-computed table of constants to enable conversion from quantisation to floating point. It also employs optimised SIMT core instructions to process these chunks in parallel, further improving computational efficiency.

In addition, the core exploits the features of modern GPU memory hierarchies to reduce memory access latency through prefetching techniques and optimised data layout. Specifically, it loads the quantisation weight matrix into shared memory and loads the chunks according to a predefined memory layout order, thus reducing the number of unnecessary memory accesses.

![image](https://github.com/user-attachments/assets/a952562f-5487-4084-949d-660cb6c41c61)

### 3. Methodological improvements
  1. **Use of a customised data storage format:** the quantisation weight matrix is split into multiple 2-bit or 4-bit chunks and the conversion from quantisation to floating-point is implemented using a pre-computed table of constants.
  2. **Optimised SIMT core instructions:** small chunks are processed in parallel to further improve computational efficiency.
  3. **Leveraging modern GPU memory hierarchy features:** memory access latency is reduced by prefetching techniques and optimised data layout.

![image](https://github.com/user-attachments/assets/2bfd375f-3ec5-44ce-9969-5bfa8dd1372e)

### 4. Issues addressed 
  1. **Reducing computation time and memory access time:** through optimised data layout and efficient SIMT-Efficient GPU runtime techniques.
  2. **Improved model accuracy:** Improved model accuracy without adding extra overhead.
  3. **Supports end-to-end quantised low-precision matrix multiplication computation:** integrating the TC-FPx kernel into existing deep learning frameworks provides efficient support for quantised low-precision matrix multiplication.

## Experiments
This paper focuses on a number of sets of comparative experiments conducted on the end-to-end reasoning performance of large-scale language models, and analyses and summarises their results.

Firstly, in the linear layer speed comparison experiments, the authors used a number of different workloads to test the performance difference between TC-FPx and other baseline methods such as cuBLAS and TensorRT-LLM. By comparing different shapes of weight matrices and different batch sizes, the authors draw the following conclusions:

  1. TC-FPx is 2.6 times faster than cuBLAS and 1.9 times faster than W8A16 of TensorRT-LLM;
  2. In the case of small batches, cuBLAS cannot fully utilise the GPU hardware cells, while TC-FPx support for 6-bit quantisation can significantly reduce DRAM accesses and thus improve computational efficiency;
  3. Compared with cuBLAS, BitsandBytes is slower because it adopts a dual-core approach to support FP4 quantisation, resulting in additional GPU core overhead.

![image](https://github.com/user-attachments/assets/e42973bc-6d9d-4949-b939-2c0ec3ca7b6d)

Second, in the 4-bit quantisation experiments, the authors compare TC-FPx with existing W4A16 support methods (e.g. Coarse-grained_W4A16 and Fine-grained_W4A16). The results show that the W6A16 performance of TC-FPx is comparable to or even slightly better than Fine-grained_W4A16, suggesting that 6-bit quantisation can achieve faster inference while maintaining model quality.

![image](https://github.com/user-attachments/assets/d5fdc171-e093-4f75-a4f3-33e49237774d)

Finally, in terms of end-to-end inference performance, the authors tested several large language models (e.g., LLaMA-65b, OPT-30b, and LLaMA-70b) and compared them to FP16 execution on the DeepSpeed system. The experimental results show that higher inference throughput can be achieved using TC-FPx and a single GPU while avoiding the NCCL overhead of cross-GPU communication. Specifically, FP6-LLM achieves 1.69x to 2.65x higher inference throughput compared to the FP16 benchmark.
 
## Conclusion

### 1. Advantages of the Thesis
  1. A unified Tensor Core supporting floating-point weights is proposed, enabling GPUs to support linear layer computations with arbitrary bit-widths.
  2. The SIMT core is utilised to efficiently handle the dequantisation operations of model weights, while optimising GPU memory access efficiency.
  3. The unfriendly memory access problem is solved by the AOT bit-level pre-packing technique, enabling the GPU to utilise the memory space more efficiently.
  4. Better LSTM inference performance and higher model quality are achieved under the existing GPU hardware constraints.

### 2. Innovative points
  1. Unified support for linear layer computation with different quantisation bitwidths, providing more options for practical applications.
  2. Efficiently handles the dequantisation operation of model weights using SIMT core, which reduces the computation time and memory occupation.
  3. Memory access efficiency is optimised by AOT bit-level pre-packing technique, which further improves GPU utilisation.
  4. Higher accuracy LSTM inference performance and higher model quality are achieved, providing better results for practical applications.

### 3. Future Works
  1. Explore more efficient GPU architectures and algorithms to achieve efficient reasoning on larger scale LLMs.
  2. Investigate how to further improve the quality of models, including issues such as improving the generalisation ability of models and reducing overfitting.
  3. Develop smarter adaptive quantisation strategies so that parameters such as quantisation bits and accuracy can be automatically adjusted according to different application scenarios.   
