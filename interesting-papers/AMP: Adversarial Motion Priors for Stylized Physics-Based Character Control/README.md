# AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control
[paper link](https://arxiv.org/pdf/2104.02180) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper introduces a new approach, AMP (Adversarial Motion Priors), for elegant and realistic behavioral synthesis in physical simulation character control         |  Generative Adversarial Networks(GANs)         |

## Methodology

### 1. Abstract
  While traditional data-driven approaches based on motion tracking require manual design of objective functions and selection of appropriate motions, AMP enables fully automated motion selection and stylization by leveraging adversarial learning. This approach allows for the specification of high-level task objectives using simple reward functions and low-level behavioral styles using action datasets that are not sorted or serialized.
  
  AMP trains an adversarial motion prior that provides stylistic rewards for reinforcement learning, which is dynamically interpolated and generalized to the dataset. Experimental results show that AMP produces high-quality actions that are comparable to state-of-the-art tracking techniques and can be easily adapted to large unordered action datasets.
  
### 2. Method Description 
  The goal of the system is to synthesize a control strategy, given a reference motion dataset and a mission goal, that enables a character to achieve the mission goal in a physical simulation environment and to utilize behaviors similar to those of the reference motion. Crucially, the character's behavior does not have to exactly match any particular behavior in the dataset, but only needs to take actions that are similar to the general characteristics exhibited in the reference motion set. Together, these reference motions provide a sample-based definition of behavioral styles, and by providing the system with different sets of motion datasets, the character can be trained to perform tasks in many different unique styles.
  
### 3. Key concepts
  _Generative Adversarial Imitation Learning (GAIL)_: A machine learning framework that combines ideas from imitation learning and GANs to train policies in a RL setting. It aims to learn a policy that can imitate expert behavior without access to the reward function that guided the expert. Instead, GAIL relies on expert demonstrations and uses an adversarial training process to achieve this.
  
### 4. Methodological improvements
  The system can be applied directly to the raw motion data, eliminating the need for task-specific annotations or segmentation of clips into individual skills. Unlike previous frameworks, the system does not require segmentation of each movement.
  
### 5. Issues addressed 
  The system solves the problem of assembling into a control strategy based on reference motion data in a physical simulation environment, while realizing the task objectives and having a natural and smooth motion performance. In addition, the system provides the ability to perform tasks in a variety of different unique styles.
  
## Experiments
  This paper focuses on the authors' findings on using deep RL algorithms to control virtual characters to accomplish a variety of tasks, and conducts several comparative experiments to validate their effectiveness.

  First, the authors show that their approach can easily handle dynamic and complex motion sequences in large unordered datasets and achieve natural high-fidelity action synthesis by mimicking the behaviors in these datasets. They evaluate the performance of AMP on different tasks and compare it with a low-level controller-based model. The results show that the AMP is better able to solve some specific tasks, such as crossing obstacles.

  In addition, the authors performed single-clip imitation experiments, demonstrating that AMP can generate high-quality actions without manually designing a reward function. Finally, the authors also conducted some ablation experiments to explore the effects of different components on training stability and final results.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/ae90155d-51da-4ce9-95c0-792c63ea93b5)

  Overall, the experimental results in this paper show that the authors' approach is able to learn natural and high-fidelity actions in large-scale unordered datasets without manually designing reward functions. This approach provides a new solution for the field of virtual character control.
  
## Conclusion

### 1. Advantages of the Thesis
  1. This thesis presents an adversarial learning-based character animation system for physical simulation that is capable of controlling the behavior of a character through a large amount of unstructured motion data.

  2. The system uses a learned motion prior to automatically combine different skills to accomplish a task and does not require manually designing trajectories or planning actions.

  3. Experimental results show that the system produces high-quality character movements and can mimic multiple behaviors without pattern collapse.
     
### 2. Innovative points
  1. This thesis proposes a novel approach that uses generators and discriminators from adversarial learning to train a motion prior for controlling character's actions in a physical simulation.

  2. The motion prior is an adversarial classifier whose goal is to distinguish the difference between actions generated by a real action dataset and those generated by a character.

  3. During training, the motion prior is used to guide the character's actions so that they are closer to the real action dataset.

  4. In addition, the paper presents some important design decisions, such as the use of multiple action segments as inputs and the use of a reward function in conjunction with the motion prior, which help to improve the performance of the system.

### 3. Future Works
  1. The motion prior proposed in this thesis can be applied to other fields, such as robot control and virtual reality interaction.

  2. Further research could be done to better handle different types of motion data, such as motion capture data and real-time motion capture data.

  3. It could also be explored how to combine motion prior with other techniques, such as reinforcement learning and deep learning, for more complex and advanced tasks.

