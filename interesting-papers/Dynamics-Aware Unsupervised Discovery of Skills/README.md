# Dynamics-Aware Unsupervised Discovery of Skills
[paper link](https://arxiv.org/pdf/1907.01657.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a new reinforcement learning approach, Dynamics-Aware Discovery of Skills (DADS), which combines model-driven and model-free learning with the aim of discovering easy-to-predict behaviors and learning their dynamic patterns.         | Unsupervised Learning          |

## Methodology
  Traditional model-driven RL typically learns a model of the dynamics of the entire environment, but this is difficult to do accurately for complex systems and may not generalize beyond the training distribution. Therefore, DADS proposes an unsupervised learning algorithm that simultaneously discovers predictable behaviors and learns their dynamics in a continuous skill space. Experimental results show that using DADS significantly improves zero-generation schedules, handles sparse reward tasks, and outperforms previous hierarchical reinforcement learning methods.
 
## Experiments
  This paper describes a series of experiments in which the authors validate the effectiveness of their unsupervised skill learning algorithm, DADS. They first performed visual and qualitative analyses to show that diverse skills can be learned using DADS in high-dimensional problems, and that these skills are predictable and stable. Next, they explored continuous space for the skills learned by DADS and compared it to discrete space, showing that continuous space generates more diverse trajectories and is more consistent with semantic meaning. They then compared the variance of DADS and DIAYN learned skills and found that DADS learned skills have lower variance, which makes them more suitable for hierarchical control tasks. Next, they applied DADS to model-based reinforcement learning and compared it to other methods, showing that DADS was able to significantly outperform the other methods in the zero-sample case. Finally, they also compare DADS with goal-based reinforcement learning and demonstrate the advantages of DADS over goal-based methods.

Specifically, in the first part, the authors conduct experiments using agents such as Ant, Half-Cheetah, and Humanoid in the MuJoCo environment, demonstrating that DADS can learn a diverse set of skills, even in high-dimensional state and action spaces. For example, for Ant, DADS can learn stabilized navigation skills, while for Half-Cheetah, a variety of different gait skills can be learned. In addition, the authors show that the skills learned by DADS are predictable and stable because they avoid some unstable actions such as flipping.

In the second part, the authors used a two-dimensional continuous space to learn skills and compared it to a discrete space. The results show that continuous space can generate more diverse trajectories and is more consistent with semantic meaning. For example, the authors use projections in the x-y direction to display trajectories of skills and find that trajectories in continuous space are more diverse and can be interpolated to make smooth transitions.

In part three, the authors compare the variance of skills learned by DADS and DIAYN and find that skills learned by DADS have lower variance. This implies that DADS learned skills are more suitable for hierarchical control tasks. The authors also discuss how DADS learned skills can be optimized to increase their diversity and propose a new technique called x-y prioritization that makes DADS learned skills more stable.

In Part four, the authors apply DADS to model-based RL and compare it with other methods. The results show that DADS can significantly outperform other methods in the zero-sample case. The authors also show that DADS can be used for long-term planning tasks and can solve test-time tasks without any learning.

In Part five, the authors compare DADS with goal-based RL and demonstrate the advantages of DADS over goal-based methods. The authors used two different types of reward functions (dense and sparse) to train an objective-based RL model and used the skills learned by DADS for a long-term planning task. The results show that DADS can achieve better performance over a wider range of initial distances and can better handle situations outside the target distribution.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/817a0746-b587-418f-81af-fbce1f55d536)

## Conclusion

### 1. Advantages of the Thesis
The paper presents a mutual information-based unsupervised learning algorithm for learning low-dimensional skills and applying them to task optimization in model predictive control

 1. The algorithm is scalable and efficient, can handle high-dimensional state spaces, and can learn diverse skills without any reward signaling.

 2. By using skill-conditional strategies and dynamic modeling, the algorithm is able to implement zero-sample planning in downstream tasks.
 
 3. The algorithm is able to better utilize known knowledge to guide exploration than MBRL methods, thus improving learning efficiency.
    
### 2. Innovative points
  1. The innovation of the methodology in this thesis is the use of mutual information as an optimization objective to maximize diversity while ensuring predictability of transition states.
     
  2. The algorithm also employs the idea of model predictive control to support subsequent task planning during the learning phase.
     
### 3. Future Works
  1. Explore how the algorithm can be combined with other reinforcement learning techniques to further improve performance.
  
  2. Investigate how the algorithm can be extended to more complex environments and tasks for real-world applications.
  
  3. Explore how knowledge can be shared across multiple tasks to better adapt to new tasks.
