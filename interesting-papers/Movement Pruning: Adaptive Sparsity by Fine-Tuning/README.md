# Movement Pruning: Adaptive Sparsity by Fine-Tuning
[paper link](https://arxiv.org/pdf/2005.07683.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces a new weight pruning method, movement pruning, which is a simple, deterministic first-order weight pruning method that is more adaptable in pre-trained model fine-tuning.          |  Neural Network         |

## Methodology

### 1. Abstract
Compared to existing zero-order and first-order pruning methods, experimental results show that movement pruning exhibits significant improvements at high sparsity when pruning large pre-trained language models. When used in conjunction with distillation techniques, the method achieves minimized accuracy loss by retaining only 3% of the model parameters. 

### 2. Method Description 
The paper proposes two NNs pruning methods based on motion pruning: **hard pruning and soft pruning**. In this case, hard pruning computes the pruning mask by learning the weights and importance scores and updating the importance scores during training, while soft pruning uses a fixed global threshold to control the binary mask and adds a regularization term to encourage the importance scores to decrease over time. Both methods utilize first-order information (i.e., changes in weights) to determine which connections should be retained, rather than relying solely on absolute magnitude.
 
### 3. Methodological improvements
  1. Compared to traditional pruning methods based on the absolute magnitude of the weights, motion pruning-based methods are better adapted to task-specific data and are able to dynamically adjust the pruning mask during training.
  
  2. In addition, soft pruning introduces a regularization term to control the sparsity level, which provides more flexibility in controlling the complexity of the model.
     
### 4. Issues addressed 
Motion-based pruning can effectively solve some problems in traditional pruning methods, such as not being well adapted to task-specific data and difficulty in dynamically adjusting the pruning mask. At the same time, soft pruning provides a flexible way to control the sparsity of the model, making it possible to reduce the size and computational effort of the model while maintaining a high level of accuracy. 

## Experiments
  This paper focuses on experiments comparing different types of sparsification methods in transfer learning with the BERT model. The authors used three English tasks (SQuAD, MNLI, and QQP) to test different sparsification methods and compared the results to a baseline. The following is a detailed description of each experiment:

**EXPERIMENT**: This experiment aims to investigate the performance of different types of sparsification methods in the BERT model. The authors used three English tasks (SQuAD, MNLI, and QQP) and compared the following sparsification methods: absolute value sparsification, motion sparsification, soft motion sparsification, reweighted L1 minimization combined with Proximal projection, and structured dropout sparsification.The authors also compare results using the mini-BERT model.

RESULTS ANALYSIS: The authors found that absolute value sparsification outperforms other methods at low sparsity, but motion sparsification and soft motion sparsification perform better at high sparsity. Specifically, on the SQuAD task, when the sparsity reaches 3%, soft motion sparsification reaches 79.9 F1, while absolute value sparsification is only 73.3 F1. In addition, the authors compare the differences between the different sparsification methods and find that the soft motion sparsification outperforms the other methods.

![image](https://github.com/user-attachments/assets/fa3b30cd-f2ba-4e84-963f-2a7991fcbd55)

CONCLUSION: The authors further explain why motion sparsification and soft motion sparsification perform better by analyzing aspects such as the distribution of residual weights, and the effects of local and global choices for different sparsification methods. 

![image](https://github.com/user-attachments/assets/172dede0-0575-411a-8cbf-3093d52269df)


## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new model compression method, motion pruning, and experimentally validates it on several NLP tasks.
  
  2. The experimental results show that motion pruning has better performance performance than the traditional weights absolute value based approach in the case of high sparsity.
  
  3. The paper also explores the application prospects of this compression method, including aspects such as improving the privacy preservation and accessibility of the model.

### 2. Innovative points
  1. Motion pruning is a pruning method based on first-order derivatives, which can be better adapted to the task of transfer learning, unlike traditional weights absolute value-based methods.
  
  2. The simple version of motion pruning proposed in the paper utilizes a straight-through estimator, which can effectively reduce the model size and maintain high accuracy.
  
  3. Experimental results show that motion pruning is able to achieve better performance than other first-order pruning methods at high sparsity.
     
### 3. Future Works
  1. As a new model compression method, motion pruning can play an important role in future deep learning research.
  
  2. In terms of hardware fabrication, it can be further explored how to design chips to accelerate the inference process of sparse networks and thus reduce energy consumption.
  
  3. Motion pruning can be used in combination with other techniques, such as group sparse regularization, to further improve the performance and interpretability of models.
