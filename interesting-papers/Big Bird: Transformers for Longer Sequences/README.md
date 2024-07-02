# Big Bird: Transformers for Longer Sequences
[paper link](https://arxiv.org/pdf/2007.14062) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper introduces a sparse attention mechanism called BIGBIRD, which aims to solve the memory overhead problem faced by Transformer-based models when processing long sequences         | Transformers          |

## Methodology

### 1. Abstract
  The method maintains the generalized approximation and Turing completeness of the sequence function by changing the attention mechanism from fully connected to sparsely connected and introducing a global labeling. Experimental results show that BIGBIRD is able to process longer sequences than before and significantly improves performance on various NLP tasks.
  
### 2. Method Description 
  The paper proposes a sparse attention mechanism and proves its expressive power in two ways: 
  <br>First, the sparse attention mechanism can be used as a universal approximator of a sequence-to-sequence function when the encoder alone is used.<br>Second, in contrast to previous research, the paper also proves that the sparse encoder-decoder converter is Turing-complete (assuming certain conditions are satisfied).
   
### 3. Methodological improvements
  Compared to the traditional full-attention mechanism, the sparse attention mechanism reduces the amount of computation and can reduce the number of parameters in the model by controlling the attention weights. This makes the sparse attention mechanism have better scalability and less memory requirement.
  
### 4. Issues addressed 
  The thesis addresses the theoretical nature of sparse attention mechanisms, including their expressive power and computational efficiency. By proving the strong expressive power and Turing completeness of the sparse attention mechanism, the study provides a theoretical foundation for the application of the sparse attention mechanism. <br> At the same time, the paper points out some limitations of the sparse attention mechanism, i.e., when the attention weights become very sparse, more layers are needed to achieve the same effect. These results are important for the further development of the sparse attention mechanism and its applications.
   
## Conclusion
### 1. Advantages of the Thesis
  1. The paper proposes a new sparse attention mechanism, BIGBIRD, which can effectively reduce the computational complexity while maintaining the expressive power of the model.

  2. Through theoretical analysis and experimental validation, the paper demonstrates the superior performance of BIGBIRD on several NLP tasks and that it can be applied to other fields, such as genomics data processing.

  3. The paper also presents some specific experimental results, including the effect of the pre-trained model, the performance of different lengths of text categorization tasks, etc., which further support the effectiveness and practicality of BIGBIRD.
     
### 2. Innovative points
  1. BIGBIRD uses a novel sparse attention mechanism that divides the attention weights into two parts: local attention and global attention, where the local attention focuses only on a few neighboring words, while the global attention considers the information of the whole sequence.

  2. The design of BIGBIRD is based on some important theoretical conclusions, such as the representational ability of sequence-to-sequence functions and Turing completeness, which makes BIGBIRD not only able to handle long sequences efficiently, but also has strong expressive power.

  3. In terms of concrete implementation, BIGBIRD adopts a scalable storage structure and efficient computational algorithms, which enable it to process large-scale datasets quickly.
     
### 3. Future Works
  1. Although BIGBIRD has achieved good results in several tasks, it still has some limitations, such as requiring a large amount of memory to store sparse matrices. Therefore, in future research, we need to explore more effective sparse attention mechanisms to solve these problems.

  2. In addition, although BIGBIRD has been successfully applied in fields such as NLP and genomics, its applications can continue to expand. We expect to see more researchers applying it to other fields such as CV and speech recognition.


