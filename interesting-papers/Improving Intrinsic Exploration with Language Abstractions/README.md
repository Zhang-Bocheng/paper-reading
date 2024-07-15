# Improving Intrinsic Exploration with Language Abstractions
[paper link](https://arxiv.org/pdf/2202.08938) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper explores how linguistic abstraction can be used to improve the intrinsic exploration of reinforcement learning (RL) agents.         |  Reinforcement Learning         |

## Methodology

### 1. Abstract
   RL agents are difficult to train when rewards are sparse, so intrinsic rewards are often used to encourage agents to explore the environment. However, recent approaches to intrinsic exploration often use state-based novelty measures, which may reward low-level exploration and may not scale to domains requiring more abstract skills. The authors address this problem by using language as a general medium to highlight relevant abstract concepts in the environment. These language-based variants improved performance by 47% to 85% over nonverbal forms on 13 challenging tasks from the MiniGrid and MiniHack suites of environments.

   ![image](https://github.com/user-attachments/assets/ed5bba94-8f34-46cf-95b0-de9ca2affd38)

### 2. Method Description 
  This paper presents a method for jointly training students and teachers, called L-AMIGo, for exploring state spaces in RL. The method extends AMIGo with a given target language and uses a collection of possible language targets to select the teacher's target. Specifically, the student is a task-conditional strategy based on the given target language, while the teacher is an adversarial strategy that selects appropriate goals for the student's initial state. And, the L-NovelD approach was introduced to combine linguistic goals with the NovelD approach to further enhance students' exploratory skills.

  ![image](https://github.com/user-attachments/assets/849a260e-47fc-4349-b299-4f491eb3be9f)

### 3. Methodological improvements
  1. In contrast to the traditional AMIGo approach, L-AMIGo extends its exploratory capabilities through the use of a target language.
  
  2. This approach allows students to better understand the goals in their environment and develop better strategies based on those goals.
  
  3. Meanwhile, the L-NovelD approach can more effectively guide students to explore unknown state spaces by combining linguistic goals with the NovelD approach.
     
### 4. Issues addressed 
  L-AMIGO and L-NovelD methods address the problem of exploration in RL, especially in complex environments. These methods, by using target languages and NovelD techniques, can help students better understand the goals in their environment and encourage them to explore unknown state spaces. This helps to improve the performance of RL algorithms and speeds up learning.
  
## Experiments
  This paper focuses on the results of experiments in two challenging environments (MiniGrid and MiniHack) using RL algorithms that use language as an exploration goal. Four methods, L-AMIGo, AMIGo, L-NovelD and NovelD, are compared in the experiments and against a benchmark with fixed message rewards. The experimental results show that methods using language as an exploration target outperform non-language exploration methods, especially in larger environments.

Specifically, the experiment is divided into the following two parts:

**Comparison Experiments**: this paper first describes experiments in the MiniGrid environment, in which the syntax provided by the BabyAI platform is used to generate task and action instructions. The experiments compare the methods L-AMIGo, AMIGo, L-NovelD and NovelD with a benchmark of fixed message reward. The experimental results show that methods that use language as an exploration goal outperform non-language exploration methods, especially in larger environments. For example, in the KeyCorridorS5R3 task, L-AMIGo and L-NovelD improved by 0.27 and 0.35 absolute scores relative to their non-language versions, and by 47% and 85% relative. 

**Semantic Influence Experiment**: in order to explore whether the semantics of the language affects the exploration effect, this paper also conducts an experiment in the MiniGrid environment by hiding the semantics of the language annotations and replacing each message with a unique identifier. The results of the experiment show that using a unique identifier instead of semantics does not significantly reduce performance, but L-AMIGo is still able to utilize semantic information to improve performance.

![image](https://github.com/user-attachments/assets/7cda5026-e32d-4320-bcef-b88faed362da)

## Conclusion

### 1. Advantages of the Thesis
 1. This paper proposes a language-based exploration methodology that improves the efficiency of exploration by using language as an exploration target.
 
 2. The method is evaluated in MiniGrid and MiniHack environments and its effectiveness is demonstrated.
 
 3. The authors also discuss the limitations of the method and future research directions.

### 2. Innovative points
  1. The exploration methodology proposed in this paper uses a linguistic abstraction space instead of the traditional state representation, which improves the exploration efficiency.

  2. The method is evaluated on two environments and its effectiveness is demonstrated relative to non-linguistic exploration methods.
  
  3. The authors also present some ideas for extending the method, such as using pre-trained models to improve the understanding of linguistic semantics.
     
### 3. Future Works
  1. Future research could further explore how to better utilize linguistic information for exploration.
  
  2. There is also a need to investigate how to cope with the problem of exploration in the presence of linguistic noise and poor quality.
  
  3. Finally, consideration needs to be given to how this exploration approach can be applied to a wider range of domains, such as NLP and CV.
