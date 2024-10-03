# Language models scale reliably with over-training and on downstream tasks
[paper link](https://arxiv.org/pdf/2403.08540) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores differences in the training and evaluation of language models and proposes two approaches to predicting the performance of large models.          |   Large Language Models (LLMs)       |

## Methodology

### 1. Abstract
The authors fit an extended scale model by training a series of language models with different parameter sizes and using different data distributions and training times to be able to predict validation loss under hyperparameters. And, they propose a power-law relation to relate the perplexity of the language model to performance on downstream tasks, which allows them to predict the performance of the model on multiple downstream tasks under hyperparameters. These experimental results show that this approach can accurately predict the performance of large language models while reducing computational cost.

### 2. Method Description 
This thesis presents two key formulas to predict model overtraining and downstream performance: **the loss equation and the downstream error equation**. These equations can help us understand how the model performs under different training parameters and can be used to select the best training parameters to improve the model's performance.

![image](https://github.com/user-attachments/assets/7d324c94-38a9-4012-bc3e-491bdddf051c)
 
### 3. Methodological improvements
Compared with previous studies, the loss equation and downstream error equation proposed in this thesis are more precise and accurate. In addition, the paper uses a large amount of experimental data to verify the validity of these equations and provides some suggestions on how to build an effective test environment.

![image](https://github.com/user-attachments/assets/69c3444f-dfc0-481b-9e55-422cc12acb02)

### 4. Issues addressed 
The paper addresses the problem of how to improve model performance by tuning the training parameters. It provides a simple but effective way to predict model over-training and downstream performance, and gives researchers a better tool to optimise the model training process.

## Experiments
This paper focuses on the predictable performance of large language models and the phenomenon of overfitting during training, and proposes a reliable hyperparameter optimisation method. The authors use a dataset containing multiple tasks to evaluate the performance of different models, and propose two important hypotheses: **1. the choice of hyperparameters should be based on the dataset size rather than the model size; and 2. the training time increases significantly when the model becomes larger**. The authors experimentally demonstrate the validity of these two assumptions and propose a new hyperparameter selection method that reduces training time and computational cost without losing performance.

Specifically, the authors first define some key terms, such as model size, amount of training data, and hyperparameters, and introduce the application of these terms in the field of NLP. Then, the authors design a series of experiments to test these hypotheses and compare the effects of different hyperparameter selection methods. The most important of these experiments is the hyperparameter search experiment, in which the authors used a method called Bayesian optimisation to automatically search for the best hyperparameter combinations and compared the results with those of manually adjusting the hyperparameters. The results show that using Bayesian optimisation can significantly improve model performance while reducing training time and computational costs.

In addition, the authors conducted a number of other experiments to further validate their hypothesis. For example, they investigated the effect of different training datasets on model performance and found that using a larger dataset can significantly improve model performance. In addition, they explored the problem of model overfitting and proposed a new approach to mitigate this problem.

## Conclusion

### 1. Advantages of the Thesis
  1. This paper addresses the issue of cost when training LLMs and proposes a new method for reliably predicting model performance.
  
  2. The researchers used large-scale experiments to validate the effectiveness and reliability of their method on different datasets.
  
  3. The results show that the method can accurately predict model performance in downstream tasks and can reduce the risk of model overfitting to some extent.

### 2. Innovative points
  1. This paper presents a new method for reliably predicting model performance in downstream tasks by establishing a relationship between the training cost of the model and the model parameters and data volume.
  
  2. The method is highly scalable and generalisable for models and datasets of different sizes and types.
  
  3. The researchers also enabled the method to scale reliably across multiple training and testing distributions by tuning the hyperparameters.

### 3. Future Works
  1. Future research could further explore how to optimise the training process of the model to improve its performance and efficiency.
  
  2. Attempts could be made to use more data sources and more complex model structures to further validate the effectiveness and reliability of the method.

  3. In addition, the application of the method to problems in other areas, such as computer vision and natural language processing, can be considered.  
