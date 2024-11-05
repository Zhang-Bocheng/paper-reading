# Linear Transformers with Learnable Kernel Functions are Better In-Context Models
[paper link](https://arxiv.org/pdf/2402.10644) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores how to improve the performance of language modelling with sub-secondary architectures in NLP.           | Transformers         |

## Methodology

### 1. Abstract
The authors find that existing innovative approaches, while outperforming Transformer on language modelling tasks, are deficient in context learning capabilities. Therefore, they propose a hybrid model of convolutional networks based on linear transformer and Taylor series expansion, and improve it to enhance its context learning capability. Experimental results show that this improved model performs well in multi-query association recall tasks and overall language modelling processes.

### 2. Method Description 
The paper proposes a Linear Transformer (LTR) based model, Based, for dealing with the problem of attention mechanisms in long sequence tasks. Compared with the traditional Transformer model, Based changes the complexity from quadratic to linear increase by using a nonlinear kernel function instead of directly computing the similarity. In experiments, the Based model performs well with large-scale context lengths and constrained model capacity, and has better performance than the Mamba model.

![image](https://github.com/user-attachments/assets/f960aee4-eb0d-4c26-bec7-b4a27a338282)

### 3. Methodological improvements
This paper further investigates the basic requirements of the Based model, including exploring the limitations of the exponential function and its approximate representation, and proposes improvements. Firstly, the nadir is adjusted to minimise the kernel function to zero, but this may lead to undesirable training results and reduced model accuracy. Therefore, the authors suggest considering a range of potential qT k values and creating adjustable parameters to accommodate these values for training. By introducing learnable parameters and layer normalisation techniques, the ReBased model achieves the learnability of arbitrary non-negative quadratic functions and the requirement of a single real root, while improving model performance.

### 4. Issues addressed 
The Based model solves the problem of inefficiency of the attention mechanism that exists in the traditional Transformer model when dealing with long sequences. By introducing linear transformers and adjustable quadratic kernel functions, as well as layer normalisation techniques, the ReBased model further optimises the Based model to better cope with large-scale context lengths and constrained model capacity. This approach helps to improve model performance and address problems in existing models.

## Experiments
This paper focuses on the results of experiments comparing the ReBased model based on the self-attention mechanism with other alternatives in an association retrieval task and a language modelling task. Specifically, the authors conducted the following five experiments:

**MQAR experiment:** the authors tested the performance of different models at different sequence lengths and compared the results with the traditional model based on the self-attention mechanism. The results show that the ReBased model performs better than the other models at longer sequence lengths, especially when using larger model sizes.
![image](https://github.com/user-attachments/assets/da5b7857-519e-4593-8c19-b621eeebceac)

**Ablation Study:** the authors conducted a detailed analysis of the different components of the ReBased model to understand the impact of each component on the overall effect. The results show that the ReBased model performs better when dealing with long sequences, while modifications such as x2, norm(x)2 and (γ-x+β)2 can improve model performance.

**Language Modelling:** the authors conducted language modelling experiments on the Pile dataset and compared the results with traditional models based on self-attention mechanisms. The results show that the ReBased model performs better in modelling short-term dependencies, but there is still a gap in modelling long-term dependencies.
![image](https://github.com/user-attachments/assets/334f485d-3fb6-4dc2-86f1-3c669f28381c)

**Few-Shot Performance:** the authors validate the performance of trained Based and ReBased models in several common small-sample benchmark tests and find that the ReBased model performs better on most tasks.

![image](https://github.com/user-attachments/assets/a82ca793-ec56-4e7e-ab5d-4a613296ff68)

**Analysis:** the authors analyse the performance of the ReBased model on the MQAR dataset by calculating the IoU and compare it with the model based on the self-attention mechanism. The results show that although the ReBased model does not reach the level of the model based on the self-attention mechanism, it still shows some potential.  

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new architecture for attentional computation based on a linear transformer model, ReBased, and experimentally validate it on the MQAR task. Compared to the existing baseline model, ReBased performs better in processing long sequences, especially in the case of smaller model sizes.
  
  2. In addition, the paper provides an in-depth analysis of different types of attention mechanisms and proposes ways to improve performance using polynomial kernel functions with learnable parameters. These findings provide valuable references for improving existing attention mechanisms.

### 2. Innovative points
  1. The main contribution of this paper is to propose a new architecture for attention computation based on the linear transformer model, ReBased.By introducing technical tools such as polynomial kernel functions and normalisation, the paper successfully solves the problem of existing attention mechanisms when dealing with long sequences.
  
  2. Meanwhile, the paper also provides an in-depth analysis of different types of attention mechanisms and proposes a method to improve the performance by using polynomial kernel functions with learnable parameters. These research results are of great significance for improving the existing attention mechanisms. 

### 3. Future Works
In future research, there is a need to further explore how to address these issues and develop attentional mechanisms that are more adaptable to the needs of various tasks. In addition, since this paper has only conducted experiments on an academic-scale model, further research is needed to investigate how these results can be applied to larger-scale real-world scenarios.   
