# ArtiGrasp: Physically Plausible Synthesis of Bi-Manual Dexterous Grasping and Articulation
[paper link](https://arxiv.org/pdf/2309.03891) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new method called ArtiGrasp for synthesising bimanual grasping and joint motion. The task is challenging because control of global wrist motion and precise finger control is required to make an object move articulately.          | Reinforcement Learning         |

## Methodology

### 1. Abstract
ArtiGrasp uses reinforcement learning and physics simulation to train a strategy for controlling global and local hand poses, and to unify grasping and articulatory motion in a single strategy, guided by a hand pose reference. To facilitate the training of the precise finger control required for joint movements, the paper also presents a learning programme of progressively increasing difficulty. 

In addition, this paper presents the Dynamic Object Grasping and Articulation task, which involves the process of bringing an object to a target joint position, including grasping, moving, and joint motion. Experimental results show that the method performs well on this task and can generate actions using noisy hand object pose estimates from a commercial image regressor.

### 2. Method Description 
This paper presents a RL framework called ArtiGrasp for grasping and manipulation tasks of dynamic objects. The framework uses physical simulation to model the behaviour of hands and objects, and trains two independent hand strategies via neural networks for the tasks of grasping and manipulating different objects. At each time step, an action is selected and applied to the physics simulation based on the current state, and then the updated state is used as input for the next time step. The ultimate goal is for the system to be able to stably grasp and manipulate an object to a specified target position and angle.
![image](https://github.com/user-attachments/assets/b5bf7239-37a7-4b56-ad21-2bc3e67b55f2)

### 3. Methodological improvements
ArtiGrasp employs a RL approach that is more adaptive and generalisable than traditional model- or rule-based approaches. In addition, ArtiGrasp introduces some technical tools to improve performance and stability, such as feature extraction layers, reward function design, and learning curves.

### 4. Issues addressed 
ArtiGrasp mainly addresses the control problem in dynamic object grasping and manipulation tasks. Traditional model- or rule-based approaches usually require the manual design of complex control algorithms, which makes it difficult to cope with complex and changing real-world scenarios. In contrast, ArtiGrasp can automatically learn the optimal control strategy by means of RL, thus better adapting to different scenarios and task requirements. At the same time, ArtiGrasp can also handle the situation of multiple hands operating together, which improves the flexibility and efficiency of the system. 

## Experiments
This paper focuses on a deep RL approach for dynamic object grasping and manipulation tasks, and several experiments are conducted to verify its performance.

First, in terms of experimental details, the authors used the PPO algorithm for RL training and RaiSim for physics simulation. All policies were trained on a single Nvidia RTX 6000 GPU and 128 CPU cores, and the whole process took about three days. The authors divided the dataset into two parts, one for training and the other for testing. For the image estimation used in the experiments, the authors only used 60 hand pose references in the validation set because the model was trained in the ARCTIC training set.
![image](https://github.com/user-attachments/assets/1f086414-c2f9-4907-88ff-154ef91f5f64)

Next, the authors evaluated the grasping and manipulation tasks separately and conducted experiments to evaluate the dynamic object grasping and manipulation tasks. For the grasping task, the authors evaluated using three metrics: **success rate, position error, and angular error**. For the manipulation task, the authors used three metrics for evaluation such as success rate, displacement error and angular error. 
![image](https://github.com/user-attachments/assets/5fcc6c12-b5e3-4e10-960c-1677d1dfb5a4)

Also, the authors define an additional metric to evaluate the success rate for dynamic object grasping and manipulation tasks. The deep RL approach proposed by the authors shows significant advantages in all metrics, with better manipulation performance and comparable grasping performance than the baseline-based approach.

In addition, the authors conducted experiments to generate new actions, using hand poses reconstructed from image predictions as input. Despite problems such as reconstruction noise, the authors' method was able to maintain comparable performance to hand poses acquired from motion capture. This demonstrates the ability of the authors' method to combat prediction noise and to synthesise new actions using hand pose information from a single image.
![image](https://github.com/user-attachments/assets/abd83f45-5bdc-4168-9a66-11089ae14fe8)

Finally, the authors performed several ablation experiments to evaluate the impact of each component on the framework. The results show that the performance of the model can be further improved by controlling the learning sequence and introducing operational features, among other things. 
![image](https://github.com/user-attachments/assets/48f4ac68-0a93-4dfe-ae16-73e2c5b04ead)

## Conclusion

### 1. Advantages of the Thesis
  1. Stable hand-object contact and force control strategies can be learnt, ensuring that objects do not undergo irrational motions such as penetration.
  
  2. Generalised control strategies that are applicable to different tasks and objects can be learned from a single hand pose reference input, avoiding the problem of retraining for each task or object.
  
  3. A learning process of gradually increasing difficulty is proposed, allowing the model to gradually master complex grasping and manipulation skills.
  
  4. Experimental results show that the method is able to successfully perform dual-arm grasping and manipulation tasks in a wide range of situations and can utilise individual hand poses from image estimation as input.

### 2. Innovative points
  1. A physical simulation environment is utilised for RL, which leads to the learning of a stable control strategy.
  
  2. A learning process of gradually increasing difficulty is proposed, enabling the model to gradually master complex grasping and manipulation skills.
A generalised reward function is introduced, allowing the model to generalise its learning across different tasks and objects.

### 3. Future Works
  1. Explore more efficient NN structures and algorithms to improve model performance and robustness.
  
  2. Investigating how to better handle noisy inputs and exploring how to combine other sensor data (e.g., depth cameras) with hand pose estimation to improve the performance of the model.
  
  3. To further investigate how this approach can be applied to robotic systems in real-world scenarios and explore how it can be combined with other techniques (e.g. SLAM) for more complex tasks. 
