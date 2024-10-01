# Q-Transformer: Scalable Offline Reinforcement Learning via Autoregressive Q-Functions
[paper link](https://arxiv.org/pdf/2309.10150) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a reinforcement learning method called Q-Transformer that trains multi-tasking policies from large offline datasets and is able to utilise human demonstrations and autonomously collected data.          | Reinforcement Learning  (RL)       |

## Methodology

### 1. Abstract
The method uses the Transformers model to provide a scalable representation for Q-functions trained via offline temporal difference backup. By discretising each action dimension and representing the Q-values of each action dimension as separate tokens, effective high-capacity sequence modelling techniques can be applied for Q learning. The article describes several design decisions to achieve good offline RL training performance and demonstrates that Q-Transformer outperforms previous offline RL algorithms and imitation learning techniques on a large and diverse set of real-world robot manipulation tasks.

![image](https://github.com/user-attachments/assets/f5f926f2-67c1-4a64-98f9-6eb475520783)

### 2. Method Description 
The Q-Transformer proposed in this paper is an offline RL algorithm based on the Transformer model for the task of sparse rewards. The method avoids the computational burden of high-dimensional data by treating the action space in dimensions and applying an autoregressive strategy. Specifically, for a given time step and the actions in the corresponding trajectory, an action vector split by dimension is defined and an autoregressive strategy is used to compute the Q-value of each action dimension within a given time window. In addition, the method introduces a conservative Q-function regularisation term to ensure that the learned Q-functions do not have negative values. Finally, to improve the learning efficiency, the article also proposes the use of Monte Carlo returns and n-step returns to accelerate the learning process.

![image](https://github.com/user-attachments/assets/dbcedb1e-c88e-487d-af2e-57fdbd5d9575)

### 3. Methodological improvements
Compared with the traditional Q-learning algorithm, Q-Transformer adopts a more efficient computation method, which can effectively reduce the computational complexity. Meanwhile, the introduced conservative Q-function regularisation term can effectively prevent the negative value problem and improve the stability of the algorithm. In addition, the combination of Monte Carlo returns and n-step returns further improves the learning efficiency.

### 4. Issues addressed 
This paper mainly addresses some challenges faced by reinforcement learning algorithms in sparse reward tasks, such as high-dimensional data, negative value problems, and learning efficiency. To address these issues, this paper proposes an offline reinforcement learning algorithm Q-Transformer based on the Transformer model, which can achieve better results in sparse reward tasks.

## Experiments
**Training dataset**: a dataset collected by 13 robots was used, including demo data and low quality data collected autonomously. The demo data came from human telemanipulation and consisted of about 700 different tasks, each with a separate linguistic description. The authors used up to 100 demos to represent each task and ended up with about 38,000 demos. 

All of these demos successfully completed the task and received a reward of 1.0. The rest of the data was collected by allowing the robot to autonomously execute a strategy, which was learned through behavioural cloning. To ensure that Q-Transformer did not observe more successful trials than other imitation learning algorithms, the authors discarded all successful autonomy collection data. This left about 20,000 additional trials with failed autonomous collection, each of which was rewarded with 0.0, yielding a total of about 58,000 trials.

**Performance Evaluation**: In order to evaluate the performance of Q-Transformer when dealing with real-world offline datasets while efficiently integrating autonomously collected sub-optimal data, the authors tested it on 72 unique manipulation tasks covering a wide range of skills, such as ‘drawer pick-and-place’, ‘open and close drawer’, “move object close to target”, with 18, 7 and 48 unique task instructions per skill to specify different object combinations and drawers.

![image](https://github.com/user-attachments/assets/202a8f01-1e85-48aa-814a-3b4e2e5ff67b)

Since there are at most 100 presentations in the training set for each task, the authors found it difficult to achieve good performance using imitation learning algorithms such as RT-1, which is similar to the Transformer architecture, when only a limited number of human presentations are used. Existing offline RL methods such as IQL and Transformer-based methods such as Decision Transformer, which can learn both successful demonstrations and failed trials, outperform RT-1, albeit by a relatively small margin. Q-Transformer has the highest success rate, outperforming both the Behavioural Cloning benchmark (RT-1) and the offline RL baseline (Decision Transformer, IQL), exceeding the average performance of the best prior method by about 70%. This demonstrates that Q-Transformer can improve human demonstrations by leveraging autonomously collected sub-optimal data.

![image](https://github.com/user-attachments/assets/280463d2-484b-4383-871c-2d517725e28d)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new robot RL framework, Q-Transformer, which uses a high-capacity Transformer model to tackle large-scale multi-task robot RL problems.
  
  2. By decomposing the action space into multiple dimensions and discretising each dimension, it makes it possible to train using a simple discrete action Q-Learning method.
  
  3. By using a combination of Monte Carlo and n-step payoffs, as well as conservative regularisation against distributional bias, it allows the method to perform well on both narrow and wide datasets.

  4. Experimental results show that Q-Transformer has better performance than other previously proposed architectures in multi-task RL under large-scale text conditions.
Methodological Innovation Points

### 2. Innovative points
  1. The paper proposes a new robot RL framework, Q-Transformer, which uses a high-capacity Transformer model to tackle large-scale multi-task robot RL problems.
  
  2. By decomposing the action space into multiple dimensions and discretising each dimension, it makes it possible to use a simple discrete action Q-Learning method for training.
  
  3. By using a combination of Monte Carlo and n-step payoffs, as well as conservative regularisation against distributional biases, it allows the method to perform well on both narrow and wide datasets.

### 3. Future Works
  1. Limitations of this thesis include the fact that it is only applicable to sparse binary reward tasks and may become complicated under high-dimensional action spaces.
  
  2. Future research directions include extending Q-Transformer to online fine-tuning for more effective autonomous improvement of complex robot strategies.   
