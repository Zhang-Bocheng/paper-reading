# ReFT: Reasoning with Reinforced Fine-Tuning
[paper link](https://arxiv.org/abs/2401.08967) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a method called Reinforcement Fine-Tuning (ReFT) for enhancing the reasoning of Large Language Models (LLMs).          |  Reinforcement Learning        |

## Methodology

### 1. Abstract
The method further optimises the model by performing supervised fine-tuning (SFT) using Chained Thinking (CoT) annotations and introducing online reinforcement learning (PPO algorithms) on top of it. Compared to traditional SFT, ReFT is able to better utilise multiple problem solution paths and achieve significant performance gains in tasks such as mathematical problem solving. Experimental results show that ReFT has better generalisation capabilities and can improve the performance of the model without relying on additional training data.

### 2. Method Description 
This paper proposes an algorithm called ‘Reinforced Fine-Tuning’ for joint knowledge-based reasoning (CoT) for natural language understanding and programme understanding. The algorithm consists of two phases: **a warm-up phase and a reinforcement learning phase**. In the warm-up phase, the model fine-tunes its strategy by training ‘problem-CoT’ pairs in a sample set to obtain basic problem solving ability. In the reinforcement learning phase, the model improves its performance by iteratively sampling responses, evaluating the correctness of the response answers and updating the parameters online. Specifically, the PPO algorithm was used and combined with a clipped objective function to train the value network.

![image](https://github.com/user-attachments/assets/6c183e98-1e2a-4c29-9bf3-a7571cd41edb)
 
### 3. Methodological improvements
Compared to traditional knowledge-based reasoning methods based on rules or manually designed features, the Reinforced Fine-Tuning algorithm proposed in this paper does not need to manually construct complex rules or features, but automatically learns the optimal policy by means of reinforcement learning. In addition, this paper introduces a partial reward mechanism, which can effectively reduce the effect of learning from sparse rewards and improve the robustness and accuracy of the algorithm.

### 4. Issues addressed 
The method in this paper mainly solves the problem of joint knowledge inference for natural language understanding and programme understanding. By means of reinforcement learning, the model is able to learn autonomously how to generate reasonable answers or solutions based on the given question and contextual information. This approach is highly flexible and generalisable, and has a wide range of applications in several fields.

## Experiments
This paper focuses on ReFT, a reinforcement learning-based approach to mathematical problem solving, and conducts comparative experiments with SFT, a traditional sample generation-based approach, and a self-training-based approach. Specifically, this paper conducts experiments on three different mathematical problem solving datasets, including GSM8K, SVAMP, and MathQA, and uses two common base models Galactica-6.7B and CodeLLAMA-7B.In the experiments, the authors use a variety of evaluation metrics, such as value accuracy, KL scatter, etc., and provide detailed analyses and discussion.

![image](https://github.com/user-attachments/assets/af6cb33c-9141-4887-a714-613ebd2bbf46)

Firstly, the authors conducted a comparison experiment between ReFT and SFT. The results show that ReFT achieves better performance than SFT on all datasets, especially on the P-CoT task. This indicates that ReFT has stronger generalisation ability and higher accuracy.

Secondly, the authors also conducted comparative experiments on self-training methods. The results show that although the online self-training method improves relative to the offline self-training method, it still lags far behind ReFT.This indicates that exploratory learning is crucial for improving the performance of ReFT.

![image](https://github.com/user-attachments/assets/65d3c988-46b6-40b3-bd0d-8959ba5f4763)

In addition, the authors also addressed the phenomenon of reward hacking in the MathQA dataset and proposed methods to control reward hacking. Meanwhile, the authors also tried some other techniques to further improve the performance of ReFT, such as voting and ranking, and the results show that these techniques can significantly improve the performance of ReFT.

![image](https://github.com/user-attachments/assets/f10c625d-79cc-44ca-aa92-b4ad16d2e1b5)

Finally, the authors verify the robustness and scalability of ReFT through several experiments. For example, ReFT still achieves good performance when using smaller language models; moreover, ReFT is able to explore and generate reasonable programs efficiently even in the case of extreme sparsity.  

## Conclusion

### 1. Advantages of the Thesis
  1. The authors conducted extensive experiments on three standard datasets with two base models CodeLLAMA and Galactica.The results show that ReFT outperforms traditional supervised fine-tuning (SFT) in terms of performance and generalisation ability.
  2. And, ReFT also performs better compared to some publicly available open-source models, which proves the effectiveness and usefulness of the ReFT method.
 
### 2. Innovative points
  1. ReFT utilises reinforcement learning to solve mathematical problems by exploring multiple CoT paths to optimise a non-differentiable objective, which improves the model's generalisation ability and performance.
  2. What is more, ReFT does not require additional or enhanced data engineering and can be used seamlessly in conjunction with other techniques.
 
### 3. Future Works
Future research directions include utilising offline reinforcement learning techniques and developing more detailed reward functions to improve training efficiency and performance, as well as extending the ReFT method to other types of inference tasks.  
