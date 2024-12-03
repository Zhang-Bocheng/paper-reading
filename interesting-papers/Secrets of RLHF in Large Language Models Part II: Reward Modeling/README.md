# Secrets of RLHF in Large Language Models Part II: Reward Modeling
[paper link](https://arxiv.org/pdf/2401.06080) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes two challenges faced when using reward models to drive optimisation in Reinforcement Learning Human Feedback (RLHF): inaccurate and ambiguous preferences in the data and the difficulty of generalising reward models to other distributions after they have been trained on a particular distribution.          |         Large Language Models (LLMs) |

## Methodology

### 1. Abstract
To address these issues, the authors propose two approaches: multiple reward models based on a voting mechanism to measure the strength of preferences in the data, and the introduction of comparative learning and meta-learning to augment the ability of the reward models to discriminate between choice and rejection responses and to improve the generalisation of the models. In addition, the authors provide datasets and training code resources for analysing the experiments. These methods can be applied to iterative RLHF optimisation to achieve language models that are more consistent with human values and intentions.

### 2. Method Description 
This research aims to explore how data affects the modelling of human preferences and presents a framework for preference modelling based on reward models. The framework consists of three stages: supervised fine-tuning (SFT), preference sampling and reward model training (RM), and reinforcement learning fine-tuning using Proximal Policy Optimization (PPO). In the second phase, a reward function is used to measure the preference strength of the user's feedback and adjust the model parameters based on this information. In the third phase, reinforcement learning techniques are used to further optimise the model performance.

![image](https://github.com/user-attachments/assets/e1c301d2-a97a-4b2e-9414-af208fe713c5)

### 3. Methodological improvements
The main improvement of this study is the proposal of a new preference strength metric that calculates the average preference difference and standard deviation between each comparison pair through multi-model voting. This method can help distinguish between preference data of different strengths and can improve the model's ability to recognise false or ambiguous preferences.

### 4. Issues addressed 
  1. The study addressed two main questions:
  2. How to accurately measure the strength of human preferences and use data of different strengths for preference modelling.
  3. How to effectively handle erroneous or ambiguous preference data to improve the robustness and accuracy of the model.

## Experiments
This paper focuses on how to use reward models to optimise the performance of large language models, and proposes two methods: label flipping and label smoothing and adaptive margins. Among them, label flipping and label smoothing can effectively avoid the influence of noisy data on the reward model, while adaptive margins can improve the effectiveness of the reward model when dealing with data of different intensities. In addition, this paper proposes a meta-learning-based method, MetaRM, for training reward models to adapt to changes in environmental distributions. Finally, this paper demonstrates the effectiveness and superiority of the proposed reward model by comparing it with the benchmark model and the soft-labelled + marginal model.  

![image](https://github.com/user-attachments/assets/7288449c-7e54-4ae1-afec-1376d0a07005)

## Conclusion

### 1. Advantages of the Thesis
  1. The authors address the problem of noise and ambiguity in preference evaluation data by introducing preference strength measures and multiple reward model voting methods, and use meta-learning and contrastive learning to enhance the generalisation ability of the reward model. Experimental results show that the final alignment performance can be significantly improved using reward models trained with the above methods.
  2. And, this paper emphasises the importance of practicality by showing a large number of training procedures, including reward models and algorithms such as PPO, to make it easier for readers to understand how to analyse and improve reward models. This is more valuable than current work which usually focuses only on outstanding results.

### 2. Innovative points
  1. Introducing preference strength measures and multiple reward model voting methods to address noise and ambiguity in preference evaluation data;
  2. The use of meta-learning and comparative learning to enhance the generalisation ability of reward models;
  3. Demonstrating a number of training procedures, including reward models and algorithms such as PPO, to help readers better understand how to analyse and improve reward models.

### 3. Future Works
In future research, the authors may continue to explore how to further optimise the reward model and enhance its generalisation capabilities, taking into account additional factors such as the quality and quantity of preference data. 
