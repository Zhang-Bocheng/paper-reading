# Replacing softmax with ReLU in Vision Transformers
[paper link](https://arxiv.org/pdf/2309.08586) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper explores the effect of replacing softmax with ReLU in a vision converter.          | Attention         |

## Methodology

### 1. Abstract
Past research has shown that accuracy decreases when replacing attentional softmax with a point-to-point activation function such as ReLU. However, the authors found that this drop can be mitigated in the case of sequence length division. By training small-to-large visual converters on ImageNet-21k, the authors found that ReLU attention can approach or match the performance of softmax attention and shows good scalability with increasing computational power. Therefore, this paper proposes a new approach that can use ReLU instead of softmax in visual converters and achieves similar or even better results than softmax.

### 2. Method Description 
This paper proposes a model based on the attention mechanism and improve the model performance by changing the form of the attention function. The model includes different forms of attention functions such as linear attention, ReLU attention, and scaled pointwise attention. Among them, ReLU attention is an attempt to replace softmax with a ReLU activation function, while scaled point-based attention is an improved way to control the size of the output value by adding an adjustable parameter to the point-based attention.

![image](https://github.com/user-attachments/assets/e2093177-bfb0-434f-8771-e2896a583e53)

### 3. Methodological improvements
Compared with the traditional softmax attention function, the ReLU attention and scaled pointwise attention proposed in this paper have better performance performance. Specifically, ReLU attention can reduce the amount of computation and accelerate the training process, while scaled pointwise attention can further improve the model performance by adjusting the parameter to better control the size of the output value.

### 4. Issues addressed 
The method proposed in this paper mainly solves the problems of high computational complexity and unstable performance in the traditional attention mechanism. At the same time, the method also provides new ideas and directions for subsequent research, which helps to promote the development and application of the attention mechanism.

## Experiments
This paper focuses on the design of experiments and analysis of results in a ViT-based image classification task. Specifically, the authors conducted the following four comparative experiments:

**The main experiment**: using ReLU-attention instead of softmax-attention mechanism under ImageNet-21k training configuration and compared with softmax-attention. The results show that ReLU-attention is able to match the performance trend of softmax-attention and has fewer gather operations, thus enabling higher parallelisation efficiency.

**Experiments on the effect of sequence length expansion**: the effect of softmax alternatives in different dot product attention mechanisms, including L-αh (α ∈ [0,1], h ∈ {relu, relu2, gelu, softplus, identity}), is investigated. The results show that the best performance is usually obtained when α is close to 1 in the three vision transformer models S/32, S/16 and S/8.

**qk-layernorm experiments**: the effect of qk-layernorm on model performance was investigated. The results show that qk-layernorm does not have a significant effect on these models, but may be different at larger scales.

![image](https://github.com/user-attachments/assets/c7675a54-7925-4d6b-be7b-4789c2b57308)

**Adding gating experiments**: investigated whether adding gating removes the need for sequence length expansion. The results show that even with the addition of gating, sequence length expansion is still required for optimal performance. 

![image](https://github.com/user-attachments/assets/0ffc2c1a-179f-431b-84af-2f30efe01a4a)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes an alternative to softmax operation, i.e., using the ReLU activation function divided by the length of the sequence instead of softmax, which achieves a scaling behaviour in the visual converter that is similar to the traditional softmax attention with better parallelisation performance.
  
  2. In addition, the article explores some limitations and unsolved problems of the method, which provide references for subsequent research.
 
### 2. Innovative points
  1. The ReLU-attention method proposed in this paper is a new alternative to softmax operation, and its main innovation lies in the use of the ReLU activation function divided by the length of the sequence to achieve scaling behaviour similar to that of traditional softmax.
  
  2. This method not only improves computational efficiency, but also better supports parallelised processing, providing new ideas and methods for the design and optimisation of deep learning models.

### 3. Future Works
In future research, it is necessary to further explore these issues and try to find more effective alternatives to softmax operation in order to promote the development and application of deep learning techniques.   
