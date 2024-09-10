# LASER: LLM Agent with State-Space Exploration for Web Navigation
[paper link](https://arxiv.org/pdf/2309.08172) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents Laser Agent, a new approach to interactive decision-making tasks for Large Language Models (LLMs).          |   Large Language Models (LLMs)       |

## Methodology

### 1. Abstract
The approach enables flexible backtracking and error recovery by modelling interactive tasks as state-space explorations, allowing the model to perform actions and transition to predefined sets of states as it completes the task. Experimental results show that the method significantly outperforms previous approaches and approaches human performance levels on Web navigation tasks.

### 2. Method Description 
This paper presents a LLM-based intelligent agent approach for handling user interaction tasks on web pages. The approach guides the behaviour of the intelligent agent by defining a state space and an action space, and uses some simple instructions to describe the characteristics and goals of each state. Unlike traditional example-driven approaches, this approach does not need to provide a large number of contextual examples to train the intelligent agent, but instead guides its behaviour by defining the state and action spaces.

![image](https://github.com/user-attachments/assets/c0d4b9aa-1e43-4667-be41-07027df61044)

### 3. Methodological improvements
  1. The main improvement of the method is the introduction of a state tracking capability that allows the intelligent agent to better understand the current state of the environment and act accordingly.
  
  2. In addition, the method introduces a memory buffer for storing intermediate results that were checked but not matched during the exploration process, so that one of them can be selected as the final output in case a final solution cannot be found.

### 4. Issues addressed 
The approach primarily addresses the challenge of implementing intelligent agents in complex environments, especially where rapid adaptation to new situations and errors is required. By defining the state and action space and providing clear and simple instructions, the approach can more effectively guide the behaviour of intelligent agents, thus improving their performance and efficiency.

## Experiments
This paper describes the experiments conducted by the authors on the WebShop task and compares them with other methods. The experimental results show that the LASER method proposed by the authors outperforms other methods in both reward and success metrics. In addition, the authors conducted A/B tests to validate the effects of different design decisions and demonstrated the generality of the method through transfer learning experiments.

Specifically, the authors first used two interactive decision-based methods, ReAct and ASH, as benchmarks, and then compared these methods with LASER, a new method proposed by the authors. In their experiments, the authors evaluated the model using 500 test set instructions and employed reward and success rates as evaluation metrics. The results of the experiment showed that LASER achieved better results on both metrics, which proved its effectiveness.

![image](https://github.com/user-attachments/assets/8ef7dfd0-0ad0-4b87-a911-94a341b880ff)

Next, the authors conducted A/B tests to verify the impact of different design decisions on performance. For example, the authors attempted to add an example input-output pair to guide the learning of the model, but found that doing so did not improve performance. Additionally, the authors compared the difference between using function calls and text generation for action selection and found some room for improvement in both areas.

![image](https://github.com/user-attachments/assets/dad99740-155e-46cf-a044-60d3fa7cedef)

Finally, the authors also conducted migration learning experiments simulated to a real environment, i.e., applying LASER directly to Amazon.com to make shopping recommendations. The results of the experiments show that even in more realistic environments, LASER is still able to achieve good results, even better than human performance.  

## Conclusion

### 1. Advantages of the Thesis
The paper presents a new interactive task-solving approach that applies LLMs to the task of exploring state spaces. This approach reduces task difficulty by defining the set of possible states and the space of actions that can be performed in each state, and enables the agent to easily backtrack through errors and always select a valid action. Experiments on the Webshop task show that the approach outperforms all baselines and approaches human performance. In addition, the method has good generalisation capabilities and can be migrated to similar tasks in other domains.

### 2. Innovative points
  1. The main contribution of this thesis is the proposal of a novel approach to interactive tasks. Unlike previous approaches, the method not only considers the global action space, but also defines a possible action space for each state.
  
  2. This allows the agent to better understand the task environment and to recover more easily in case of errors.
  
  3. In addition, the approach does not require the use of any contextual examples, but is based entirely on state-specific instructions, which makes it more flexible and versatile.

### 3. Future Works
One of the future research directions is to develop a multilevel system in which each specific domain is managed by an agent like LASER, while the general open-world agents collaborate with other domain agents to fulfil various user commands. In addition, since the approach still carries some risks, more testing and validation is needed before it can be applied to real-world scenarios.  
