# Evolving Curricula with Regret-Based Environment Design
[paper link](https://arxiv.org/pdf/2203.01302) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 |This paper explores how general ability agents can be trained through the use of regret design methods.          | Reinforcement Learning          |

## Methodology

### 1. Abstract
   The authors propose a method called Adversarially Compounding Complexity by Editing Levels (ACCEL), which utilizes the power of evolution to find effective levels in principled regret design. This approach consistently produces levels at the frontiers of agent competence, resulting in courses that start out simple but gradually become more and more complex. Experimental results show that ACCEL achieves significant empirical gains in multiple settings and maintains the theoretical strengths of previous regret design approaches.

   ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/3fa55294-506c-4f62-bcb6-b0d2435025a3)

### 2. Method Description 
  This paper presents two methods for Unsupervised Environment Design (UED), PAIRED and Prioritized Level Replay (PLR), as well as a new method Adversarially Compounding Complexity by Editing Levels (ACCEL).

**PAIRED** maximizes the regret value of a teacher agent by estimating the difference between a student agent and another agent. This approach requires an RL problem and may encounter convergence difficulties in practice.

**PLR** uses a rolling buffer to store the level of high regret values and trains the student agent on the set of this level. This approach can produce strategies with strong generalization capabilities, but is limited to random sampling levels.

ACCEL combines an evolutionary environment generator with a regret-value based advisor. It avoids the drawbacks of random search by editing existing levels to continuously discover new complex structures. This approach does not require a specific editing mechanism and can be performed using simple random mutations.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/3f67922b-7f31-43c7-a66f-3d43bbf8249b)

### 3. Methodological improvements
   ACCEL is able to learn complex structures more efficiently compared to PAIRED and PLR and does not require craft rules or complex editing mechanisms. In addition, it is more efficient compared to other evolutionary algorithms because it only requires a single GPU for training.
   
### 4. Issues addressed 
  This paper addresses two issues in the design of unsupervised environments:

1. How to design more challenging environments to promote students' system generalization ability.
   
2. How to improve the efficiency and generalization ability of UED algorithms for better application in real-world scenarios.
   
## Experiments
  This paper focuses on the performance of the ACCEL algorithm in a selection of sizable navigation environments and BipedalWalker environments, and compares it to several benchmark methods. Specifically, the authors use MiniGrid, Wang et al.'s BipedalWalker environment, and a Lava environment of their own design to test ACCEL's performance. In each environment, the authors used different evaluation metrics to measure the performance of different algorithms, including IQM, reliability, and training time. From these experiments, the authors draw the following conclusions:

1. ACCEL performs better than other benchmark methods in partially sizable navigation environments, especially in environments with high generative complexity.

2. ACCEL also performs well in BipedalWalker environments and is able to achieve higher rates of return in a variety of challenging environments.

3. ACCEL is able to converge faster and produce more consistent performance than other benchmark methods.

   ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/879d963c-7042-48b6-a7c7-dfba9ef56126)

## Conclusion

### 1. Advantages of the Thesis
 ACCEL is a new adaptive learning algorithm that improves the capabilities of student agents by editing previously designed environments to continuously evolve new complex environments. The algorithm avoids methods that require domain-specific heuristics and provides theoretical robustness guarantees. 
 
 Experimental results show that ACCEL performs well in both the navigation task and the 2D bipedal walking task, rapidly increasing the complexity of the environments and producing highly capable student agents. In addition, ACCEL uses a regret-based curriculum design strategy that reduces dependence on domain-specific heuristics and provides better generalization and scalability.
 
### 2. Innovative points
  The core idea of ACCEL is to continuously evolve new complex environments by editing previously designed environments, thus improving the ability of student agents. The algorithm utilizes a regret mechanism to select the next environment to be edited, which allows the algorithm to maintain some stability while continuously exploring new environments. Meanwhile, ACCEL also provides some novel techniques, such as neural network-based editors and genetic algorithm-based evolutionary strategies, which provide strong support for achieving an efficient learning process.
  
### 3. Future Works
  Future research could consider how to address these issues to further improve the effectiveness of ACCEL. In addition, ACCEL can be combined with other adaptive learning algorithms to achieve a more efficient adaptive learning process.
