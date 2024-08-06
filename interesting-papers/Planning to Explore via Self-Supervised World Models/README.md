# Planning to Explore via Self-Supervised World Models
[paper link](https://arxiv.org/pdf/2005.05960.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a self-supervised reinforcement learning agent called Plan2Explore that addresses challenges in reinforcement learning through a new exploration method and the ability to quickly adapt to new tasks.        |  Reinforcement Learning         |

## Methodology

### 1. Abstract
Unlike previous approaches, during exploration, the agent utilizes planning to seek the novelty of the expected future, rather than calculating the novelty of an observation point once it is reached. Experimental results show that Plan2Explore outperforms previous self-supervised exploration methods even without training supervision or task-specific interactions, and nearly matches the performance of oracle with rewarded access.

![image](https://github.com/user-attachments/assets/b3c83f45-d7ff-4b77-919d-631ae8a99152)

### 2. Method Description 
The paper presents a world model-based RL algorithm for exploring unknown environments and adapting to downstream tasks. The main idea is to predict future state sequences by training a parameterized world model and use these predictions for planning and decision making.

  1. **Image encoder**: converts the observed image into a latent space representation.
  2. **A posteriori dynamic model**: estimates the probability distribution of the next state based on the current state, the action, and the output of the image encoder.
  3. **A priori dynamic model**: estimates the probability distribution of the next state considering only the current state and action.
  4. **Reward predictor**: given the current state, predicts the expected reward value.
  5. **Image decoder**: given the current state, generate the corresponding image.

These components are jointly trained to maximize the Evidence Lower Bound (ELBO), resulting in a valid world model. This model can then be used to plan actions to be taken in the current state, and a value function can be computed by sampling the distribution of future states. In addition, the algorithm introduces two important techniques:

  1. **The "dreamer" algorithm** is used to efficiently learn parameterized strategies in the world model to maximize long-term rewards.

  2. **Using "implicit information entropy"** as an exploration goal to guide the agent to explore the unknown state space.

![image](https://github.com/user-attachments/assets/42908d68-aba8-4ece-90c0-1e8ceb18ce0f)

### 3. Methodological improvements
The algorithm has the following advantages over traditional model-based RL methods:

  1. It does not need an explicit environment model, but learns a parameterized world model directly from the data.
  
  2. Can handle high-dimensional, continuous state space and action space without discretization or projection to lower dimensional spaces.
  
  3. Can share the same world model across multiple tasks, leading to increased efficiency and generalization capabilities.

### 4. Issues addressed 
The algorithm solves the following problem:

  1. How to explore efficiently in unknown environments in order to collect sufficient empirical data?
  
  2. How to utilize existing empirical data to adapt to downstream tasks without additional environment interactions?
  
  3. How to design an efficient learning algorithm that can share the same world model across multiple tasks?

## Experiments
This paper focuses on the performance of a RL model based on the Plan2Explore algorithm on zero- and few-sample adaptation tasks, and compares it with other related methods. Specifically, the paper includes four areas of experimentation:

  1. Is the model able to transfer and solve new tasks?

The experiment tests whether the model is able to learn a global model of the environment without using any task-specific information, and whether it can effectively apply this model in downstream tasks, by providing a reward function and training a predictor. The results show that Plan2Explore outperforms other unsupervised methods and is comparable or even better than Dreamer.

  2. After how many interactions can fully supervised learning be achieved?

The experiment was designed to test the number of interactions required for the model to adapt to a specific task when it needs to. The results show that even with only 100-150 supervised interactions, Plan2Explore is able to adapt quickly to the task and is comparable to Dreamer in terms of data efficiency.

![image](https://github.com/user-attachments/assets/27a7bbc9-889c-4d2e-aaa5-57e80954ed0d)

  3. Are self-supervised models more capable of generalization than models dedicated to a specific task?

This experiment was designed to test the generalization ability of the model. The results show that Plan2Explore performs well on multiple tasks, while Dreamer can only perform well on a single task.

  4. Should expected novelty be maximized instead of retrospective novelty?

This experiment aimed to compare the advantages of calculating expected novelty and retrospective novelty. The results show that the method of calculating expected novelty performs better than the method of recalling novelty. 

![image](https://github.com/user-attachments/assets/57b2a573-3e76-43ae-86f2-732a241d75de)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a self-supervised RL method called Plan2Explore that collects data through a reward-free exploration environment and uses that data to solve downstream tasks.
  
  2. The method uses a world model to plan exploration to maximize expected novelty rather than retrospective novelty. This approach avoids the problem of needing a large number of samples in order to fit the downstream task and can accurately train the world model with high-dimensional image inputs.
  
  3. In addition, the method explores issues such as how to compare different types of intrinsically motivated goals and the ability to generalize between self-supervised models and task-specific models.

### 2. Innovative points
  1. The methodological innovation of the thesis is the introduction of a world model to plan exploration and the use of expected novelty as an exploration goal.
  
  2. This approach solves downstream tasks without additional environment interaction and can efficiently process high-dimensional image inputs.
  
  3. In addition, the approach explores important issues such as how to define effective exploration goals and how to evaluate different types of intrinsically motivated goals.

![image](https://github.com/user-attachments/assets/f1050cb1-19d1-43fe-ba55-9f2cf8fe8967)

### 3. Future Works
  1. Future research directions include further improving the design of world models and optimization algorithms to better handle complex environments and tasks.
  
  2. It is also possible to investigate how to extend this approach to broader domains, such as natural language processing and speech recognition.


