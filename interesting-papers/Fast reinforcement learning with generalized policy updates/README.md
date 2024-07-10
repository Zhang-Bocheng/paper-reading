# Fast reinforcement learning with generalized policy updates
[paper link](https://www.pnas.org/doi/epdf/10.1073/pnas.1907370117) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |This paper presents a new approach based on Deep Reinforcement Learning to solve currently intractable problems by decomposing complex decision-making problems into multiple tasks and exploiting the relationships between these tasks, which can significantly reduce the amount of data required.          | Reinforcement Learning          |

## Methodology
 The authors propose the concept of "generalized policy updating", which is based on an extended version of two basic operations (policy evaluation and policy improvement) that allow an agent to leverage the solution of a previous task while solving a task in order to speed up the problem solving process. This approach can mimic human learning to a certain extent and has a wide range of applications.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/d0fe7df5-7895-4032-a8a4-7b61a2909e7a)

## Experiments
  In this paper, a reinforcement learning algorithm based on dynamic planning is introduced, and generalized policy evaluation and improvement methods (GPE and GPI) are proposed. Also, the effectiveness of the method is verified through experiments.

In the experiments, the authors used a simple environment as an example, in which an agent needs to select actions from a 10x10 grid to obtain rewards. The agent can pick up objects by moving to where they are located and different types of objects give different rewards. 

The authors first define some feature functions to characterize the effects of different types of objects on the agent. Then, they construct a set of baseline strategies that are designed for specific tasks. Next, they use GPE and GPI methods to compute the value functions of these strategies and use these value functions to generate new strategies. Finally, they compared the performance of the new strategies with the baseline strategies and demonstrated the effectiveness of the GPE and GPI methods.

Specifically, in their experiments, the authors used two tasks, one that focused only on one type of object and the other that focused only on another type of object. For each task, they used the GPE and GPI methods to compute the new strategy and compared it to the baseline strategy. The experimental results show that the new strategy performs better than the baseline strategy, and is especially effective when dealing with multiple tasks.

![1720603556401](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/b50268c8-89fa-4c0b-bf98-431c30a5ab46)

## Conclusion

### 1. Advantages of the Thesis
  1. The approach enables knowledge sharing and migration between different tasks by decomposing the task into multiple subtasks and using successor characteristics to characterize the state transfer of each subtask.
  
  2. In addition, the article describes some important algorithms and techniques such as Generalized Policy Improvement (GPI) and Generalized Value Estimation (GPE), and how techniques such as linear regression can be used to improve efficiency.
 
### 2. Innovative points
The main contribution of this paper is to propose an approach based on successor characteristics to solve the problem decomposition problem in RL. 

  1. This approach can effectively utilize the existing knowledge and improve the learning efficiency and generalization ability.

  2. And the authors propose some new algorithms and techniques, such as GPI and GPE, and how to use techniques such as linear regression to improve efficiency.

### 3. Future Works
  1. In future research, it is necessary to continue to explore these issues in depth and try to propose more effective and practical solutions.
  
  2. At the same time, it is also necessary to further expand and improve this method to adapt to more complex application scenarios and practical needs.
