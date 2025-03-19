# Intrinsic Dimensionality Explains the Effectiveness of Languaeg Model Fine-Turning
[paper link](https://arxiv.org/pdf/2012.13255) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper explores the effectiveness of fine-tuning in pre-trained language models and makes the case for explaining this phenomenon by analyzing intrinsic dimensionality.          |Model Fine-Turning          |

## Methodology

The authors find that common pre-trained models with very low intrinsic dimensionality, i.e., the presence of a low-dimensional reparameterization, are equally effective for fine-tuning. For example, with a random projection back to full space, optimizing only 200 trainable parameters can fine-tune the RoBERTa model to close to 90% of the full parametric performance level. 

![image](https://github.com/user-attachments/assets/6de7a33e-de92-4b90-847f-b0c37135b1f5)

In addition, the authors find that pre-training implicitly minimizes intrinsic dimensionality, and that larger models tend to have lower intrinsic dimensionality after a fixed number of pre-training updates, which at least partially explains their extremely efficient performance. The authors link intrinsic dimensionality to low-dimensional task representations and compression-based generalization bounds, providing generalization bounds based on intrinsic dimensionality that are independent of the full parameter count.

![image](https://github.com/user-attachments/assets/88f757f9-adf3-45de-becb-a82c48703467)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes to use the new perspective of “intrinsic dimensionality” to explain the behavior of pre-trained models in the fine-tuning process, and experimentally demonstrate that pre-trained models can learn many NLP tasks with few parameters.
  2. What is more, the authors also found a negative correlation between the intrinsic dimensionality and the number of parameters of pre-trained models through experimental studies of several pre-trained models, which further proves the effectiveness and superiority of pre-trained models.
  3. The authors link intrinsic dimensionality to low-dimensional task representations and compression-based generalization bounds, providing intrinsic dimensionality generalization bounds independent of full parameter counts, further explaining why these methods generalize well across tasks in practice.

### 2. Innovative points
This paper proposes a new method for interpreting pre-trained models, intrinsic dimensionality, which can help us understand the complex behavior of large models. By measuring the intrinsic dimensionality of each task, we can understand the number of free parameters required for each task and thus better understand the behavior of pre-trained models. And, the authors link intrinsic dimensionality to low-dimensional task representations and compression-based generalization bounds, providing a new way of interpreting pre-trained models. 

### 3. Future Works
Future research can further explore how to combine other techniques (e.g., regularization) to improve the generalization ability and efficiency of models. Also, attempts can be made to apply the intrinsic dimensionality approach to other areas to better understand and optimize complex machine learning problems.    
