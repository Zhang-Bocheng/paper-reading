# Tasks, stability, architecture, and compute: Training more effective learned optimizers, and using them to train themselves
[paper link](https://arxiv.org/pdf/2009.11243) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper focuses on a general-purpose learning optimizer that uses neural network parameterization to automate regularization and train more efficient models.         | Neural Network          |

## Methodology

### 1. Abstract
Compared with traditional optimization algorithms, these learning optimizers have better generalization capabilities and can adaptively adjust the update steps under different tasks and architectures. In addition, experimental results show that these learning optimizers can also be used to train themselves. By training on thousands of tasks, these learning optimizers not only perform well, but also learn to behave differently than existing first-order optimizers.

### 2. Method Description 
This paper proposes an optimizer optimized for ML models and use a genetic algorithm to optimize the parameters of this learner. Specifically, they designed a NN architecture as a learner and used a genetic algorithm to optimize the hyperparameters. In the process, they also considered issues such as how to deal with long-term dependencies and computational efficiency.

![image](https://github.com/user-attachments/assets/c6a444ca-a3bf-4390-99e3-2978c36aac0d)

### 3. Methodological improvements
Compared with the traditional gradient descent based optimization method, this method has better performance and generalization ability. At the same time, it automatically adjusts the learning rate and other hyperparameters, reducing the need for manual intervention. In addition, since the method is based on NN, it can be well adapted to different tasks and datasets.

### 4. Issues addressed 
This method solves some of the limitations of traditional optimization methods, such as the need to manually set the learning rate, and the difficulty of adapting to different tasks and datasets. By using a genetic algorithm to optimize the parameters of the learner, the method is able to better adapt to different situations and improve the effect of optimization. At the same time, this method also provides a new idea, that is, to realize the optimization process through NN, which provides a reference for future optimization research.

## Experiments
This paper mainly introduces the experimental research on learning optimizers, and verifies the effects and performance of different optimizers through multiple comparative experiments. Specifically, this paper first compares the performance of different learning optimizer architectures when the training task set size is different, and finds that the fully connected optimizer of Metz et al. performs better on small task sets and is inferior to Andrychowicz et al.'s LSTM optimizer on large task sets. 

![image](https://github.com/user-attachments/assets/cc39083f-5d62-49ff-8289-d1b9f986d27d)

Next, the paper compares the performance of different optimizers when manually adjusting hyperparameters and using search algorithms to adjust hyperparameters, and finds that the performance of optimizers can be significantly improved by using search algorithms. In addition, the paper compares the differences between learning optimizers and traditional handwriting optimizers, and finds that learning optimizers can surpass traditional handwriting optimizers to a certain extent. 

Finally, the generalization ability of the learning optimizer is discussed, and some experimental results prove that the learning optimizer has a certain generalization ability. In general, this paper systematically analyzes the effect and performance of the learning optimizer through multiple comparative experiments, and provides a valuable reference for subsequent research. 

![image](https://github.com/user-attachments/assets/986b5637-febc-45ac-aa03-09096cdefb9a)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new training method to train a more efficient optimizer through massively parallel computing.

  2. The paper uses a larger, more diverse set of tasks to train the optimizer, and adopts better optimization techniques and an improved optimizer architecture.
  
  3. The paper proves that this method of learning optimizers can surpass the hand-designed optimizers and can be generalized to different optimization tasks to a certain extent.
  
  4. Finally, the paper also shows that the learning optimizer can be used for self-training to further improve its performance.

Methodological innovation

### 2. Innovative points
  1. This paper proposes a new hierarchical optimizer architecture that makes better use of task information and performs better on multiple tasks.
  
  2. The paper uses a large amount of computational resources to train the optimizer, which allows the optimizer to generalize on a larger scale.

  3. The paper also proposes some new techniques and techniques, such as the use of verification losses, to help the optimizer better adapt to different tasks.
Future outlook
   
### 3. Future Works
  1. an optimizer still requires more compute resources to train better, and it also has higher storage requirements than traditional optimizers.
  
  2. In addition, further research is needed on how to choose the right set of tasks and how to combine these tasks so that the optimizer can better generalize to different tasks.
  
  3. In conclusion, the optimizer proposed in this paper is an important progress, but it is still an open question that requires further research and development.    

