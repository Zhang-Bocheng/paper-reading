# Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion
[paper link](https://arxiv.org/pdf/2401.17583) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes an Agile But Safe learning control framework designed to enable quadrupedal robots to walk efficiently and safely in complex environments. The framework consists of an agility strategy and a recovery strategy that work together to achieve high-speed and collision-free navigation.           | Reinforcement Learning         |

## Methodology

### 1. Abstract
In this case, the agility strategy is responsible for executing agile motor skills in obstacles, while the recovery strategy is used to prevent failure situations. The switching of the whole framework is driven by a learned control-theoretic value network and protects the robot through a closed loop. The training process involves the learning of the agility strategy, the value network, the recovery strategy, and the external perceptual representation network, and is done in a simulation environment. These trained modules can be directly deployed in the real world to achieve the ability to walk at high speed and without collision in both indoor and outdoor spaces.

### 2. Method Description 
The dual-policy architecture proposed in this paper consists of an agility policy and a recovery policy designed to achieve efficient and safe locomotion capabilities for robots. During training, a reinforcement learning algorithm is used to train the two policies by simulating the environment and optimising their performance through an evaluation function. Specifically, the method uses target-based position and orientation as states, with collision avoidance and reaching a predefined target position as the target reward value, while considering constraints such as joint angles and velocities. In addition, the method introduces a time discount factor to balance current and future rewards, as well as random noise and dynamic changes to increase the robustness and generalisation of the model.
![image](https://github.com/user-attachments/assets/6c9bf97b-74e8-430c-ac95-e84dd8e5f469)

### 3. Methodological improvements
  1. Reinforcement learning based training approach can automatically learn the optimal policy without manually designing the control rules.
  2. The use of dual-policy architecture can better balance the trade-off between speed and safety and improve the overall performance of the robot.
  3. Introducing a time discount factor can make the robot more focused on future gains and thus act more cautiously.
  4. Random noise and dynamic changes can increase the robustness and generalisation of the model, allowing it to adapt to different scenarios and tasks.

### 4. Issues addressed 
  1. How to achieve efficient robot motion control so that the robot can move quickly to a specified position in a complex environment.
  2. How to ensure the safety of the robot to avoid collision and other dangerous situations during the movement.
  3. How to improve the performance of the robot so that it can perform better in different scenarios and tasks.

## Experiments
This paper focuses on the experimental results of an agile obstacle avoidance system (ABS) based on inverse reinforcement learning in both simulated and real environments, and compares them with previous studies. Specifically, the authors conducted the following comparison experiments:

  1. between an agile strategy based on inverse reinforcement learning (πAgile) and an agile strategy without external modules (PPO-Lagrangian) to understand the trade-off between agility and safety;

 ![image](https://github.com/user-attachments/assets/14c2533c-12b5-4ce4-976c-649799378e5b)
 
  2. A comparison between the ABS system and the previous state-of-the-art agile running strategy (SOTA) to verify the superiority of the ABS system;
  
  3. Simulation experiments of the ABS system in different settings, including different distributions of the number and difficulty of obstacles and the use of different RA values and recovery strategies to measure the boundaries of agility and safety;
 
 ![image](https://github.com/user-attachments/assets/900081ed-67af-4700-9505-c79cd6975f3b)
 
  4. Comparison of the performance of the ABS system with other baselines (πAgile and LAG) in simulated and real environments, including metrics such as success rate, collision rate, and average peak speed;
  
  ![image](https://github.com/user-attachments/assets/44781dfa-9616-4a3c-a9bb-0861797e0fb6)

  5. Robustness tests of the ABS system under different conditions, such as operating on icy terrain, carrying heavy loads, and suffering from external disturbances.

In response to these experiments, the authors draw the following conclusions:
  1. There is a trade-off between agility and safety, but by introducing RA values and recovery strategies, it is possible to break this boundary and improve safety with only a small loss of agility;
  2. The ABS system has a higher success rate and lower crash rate relative to the other baselines and performs well in both simulated and real environments;
  3. That the ABS system has better robustness and is able to maintain efficient and stable performance under different conditions.

## Conclusion

### 1. Advantages of the Thesis
  1. Safe quadruped robot motion planning at high velocities was achieved;
  2. A dual-strategy design was used to achieve a balance between perceptual agility and safety;
  3. An RA-valued network was utilised to control strategy switching, simplifying the learning process and allowing offline learning;
  4. A low-dimensional external sensory representation was used to improve efficiency, and a ray prediction network was trained to map raw depth images onto this representation.

### 2. Innovative points
  1. A two-policy design is proposed that allows a balance between the perceptual agility and safety of the robot;
  2. An RA-valued network is used to control policy switching, which makes the learning process simpler and allows for offline learning;
  3. Using a low-dimensional external sensory representation to improve efficiency and training a ray prediction network to map raw depth images onto this representation.
     
### 3. Future Works
  1. Extending this approach to other types of robots or mobile platforms;
  2. Investigating how to achieve safe quadrupedal robot motion planning at high speeds in more complex environments;
  3. Exploring how to further improve the robustness and generalisation of the algorithm.   
