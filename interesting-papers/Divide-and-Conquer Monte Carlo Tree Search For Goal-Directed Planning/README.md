# Divide-and-Conquer Monte Carlo Tree Search For Goal-Directed Planning
[paper link](https://arxiv.org/pdf/2004.11410.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces an algorithm called "Divide-and-Conquer Monte Carlo Tree Search" for solving goal-directed reinforcement learning in sequential decision problems.         |  Reinforcement Learning         |

## Methodology

### 1. Abstract
  The core idea of the algorithm is to approximate the optimal plan by dividing the initial task into simpler subtasks and solving them recursively. To achieve this goal, the authors propose a machine-learning based subgoal suggestion strategy to find appropriate sub-task division trees based on prior experience. Experimental results show that the algorithm performs better than traditional sequence planning methods in grid-world navigation tasks and challenging continuous control environments.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/481d4c3e-8f10-4be3-b082-687a85ad46af)

### 2. Method Description 
  The DC-MCTS planner proposed in this paper is a method based on a variant of MCTS (Browne et al., 2012) inspired by recent best-first or bootstrap searches. It can be understood as a heuristic, bootstrapped version of the classical Floyd-Warshall algorithm. The algorithm computes all shortest paths by iterating over all subgoals and computing all paths for a given subgoal in an inner loop. 
  
  For planar graphs, small sets of subobjectives, also known as vertex separators, can be constructed which can favorably partition the remaining graph, leading to the linear-time ASAP algorithm. The heuristic subgoal proposer p that leads to DC-MCTS can be roughly understood as a probabilistic vertex separator. In addition, this paper considers neural networks that mimic algorithms for decomposition tasks, similar to the subgoal proposers used.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/2b28cfff-ce4a-4a65-bd0d-c5d705b6fe06)

### 3. Key concepts
  _Monte Carlo Tree Search (MCTS)_: A heuristic search algorithm used for decision-making in various domains, particularly in game playing and planning problems. It combines the precision of tree search with the randomness of Monte Carlo simulations, allowing it to effectively explore large decision spaces and make informed decisions.
  
### 4. Methodological improvements
  Compared with the classical AO* algorithm, the DC-MCTS planning apparatus proposed in this paper has the following improvements:

  1. Uses a learned value function and strategy prior, whereas AO* assumes a fixed search heuristic.
  
  2. Relaxes the cost lower bound requirement and does not have to require complete accuracy.
  
  3. Exploration incentives are introduced to compensate for the violation of the "optimism under uncertainty" principle.

### 5. Issues addressed 
  The DC-MCTS planner proposed in this paper addresses the following question:

  1. How to effectively use heuristic information and strategic priors when decomposing tasks. 
  
  2. How to balance the relationship between exploration and exploitation for better discovery of unknown subgoals.

  3. How to improve planning efficiency without degrading performance.

## Experiments
  This paper presents the authors' experimental study of the DC-MCTS algorithm, including applications in navigation and applications performed in a continuously controlled version. The authors compare DC-MCTS with standard sequential MCTS and evaluate the effectiveness of both approaches by solving a maze problem. Specifically, the authors first tested both approaches in a grid world consisting of new, randomly generated mazes and used wall density as a measure of task difficulty. Then, a challenging version of continuous control was simulated in a physical 3D environment where the agent was embedded in a quadrupedal "ant" body. In this environment, the authors also trained low-level controllers and combined them with a higher-order search strategy to improve planning performance.

For the first experiment, the authors applied DC-MCTS and standard sequential MCTS to solve the maze problem and used the percentage of successful maze solutions as an evaluation metric. The results show that DC-MCTS performs better than standard sequential MCTS when given the same search budget. In addition, the authors found that DC-MCTS was able to efficiently find feasible paths even without a pre-trained search heuristic function, whereas standard sequential MCTS was unable to do so.

For the second experiment, the authors applied DC-MCTS and standard sequential MCTS to a continuous control problem in a physical 3D environment and used the percentage of successfully completed tasks as an evaluation metric. The results show that DC-MCTS performs better than standard sequential MCTS and isolates the relationship between high-level planning and low-level execution. In addition, the authors observed that the standard sequence MCTS search priority due to the left-first parser is overly biased towards selecting the next subgoal that is too close to the previous subgoal, which leads the method to over-manage the low-level controllers, especially in long corridors where the agent can solve the problem by itself.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/a5d41481-453d-4964-834e-64f4db50bf64)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new planning method that uses a sequence of subgoals instead of the original action sequence to improve the effectiveness of low-level strategies. This approach is realized by decomposing the original task into multiple subtasks and selecting the best subgoal in each subtask. 
  
  2. Compared to the traditional sequential execution approach to action planning, this method allows more flexibility in controlling the execution order of the plan, thus better adapting to different environments and task requirements. 
  
  3. In addition, the method introduces two search heuristic functions to reduce the number of evaluations and improve the search efficiency.
     
### 2. Innovative points
   The methodological innovations in this thesis are the use of subgoal sequences instead of original action sequences for planning and the introduction of two search heuristic functions to improve search efficiency. These innovations make the method more flexible and scalable, and can be adapted to a wider range of environments and task requirements.
   
### 3. Future Works
Future research can be carried out in the following aspects: 

  1.further optimizing the search heuristic function to make it more efficient; 
  
  2. exploring how to combine other planning algorithms to improve the performance; 
  
  3. investigating how to deal with complex dynamic environments and multi-intelligence collaboration problems.
