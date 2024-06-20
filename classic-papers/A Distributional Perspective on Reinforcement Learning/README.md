# A Distributional Perspective on Reinforcement Learning
[paper link](https://arxiv.org/pdf/1707.06887) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2017 |   The article proves theoretically some properties of the distributive Bellman operator and proposes an implementation method that becomes an important cornerstone for subsequent research       |     Reinforcement Learning       |

## Methodology

### 1. Abstract
  This paper presents a new perspective on reinforcement learning, the value distribution. Unlike traditional reinforcement learning methods, not only focuses on the expected returns but also considers the probability distribution of random returns. The authors demonstrate through theoretical analysis and experimental results that there is significant instability of value distributions in control settings, and based on this, they design a new algorithm to learn approximate value distributions.

### 2. Method Description 
  The paper proposes a distribution-based reinforcement learning algorithm called Disributed Bellman Projection. While traditional reinforcement learning algorithms typically use expectation values to represent the value function of a state, the distributed reinforcement learning algorithm treats the value function as a random variable and considers its probability distribution. The algorithm optimizes the value function by maximizing the expected value of the cumulative payoff, while taking advantage of the distributed nature to deal with continuous state space and action space.

### 3. Key concepts
  The Distributed Bellman Projection typically refers to a projection step in the context of distributional RL algorithms. This step involves projecting a distribution (resulting from applying the Bellman operator) back onto a parameterized family of distributions used by the algorithm. This ensures that the updated distribution remains within the representable family, facilitating stable learning.
  
### 4. Methodological improvements
  Distributed reinforcement learning algorithms have the following advantages over traditional reinforcement learning algorithms:

  1. Can handle continuous state space and action space.
  2. Can effectively handle sparse reward problems.
  3. Can share knowledge in different environments.

  In addition, the algorithm introduces the distributed Bellman projection operation, which can efficiently compute the distribution of the value function and can handle high-dimensional, discrete state spaces and action spaces.
  
### 4. Issues addressed 
  The algorithm mainly solves the problem that traditional reinforcement learning algorithms cannot deal with continuous state space and action space, as well as the sparse reward problem. In addition, it can improve the efficiency and generalization ability of the algorithm, which enables the reinforcement learning algorithm to be used in a wider range of application scenarios.

## Experiments
  This paper focuses on the application of distribution learning algorithms in reinforcement learning, and verifies and compares them through experiments. Specifically, this paper uses the following three comparison experiments:

  1. Comparing the effect of different numbers of atoms on performance: this paper uses different numbers of atoms to represent value distributions and compares their performance on training games. The results show that using more atoms improves performance, but too many atoms can lead to overfitting.

  2. comparing the performance of C51 with existing algorithms: In this paper, auther compares C51 with other existing reinforcement learning algorithms (e.g., DQN, Double DQN, Dueling architecture, and Prioritized Replay) and evaluate them on a test set. The results show that C51 achieves better performance in most of the games, especially excelling in the case of sparse rewards.

  3. Comparing the performance of C51 with that of a human player: this paper also compares the difference between the performance of C51 during training and that of a fully trained human player. The results show that in many games, C51 outperforms the human player during training, which demonstrates the algorithm's strong learning ability.

  Overall, the experimental results in this paper show that distribution learning algorithms have great potential in reinforcement learning and can achieve better performance with reasonable parameter settings and network architecture design.
  
## Conclusion
### 1. Advantages of the Thesis
  1. The paper presents a distribution-based learning approach that is able to outperform most previous results on the Atari 2600.
  2. The distributional learning approach mitigates the instability in Bellman's optimality equation and provides more stable prediction results.
  3. The approach to learning value distributions provides a new framework for the design of reinforcement learning algorithms that can be designed with assumptions about the domain or the learning problem itself in mind.
  4. The researchers used the DQN algorithm to implement distributed learning and achieved significant performance gains on the Arcade Learning Environment.

### 2. Innovative points
  1. A distribution-based learning approach is proposed to make reinforcement learning algorithms more stable and with better performance.
  2. The perspective of distribution is introduced to make the design of reinforcement learning algorithms more flexible and smooth.
  3. The Wasserstein distance is used as the loss function, which can better approximate the real distribution.

### 3. Future Works
  1. Further research can be done on how distributed learning can be applied to reinforcement learning tasks in other domains.
  2. Other loss functions such as KL scatter can be explored for better results.
  3. Other techniques such as deep neural networks can be combined to improve the effectiveness of distributed learning.


