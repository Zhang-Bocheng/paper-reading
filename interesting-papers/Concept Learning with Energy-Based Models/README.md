# Concept Learning with Energy-Based Models
[paper link](https://arxiv.org/pdf/1811.02486.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2018 |  This paper describes a new concept learning framework that describes events in the environment by defining an energy function and an attention mask, and uses an inferential time optimization procedure to generate entities that involve similar concepts or identify participating concepts.   |  Reinforcement Learning          |

## Methodology

### 1. Abstract
  The authors successfully learn visual, quantitative, relational and temporal concepts in an unsupervised context and can reuse the learned concepts in different environments. The method has a wide range of applications, especially in the field of AI for tasks that require understanding and reasoning about complex scenarios.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/d133cbd2-91e7-465c-bc91-3521005a1a9e)

### 2. Method Description 
  This thesis presents an energy model-based concept learning method for learning concepts from events. The method uses an energy function to represent concepts and learns concepts by optimizing the parameters of the energy function. Specifically, the method first defines a trajectory energy function to describe a sequence of states in an event. Then, it introduces an attention mechanism that allows concepts to focus on specific entities or relationships in an event. Finally, the method uses the energy function to generate and recognize concepts, and uses a maximum entropy inverse reinforcement learning method to learn concept codes during training.
  
### 3. Key concepts
  _Markov Chain Monte Carlo (MCMC)_ : A class of algorithms used to sample from probability distributions that are difficult to sample from directly. These algorithms generate a Markov chain whose equilibrium distribution is the target distribution. Over time, the states visited by the chain will represent samples from the target distribution.
  
### 4. Methodological improvements
  Unlike traditional visual concept learning methods, the method is able to handle temporal and relational concepts. In addition, the method introduces an attention mechanism that allows concepts to focus on specific entities or relationships in an event. This makes the method more flexible and adaptable.
  
### 5. Issues addressed 
  The main objective of the method is to learn concepts from events in order to better understand complex real-world scenarios. By using an energy model and an attention mechanism, the method is able to effectively capture key information from events and extract meaningful concepts from them. Therefore, the method can be applied to various fields such as robot control, natural language processing, etc.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/71b38182-b32b-438c-aa20-68aaa42dfaab)

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/85c4cd0a-cc1b-45ad-a136-02145ee64c2d)

## Experiments
  This paper describes five experiments whose main purpose is to explore whether a single model can learn to understand the application of various concepts in multiple contexts, and to validate the reasoning process of iterative optimization and the ability to reuse concepts. 

  **Experimental environment and task design**: In order to address the current problem of not having a dataset or environment for testing concepts in both contexts (generation and recognition) simultaneously, the authors designed a new simulation environment and task. The environment is a two-dimensional scene consisting of multiple entities, each with position, color, and shape attributes. The task is to perform behaviors similar to those events in N new test situations given N demonstration events. 

  **Conceptual understanding**: The authors investigated the effect of shared experience, i.e., training the model to handle generating and recognizing both contexts and then applying it to the other. The results show that even when not explicitly trained for a specific context, the models perform better than networks trained independently, but not as well as networks trained for both contexts.

  **Optimization-based inference**: The authors found that the model's inference process is based on iterative stochastic optimization dynamics, which may involve non-trivial feedback corrections. For the concept of generating different shapes, it can be seen that there are many non-trivial feedback corrections in the multi-step process to achieve proper entity alignment. However, single-step processes must achieve simple shapes in a very precise step. The authors also observe that attention vectors are sometimes determined very early in the optimization trajectory of an attention vector, while in other cases complex feedback corrections are required. 

  **Impact of the LKL objective function**: The authors wanted to understand whether it was necessary to explicitly encourage the reasoning process to produce good samples, and therefore conducted experiments with the LKL objective function. The results show that the gradient-based inference process cannot produce good samples in a small number of steps if the LKL objective function is not used. In contrast, networks using both LML and LKL objective functions were able to generate samples that matched the energy of the examples, as well as distinguish between true examples and random events.

  **Reuse of concepts**: The authors recreated similar concept behaviors in a 3D physical simulation environment and used energy functions learned from the original environment as optimization costs. The results show that although the correspondence between the two environments is defined manually, the learned energy function is still able to remain robust under different dynamics, control algorithms, and action mechanisms.

In summary, this paper demonstrates the ability of a single model to learn to understand and apply a wide range of concepts through five experiments, and validates the reasoning process and concept reuse of iterative optimization.

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a conceptual model based on energy functions that can be used for execution time optimization to enable the simulation of human intelligence capabilities such as knowledge acquisition, abstract reasoning and communication.
  
  2. Unlike traditional generative models or inverse RL methods, the approach in this paper does not require explicit learning of generative/policy functions, but rather defines the energy function through optimization, which allows the energy function to be reused in different domains.
 
  3.  In addition, this paper presents optimization methods for identifying and generating concepts, and shows how these concepts can be used for tasks such as event reenactment, similar event identification, and streamlining event descriptions. This approach has the advantage of being able to process concepts dynamically, rather than just being done in an offline training process.
     
### 2. Innovative points
 The conceptual model proposed in this paper is a new approach that utilizes energy functions as the basic units to build complex conceptual structures through combinatorial and recursive operations. This structure can be combined by simple summation of energy functions, thus realizing the complexity and recursion of concepts. 

  This paper proposes an optimization method based on energy functions, which can be used to identify and generate concepts. The advantage of this method is that it can dynamically adjust the concepts during the execution process, thus better adapting to the changes of the environment. Also, this method can be applied to other domains, such as concept reproduction in the physical world on robotic platforms.

### 3. Future Works
  1. More complex conceptual structures, such as multi-parameter concepts and recursive concepts, can be explored to further improve the expressiveness and adaptability of the models.

  2. Investigate how to combine conceptual models with other technologies, such as DL and RL, to achieve more intelligent behaviors and decisions.

  3. Consider how to apply the conceptual model to real-world scenarios, such as autonomous driving and smart home, in order to realize real AI applications.


