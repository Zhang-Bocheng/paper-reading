# Big Transfer (BiT): General Visual Representation Learning
[paper link](https://arxiv.org/pdf/1912.11370.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |  This paper introduces a visual representation learning method called Big Transfer (BiT).        | Transfer Learning          |

## Methodology

### 1. Abstract
  The method can achieve strong performance on more than 20 datasets by pre-training on large-scale supervised datasets and fine-tuning using a simple heuristic algorithm. The BiT method is applicable to a variety of data sizes, including datasets with only a few samples. Experimental results show that BiT achieves 87.5% and 99.4% accuracy on datasets such as ILSVRC-2012 and CIFAR-10, respectively, and is able to perform well with small samples.
  
### 2. Method Description 
The paper focuses on how to use pre-trained models in transfer learning and proposes two effective methods: Group Normalization (GN) and Weight Standardization (WS). Also, they designed a simple hyperparameter selection rule, BiT-HyperRule, for dealing with dataset size and image resolution for various downstream tasks.

First, in the pre-training phase, authors improve the model performance by increasing the network size and using techniques such as GN and WS. <br> Second, in the downstream task phase, they used an inexpensive fine-tuning protocol that attempts only one hyperparameter, i.e., selecting the most appropriate hyperparameter based on the intrinsic image resolution and number of data points of the task. <br> In addition, they used some standard data preprocessing methods such as random cropping and horizontal flipping during the fine-tuning process.

### 3. Key concepts
   _Transfer learning_: A ML technique where a model developed for a particular task is reused as the starting point for a model on a second, related task. This approach leverages the knowledge gained from the initial task (source task) to improve learning efficiency and performance on the new task (target task).
   
### 4. Methodological improvements
  Compared with the traditional Batch Normalization (BN), the GN and WS proposed in this paper are more suitable for the training of large-scale pre-trained models, and especially perform better in small batch training. And the BiT-HyperRule can effectively reduce the cost of hyperparameter search in downstream tasks, which improves the efficiency of the whole transfer learning process.
  
### 5. Issues addressed 
  The paper addresses a number of issues in transfer learning, such as how to use effective regularization techniques in pre-trained models, how to select appropriate hyperparameters for different downstream tasks, and how to optimize the efficiency of the entire migration learning process. These solutions can help researchers better utilize pre-trained models for migration learning, thus accelerating the process of model development and deployment.
  
## Experiments
 This paper describes the performance of the BiT model released by Google on standard CV benchmarks and conducts several comparative experiments to explore the impact of different factors on model performance.

First, the authors used three pre-training datasets of different sizes (ImageNet-S, ImageNet-M, and ImageNet-L) to train the model and evaluated it on several downstream tasks. The results show that using a larger dataset significantly improves the performance of the model.

Second, the authors investigated the effects of model size and dataset size on model performance. They found that on small datasets, better performance can be obtained by using smaller models, while on large datasets, better performance can be obtained by using larger models. 

Next, the authors compared the effects of different optimization strategies on model performance. They found that for large datasets, longer computation times are required for optimal performance. In addition, they found that low weighted decay may lead to faster initial convergence, but ultimately leads to poorer model performance.

Finally, the authors compared the effects of different normalization methods such as BN, GN and WS on model performance. They found that methods using a combination of GN and WS work better in large batch training and are better than Batch Normalization.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/de9b1524-2832-461a-a87b-9735b1c56b1c)

Overall, this paper provides important guidance on how to select appropriate pre-training datasets, model sizes and optimization strategies, and normalization methods to help researchers achieve better performance in real-world applications.

## Conclusion
### 1. Advantages of the Thesis
  1. This paper proposes a simple but effective pre-training model for deep learning called "Big Transfer" (BiT).

  2. The BiT model achieves state-of-the-art best performance on multiple datasets and can be applied to many downstream tasks with only one pre-training, which greatly reduces the cost.

  3. The authors also provide a simple training and fine-tuning setup to balance complexity and performance, and use a large amount of training data to improve the model's generalization ability.
     
### 2. Innovative points
  1. This paper provides a simple but effective deep learning pre-training model that can achieve the latest best performance on multiple datasets.

  2. The BiT model is trained using three datasets of different sizes, the largest of which, JFT-300M, contains 300 million poorly labeled images, which gives the model better generalization capabilities.

  3. The authors also provide a simple training and fine-tuning setup to balance complexity and performance and use a large amount of training data to improve the model's generalization ability.
     
### 3. Future Works
  1. More sophisticated pre-trained models can be further explored in the future to improve their performance on various downstream tasks.

  2. Combining pre-trained models with other techniques, such as transfer learning or augmentation learning, could be considered to further improve their performance.

  3. Future research could also be conducted on how to better handle small-sample learning problems in order to better utilize the advantages of pre-trained models in real-world applications.




