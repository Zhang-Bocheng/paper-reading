# MathAttack: Attacking Large Language Models Towards Math Solving Ability
[paper link](https://arxiv.org/pdf/2309.01686) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This thesis focuses on a security attack methodology against Large Language Models (LLMs) in terms of their mathematical problem solving capabilities.          |   Large Language Models (LLMs)       |

## Methodology

### 1. Abstract
Unlike traditional text adversarial attacks, the approach employs logical entity recognition techniques to identify and freeze logical entries and attack the remaining text via word-level attackers. Also, the authors present the RobustMath dataset for evaluating the robustness of LLM in terms of mathematical problem solving ability. The experimental results show that MathAttack can effectively attack the mathematical problem solving ability of LLMs, and that high-precision LLMs can also be attacked by low-precision LLMs.

![image](https://github.com/user-attachments/assets/43a193ef-3d4c-4016-a7dd-7ead0aa991fa)

### 2. Method Description 
The paper proposes an attack method for Math Word Problem (MWP) called MathAttack. The main goal of MathAttack is to make the pre-trained model produce incorrect predictions by modifying the logical entities in the MWP while keeping the semantics of the MWP unchanged. Specifically, MathAttack is divided into three main steps: **identifying logical entities, freezing logical entities, and attacking with a word-level attacker.**

  First, MathAttack uses the Named Entity Recognition (NER) model to identify three types of logical entities: character entities, numeric entities, and scene entities. 
  Then, these entities are marked as immutable to prevent changing them during the attack. 
  Finally, MathAttack uses a word-level attacker-based attack strategy to generate adversarial samples. 
  Specifically, it first determines which words are important and selects the words with the highest importance scores as vulnerable words. 
  Next, MathAttack tries to replace it with a synonym of the vulnerable word and decides whether to keep or discard the change based on the model's predictions.

![image](https://github.com/user-attachments/assets/3a6af14c-094e-4270-bc92-80c2a7d88e06)

### 3. Methodological improvements
  1. The quality of the adversary samples depends on the word-level attacker used by the attacker.Therefore, improving the attack algorithm can further improve the quality of the generated adversary samples.
  
  2. MathAttack currently considers only three types of logical entities, whereas in reality there may be other types of entities that need to be protected. Therefore, expanding the list of logical entity types can enhance the scope of application of MathAttack.
  
  3. In practice, there may be many different models that need to be attacked. Therefore, designing a common attack framework can share attack techniques among different models and improve the efficiency of attacks.

### 4. Issues addressed 
  1. The key innovation of MathAttack is its ability to protect the logical entities in the MWP from being modified, thus avoiding destroying the original logical structure of the MWP. In addition, MathAttack uses a word-level attacker to ensure that the generated adversarial samples are as close as semantically possible to the original text.
  
  2. Aiming at the limitation that traditional text attacks cannot deal with mathematical problems, MathAttack introduces a protection mechanism for mathematical logic entities, so that the attack process will not destroy the original logical structure of MWP.
  
  3. MathAttack proposes a word-level attacker-based attack strategy for mathematical problems in black-box attack environments, which is capable of generating high-quality adversarial samples while ensuring semantic similarity. This helps to increase the success rate of the attack and reduce the detection risk.

## Experiments
This paper focuses on experiments on mathematical attacks on large language models and presents a new mathematical problem dataset, RobustMath. In the experiments, the authors use four mainstream large language models as victim models, including Flan-T5-large, Flan-T5-xl, ChatGLM2, and ChatGPT.Meanwhile, the authors chose two benchmark datasets for maths word problems, GSM8K and MultiArith, to serve as data sources for the experiments. The experiments used four evaluation metrics, including clean accuracy, attack accuracy, attack success, and similarity, and manually checked each adversarial sample to ensure correctness. 

![image](https://github.com/user-attachments/assets/cde2fefb-00ee-4a77-8aa4-8e97e21d1769)

The experimental results show that the method can effectively attack the mathematical problem solving ability of large language models and that more powerful models are harder to attack. In addition, the authors conducted experiments comparing zero-shot and few-shot, and found that the use of few-shot hints enhances the mathematical problem-solving ability and robustness of large language models.

![image](https://github.com/user-attachments/assets/89d13c0d-51f5-4b00-8ebe-61e9c8ca2183)

Finally, the authors propose a new mathematical problem dataset, RobustMath, for measuring the robustness of mathematical problem solving ability of large language models. The experimental results show that RobustMath can effectively measure the robustness of the mathematical problem-solving ability of the model, and the robustness of the model can be further improved by finetuning.  

![image](https://github.com/user-attachments/assets/e63ba0c8-f449-4e32-b7d6-9ecb2b5f1e74)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a study on the security of large language models with respect to their mathematical problem solving capabilities and proposes a new attack method, MathAttack.
  
  2. MathAttack can effectively attack the mathematical problem solving ability of large language models and can maintain the consistency of mathematical logic.

  3. The paper also proposes a new dataset, RobustMath, which contains high-quality samples of mathematical problem confrontation and can be used to assess the robustness of mathematical problem solving ability of large language models.

  4. Experimental results show that the adversarial samples generated using MathAttack can be transferred between large language models of different sizes and accuracies, and that mathematical problems of higher complexity are more susceptible to attack.

### 2. Innovative points
  1. MathAttack is an attack method against large language models in terms of their mathematical problem solving capabilities, which ensures the consistency of mathematical logic by identifying and freezing mathematical logic entities.
  
  2. The RobustMath dataset proposed in the paper is the first dataset specifically designed to assess the robustness of large language models in terms of their mathematical problem solving ability. 

### 3. Future Works
  1. Other types of attack methods such as instruction learning or reinforcement learning can be further explored to improve the robustness of large language models in terms of mathematical problem solving ability.

  2. This approach can be extended to tasks in other domains, such as natural language reasoning, machine translation, etc., to evaluate the security of large language models in these tasks.  
