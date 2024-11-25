# Self-Rewarding Language Models
[paper link](https://arxiv.org/pdf/2401.10020) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores the problem of using self-rewarding language models to train superhuman agents.          |  Large Language Models        |

## Methodology

### 1. Abstract
The current common training method is to train reward models by human preferences, but this approach can be limited by the level of human performance, and these isolated frozen reward models cannot learn to improve during the training of the language model. The authors' proposed self-rewarding language model uses the language model itself as a discriminator that provides its own rewards during training. Experimental results show that this iterative DPO training not only improves instruction adherence, but also improves the model's ability to provide high-quality rewards. After three iterations, the model fine-tuned for Llama 2 70B outperformed many existing systems including Claude 2, Gemini Pro, and GPT-4 0613 on the AlpacaEval 2.0 leaderboard.

### 2. Method Description
The method is based on the Overall Self-Alignment Algorithm (OSAA), an adaptive feedback learning algorithm with iterative training, which improves its performance by gradually optimising the model. Specifically, the method first uses a pre-trained language model (Base pretrained LLM) as the initial model and names it M0. Then, based on M0, the IFT+EFT seed data is fine-tuned using SFT to obtain the model M1. next, M2 is trained using AIFT(M1) data and DPO, and finally M3 is trained using AIFT( M2) data and DPO to train M3. This process is similar to the iterative DPO method used in Pairwise Cringe Optimisation, but in this method an external fixed reward model is used.

![image](https://github.com/user-attachments/assets/5223d9c1-713d-4e68-bb99-1418084ca7d1)

### 3. Methodological improvements
The method improves the traditional feedback learning algorithm by introducing iterative training and adaptive tuning to improve the performance and robustness of the model. Instead of manually setting the parameters of feedback learning, the method is automatically tuned to get better results compared to the traditional method.

### 4. Issues addressed 
The method mainly solves two problems in feedback learning: one is how to choose appropriate feedback data; the other is how to determine the parameters of feedback learning. Through iterative training and adaptive adjustment, the method can automatically select the best feedback data and dynamically adjust the parameters of feedback learning according to the actual situation, thus effectively improving the performance and robustness of the model.

## Experiments
**Comparative Experiments on Instruction Following Ability:** this experiment used a variety of datasets and models to test the performance of different models on an instruction following task and used several evaluation metrics for the evaluation. The results show that iterative training significantly improves the performance of the models and that self-reward training does not degrade the models' capabilities compared to standard supervised learning-based training methods.

![image](https://github.com/user-attachments/assets/754f53c1-d4f8-4851-b5b8-0772b445ecf8)

**Comparative experiment on self-reward modelling capabilities:** this experiment uses a variety of evaluation metrics to test the performance of different models on a self-reward modelling task. The results show that iterative training also significantly improves the model's performance on this task, and that self-reward training does not degrade the model's capabilities compared to standard supervised learning-based training methods.

**Experiment comparing reward modelling capabilities:** this experiment uses a variety of evaluation metrics to test the performance of different models on a reward modelling task. The results show that iterative training also significantly improves the model's performance on this task, and that self-reward training does not degrade the model's capabilities compared to standard supervised learning-based training methods.  

![image](https://github.com/user-attachments/assets/11b32fc4-eabd-452c-94a4-87d13f4e3921)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new approach to training large language models, Self-Rewarding Language Models (SRLMs), which enables iterative self-improvement by giving the models the ability to both instruction follow and self-create new examples.
  2. This approach avoids the problem of fixing the reward model in existing approaches and improves the model's reward modelling capability and instruction following performance. Experimental results show that training with a self-rewarding language model yields better results compared to the baseline model.

### 2. Innovative points
The self-rewarding language model proposed in this paper is a novel approach to training large language models, with the innovation of combining the reward model and the language model into one, enabling the model to create new examples and evaluate them autonomously, thus enabling iterative self-improvement. In addition, the method employs the LLM-as-a-Judge mechanism, which enables the model to better understand the user's needs and provide high-quality responses.

### 3. Future Works
Future research directions include further exploring the application of self-rewarding language models in different domains, investigating how to train self-rewarding language models using less manually labelled data, and how to improve the effectiveness of self-rewarding language models by combining with other techniques (e.g., transfer learning).   
