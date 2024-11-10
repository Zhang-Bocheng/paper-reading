# Offline Actor-Critic Reinforcement Learning Scales to Large Models
[paper link](https://arxiv.org/pdf/2402.05546) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |This paper explores how offline reinforcement learning algorithms can be used to train on large models such as transformer and finds that such algorithms can outperform benchmark models of supervised behavioural cloning on large-scale datasets, outperforming them in 132 successive control tasks.           | Reinforcement Learning (RL) &  Large Models       |

## Methodology

### 1. Abstract
The authors introduce a Perceiver-based Actor-Critic model and explain the key model features required to make offline RL work with self and trans-attentive modules. Overall, the study shows that: i) simple offline Actor-Critic algorithms are a natural choice for a gradual shift away from the currently dominant behavioural cloning paradigm; and ii) multi-tasking strategies, including realistic robotics tasks, can be learned from sub-optimal demonstrations or automatically generated data through offline RL, allowing for simultaneous mastery of multiple domains.

### 2. Method Description 
This paper presents an online RL algorithm based on offline data called Scalable Offline Actor-Critic Learning (SOAC). The algorithm improves performance by introducing the KL scatter of the behavioural policy into the objective function, and uses a behavioural encoder as a supervisory signal to prevent overfitting. In addition, the algorithm uses the Perceiver-IO architecture for multimodal input processing, which improves the efficiency and scalability of the model.
![image](https://github.com/user-attachments/assets/bf85e85c-9c7b-4b48-a11b-a70464bc5e8d)

### 3.  Methodological improvements
The main improvement of the SOAC algorithm over traditional reinforcement learning algorithms is the introduction of KL dispersion for behavioural strategies to avoid overfitting and improve performance. In addition, the algorithm employs the Perceiver-IO architecture for better handling of multimodal inputs and to achieve efficiency and scalability in real-time control tasks.

### 4. Issues addressed 
The SOAC algorithm solves the problems of traditional reinforcement learning algorithms when dealing with offline data, such as overfitting and poor generalisation. It can also be applied to tasks with multiple input sources, such as vision, speech and motion perception. This makes the SOAC algorithm a very promising reinforcement learning algorithm that can play an important role in various real-world applications.

## Experiments
The first experiment **analyses the performance and scalability of the PAC (Offline Actor-Critic) algorithm and compares it with supervised learning and reinforcement learning.** The authors used three different datasets to test the performance of the PAC algorithm on different tasks and explored variations in the performance of the PAC algorithm by adjusting the model parameters and the number of training sessions. The results show that the PAC algorithm outperforms the benchmark methods in supervised learning and reinforcement learning on the same datasets.

![image](https://github.com/user-attachments/assets/e6f7af47-aee2-47d1-8611-9d7464bdcdc7)

The second experiment **compares the performance of the PAC algorithm with two other large pre-trained models (Gato and RoboCat) on multiple continuous control tasks.** The authors used the same training dataset and optimiser hyperparameters to train these models and compared them to other methods. The results show that the PAC algorithm shows better performance on all tasks, especially when dealing with low-quality data.

![image](https://github.com/user-attachments/assets/4a01e206-093c-4a9d-ba8f-28803a56ec81)

The third experiment explores how the learning capabilities of the PAC algorithm can be used to make adaptive improvements and apply them to real robotics tasks. The authors first pre-trained on a target task using the PAC algorithm, then collected some additional data and added it to the original dataset. Then, they use this new data to retrain the model and repeat the process over and over again until they reach a near-perfect level of performance. The results show that the PAC algorithm can make good use of self-generated data to improve its performance, and can do so without compromising other tasks.  

## Conclusion

### 1. Advantages of the Thesis
  1. PAC can be applied to pre-trained models without any model changes, thus improving the success rate of robotic tasks.
  2. The PAC is able to gradually transition to RL learning without instability.
  3. The PAC can process data from multiple input modalities simultaneously and is able to control a real robot at 20Hz.

### 2. Innovative points
  1. high-quality behavioural modelling. Specifically, PAC has the following innovations:
  2. PAC uses a KL regularised RL objective function to balance the trade-off between exploration and exploitation, which makes PAC more stable.
  3. PAC incorporates actions into the Q function, which allows for quick estimation of Q values for multiple actions.
  4. PAC uses a Perceiver-style attention mechanism to handle data from multiple input modalities and can efficiently train large models.

### 3. Future Works
further research on generic reward functions or unsupervised reward labelling may help to extend the application of PAC. In addition, the research in this paper focuses on large-scale modelling for control tasks, which can be considered to be extended to other domains such as natural language processing in the future.   
