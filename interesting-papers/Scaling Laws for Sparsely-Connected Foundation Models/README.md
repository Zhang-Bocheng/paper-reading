# Scaling Laws for Sparsely-Connected Foundation Models
[paper link](https://arxiv.org/pdf/2309.08520) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper explores the impact of sparse connectivity on the training of Transformer models on large-scale datasets, and validates a new relationship between parameter sparsity and the amount of training data in the fields of vision and language.          |  Transformer        |

## Methodology

### 1. Abstract
It is experimentally demonstrated that there exists an ‘optimal sparsity’ that achieves the best performance for a given effective model size and training budget. Furthermore, the study is extended to different sparsity structures and strategies, such as the hardware-friendly n:m model and starting with a pre-trained dense model. These findings provide a theoretical basis for understanding the power and limitations of sparsity under different parameters and computational settings, and provide practical applications for exploiting sparsity to improve computational efficiency.

![image](https://github.com/user-attachments/assets/41f43f71-52e1-4d16-811a-64f5d94d816f)

## Experiments
This article focuses on the effect of using parameter sparsification techniques in large-scale pre-trained models, and demonstrates the feasibility of the method through experiments. The article first describes the main design and data sources of the experiments, including the use of large-scale models such as Vision Transformers and Transformer-based language models with different settings of training time and size. Then, the authors draw the following conclusions by analysing the experimental results:
<br>&emsp;Parameter sparsification can significantly improve the efficiency of the model, especially when the training time is short;
<br>&emsp;Sparsified models can achieve similar or even better performance than dense models with the same computational resources;
<br>&emsp;Different types of sparsification methods (e.g., stochastic sparsification and hierarchical sparsification) may have different effects for different types of models;
<br>&emsp;For already trained models, starting sparsification from a pre-trained model can result in higher efficiency gains.

![image](https://github.com/user-attachments/assets/5b201d17-9c53-4dfa-b10e-d06bdc030d81)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper focuses on the impact of sparsification on the performance of Transformer models under large-scale data training, and proposes a new joint scaling law to quantify the relationship between sparsity and model size as well as the amount of training data.
  
  2. This study provides important insights into the efficiency issues in deep learning and can guide practical applications on how to choose appropriate compression strategies to improve computational efficiency.
 
### 2. Innovative points
  1. The law takes into account three factors, namely sparsity, number of non-zero parameters, and amount of training data, and is able to accurately predict the model performance performance under different sparsities.
  
  2. In addition, the authors explored the performance of sparsification at different training stages and found that the effect of sparsification gradually increases as the training time grows.
 
### 3. Future Works
In future research, more general compression methods need to be further explored to adapt to the needs of more scenarios. Also, the impact of sparsification on aspects such as model interpretability and stability needs to be thoroughly investigated to better understand its role and limitations in practical applications.
