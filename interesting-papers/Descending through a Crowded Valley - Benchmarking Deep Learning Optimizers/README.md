# Descending through a Crowded Valley - Benchmarking Deep Learning Optimizers
[paper link](https://arxiv.org/pdf/2007.01547) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper focuses on the importance of choosing an optimizer in deep learning, and performs extensive benchmarking to provide evidence-supported selection methods.         |  Deep Learning         |

## Methodology

### 1. Abstract
  By analyzing fifteen popular optimizers, the authors draw the following three conclusions: (i) optimizer performance varies from task to task; (ii) using default parameters when evaluating multiple optimizers has a similar effect as tuning the hyperparameters of a single, fixed optimizer; and (iii) ADAM is still a strong contender, and the newer methods do not significantly and consistently outperform it. This paper provides challenging and well-tuned baseline results that can be used by researchers as a basis for more meaningful evaluation of new optimization methods.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/e5778274-f8d5-4f5a-a6ed-51f18371d043)

### 2. Method Description 
  The aim of the paper is to compare the performance of different optimizers in DL and to evaluate their strengths and weaknesses in real-world applications. The researchers chose eight real-world DL problems as a benchmark test set and selected fifteen of the most popular choices from over one hundred common optimizers. For each problem and optimizer, they evaluated all possible combinations of four different budgets and four selected learning rate scheduling schemes, yielding a total of 1,920 configurations. In addition, to evaluate the effectiveness of the hyperparameter search, they performed 128 training curve estimations on each configuration.
   
### 3. Methodological improvements
  The main innovation of this study is the use of a large-scale experimental setup containing multiple problems, multiple optimizers, and multiple learning rate scheduling schemes to compare different optimizers. This approach allows for a more comprehensive understanding of the performance differences between various optimizers and provides additional insights to help researchers select the most appropriate optimizer for their particular task.
  
### 4. Issues addressed 
  With this large-scale experimental setup, the study addresses the following questions:

  1. Compare the performance of different optimizers in DL;
  
  2. Evaluate the advantages and disadvantages of various optimizers in real-world applications;

  3. Provide insights on how to select the most suitable optimizer for a given task.

## Experiments
  This paper focuses on the performance of optimizers in ML and conducts a number of comparative experiments to explore the performance differences and tuning effects of different optimizers. Specifically, the following comparison experiments were conducted in this paper:

The performance differences between the one-time results of all optimizers and the results after tuning were compared, and a 15x15 matrix was constructed to show the performance of each optimizer. By comparing the color of each cell in the matrix, it can be seen that some optimizers with poor default settings (e.g., MOMENTUM, NAG, and SGD) can be tuned to get better performance, while some adaptive methods (e.g., ADAM, NADAM, and RADAM) show better default parameter settings. This suggests that different optimizers are differently problem-dependent and that there is no one universal best optimizer for all tasks.

The impact of tuning and learning rate scheduling on performance is explored. By comparing the final performance of the optimizers with different budgets and scheduling, it is found that the performance improves with increasing budgets, but with diminishing returns as the budget increases. In addition, untuned learning rate scheduling can also improve performance, e.g., using trapezoidal learning rate scheduling leads to a relative performance improvement of about 5.2%.

The performance of various optimizers after tuning is compared. While no single optimizer can perform best on all tasks, there are some optimizers that typically perform better, such as ADAM and ADABOUND. these optimizers can achieve similar performance to tuned optimizers without tuning. Therefore, in practical applications, choosing several untuned optimizers to try can achieve similar or even better performance performance than the tuned optimizers.

In summary, this paper reveals the performance differences and tuning effects of optimizers in machine learning through the study of several comparative experiments, and provides useful guidance suggestions for practical applications.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/399d6638-177d-4e72-a476-5df22f6ebba2)

## Conclusion

### 1. Advantages of the Thesis
  1. The study provides extensive benchmarking of deep learning optimizers and reveals the structure and similarities between existing approaches.
  
  2. The study uses datasets from DEEPOBS, including different models and datasets of varying complexity and size.
  
  3. The study considers different hyperparameter search strategies and budgets and quantifies their impact on performance.
  
  4. The study also explores the importance of key challenges such as automatic inner loop tuning.

### 2. Innovative points
  1. The study provides an extensive benchmarking of deep learning optimizers to help select the right optimizer and understand its performance on different problems.
  
  2. The study uses datasets from DEEPOBS, which makes the results generalizable and able to cover a wide range of models and dataset complexities and sizes.
  
  3. The study also considers different hyperparameter search strategies and budgets and quantifies their impact on performance. This helps to understand how best to tune hyperparameters for optimal performance.
     
### 3. Future Works
  1. The results of the study suggest that many similar approaches exist in the current market for deep learning optimizers, so more research is needed to develop new optimizers or improve existing ones.
  
  2. The study suggests focusing on key challenges such as automatic inner loop tuning to achieve more efficient and robust optimization.
  
  3. The results of the study can provide guidance for future research on deep learning optimizers and promote better understanding and comparison of different optimizers.
