# Toward a Deeper Understanding: RetNet Viewed through Convolution
[paper link](https://arxiv.org/pdf/2309.05375) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper focuses on the effectiveness of RetNet based on the convolutional neural network (CNN) perspective and proposes a RetNet variant for the visual domain.          | CNN         |

## Methodology

### 1. Abstract
Similar to RetNet, this variant improves the local modeling capability of ViT by applying a weight mask on the original self-attention matrix. The authors use a simple learnable weight mask (ELM), but this approach not only leads to non-trivial additional parameter overhead, but also increases the optimization complexity. Therefore, this paper proposes a new Gaussian Mixed Mask (GMM) in which only one mask has two learnable parameters and can be easily applied to any ViT variant that allows the use of masks. Experimental results show that the method is very effective for free ViT enhancement with little additional parameter or computational cost.

### 2. Method Description 
This paper proposes two new attentional mechanisms: **element-wise mask (ELM) and Gaussian Mixture Mask (GMM)**. Among them, ELM is an element-wise mask matrix with learnable parameters that dynamically adjusts the attentional tendency between patches, while GMM further improves the performance of the model by combining multiple Gaussian distributions to form a dynamic mask matrix.

![image](https://github.com/user-attachments/assets/895a1770-9942-4284-8b3d-b6adeba5b276)

### 3. Methodological improvements
Compared with the traditional static mask matrix, both ELM and GMM have better adaptability and flexibility, and can adaptively adjust the attentional weights according to different input data. Meanwhile, GMM also introduces the concept of Gaussian distribution, which makes the mask matrix smoother and avoids the overfitting problem in some local extreme cases.

![image](https://github.com/user-attachments/assets/6f995d4c-c73f-42cb-831c-0fbd392c1c66)

### 4. Issues addressed 
Both the ELM and GMM proposed in this paper are able to effectively improve the performance of the model in image classification tasks and can be implemented without increasing the computational complexity. In addition, the GMM is able to further improve the generalization ability of the model so that it can achieve better results on different datasets. These improvements not only help to improve the performance of the model, but also contribute to a better understanding of how the attention mechanism works.

## Experiments
This paper focuses on the authors' use of the Gaussian Mixture Mask (GMM) structure in an image classification task and conducts several comparative experiments to verify its effectiveness.

In Experiment 1, the authors added the GMM structure to several different types of ViT models and evaluated their performance. The experimental results show that compared to the standard ViT models, the GMM-ViT models have improved Top-1 accuracy on both the CIFAR-10 and Tiny-ImageNet datasets with a smaller increase in the number of parameters.

In Experiment 2, the authors explored the effect of hyperparameter settings in the GMM structure on the model performance. By adjusting how the learnable parameters α and σ are initialized and the number of Gaussian kernels in the GMM hybrid model, the authors found that the appropriate number of Gaussian kernels can significantly improve the accuracy of the model, while too few or too many Gaussian kernels can lead to performance degradation.

In Experiment 3, the authors compare the GMM structure with several other mainstream ViT structures, including Swin and CaiT. The experimental results show that GMM still has stronger expressive ability and better performance performance than other structures.

![image](https://github.com/user-attachments/assets/61a32635-027b-4b91-831c-47ac3e564d64)
 
## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a method called Element-wise Learnable Mask (ELM) to enhance the training of ViT on small datasets, and further propose Gaussian Mixture Mask (GMM) to reduce the parameter and computational cost.
  
  2. This approach can dynamically adjust the attention mechanism to make it more adaptable to different task requirements.
  
  3. In addition, the paper compares the performance of different pre-training models on small datasets, proving the effectiveness of ELM and GMM.

### 2. Innovative points
  1. The main contribution of the paper is to propose a new MASK method, ELM, which can dynamically adjust the attention mechanism according to the task needs.
  
  2. In addition, the authors introduced GMM to further reduce the parameter and computational cost.
      
### 3. Future Works
Although the ELM and GMM methods proposed in this paper have achieved good results on small datasets, the performance on large-scale datasets still needs further research. In addition, with the development of deep learning technology, the research on self-supervised learning will continue to deepen, which also provides more possibilities for the improvement of ViT. 
