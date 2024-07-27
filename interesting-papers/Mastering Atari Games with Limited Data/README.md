# Mastering Atari Games with Limited Data
[paper link](https://arxiv.org/pdf/2111.00210) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper presents a reinforcement learning algorithm called EfﬁcientZero, which is based on MuZero and has efficient visual RL capabilities.         | Reinforcement Learning          |

## Methodology

### 1. Abstract
The method beyonds human performance in Atari gaming benchmarks and requires only two hours of gaming experience. Compared to the previous best performance, EfﬁcientZero improves on the mean and median human scores by 176% and 163%, respectively, and is the ﬁrst algorithm to outperform the human average in the Atari 100k benchmark. Additionally, EfﬁcientZero was able to exceed the previous best performance in the DMControl 100k benchmark. This efficient learning capability and high performance could bring RL closer to real-world applications.

![image](https://github.com/user-attachments/assets/d8472506-a4fc-49a4-9f0e-4f54331ac0a4)

### 2. Method Description 
The paper presents a model-based RL algorithm called EfficientZero, which aims to improve sample efficiency in the case of limited data by using Monte Carlo Tree Search (MCTS) and to achieve performance that exceeds that of humans in the Atari game. The algorithm employs three key modifications:

**Self-supervised consistency loss**: a dynamic function is utilized to compare the predicted next state with the actual next state to provide more training signals.

**Structured Predictive Value Prefix**: uses a RNN to predict the sum of future rewards, thus estimating the value more accurately and avoiding the state aliasing problem.

**Model-based strategy correction**: recalculates value targets in trajectories using the current strategy to reduce bias in trajectories based on old strategies.

![image](https://github.com/user-attachments/assets/beb917b9-a898-40e4-96bb-721f0e3eea5b)

### 3. Methodological improvements
1. The main improvements to the algorithm are the introduction of self-supervised consistency loss, structured predictive value prefixes, and model-based policy corrections.

2. These improvements allow the algorithm to better learn environmental models with limited data and improve the exploration capabilities of MCTS, resulting in better performance.

### 4. Issues addressed 
The algorithm solves the following three main problems:

1. **Lack of supervision for the environment model**: the traditional MCTS algorithm only relies on signals such as rewards, values, and strategies, which cannot provide enough training signals. Therefore, the algorithm introduces self-supervised consistency loss to provide more training signals for the environment model.

2. **State aliasing problem**: In long-term prediction, the state aliasing problem leads to inaccurate reward prediction. Therefore, the algorithm proposes structured prediction value prefixes that can automatically handle the intermediate state aliasing problem.

3. **Bias in value targets**: due to trajectories coming from old strategies, it leads to bias in value targets. Therefore, the algorithm proposes model-based strategy correction that reduces the bias of trajectories based on old strategies by recalculating the value targets in the trajectories.

## Experiments
This paper focuses on the performance of the EfficientZero algorithm in two benchmarks, the Atari 100k and the DMControl 100k, and ablation experiments with multiple components are performed to analyze the role of each component.

First, the EfficientZero algorithm is compared against multiple baselines in the Atari 100k benchmark test, including SimPLe, OTRainbow, CURL, DrQ, SPR, and MuZero methods. The results show that the EfficientZero algorithm outperforms human players and all other methods on Atari 100k, with a mean score of 1.904 and a median score of 1.160. 

Second, the EfficientZero algorithm was compared to several other methods in the DMControl 100k benchmark, including Pixel SAC, SAC-AE, State SAC, Dreamer, CURL, and MuZero.The results show that the EfficientZero algorithm also performs well on this task and achieved a high level of performance.

Next, the authors conducted ablation experiments on three components of the EfficientZero algorithm, self-supervised consistency, end-to-end value prefixes, and model primitives off-policy correction. The experimental results show that all three components have a positive impact on the performance of the EfficientZero algorithm, with self-supervised consistency being one of the most critical components. 

In addition, the authors conducted several other experiments to validate some of the assumptions of the EfficientZero algorithm, such as the difference between direct prediction of rewards and end-to-end learning of value prefixes and the effectiveness of the off-policy correction.

![image](https://github.com/user-attachments/assets/bc0890e6-82ea-4bd0-a99b-ba9b4cb543b6)

## Conclusion

### 1. Advantages of the Thesis
1. EfficientZero has higher efficiency and better performance.

2. In addition, the authors conducted detailed experiments and analysis to demonstrate the effectiveness and feasibility of EfficientZero.

![image](https://github.com/user-attachments/assets/abfa96ba-4051-4213-9927-3b5ec312fa78)

### 2. Innovative points
1. Using self-supervised learning to learn a temporally consistent model of the environment;

2. learning the value prefixes in an end-to-end manner, which helps to mitigate cumulative errors in the model; 

3. utilizing learned models to correct for out-of-policy value targets.

These improvements allow EfficientZero to better handle image-based environments and enable efficient learning with limited data.

### 3. Future Works
1. Future research can further explore how to extend EfficientZero to a wider range of domains, such as designing better continuous action spaces.

2. It can also investigate how to accelerate MCTS and how to combine it with lifelong learning to realize more efficient and flexible RL algorithms. 
