# Learning to Learn Faster from Human Feedback with Language Model Predictive Control
[paper link](https://arxiv.org/pdf/2402.11450) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new approach called Language Model Predictive Control (LMPC) for improving the teachability of large language models (LLMs).           | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
LLMs are capable of quickly adapting to new tasks by learning from human feedback and have a wide range of applications in robot control. However, these capabilities are limited by short-term interactions, as user feedback can only remain valid for a limited period of time. To address this problem, researchers proposed the LMPC framework by fine-tuning PaLM 2 to remember previous interactions and improve its teachability. Experimental results show that using LMPC significantly improves the teaching success and robot responsiveness for non-expert users, while reducing the number of corrections needed. In addition, the approach yields a powerful meta-learner that accelerates the learning of tasks on new robot instances and APIs.

### 2. Method Description 
Fast adaptation refers to enabling the robot to learn new tasks faster based on user feedback by creating a link between natural language input and the robot's reward code. The approach uses PromptBook-formatted prompts to translate user intent into meaningful reward functions, which are used for low-level motion control to respond to user feedback in real-time. In addition, a sequential reward function based on conditional functions is introduced, which enables conversion between multiple reward functions.

Slow adaptation, on the other hand, refers to further optimising the performance of the LLM through supervised training on already completed task data. Specifically, the authors propose a technique called Language Model Predictive Control (LMPC), which uses the history of multiple rounds of dialogues as a training sample, and finds the optimal action paths by predicting the contents of future dialogues and searching for them through the model. Meanwhile, in order to further improve the performance of LLM, the authors also introduce the concept of ‘top users’, which is specially treated in the training and inference process, so that it can better adapt to the needs of users of different levels.

### 3. Methodological improvements
The fast adaptation and slow adaptation methods proposed in this paper are optimised for different problems. For fast adaptation, by using technical means such as PromptBook format prompts and conditional functions, the robot is able to understand the user's intention more quickly and accurately and make corresponding actions. For slow adaptation, LMPC technology and ‘top-user’ processing are used to enable the LLM to continuously improve its performance as it learns.

### 4. Issues addressed 
  1. How to adapt the robot to new tasks faster? Traditional LLMs require a large amount of training data to achieve a high level of performance, which is not suitable for some new tasks. Therefore, this paper proposes a fast adaptation method that can make the robot learn new tasks in a short time.
  2. How to further improve the performance of LLM? Although traditional LLMs can improve their performance with a large amount of training data, their effectiveness is affected by many factors, such as data quality and model structure. Therefore, this paper proposes a slow adaptation approach, i.e., supervised training to further optimise the performance of LLMs.

## Experiments
This paper presents the process and results of an experimental study of an online interactive learning method where humans use natural language feedback to teach robots to learn. The authors conducted the following comparison experiments:

**Comparing the performance of different models:** the authors compare the performance of the baseline model PaLM2-S with two LMPC-based finetuning methods (LMPC-Rollouts and LMPC-Skip) and a Retrieval-Augmented Generation (RAG)-based method in terms of the task success rate, the average number of chatting rounds, and positive response evaluation rate, and conclude that LMPC-Rollouts and LMPC-Skip show better teachability on the test task compared to the baseline model, and that LMPC-Rollouts is better suited to improve information from user feedback.

**Comparing the impact of different training data:** the authors explored the effect of training with only specific user data or all user data by restricting the training data to user-specific feedback and found that training with only specific user data did not achieve better results, while training with all user data better simulated a high-quality model.
![image](https://github.com/user-attachments/assets/41629218-9aa6-475d-bddb-b7c84ad2b9fd)
  
## Conclusion

### 1. Advantages of the Thesis
  1. The authors use a Language Model Predictive Control (LMPC)-based approach to train LLMs to be able to predict the dynamics of human-robot interactions and to have good generalisation performance. Experimental results show that the method can significantly improve the success rate of non-expert users in teaching new tasks to robots and reduce the number of human corrections required.
  
  2. In addition, this paper proposes an approach that combines multiple data collection and fine-tuning cycles to further improve the performance of the model. Although this approach has some limitations, it provides valuable ideas for future related research.

### 2. Innovative points
  1. The main contribution of this paper is to propose a new approach to improve robot teachability using Language Model Predictive Control (LMPC). Specifically, the authors first train a robot code writer based on Large Language Models (LLMs), which is then used to predict the interaction dynamics between humans and robots. 
  
  2. The authors use classical robotics techniques (e.g., model predictive control) to discover shorter paths to success. Finally, when reasoning, the authors use a recursive temporal control strategy in order to better search for optimal action sequences. This approach not only solves the problems in the traditional methods, but also significantly improves the teachability of the robot.
 
### 3. Future Works
Future research could explore more efficient and effective algorithms and techniques to meet practical needs. In addition, the authors also mentioned the possibility of incorporating multimodal information (e.g., video/audio inputs) into the feedback mechanism, which can also be one of the future research directions. In conclusion, the methods proposed in this paper to improve the teachability of robots provide some useful ideas and insights for research in related fields.    
