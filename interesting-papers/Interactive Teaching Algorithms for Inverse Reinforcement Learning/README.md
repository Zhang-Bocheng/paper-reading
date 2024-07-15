# Interactive Teaching Algorithms for Inverse Reinforcement Learning
[paper link](https://arxiv.org/pdf/1905.11867) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 | This paper investigates the problem of Inverse Reinforcement Learning (IRL) and introduces a helpful instructor to assist learners in accelerating the learning process.         | Reinforcement Learning          |

## Methodology

### 1. Abstract
   The authors propose an interactive teaching framework in which the teacher selects the next presentation to provide information based on the learner's current strategy. Teaching algorithms are designed for two specific scenarios - an omniscient scenario and a black-box scenario - and convergence guarantees are demonstrated in the omniscient scenario. Experimental results show that learning can be significantly accelerated in a car driving simulation environment compared to an uninformed instructor.
   
### 2. Method Description 
  The paper proposes two interactive teaching frameworks: an "omniscient teacher" model with full knowledge of the learner's dynamics, and a "black-box teacher" model with only partial information about the learner's dynamics. 
  
  In the omniscient teacher model, the teacher observes the learner's current strategy and provides a demonstration to help the learner learn better, while in the black-box teacher model, the teacher can only obtain information about the learner's strategy by questioning the learner, and selects the demonstration that best helps the learner to improve his/her performance based on this information.

For the omniscient teacher model, the authors propose the OMNITEACHER algorithm, which first converts the target strategy into a corresponding hyperparameter, and then achieves fast learning by greedily guiding the learner closer to this hyperparameter. For the black-box teacher model, the authors propose the BBOXTEACHER algorithm, which guides the learner by constantly estimating his/her strategy and selecting the demonstration that differs most from it.

![image](https://github.com/user-attachments/assets/e6eb4f80-af8c-4c31-a2ef-1e6a914a0022)

### 3. Methodological improvements
  1. Compared with traditional methods such as randomized demonstration or fixed strategy demonstration, the interactive teaching framework proposed in this thesis can target the demonstration that can best help learners improve their performance according to their current state and strategy information, thus greatly improving the learning efficiency.

  2. In addition, the paper also considers the problems in practical applications, such as the difficulty of observing the learner's strategy and the unknown dynamic information of the learner, and proposes corresponding solutions to make the method more practical.
     
### 4. Issues addressed 
  The interactive teaching framework proposed in the paper can effectively help learners acquire knowledge and skills faster, especially in situations that require a lot of practice and trial-and-error, such as in the fields of machine learning and autonomous driving. At the same time, the method can be personalized according to learners' characteristics and needs to further enhance the learning effect.

## Experiments
  This paper focuses on the authors' experiments using different teaching algorithms to teach learners in a simulated driving environment and compares their effectiveness. Specifically, the authors conducted the following two comparison experiments:

The first experiment is a comparison of the effectiveness of teaching in a linear reward setting. In this experiment, the authors considered the first seven of eight tasks, each with five lanes and a total of 20 states. The teacher used a linear reward function to define his behavioral strategy, while the students used a state-dependent linear reward function to try to imitate the teacher's behavior. The authors used the results of an average of ten runs to evaluate the effectiveness of the different teaching algorithms and found that the OMNITEACHER algorithm, which is based on hyperparametric optimization, was more effective than the other algorithms.

 ![image](https://github.com/user-attachments/assets/20fb9b4e-9f0d-4d7e-a28d-228fd3956aa9)
 
The second experiment compares the effectiveness of teaching in a nonlinear reward setting. In this experiment, the authors still considered the first five of the eight tasks, but used a nonlinear reward function to define the teacher's behavioral strategy. Students similarly used a state-dependent linear or nonlinear reward function to try to imitate the teacher's behavior. The authors similarly used the results of an average of ten runs to evaluate the effectiveness of the different teaching algorithms and found that the BBOXTEACHER algorithm, which is based on hyperparameter optimization, was more effective than the other algorithms when using a nonlinear reward function.

![image](https://github.com/user-attachments/assets/335036d9-e176-4f36-aa90-8055a00335da)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new interactive teaching algorithm that can effectively help machine learning models learn tasks and can be used in a black-box environment.
  
  2. The algorithm is based on the Maximum Entropy Inverse Reinforcement Learning (MCE-IRL) framework, which optimizes the parameters by minimizing the difference between the target strategy and the teacher's strategy.
     
### 2. Innovative points
  1. The methodological innovation of this thesis is to apply the Maximum Entropy Inverse Reinforcement Learning (MCE-IRL) framework to interactive teaching and learning, and propose two algorithms, OMNITEACHER and BBOXTEACHER, which are applicable to different contexts.
  
  2. In addition, the paper provides an effective hyperparameter search method, which can help users quickly find the optimal hyperparameter settings.

### 3. Future Works
  There are issues such as how to ensure that the teacher's behavior is reasonable in practical applications, and how to deal with incomplete or incorrect information provided by the teacher. Therefore, future research directions can further explore these issues and try to develop more efficient and reliable interactive teaching algorithms.

