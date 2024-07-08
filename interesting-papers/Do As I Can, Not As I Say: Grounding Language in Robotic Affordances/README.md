# Do As I Can, Not As I Say: Grounding Language in Robotic Affordances
[paper link](https://arxiv.org/pdf/2204.01691) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper proposes an approach called SayCan, which aims to provide robots with real-world context-awareness by combining the value function of pre-trained skills with a large-scale language model.         | LLMs          |

## Methodology

### 1. Abstract
  This approach can help robots execute complex, long-term natural language commands and realize tasks in specific environments. The authors conducted tests in several real-world scenarios to demonstrate the effectiveness of this approach. This research has important implications for the application of natural language commands to robot control.
  
  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/9b750be4-1af0-4a4e-a172-7a19986cafac)

### 2. Method Description 
  The algorithm proposed in this paper is called SayCan, which selects which skill to perform by combining probability distributions. The algorithm accepts as input a high-level instruction, an initial state, and a set of skills and their linguistic descriptions, and based on this information selects the skill that will successfully perform the task and is most likely to be used. 
  
  Specifically, SayCan first uses a pre-trained language model to generate text embedding vectors for each skill, and then passes these vectors as input to the policy and value functions. During execution, SayCan continuously updates the state and repeats the process until a termination condition is reached.
  
  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/4dcf0bf0-7a88-43ac-82fd-d589a929ef70)
 
### 3. Methodological improvements
  The main advantage of SayCan over traditional robot control methods is its ability to utilize different language models to accommodate planning problems at different levels of abstraction. In addition, SayCan employs both BC and RL training methods to learn policies and value functions under linguistic conditions to improve the performance of the algorithm.
  
### 4. Issues addressed 
  SayCan aims to address the challenges faced by robots when performing complex tasks in complex environments. By combining probability distributions and language models, SayCan is able to make informed choices between multiple skills for efficient task completion. In addition, SayCan can adaptively adjust its policy and value function according to different abstraction levels, further improving the performance of the algorithm.
  
## Experiments
  This paper presents the experimental content and results of the SayCan algorithm. The experiment is divided into two main parts: the experimental setup and the experimental results. In the experimental setup, the authors used a mobile robotic arm and a set of object manipulation and navigation skills in an office kitchen environment. The authors used 15 common office items and 5 semantically meaningful locations and tested 101 commands including different aspects such as time span, linguistic complexity, and entity variations. In the experimental results, the authors compare the performance of the SayCan algorithm with other methods and analyze the strengths and weaknesses of the algorithm.

First, the authors compare the SayCan algorithm with other language model-based approaches. They used three different language models (including PaLM, GPT-3, and FLAN) to train the SayCan algorithm and compared their performance. The results show that using PaLM as the language model can significantly improve the success rate of the algorithm, while the other two language models are less effective. This suggests that choosing the right language model is crucial for the performance of the algorithm.

Second, the authors compared the SayCan algorithm with other behavioral model-based approaches. They used three different behavioral models (including BC NL, BC USE, and No VF) to train the SayCan algorithm and compared their performance. The results show that the method using the value function (No VF) performs the worst, while the methods using BC NL and BC USE have similar performance. This shows that the value function is also important for the performance of the algorithms.

Finally, the authors also compare the SayCan algorithm with other NLP based methods. They used two different NLP techniques (including Chained Thought Reasoning and Multilingual Support) to improve the SayCan algorithm and compared their performance. The results show that the use of Chained Thought Reasoning significantly improves the algorithm's capabilities, while multilingual support allows the algorithm to be more flexible and adaptable to different linguistic environments.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/a3d06d4a-b01d-44b2-8632-06466c653a36)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes an approach called SayCan that is able to utilize large language models for tasks with physical properties and train value functions through RL to provide feasibility and viability probabilities for each skill.
  
  2. The method solves the problem of natural language understanding in the physical world, allowing robots to perform tasks based on human-provided instructions.
  
  3. Experimental results show that using the SayCan method can lead to a nearly twofold increase in robot performance compared to a non-grounded baseline.
     
### 2. Innovative points
  1. The SayCan method applies knowledge from large-scale language models to real physical tasks, enabling the translation of natural language understanding to physical behavior.
  
  2. The method improves the robot's decision-making ability by training the value function through reinforcement learning, which provides feasibility and viability probabilities for each skill.
  
  3. The SayCan method also takes into account the interactions between different skills, enabling the robot to select the most appropriate skill based on the scenario.
     
### 3. Future Works
  1. Further research could be conducted on how to optimize the training process of the value function so that it more accurately predicts the success rate of each skill.
  
  2. It could be explored how to integrate knowledge from other sources into the SayCan method, such as knowledge based on visual perception or knowledge based on prior knowledge.
  
  3. It could be investigated how to extend the SayCan method to more complex tasks and environments, such as multi-robot collaboration or complex urban environments.
