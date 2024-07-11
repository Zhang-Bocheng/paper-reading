# Fastformer: Additive Attention Can Be All You Need
[paper link](https://arxiv.org/pdf/2108.09084) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper presents an efficient Transformer model called Fastformer for text understanding tasks.         | Transformer          |

## Methodology

### 1. Abstract
   While traditional Transformer models are inefficient when dealing with long sequences, Fastformer achieves efficient context modeling with linear complexity by using an additive attention mechanism for global context modeling and further transforming each token according to its interaction with the global context in which it resides. Experimental results show that Fastformer is more efficient than many existing Transformer models and can achieve with even better long-term text modeling performance.

### 2. Method Description 
  This paper proposes a new self-attentive mechanism, Fastformer, that summarizes query sequences by using an additive attention mechanism and captures global contextual information using element products. Specifically, the model first transforms the input embedding matrix into a sequence of queries, keys, and values, and then transforms it into an attention query, key, and value matrix using three separate linear transformation layers.
  
  The query matrix is compressed into a global query vector using an additive attention mechanism to capture global context information. Then, an elementwise product is used to compute the interaction between the global context vector and the key matrix, and the results are merged into the global context-aware key matrix. Finally, the interaction between the global key vectors and the value matrix is computed using the product of elements and its hidden representation is learned using a linear transformation. 
  
![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/980d889c-3a10-47cb-9699-35d9f1b72d18)

### 3. Methodological improvements
  Compared to the traditional Transformer architecture, Fastformer employs a more efficient additive notation mechanism, which reduces the computational complexity to a linear level. In addition, Fastformer employs a weight-sharing technique that reduces the number of parameters, further minimizing the risk of overfitting.
  
### 4. Issues addressed 
  Fastformer aims to improve the efficiency of Transformer on long sequences while maintaining good performance. The traditional Transformer structure will have serious computational bottlenecks when dealing with long sequences, while Fastformer effectively solves this problem by using an additive attention mechanism and weight sharing techniques.
  
## Experiments
  This paper focuses on the performance of the Fastformer model on different tasks and compares it with other Transformer variants. Specifically, the authors conducted the following five experiments:

The performance of Fastformer and other Transformer variants on three categorization tasks, including the standard Transformer, Longformer, BigBird, Linformer, and Linear Transformer methods, were compared. The results show that the  Fastformer can achieve comparable or even better performance than these efficient Transformer variants.

In the news recommendation task, Fastformer was compared to three other recent approaches, including NRMS, FIM, and PLM-NR. The results show that Fastformer achieves the best performance in all cases and can further improve the performance of PLM-NR.

Experiments on text summarization tasks were conducted to verify the effectiveness of Fastformer in natural language generation. The results show that Fastformer can achieve the best performance.

The theoretical computational complexity and practical training and inference costs of Fastformer and other Transformer variants are compared. The results show that Fastformer has linear computational complexity and is more efficient than other efficient Transformer variants in both training and reasoning time.

The impact of using different functions to model the interaction between queries, keys and values on Fastformer is investigated. The results show that the element product function is the best choice because it better captures complex contextual relationships.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/09e44b00-7368-4c7a-9583-130b61919e89)

## Conclusion

### 1. Advantages of the Thesis
   This paper inputs query matrix is compressed into a global query vector using the additive attention mechanism; then, the global context-aware key matrix is learned by elementwise product and further compressed into a global key vector, and then the global keys and values are aggregated using elementwise product, and finally the global context-aware attention value is computed by a linear transformation. 
   
   1. These operations allow Fastformer to efficiently model global contextual information with linear computational complexity.
   
   2. In addition, the authors conduct extensive experiments to validate the effectiveness and efficiency of Fastformer and demonstrate its excellent performance in long text modeling tasks.
      
### 2. Innovative points
   1. The input query matrix is compressed into a global query vector using an additive attention mechanism;
   
   2. Learning the global context-aware key matrix by elementwise product and further compressing it into a global key vector, then aggregating the global keys and values using elementwise product, and finally computing the global context-aware attention value by a linear transformation.

  These points allow Fastformer to efficiently model global context information with linear computational complexity. 
  
### 3. Future Works
  1. The authors plan to pre-train Fastformer-based language models in future work to better support long document modeling in NLP tasks.
  
  2. In addition, they will explore applying Fastformer to other scenarios such as e-commerce recommendation and advertising CTR prediction to improve user modeling capabilities.
     
