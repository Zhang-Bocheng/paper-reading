# Rethinking Attention with Performers
[paper link](https://arxiv.org/pdf/2009.14794) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper describes a novel Transformer architecture called Performers that estimates regular (softmax) full-rank attention Transformers using linear space and time complexity and does not require any a priori knowledge        |  Transformer         |

## Methodology

### 1. Abstract
Performers does this by using a novel called FAVOR+ orthogonal stochastic feature method to approximate the softmax attention kernel. In addition, FAVOR+ can be used to efficiently model attentional mechanisms that can be transformed into kernels, not just softmax. This representational capability is important for accurately comparing softmax to other kernels on large-scale tasks, beyond the scope of conventional Transformers, and investigating the optimal attentional kernel. 

Experimental results show that Performers' performance on rich tasks such as pixel prediction, text modeling, and protein sequence modeling is comparable to other efficient sparse and dense attentional methods that have been examined, demonstrating the effectiveness of Performers in leveraging novel attentional learning paradigms.

### 2. Method Description 
The paper proposes a new mechanism, FAVOR+, for efficiently estimating orthogonal random features (ORFs) and applying it to the attention mechanism. The mechanism consists of two parts: **the R+ part and the O part**. In the R+ part, the authors propose a new orthogonal random feature estimation algorithm that can be used to accurately approximate softmax and Gaussian kernel functions. In Part O, the authors use the standard Gram-Schmidt orthogonalization procedure to ensure orthogonality between random samples and further reduce variance.

![image](https://github.com/user-attachments/assets/757fc448-b204-4b72-af07-edc5b8ce27fc)

### 3. Methodological improvements
The main improvement of FAVOR+ over traditional randomized feature algorithms is the introduction of orthogonal random features (ORFs), which helps to reduce variance and improve accuracy. In addition, the authors propose a new orthogonal stochastic feature estimation algorithm that can be applied to attention mechanisms in various dimensions and situations.

### 4. Issues addressed 
The paper addresses the following issues:

  1. How to efficiently estimate orthogonal random features (ORFs) for more accurate attention mechanisms.
  2. How to deal with the limitations of non-negativity in order to be able to apply orthogonal random features (ORFs) to approximate softmax and Gaussian kernel functions.

By introducing orthogonal random features (ORFs) and a new orthogonal random feature estimation algorithm, FAVOR+ can significantly improve the accuracy and efficiency of the attentional mechanism while satisfying the constraints of non-negativity and orthogonality.

![image](https://github.com/user-attachments/assets/97d70202-9255-4508-a808-a286e3f69880)

## Experiments
This paper focuses on the approximation of the attention mechanism using the Performer model, which is validated and compared with several experiments. Specifically, the authors conducted the following experiments:

**Computation Cost Comparison Experiment**: the authors compare the computational cost of Performer and Transformer in a bidirectional language modeling task, and find that Performer achieves near-linear speedup and lower memory consumption.

![image](https://github.com/user-attachments/assets/2f1799f1-93b0-4461-9bd1-093e23d32e78)

**Attentional Approximation Error Experiment**: The authors compare the attentional approximation error of Performer with different feature types (orthogonal features, sinusoidal cosine features) and random sampling strategies (no resampling, periodic resampling), and find that the orthogonal features and periodic resampling strategies are better at reducing the error.

**Experiments on the Effectiveness of Softmax Approximation in Transformer**: The authors applied Performer's Softmax approximation to Transformer and compared it with other models. The results show that better performance can be obtained with Performer, especially on large datasets.

![image](https://github.com/user-attachments/assets/85360d4e-62a0-40e6-88f9-f120e982dad0)

**Experiments on Multi-Layer Training Protein Sequence Classification**: The authors apply Performer to a multi-layer training protein sequence classification task and compare it with Reformer and Linformer. The results show that Performers can achieve higher accuracy and have smaller memory consumption. 

![image](https://github.com/user-attachments/assets/3677527f-b83a-4024-8224-72dca0a7e906)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new Transformer architecture, Performers, and uses the Fast Attention Via positive Orthogonal Random features (FAVOR+) mechanism to significantly improve the traditional Transformer's space and time complexity.
  
  2. Through efficient unbiased estimation, the mechanism provides linear space and time complexity to the original softmax-based Transformer and provides new ideas for studying efficient Transformer architectures.
  
  3. In addition, the method can be applied to the research in the fields of biological sequence analysis, environment, and attention mechanism, which has a wide range of application prospects.

### 2. Innovative points
  1. The main contribution of this thesis is to propose a new Transformer architecture, Performers, and realize the effective unbiased estimation of softmax-based Transformer using the FAVOR+ mechanism.
  
  2. The method not only significantly reduces the computational cost and space complexity, but also provides strong theoretical guarantees by being fully compatible with the traditional Transformer.
  
  3. In addition, the method can be extended to other kernel function-based attention mechanisms, such as Gaussian kernel function, etc., which provides new ideas for studying efficient attention mechanisms.
     
### 3. Future Works
  1. Future research directions include further optimizing the performance of the algorithm, exploring a wider range of attention mechanisms, and applying the method to more fields, such as image processing and speech recognition.
  
  2. Meanwhile, the mathematical principles of the FAVOR+ mechanism need to be explored in depth to better understand its mechanism of action and develop a more efficient method.
