# Decision Transformer: Reinforcement Learning via Sequence Modeling
[paper link](https://arxiv.org/pdf/2106.01345) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper introduces Decision Transformer, a new framework for abstracting reinforcement learning problems into sequence modeling problems         | Reinforcement Learning          |

## Methodology

### 1. Abstract
  The approach leverages relevant advances in the Transformer architecture and language modeling to output optimal actions by means of conditional sequence modeling. Unlike previous approaches, Decision Transformer does not need to fit a value function or compute a policy gradient, but simply utilizes a causally masked Transformer model to output optimal actions directly. Experimental results show that the Decision Transformer exhibits comparable or even better performance than state-of-the-art offline reinforcement learning baselines on Atari, OpenAI Gym, and Key-to-Door tasks.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/34a472f5-fc45-4ae6-b3bb-5491ac751a1c)

### 2. Method Description 
  This paper presents a model called Decision Transformer for autoregressively modeling trajectories in RL. The model is based on the transformer architecture and is optimized for trajectory representation, making it possible for transformers to learn meaningful patterns and to be able to conditionally generate actions at test time. To address the difficulty of modeling rewards directly, this paper uses returns-to-go as an alternative to rewards as inputs. Specifically, the model inputs information from the last K time steps into the model, including information such as returns-to-go, states, or actions. For environments with visual inputs, the state is fed into a convolutional encoder instead of a linear layer. In addition, an embedding is added to each time step to distinguish it from the standard location embedding. These embeddings are processed by a layer of GPT model to predict future action tokens. During training, discrete and continuous actions are predicted using either cross-entropy loss or mean square error loss, respectively.
    
### 3. Methodological improvements
  The main improvements of Decision Transformer over traditional transformer models are the choice of trajectory representation and the design of the autoregressive generation method. Specifically, the model uses payoffs to goals instead of rewards as inputs, which allows the model to better predict future actions and thus improve performance. The model employs an autoregressive generation approach, where an action is generated one at a time based on the current state, and then the state and reward-to-goal are updated based on this action until a termination state is reached. This autoregressive generation approach allows the model to better utilize historical information to guide future decisions.
  
### 4. Issues addressed 
  Decision Transformer solves two problems in traditional RL: 
  1. how to make transformers learn meaningful patterns; 
  2. how to conditionally generate actions at test time.

  By choosing a suitable trajectory representation and autoregressive generation method, the model can effectively solve these problems, thus improving the effectiveness of RL.
  
## Experiments
  This paper focuses on the performance of Decision Transformer (DT) in the field of offline RL and compares it with some traditional model free offline RL algorithms and behavioral cloning algorithms. The experiments included two control task environments, Atari and OpenAI Gym, which were tested for high-dimensional visual inputs and continuous control tasks, respectively.

  For the experiments in the Atari environment, the authors chose four tasks (Breakout, Qbert, Pong, and Seaquest) and used the dataset from Agarwal et al. for evaluation. The authors compared the DT to three other methods (CQL, REM, and QR-DQN) and reported the mean normalized scores. The results show that DT is comparable to CQL in three games and outperforms REM, QR-DQN and the behavioral cloning algorithm in all four games.

  For the experiments in the OpenAI Gym environment, the authors considered a continuous control task and used three settings from the D4RL benchmark dataset (Medium, Medium-Replay, and Medium-Expert). The authors compared the DT with four other methods (CQL, BEAR, BRAC and AWR) and reported the mean normalized scores. The results show that DT achieved the highest scores on most tasks and was competitive on the remaining tasks.
  
## Conclusion

### 1. Advantages of the Thesis
  The paper presents a new RL algorithm, Decision Transformer, which enables effective behavior generation and long-term reward prediction by applying ideas from sequence modeling to RL. The algorithm performs well on standard offline RL benchmarks and does not require the use of techniques such as value pessimism or behavioral regularization to ensure stable performance. And, the algorithm can be used for model generation tasks in online RL, providing new ideas and directions for subsequent research.
  
### 2. Innovative points
  The main contribution of the paper is the proposal of Decision Transformer, a novel RL algorithm whose core idea is to apply the idea of sequence modeling to RL for effective behavior generation and long-term reward prediction. Specifically, the algorithm adopts a form of autoregressive modeling to generate corresponding behavior and reward predictions by encoding sequences of historical states, actions and rewards. 
  
  The algorithm also introduces a variable-length context mechanism, which allows the model to better capture the impact of historical information on current decisions. These innovations lead to better generalization ability and robustness of the decision transformer, which achieves excellent performance in various RL tasks.
  
### 3. Future Works
  The DT algorithm proposed in this thesis has achieved some success in the field of RL, but there are still some challenges and unsolved problems. There are issues such as how to further improve the efficiency and interpretability of the model, and how to cope with more complex and diverse environments and tasks.
  
  Therefore, future research can consider combining other technical means, such as meta-learning and transfer learning, to improve the adaptability and generalization ability of the model; and also try to explore more application scenarios, such as multi-intelligent body collaboration, robot control and other fields, to expand the application scope of RL.
  
