# Self-driven Grounding: Large Language Model Agents with Automatical Language-aligned Skill Learning
[paper link](https://arxiv.org/pdf/2309.01352) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes the power of Large Language Models (LLMs) for automated reasoning and planning, and proposes a Self-Driven Grounding (SDG) framework to address the application of LLMs in real-world environments.          | LLMs         |

## Methodology

### 1. Abstract
The SDG framework addresses the problem of LLMs in real-world environments by using LLMs to formulate subgoal hypotheses and validate their feasibility, and then learning generalized skills by utilizing the successfully grounded subgoals to learn generic skills that can be further used to accomplish more complex tasks. Experimental results show that SDG achieves comparable performance to imitation learning methods in the well-known instruction-following task set-BabyAI, proving the effectiveness of the learned skills and demonstrating the feasibility and efficiency of the framework.

![image](https://github.com/user-attachments/assets/58451056-a33e-4133-b9f4-6f42c3ea0dc9)

### 2. Method Description 
The paper proposes a framework called Self-Driven Grounding (SDG) for automatically learning generic low-level behavioral APIs to solve tasks based on natural language instructions. SDG is divided into four phases: **hypothesis, validation, induction, and deduction**. In the hypothesis phase, the model decomposes the task into multiple sub-goals and generates the corresponding checking functions. In the validation phase, each sub-goal is verified to be feasible by interacting with the environment, and successes are collected. In the generalization phase, a clustering algorithm is used to group similar sub-objectives and train generic skills. Finally, in the deduction phase, the learned skills are utilized as part of a high-level planner to generate programs to solve unseen complex tasks.

![image](https://github.com/user-attachments/assets/6c7ed823-667c-454f-8d3b-71c648d52dd0)

### 3. Methodological improvements
The methodology focuses on improving two challenges in the traditional approach: how to gain successful ground experience and how to efficiently train generic low-level behavioral APIs. SDG addresses the first challenge with a fast try-and-feedback mechanism, while the introduction of density rewards and an initial state restoration mechanism improves the efficiency of the second challenge.

### 4. Issues addressed 
The main objective of SDG is to help LLMs learn generic low-level behavioral APIs autonomously, thereby reducing the need for human intervention. This helps to improve the generalization ability of the model, allowing it to solve more unknown or complex tasks. In addition, SDG provides a scalable solution that can be adapted to different task types by adding more subgoals and skills.

## Experiments
This paper focuses on the experimental results and effect analysis of SDG (Self-Driven Goal) framework in BabyAI environment. The experiment mainly includes the following aspects:

  1. **Experimental setup**: the BabyAI environment was used for testing and compared with multiple baselines;
  
  2. **Comparison of overall results**: 100 randomly selected instructions were validated for each task level, and the experiment was repeated three times to take the average value, which showed that SDG was able to accomplish the task by learning skills automatically, proving the effectiveness of the framework;
  
  3. **Ablation results**: including the efficiency of skill learning, the number of interaction debugging, and the effect of multiple attempts of the skill;
  
  4. **Method details**: key intermediate results such as task validation and skill clustering are shown.

 ![image](https://github.com/user-attachments/assets/61053576-d207-4ede-85ef-10f07234b592)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a framework called SDG to address the challenge of automating the application of LLMs to a specific context. The framework alleviates the problem of gaining experience by having LLMs not only decompose tasks but also generate intrinsic rewards to help reinforcement learning (RL) agents verify the decomposition results.
  
  2. In addition, the authors propose a generalized skill learning approach based on semantic similarity to enhance the generality of skills. Compared to imitation learning methods that require millions of demonstrations, SDG achieves comparable performance on the most difficult tasks in BabyAI. Experimental results demonstrate the effectiveness and feasibility of the learned skills and demonstrate the flexibility and efficiency of the framework.

### 2. Innovative points
The methodological innovation of this paper is to propose an autonomous grounding framework that maps the semantic planning of LLM to practical implementations. Specifically, the SDG consists of three key phases: **hypothesis, verification and generalization**. 

<br>&emsp;In the hypothesis phase, the LLM not only acts as a planner to decompose the task into sub-goals, but also provides checking functions so that RL agents can assess whether they can accomplish these sub-goals. This intrinsic reward from the LLM significantly mitigates the sparse reward problem. 
<br>&emsp;In the validation phase, using the sub-goals and their corresponding checking functions, the RL agents learn the strategies for the sub-goals based on intrinsic rewards and are ultimately validated by whether the task is completed or not. 
<br>&emsp;In the generalization phase, the RL agent clusters the verified subgoals by semantic similarity and learns generic skill policies based on them. Utilizing these generic skills, LLMs can generate solutions and even solve unseen or more complex problems with minimal and efficient interactions.

### 3. Future Works
1. SDG can currently only handle tasks with textual descriptions because of its simpler way of perceiving the state of the environment. The introduction of multimodal LLMs can extend the range of SDG applications.
2. SDG contains only a single loop of hypothesis, verification and generalization process.

Designing multiple loop mechanisms is an interesting and promising direction for SDGs, which will allow SDGs to learn more powerful and diverse hierarchical skills for more flexible tasks. 
