# Learning advanced mathematical computations from examples
[paper link](https://arxiv.org/pdf/2006.06462v2.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 |  This paper explores how neural networks can be used to learn mathematical properties of differential systems, such as local stability, behavior at infinity, and controllability.        |  Neural Networks         |

## Methodology

### 1. Abstract
 The authors use a large generative dataset and train the model with transformers to enable it to predict fundamental features of the system and approximate numerical properties. It was shown that NN can learn complex computational tasks from examples without the need for built-in mathematical knowledge. This work provides new ideas and methods for applying artificial intelligence to the field of mathematics.
 
### 2. Method Description 
  The paper presents a deep learning-based approach to predicting answers to math problems. Specifically, they used the TRANSFORMER architecture and adapted it differently for each task to suit the particular type of problem. For example, in predicting stability, they needed to compute the eigenvalues of the Jacobi matrix, while in control theory, they needed to find the observability and controllability of the system. 
  
### 3. Methodological improvements
The main advantage of this method over traditional mathematical methods is its ability to handle complex nonlinear problems and automatically extract useful features. In addition, it can improve the accuracy by training the model to better solve real-world problems.

### 4. Issues addressed 
The method addresses three main mathematical problems: **local stability, control theory and stability of partial differential equations**. These problems are classical problems in mathematics, but they are usually difficult to solve. By using deep learning methods, the authors have succeeded in developing some new solutions that can be widely used in practice.

## Experiments
  This paper describes five experiments on predicting the qualitative properties of differential systems that

**Predicting qualitative properties of differential systems**
This experiment was designed to train the model to predict the stability and controllability of the differential system. The authors used two text categorization tools for comparison, fastText based on a bag-of-words model and Transformer based on a self-attention mechanism.The results of the experiment show that for the stability prediction task, Transformer is able to correctly predict 96.4% of the cases with 6 hidden layers and 512 dimensional parameters, while fastText can only achieve 60.6% accuracy. 

For the controllability prediction task, Transformer can correctly predict 97.4% of the cases with 6 hidden layers and 512 dimensional parameters, while fastText can only achieve 70.5% accuracy. These results show that Transformer based on the self-attention mechanism has better performance even for simple qualitative problems.

**Predicting Numerical Properties of Differential Systems**
The experiment was designed to train the model to predict the convergence rate and control feedback matrix of the differential system. The authors used the same Transformer model for comparison and considered the prediction effects at different accuracies. The experimental results show that Transformer is able to correctly predict the convergence rate 86.6% of the time with 8 hidden layers and 1024 dimensional parameters. 

As for the prediction task of controlling the feedback matrix, although the model correctly predicts a lower percentage of cases within 10% error, it correctly predicts 66.5% in a mathematical sense, indicating that the model has learned some mathematical properties related to the feedback matrix.

**Predicting qualitative properties of partial differential equations**
The experiment was designed to train the model to predict whether a solution to a partial differential equation exists and whether it tends to zero. The authors used the Transformer model, which is based on a self-attention mechanism, for comparison and observed that adding an auxiliary task improves the stability and accuracy of the model.

The experimental results show that Transformer is able to correctly predict 98.4% of the cases in different dimensions and spatial dimensions, and the stability of the model is further improved with the addition of an auxiliary task.

**Predicting nonlinear features of differential systems**
The experiment was designed to train the model to predict the local stability of differential systems. The authors used a Transformer model based on the self-attention mechanism for comparison and observed that smaller models also achieve better performance.

The experimental results show that Transformer is still able to correctly predict the local stability of nonlinear differential systems even for high dimensional ones.

**Predicting the Dynamical Behavior of Differential Systems**
The experiment aims to train the model to predict the periodicity of a differential system. The authors used a Transformer model based on a self-attention mechanism for comparison and observed that the model's performance decreased with increasing system size. 

The experimental results show that Transformer is still able to correctly predict the periodicity even for complex dynamical systems.

![image](https://github.com/user-attachments/assets/584fd510-b723-4120-b9f2-b23d61c5dbc5)

![image](https://github.com/user-attachments/assets/89f69b46-9dc7-47b8-93dc-015c10d3a4d1)

## Conclusion

### 1. Advantages of the Thesis
  1. The method is capable of predicting qualitative and theoretical features of differential systems and has achieved up to 85% accuracy in numerical computations.
  
  2. In addition, the method has the ability to generalize and maintain high accuracy with different data distributions. By analyzing the model behavior, the authors found that the model may have learned some shortcuts rather than really understanding the mathematical background knowledge.
  
  3. This phenomenon is similar to the way we learn languages in our daily lives, i.e., we can acquire language skills by practicing them without fully understanding the rules of the language.
     
### 2. Innovative points
  1. Unlike traditional rule-based or heuristic algorithms, the method utilizes a large amount of synthetic data to train the model so that it can automatically learn complex mathematical operations and techniques.
  
  2. At the same time, the method is generalizable and extensible to a wider range of mathematical domains and problem types.

### 3. Future Works
  1. Future research can further explore how to optimize the design and training process of the model to improve its performance and efficiency.
  
  2. In addition, the method can be considered to be applied to other fields, such as physics and engineering, to solve practical problems.
  
  3. Finally, the learning mechanisms and behavioral laws of the models need to be explored in depth for better understanding and application of these models.


