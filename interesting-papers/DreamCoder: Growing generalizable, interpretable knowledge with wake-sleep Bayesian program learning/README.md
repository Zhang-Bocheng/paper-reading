# DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning
[paper link](https://arxiv.org/pdf/2006.08381) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a machine learning system called DreamCoder that learns and masters a variety of tasks and domain knowledge as efficiently as a child.         | Neural Networks         |

## Methodology

### 1. Abstract
  While traditional programming requires human experts to write code manually, DreamCoder automatically discovers reusable, interpretable knowledge and applies it to new tasks by self-learning and optimizing the programming language. This approach not only improves efficiency, but also enables machines to better understand and solve complex problems. Experimental results show that DreamCoder has been successfully applied in a number of areas, including classical program synthesis challenges, creative visual drawing and architectural problems, and the learning of basic programming languages.
  
### 2. Method Description 
  The paper presents a program learning system called DreamCoder, whose main purpose is to write programs automatically through learning. DreamCoder uses an iterative process with three phases: **wake, sleep and dream**. During the wake phase, the system attempts to solve the task and selects the program most likely to solve the problem based on a neural recognition model. During the sleep phase, the system continuously optimizes its programming library and neural network. The dream phase is then used to train the neural network to better guide the program search.

Specifically, during the wake phase, the system selects a number of tasks from a small randomized training set, then searches for all possible solutions and calculates the probability of each one. These probabilities are given by a neural recognition model that generates probability distributions based on observed data as well as programs in the program library. The system selects the top k programs with the highest probability as candidate solutions and compares them with the true solution. If a program is selected as a candidate solution, it is added to the neural network to improve its accuracy.

During the sleep phase, the system performs two different operations: abstraction and dreaming. In the abstraction phase, the system discovers new programming patterns by refactoring existing programs to increase the size and depth of the program library. In the dreaming phase, the system trains the neural network so that it can predict solutions more accurately. The goal of this phase is to improve the accuracy of the neural network through constant iterative training.

### 3. Methodological improvements
  The DreamCoder method proposed in this paper has several improvements over traditional program learning methods:

  1. A more complex neural network structure is used, which can handle more input data.
  
  2. Probabilistic calculations are introduced in the wake-up phase, allowing the system to choose the optimal solution.
  
  3. In the sleep phase, the system increases the size and depth of the program library by reconstructing existing programs to discover new programming patterns.
  
  4. In the dream phase, the system further improves its performance by training the neural network to improve its accuracy.

### 4. Issues addressed 
  The DreamCoder method proposed in this thesis solves some of the problems of traditional program learning methods:

  1. Rule-based program learning methods require writing a large number of rules manually, whereas DreamCoder can write programs automatically through learning.
 
  2. Classical program learning methods can only solve specific types of tasks, whereas DreamCoder can be applied to many different types of tasks.
  
  3. Classical program learning methods usually require a lot of manual intervention, whereas DreamCoder can adaptively learn without human intervention.

 ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/7704285d-1d54-418c-a0c4-54ab9b82d8e6)

## Experiments
  This article presents the results of experiments with the DreamCoder model, which is able to generate more complex programs from a simple library of basic functions through learning, and excels in several domains. The article conducts a total of four comparison experiments:

The first experiment was for list processing and text editing tasks, where the DreamCoder model was trained to automatically build problem-solving programs given input and output examples. The results of the experiments show that the DreamCoder model was able to improve its performance by automatically generating about 20 new function libraries while solving 218 problems.

The second experiment was conducted on the tasks of generating images, plans, and text, which require the DreamCoder model to be visually perceptive. The results of the experiments show that the DreamCoder model is able to draw complex images by learning basic shapes such as logo graphics, and is able to plan and execute a series of operations to accomplish a specific task.

The third experiment was conducted on the task of generating probabilistic concepts, which requires the DreamCoder model to have the ability to reason and generalize. The results of the experiments showed that the DreamCoder model was able to infer various probabilistic laws by observing a number of string samples and using these laws to generate new string samples.

The fourth experiment was conducted on the task of learning the laws of physics and mathematical formulas, which requires the DreamCoder model to have the ability to understand and express abstract concepts. The results of the experiments show that the DreamCoder model can learn the basic structure of a set of physics laws and mathematical formulas from them and use these structures to solve related problems.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/35c83dd8-cce7-442a-b182-f33ac37f4749)

Overall, these experiments show that the DreamCoder model performs very well in different domains, proving that it has a strong learning ability and adaptability.

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents DreamCoder, a new program learning system that learns many different programming tasks and excels in several domains.
  
  2. DreamCoder uses a combination of symbolic and NN approaches to knowledge growth and application, which allows it to handle complex tasks and adapt to new environments.
  
  3. The paper also explores how DreamCoder can be extended to a wider range of AI domains, including natural language understanding and causal reasoning
     
### 2. Innovative points
  1. DreamCoder uses a novel knowledge representation that combines implicit skills in problem solving with explicit knowledge to improve the performance of the system.
  
  2. DreamCoder employs a deep RL algorithm to train the model so that it can learn and explore autonomously in unknown environments.

  3. The paper proposes a simulator-based learning method to improve the intelligence of the robot through a simulator, which can get better results in the real world.

### 3. Future Works
  1. The success of DreamCoder provides insights for AI research in other fields, such as NLP and causal reasoning, which can also learn from its approach.
  
  2. Further research can be conducted on how to combine DreamCoder with other AI techniques, such as augmentation learning and transfer learning, to improve its performance and applicability.
  
  3. In practical applications, issues such as security and reliability of DreamCoder need to be considered to ensure its stable operation in complex environments.
     
