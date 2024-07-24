# Linformer: Self-Attention with Linear Complexity
[paper link](https://arxiv.org/pdf/2006.04768.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces a new self-attention mechanism, Linformer, which achieves efficient processing of long sequences by converting the self-attention mechanism in the standard Transformer into the form of a low-rank matrix and reducing its complexity from O(n^2) to O(n).          | Transformer          |

## Methodology

### 1. Abstract
Experimental results show that Linformer is more memory and time efficient with comparable performance to the standard Transformer model. This research is important for solving the problem of high cost of training and deployment of large Transformer models.

### 2. Method Description 
The paper proposes a new self-attention mechanism, Linear Self-Attention, designed to reduce memory consumption and computational complexity. The method implements a low-dimensional projection by adding two linear projection matrices, and then converts the low-dimensional vectors to high-dimensional vectors using weighted averaging. This allows the self-attention matrix to be computed in linear time without adding additional complexity and requires very little memory space.

![image](https://github.com/user-attachments/assets/94248ae7-48b7-4507-949e-04821bf71ce4)

### 3. Methodological improvements
Traditional self-attention mechanisms require a large number of computations in calculating the self-attention matrix, resulting in high computational complexity. Linear self-attention, on the other hand, reduces the computational complexity by reducing the dimensionality, thus improving the computational efficiency. In addition, the method can select different projection dimensions according to different layers and heads to further improve the computational efficiency.

![image](https://github.com/user-attachments/assets/1ac93304-7240-4c7c-9f86-d74524075e8a)

### 4. Issues addressed 
The traditional self-attention mechanism encounters the problem of high computational complexity when dealing with long sequential data, resulting in long computation time. Linear self-attention solves this problem by reducing the dimensionality, resulting in faster computation and less memory usage. This approach can be applied to various natural language processing tasks, such as text categorization, machine translation and so on.

## Experiments
  This paper focuses on the performance of the Linformer model on pre-training and downstream tasks and compares it with Transformer. Specifically, the authors conducted the following four comparison experiments:

**Pre-training effect comparison experiment**: the authors used BookCorpus and English Wikipedia as the pre-training datasets, adopted the Masked Language Modeling (MLM) loss function to pre-train Linformer and Transformer, and compared the validation perplexity curves of Linformer with different projection dimensions and sharing strategies. 

The results show that Linformer performs better and better as the projection dimension increases, and even approaches the performance of the original Transformer at n=512 and k=128. Moreover, when only a single projection matrix is used, i.e., the hierarchical sharing strategy, the verification perplexity of Linformer is almost equal to that of the non-shared model, which suggests that reduce the number of additional parameters in the model and thus reduce the memory consumption without much impact on the performance.

**Sequence Length Comparison Experiment**: The authors investigated the effect of sequence length on Linformer pre-training and compared the validation perplexity curves under different sequence lengths. The results show that with a fixed projection dimension of 256, the final perplexity remains constant as the sequence length increases, further supporting the idea that Linformer is linear time.

**Experiments comparing performance on downstream tasks**: the authors applied Linformer to downstream tasks such as IMDB, SST-2, QNLI, and QQP, and compared it to RoBERTa, 12-layer Bert-base, and 6-layer distilled Bert. All models were fine-tuned using the same pre-training target, pre-training corpus and up to 250k updates. 

The results show that the Linformer model (n=512, k=128) has comparable performance to RoBERTa on downstream tasks, and even slightly outperforms it at k=256. In addition, Linformer's hierarchical sharing strategy actually exhibits better accuracy results than the other two sharing strategies, despite the fact that it shares a projection matrix throughout the model. 

**Reasoning Efficiency Comparison Experiments**: the authors compare the efficiency of Linformer and standard Transformer in terms of reasoning time and memory, and report the amount of time and memory saved for various projection dimensions k and sequence lengths n. 

The results are summarized as follows. The results show that Linformer is 1.5 times faster than Transformer even for n=512 and k=128, allowing for larger maximum bulk sizes. The speedup in inference time and memory savings are even more significant as the sequence length increases. Also, the authors plotted the inference time of Linformer and Transformer on 100 samples.

![image](https://github.com/user-attachments/assets/23097937-50e3-4916-a14c-72f928bc6412)

![image](https://github.com/user-attachments/assets/75de9d1d-bf52-4b42-b10a-665d001c6d7e)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper reduces the time complexity of self-attention to O(n) and the space complexity accordingly by decomposing self-attention into multiple small attention operations and forming a low-rank factorization.
  
  2. In addition, the method has potential applications to improve the efficiency and accessibility of NLP models, as well as to support longer sequence lengths.

### 2. Innovative points
  1. The method achieves efficient computation by decomposing self-attention into multiple small attention operations and combining them into a low-rank matrix using linear projection.
  
  2.  This innovative approach can significantly improve the efficiency and accessibility of natural language processing models without sacrificing performance.
      
### 3. Future Works
  1. Future research directions may include further optimizing the method to improve its performance and efficiency, as well as exploring how to extend the method to other types of neural network structures.
  
  2. In addition, it may also be investigated how to combine the method with other techniques, such as sparsity and locally sensitive hashing, to achieve higher efficiency and better performance.
