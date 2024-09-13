# Compositional Foundation Models for Hierarchical Planning
[paper link](https://arxiv.org/pdf/2309.08587) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a foundation model called Hierarchical Planning Foundation (HiP), which is designed to address the problem of making decisions in new environments over long time domains.          |  Large Language Model (LLMs)        |

## Methodology

### 1. Abstract
The model utilizes multiple expert base models trained separately on linguistic, visual, and action data, and combines them to solve long-term tasks. Effective reasoning and execution is achieved by using a large-scale language model to construct symbolic plans and relate them to the environment, followed by an inverse dynamics model that maps the video plans to visuo-motor control. To ensure coherence between models, the researchers used an iterative refinement method. Finally, the effectiveness and adaptability of the approach is demonstrated on three different long-time domain desktop manipulation tasks.

![image](https://github.com/user-attachments/assets/958fd3e7-b66b-49be-8a07-432ed73b2483)

### 2. Method Description 
This paper proposes a base model called HiP (Hierarchical Planning) for generating action trajectories for long time-series tasks. The model decomposes the problem into three levels of task planning, visual planning and action planning and uses a pre-trained large language model as a task planner to decompose the goals. In addition, a video diffusion model is used for visual planning and an inverse dynamics model is used for action planning.

![image](https://github.com/user-attachments/assets/41a52348-0a89-48c6-add7-b4be195261b4)

### 3. Methodological improvements
To address the problem of inconsistent samples due to direct sampling of subgoals, this paper employs an iterative correction approach to ensure that the sampled subgoals maximize the joint distribution. Specifically, appropriate sub-targets are selected by using a multi-classifier to estimate the density ratio. In visual planning, in order to avoid the problem of inconsistent samples caused by directly sampling observation trajectories, this paper also adopts an iterative correction approach to ensure that the sampled observation trajectories can maximize the joint distribution. Specifically, the correction is performed by using a binary classifier to estimate whether a trajectory is feasible or not.

### 4. Issues addressed 
The HiP base model proposed in this paper can effectively solve the action planning problem for long time-series tasks, enabling robots to autonomously accomplish various tasks in complex environments. Meanwhile, the model can also be applied to other fields, such as autonomous driving.

## Experiments
This paper focuses on HiP, a long-term task planning model based on visual planning and inverse dynamics, and verifies its performance through several comparison experiments. Specifically, this paper conducts the following four comparison experiments:

**Comparison experiment based on task planning**: this experiment compares HiP with two existing strategies, i.e., a linguistic target-based task planning strategy and a video diffusion model. The results show that HiP significantly outperforms these two benchmark strategies in all three environments.

**Comparison experiment based on visual planning**: this experiment compares HiP with a video diffusion model to test its ability in solving unseen tasks. The results show that a pre-trained video diffusion model improves the performance of HiP.

![image](https://github.com/user-attachments/assets/803b1505-4760-46f3-94f4-06a68e01f5c9)

**Inverse Dynamics-based Comparison Experiment**: this experiment compares HiP with several different inverse dynamics models, including a model initialized using VC-1 and other randomly initialized models. The results show that the model using VC-1 initialization can achieve better performance on less data.

**Comparative experiment based on sub-target prediction**: this experiment compares HiP with a strategy using a visual classifier to test its effect on sub-target selection. The results show that improved visual planning in HiP can improve performance.

![image](https://github.com/user-attachments/assets/55d08410-6e91-437e-abab-3482cbe686bd)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a Composable Foundation Models for Hierarchical Planning (HiP) trained on different modal data for solving long-term decision-making problems. Compared to previous approaches that require the collection of large amounts of paired visual, linguistic, and action data, HiP is able to construct a foundation model with multiple hierarchical structures with less data and can use less data when solving new tasks or adapting to new environments.
  
  2. In addition, HiP employs an iterative optimization mechanism to ensure coherence between the different models, resulting in plans that are responsive to the goal and can be executed given the current state and robot capabilities. The methodology has been demonstrated in three long-distance tabletop operating environments with significant results.

### 2. Innovative points
  1. This approach not only reduces the amount of data required to construct the base model, but also allows reasoning at different levels by leveraging the expertise of different models and enables joint decision making without the need to collect costly decision data across modalities.
  
  2. In addition, HiP introduces an iterative optimization mechanism to ensure consistency and coordination between different models, resulting in a more reliable and practical final plan.

### 3. Future Works
HiP uses an approximate sampling method, so it would also be an interesting future research direction to develop more accurate and efficient ways to ensure that consistent samples are obtained from the joint distribution. In conclusion, this paper provides a promising research direction towards more efficient and pervasive decision-making systems by combining multiple powerful pre-trained models.   
