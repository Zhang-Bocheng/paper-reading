# Meta-Learning through Hebbian Plasticity in Random Networks
[paper link](https://arxiv.org/pdf/2007.02686) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper describes a new search method that implements meta-learning through the use of Hebbian learning rules.         |   Meta-learning        |

## Methodology

### 1. Abstract
This approach enables the network to self-organize its weights over its lifetime and does not require direct optimization of the neural network's (NNs) weight parameters. The authors conducted experiments in a dynamic 2D pixel environment and on a simulated 3D quadrupedal robot, and the results show the effectiveness of this new approach. This work provides the field of machine learning with a new idea to better model the learning and adaptation capabilities of biological brains.

![image](https://github.com/user-attachments/assets/927fddad-4a43-4fa9-b2cb-e696dfba47a1)

### 2. Method Description 
This paper proposes a meta-learning method based on Evolutionary Strategy (ES) to optimize the performance of NNs by evolving network connection rules. Specifically, the method uses a local learning rule model based on a biological Hebbian mechanism that controls the synaptic strength between artificial neurons and updates the weights according to the cumulative reward at each time step. Then, an evolutionary strategy is used to find learning rule parameters with higher cumulative rewards in order to progressively discover more efficient learning rules for an arbitrarily initialized network.

![image](https://github.com/user-attachments/assets/39d9310e-7928-4a34-b573-83673b50c611)

### 3. Key concepts
_Meta-learning_ : A subfield of machine learning focused on developing algorithms and models that have the ability to improve their learning processes based on experience. Essentially, meta-learning aims to create systems that can adapt quickly to new tasks or environments with minimal data.

### 4. Methodological improvements
  1. In contrast to previous work, the method is not only not limited to uniform plasticity or optimizing only connection-specific plasticity values, but also allows each connection to have a different learning rule and learning rate.

  2. In addition, the method uses an evolutionary strategy algorithm to optimize the Hebbian coefficients instead of directly optimizing the weights, thus avoiding the need for gradient backpropagation.

### 5. Issues addressed 
The method aims to address the meta-learning problem in deep RL, i.e., how to quickly discover efficient learning rules in order to bootstrap a randomly initialized network to a high-performance state. By using an evolutionary strategy to dynamically adjust the Hebbian coefficients, the method can efficiently find local learning rules adapted to different tasks and achieve fast convergence without any environmental feedback.

## Experiments
This paper presents the authors' experiments in two continuously controlled environments, **a visual control task and a 3D motion task**. In each task, the authors used two different network structures, **a traditional static weighting network and a dynamic weighting network based on Hebbian learning rules**. In each task, the authors performed three independent evolutionary runs and compared the performance of the static and dynamic weighting networks.

For the visual control task, the authors used a racing game environment built from the Box2D physics engine and adapted its output state to a 3x84x84 pixel observation space with RGB channels. The static weighting network used by the authors is an ANN with three convolutional and three fully connected layers, while the dynamic weighting network performs Hebbian learning of the weights in the fully connected layers only. 

The authors used average returns as an evaluation metric and compared the dynamic weighting network to state-of-the-art deep RL methods. The results show that the dynamic weighting network performs slightly lower than the state-of-the-art methods, but much better than other image recognition based methods.

![image](https://github.com/user-attachments/assets/9f2785b6-76e1-48d7-a4e7-ddbbc5b5113c)

For the 3D motion task, the authors used a quadruped robot model built by the pyBullet physics engine and set its input size to 28 position and velocity information and 8 joint movements. The static weighting network used by the authors is an ANN with three fully connected layers, while the dynamic weighting network performs Hebbian learning for all weights. 

The authors used distance from walking as an evaluation metric and compared the dynamic weighting network to a traditional fixed weighting network. The results show that the dynamic weighting network can adaptively adjust its weights to address unseen damage patterns, while the fixed weighting network cannot do so.  

![image](https://github.com/user-attachments/assets/2b541313-7b0e-4bdf-ac1a-1827a82864a6)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new approach that enables agents with randomized weights to adapt quickly to tasks.
  
  2. It shows that by using self-organizing Hebbian learning rules, fast weight adjustment can be achieved, which is useful for tasks that require continuous learning.
  
  3. The researchers demonstrated the effectiveness of this approach in two complex RL tasks and proved it to be more efficient than fixed-weight networks.
  
  4. This research provides an interesting direction for the intersection between neuroscience and ML as it explores how organisms can utilize genetic learning rules to quickly adapt to their environment.

### 2. Innovative points
  1. The paper proposes a novel approach that allows randomly initialized neural networks to quickly adapt to tasks by self-organizing Hebbian learning rules.
  
  2. Unlike traditional static networks, this Hebbian learning rule-based network can self-organize and converge to high-performing weights in an attractive subspace over its lifetime.
  
  3. The researchers also explored the possibility of introducing neuromodulation into the method to further improve performance.

 ![image](https://github.com/user-attachments/assets/39d04aa2-5efd-4d70-8455-57b946a2cbe4)

### 3. Future Works
  1. Consideration could be given to combining neuromodulation mechanisms with Hebbian learning rules to further improve performance.
  
  2. Attempts could also be made to optimize the structure of the NN itself to better adapt to different tasks and environments.
  
  3. In addition, one can explore how these findings can be applied to other areas such as CV and NLP.
