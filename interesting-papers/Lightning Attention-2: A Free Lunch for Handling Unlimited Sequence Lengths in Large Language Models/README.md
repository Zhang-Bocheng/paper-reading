# Lightning Attention-2: A Free Lunch for Handling Unlimited Sequence Lengths in Large Language Models
[paper link](https://arxiv.org/pdf/2401.04658) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a linear attention mechanism called ‘Lightning Attention-2’, which can process sequence data of infinite length without sacrificing speed, and maintains consistent training and inference speeds across different model sizes and sequence lengths.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The method employs the block idea to handle linear attention computation for internal and external blocks separately, and utilises the traditional attention computation mechanism for internal blocks and the linear attention kernel trick for external blocks. At the same time, the GPU hardware is fully utilised by the block technique in both forward and backward processes.

![image](https://github.com/user-attachments/assets/4ff85dac-f3f6-4a13-8d00-22a2c247f29d)

### 2. Method Description 
This paper proposes a new self-attention mechanism, Lightning Attention-2, for dealing with computational efficiency in sequence prediction tasks. The method employs matrix multiplication and recursive computation to optimise memory usage while maintaining efficient computation.

Lightning Attention-2 employs a tiling strategy, which splits the input sequence into equal-sized chunks and computes the left and right matrix products separately within each chunk. In this way, the difference in memory bandwidth between HBM and SRAM in GPUs can be fully utilised to improve computational efficiency. At the same time, the method also takes advantage of recursive computing to achieve fast and efficient self-attentive computation.
 
![image](https://github.com/user-attachments/assets/ed4a5a0e-0e59-4742-8479-b6b936d3b5c7)

![image](https://github.com/user-attachments/assets/08ceebcd-8624-44e0-82fe-94c04123bd7c)

### 3. Methodological improvements
Compared with the traditional softmax attention mechanism, Lightning Attention-2 employs linear attention computation, which eliminates the expensive softmax and scaling operations and greatly improves the computational efficiency. In addition, the method also adopts a chunking strategy to further optimise memory usage, making the computation process more efficient.

### 4. Issues addressed 
The traditional self-attention mechanism suffers from high computational complexity when dealing with long sequences, resulting in long training time. Lightning Attention-2, on the other hand, effectively solves this problem by adopting linear and recursive computation methods as well as chunking strategy, which allows the model to complete training in a shorter time. In addition, the method can also achieve the computation of infinitely long sequences in the inference process, which has strong practical application value.

## Experiments
This paper focuses on the performance of the TransNormerLLM model using the Lightning Attention-2 module in a number of areas and comparative experimental results. Specifically, it includes:

**Attention Module Evaluation:** this section compares the speed and memory usage of the Lightning Attention-1, Lightning Attention-2 and FlashAttention-2 modules and concludes that Lightning Attention-2 has the superior performance of linear growth, and its speed advantage becomes more and more obvious as the sequence length increases. At the same time, the method is able to significantly reduce memory usage.

**Language Modeling Comparison:** This section compares two versions of the TransNormerLLM-0.4B model, one equipped with Lightning Attention-1 and the other with Lightning Attention-2, by using the TransNormerLLM-0.4B model. in After 100,000 iterations with 8 A100 80G GPUs, the performance difference between the two versions was observed to be very small, with the version with Lightning Attention-2 having a decrease of only 0.001 compared to the version with Lightning Attention-1.

**Efficiency Evaluation:** This section compares the training speed of three different models, TransNormerLLM with Lightning Attention-2, TransNormerLLM with Lightning Attention-1, and LLAMA- FA2. The results show that the TGS values of Lightning Attention-2 always maintain a high level throughout the change of sequence length from 1K to 92K, while the other two models show a rapid decreasing trend, which suggests that Lightning Attention-2 has a significant advantage in dealing with unrestricted sequence lengths.

**Benchmarking Lightning Attention-2 in Large Language Model:** this section analyses the TransNormerLLM-15B model, which consists of 1.5 billion parameters with 42 layers, 40 headers, and 5120 dimensional embedding dimensions . In two key domains evaluated using the lm-evaluation-harness framework, namely commonsense reasoning (CSR) and multiple-choice questions (MCQs), TransNormerLLM-15B outperforms Pythia-12B in all tasks, especially in the HellaSwag task, the TransNormerLLM-15B showed an improvement of about 3.5% relative to its 5 billion token phase. In addition, TransNormerLLM-15B also outperformed Pythia-12B by about 2% in the overall results.

![image](https://github.com/user-attachments/assets/8106400d-815e-4662-8418-07fa750d81c9)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a linear attention computation method called ‘Lightning Attention-2’, which successfully solves the challenges of current linear attention algorithms and outperforms the existing optimal state attention mechanisms in terms of training speed and accuracy. The approach employs the concepts of ‘divide-and-conquer’ and tiling techniques to divide the computation into intra-block and inter-block components, effectively utilising the GPU hardware to achieve maximum efficiency.
  
  2. In addition, the method accelerates the computation by using convolutional operations, thus eliminating the cumulative summation problem and enabling it to achieve theoretical training speedups in causal settings. Experimental results show that Lightning Attention-2 not only maintains consistent training speeds, but also processes large-scale datasets faster than other methods regardless of input sequence length.

### 2. Innovative points
The method adopts the concepts of ‘divide-and-conquer’ and tiling techniques to deal with intra-block and inter-block computations separately, and accelerates the computation through convolutional operations, thus eliminating the cumulative summation problem. In addition, the method makes full use of GPU hardware to ensure efficient computation speed. 

### 3. Future Works
The authors plan to introduce sequence parallelism in future research to better handle ultra-long sequences and overcome existing hardware limitations. This will further advance the application and development of large-scale language models.  
