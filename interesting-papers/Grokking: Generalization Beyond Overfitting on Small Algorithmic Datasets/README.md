# Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets
[paper link](https://arxiv.org/pdf/2201.02177) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper explores the generalization ability of neural networks (NN) on small algorithmically generated datasets and introduces the concept of "understanding" to explain how NN can improve generalization performance by recognizing patterns in the data.         |  neural networks         |

## Methodology

### 1. Abstract
   The results show that in some cases, even beyond the overfitting point, the NN can still achieve perfect generalization performance by understanding patterns in the data. In addition, the paper examines the relationship between generalization performance and dataset size and finds that smaller datasets require more optimization to achieve generalization. The authors believe that these datasets provide a good experimental basis for an in-depth study of an under-understood problem in DL - the generalization ability of hyper-parameterized NN.

   ![image](https://github.com/user-attachments/assets/dc589ae9-5d56-4d7f-bd51-33a83e9d75ec)

### 2. Method Description 
  The study used a small transformer to train the equations in the dataset, where each symbol ("a", "◦", "b ", "=" and "c") is a separate token. The method aims to enable computers to understand and perform different mathematical operations by mapping them to specific sequences of tokens.
  
### 3. Issues addressed 
  The main goal of the research was to enable computers to understand and perform different operations in mathematical equations. To do this, the researchers used small transformers to train the dataset and used it to parse and compute the equations. This approach can help computers better understand mathematical equations and automatically perform the appropriate operations when needed.
  
## Experiments
  This paper presents three experiments:

The first experiment is on the **generalization ability** of the model, where the authors observe that in some cases there is a hyperbolic decrease in the validation loss, i.e., the validation accuracy continues to increase after the initial overfitting. This phenomenon is more common on small datasets, and different models, optimizers, and dataset sizes can have an impact on generalization ability. Additionally, the relationship between training and validation losses can also show a hyperbolic decline.

The second experiment examined the **learning time profile** of different optimization algorithms. The authors found that the convergence performance of the model is not affected with reduced training data, but more optimization steps are required to achieve the same accuracy. Thus, the time required for optimization increases rapidly as the amount of data is reduced.

The third experiment measured the **average accuracy** of the NN on different operational tasks and analyzed some patterns. For example, for symmetric operational tasks, they are usually easier to learn than asymmetric ones. In addition, the authors tried some regularization methods to improve the generalization ability of the model, such as weight decay and residual discard, among which weight decay has the most significant effect.

![image](https://github.com/user-attachments/assets/7a6c1edc-70b5-40e4-9a02-53ef0ef58233)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper investigates the performance of NN on small algorithmic binary operation tables and identifies phenomena such as double-declining or late generalization as well as improvements in generalization through interventions such as weight decay.
  
  2. These datasets may be a good place to explore aspects of generalization. In addition, the authors show that visualizing the embedding space can reveal structure in natural problems, such as in modulo addition, where the topology of the embedding space tends to be cylindrical.
  
  3. The authors document the interesting phenomenon that the number of optimization steps required to reach a given level of performance increases rapidly as the amount of training data decreases.
     
### 2. Innovative points
  1. In this paper, small algorithmic binary operation tables are used as experimental datasets, and the generalization ability of NN is observed by training on these datasets.
  
  2. In addition, the authors propose some new optimization details such as using weight decay to improve the generalization ability.
  
  3. Finally, the authors also tried to visualize the embedding space to understand the structure of the mathematical objects learned by the NN.
     
  ![image](https://github.com/user-attachments/assets/3f64fc9f-6e74-4098-87bd-66161cd2d2a5)

### 3. Future Works
  1. the phenomena and conclusions presented in this paper can be verified through more experiments;
  
  2. this approach can be extended to more complex tasks and larger datasets;
  
  3. further research can be conducted on how to utilize the visual embedding space to aid in the understanding of what the NN has learned.
     
