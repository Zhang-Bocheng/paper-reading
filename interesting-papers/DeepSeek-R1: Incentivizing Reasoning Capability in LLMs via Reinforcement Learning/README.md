# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
[paper link](https://arxiv.org/pdf/2501.12948) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 |  This paper introduces DeepSeek-R1 and its two versions: DeepSeek-R1-Zero and DeepSeek-R1.         | LLMs         |

## Methodology

### 1. Abstract
DeepSeek-R1-Zero, trained by large-scale reinforcement learning (RL), has excellent inference capabilities and naturally emerges with many powerful inference behaviors. However, it suffers from some problems such as poor readability and language mixing. To address these issues and further improve the inference performance, the authors introduced DeepSeek-R1, a model that performs RL training prior to multi-stage training and cold-start data. Experimental results show that DeepSeek-R1 performs comparably to OpenAI-o1-1217 on the inference task.

### 2. Method Description 
The paper proposes two approaches to improve the model's reasoning ability: one is to apply reinforcement learning (RL) directly to the base model, and the other is to “distill” the reasoning patterns of a larger model into a smaller one.

In the first approach, researchers use RL to train the base model directly, without relying on supervised fine-tuning (SFT). This approach allowed the model to explore Chain Thinking (CoT) to solve complex problems and develop DeepSeek-R1-Zero. DeepSeek-R1-Zero demonstrated capabilities such as self-validation, reflection, and generating a long chain of CoTs, marking an important milestone for the research community. Notably, this is the first publicly available research demonstrating that the ability to motivate LLM reasoning through pure RL can be achieved without the need for SFT.This breakthrough paves the way for future developments.

In the second approach, the researchers introduced a pipeline to develop DeepSeek-R1. the pipeline consists of two RL phases aimed at discovering better reasoning patterns and aligning them with human preferences, as well as two SFT phases that serve as seeds for the model's reasoning and non-reasoning abilities. They believe this pipeline will benefit industry by creating better models.

### 3. Methodological improvements
One of the main contributions of the paper is the improvement of the existing methodology. The researchers applied RL directly to the base model instead of performing supervised fine-tuning first. In addition, they demonstrated how to “distill” the inference patterns of a larger model into a smaller model, thus improving performance.

### 4. Issues addressed 
This paper addresses the problem of inference in natural language processing. By applying RL directly to the underlying model, the researchers were able to explore chain thinking to solve complex problems. In addition, they demonstrated how to “distill” the reasoning patterns of a larger model into a smaller model, thereby improving performance. These methods help to improve the reasoning power and performance of models, providing important support for further developments in the field of natural language processing.

## Experiments
This paper focuses on methods to reinforce the reasoning ability of large language models(LLMs), and conducts several comparative experiments to verify their effectiveness. Specifically, this paper first uses a rule-based reward system and a pure RL approach to train a base model, DeepSeek-R1-Zero, which performs well on math problems. Then, a new model DeepSeek-R1, which combines RL with human-friendly data, is obtained by collecting some high-quality data as cold-start data, which is used to further optimize the model. Finally, the authors also use a model distillation technique, which applies the power of reinforcement learning to a smaller model.

**Comparison Experiment 1: DeepSeek-R1-Zero vs DeepSeek-R1** In this experiment, the authors compare the performance of two models. In this case, DeepSeek-R1-Zero is a model trained using only reinforcement learning, while DeepSeek-R1 is a model trained with a combination of reinforcement learning and human-friendly data. The results show that DeepSeek-R1 performs better on several benchmarks relative to DeepSeek-R1-Zero, especially on programming-related tasks. This suggests that adding human-friendly data can significantly improve the performance of the model.

**Comparison Experiment 2: DeepSeek-R1 vs DeepSeek-V3** In this experiment, the authors compare the performance of two models, DeepSeek-R1 and DeepSeek-V3. The results show that DeepSeek-R1 outperforms DeepSeek-V3 on most benchmarks, especially on tasks that require long-chain thinking (e.g., programming). This further demonstrates the effectiveness of reinforcement learning for improving model reasoning.

**Comparison Experiment 3: DeepSeek-R1 vs. other baselines** such as Qwen2.5-Math-1.5B In this experiment, the authors compare the performance of DeepSeek-R1 with several other baseline models. The results show that DeepSeek-R1 outperforms the other baseline models on most of the benchmarks, especially on tasks that require long-chain thinking (e.g., programming). This reaffirms the importance of reinforcement learning for improving model reasoning.

![image](https://github.com/user-attachments/assets/414756d8-2fd5-46e3-b478-ae04d84b2125)

## Conclusion

### 1. Advantages of the Thesis
This paper proposes a RL based approach to enhance the inference of models and achieve excellent performance on several tasks. The authors improved the performance of the model by using a large model for RL training and transferring it to a smaller model using data distillation techniques. In addition, the article shares the failures that the authors encountered during the development process, providing a valuable reference for readers.

### 2. Innovative points
The main contribution of this paper is to propose a new RL method to improve the inference ability of the model. The method utilizes the powerful capability of large models and the efficiency of small models by transferring the knowledge from large models to small models through data distillation techniques, thus improving the performance of the models. And, the authors explored some other approaches such as process reward modeling and Monte Carlo tree search, but these approaches encountered some challenges in practice.

### 3. Future Works
In future research, the authors plan to further extend the capabilities of DeepSeek-R1, including improving its ability to handle multilingual queries, optimizing its cue engineering, and investigating how to apply CoT to more complex tasks such as function calls and JSON output. What is more, the authors will continue to improve data distillation techniques and reinforcement learning algorithms to further enhance the performance of the model.   
