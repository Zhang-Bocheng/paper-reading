# TinyLlama: An Open-Source Small Language Model
[paper link](https://arxiv.org/pdf/2401.02385) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a small language model called TinyLlama, built on a variety of state-of-the-art technologies from the open-source community and using the Llama2 architecture and disambiguator.          | Llama2         |

## Methodology

### 1. Abstract
Despite its relatively small size, TinyLlama performs well on a range of downstream tasks and outperforms existing open source language models of equivalent size. The model's checkpoints and code are publicly available on GitHub. The article also describes the development of large-scale pre-trained language models and how model size and training data allocation can be optimised for optimal computational efficiency.

### 2. Method Description 
  1. Two different data sources, SlimPajama and StarCoder, were used to construct the pre-training dataset.
  2. A model architecture based on Transformer decoder was used and some optimisations such as pre-norm, RMSNorm, SwiGLU were introduced in it.
  3. During the training process, techniques such as FSDP, FlashAttention, xFormers are used to improve the training speed and efficiency.

![image](https://github.com/user-attachments/assets/4e4f8fca-94cc-4cf2-9904-3ac930dd893c)

### 3. Methodological improvements
  1. Training speed and efficiency were improved by using more efficient training frameworks and optimisation methods.
  2. A new pre-training phase was introduced to allow the model to be better adapted to domain-specific tasks.
  3. By adjusting parameters such as learning rate and batch size, the model is able to maintain good convergence performance even in the later stages of training.

### 4. Issues addressed 
The main goal of the thesis is to develop a pre-training model that is efficient and suitable for a variety of natural language and code tasks. By introducing a variety of optimisation techniques and a pre-training phase, the model can understand the semantic information in text more accurately and perform well in various application scenarios. Also, the paper provides an effective tool and technique for other researchers to achieve similar goals in their own research.

## Experiments
This paper presents the results of experiments on multi-task evaluation of the language model TinyLlama and compares it with other existing open source language models. Specifically, the authors conducted experiments in the following three areas:

**Common sense reasoning tasks:** including Hellaswag, OpenBookQA, WinoGrande, ARC-Easy and ARC-Challenge, BoolQ and PIQA tasks. These tasks were designed to understand TinyLlama's capabilities in common sense reasoning. The authors used the Language Model Evaluation Harness framework to evaluate the model, testing it in a zero-sample setting. The results of the experiment showed that all TinyLlama models outperformed the baseline model on many tasks and received the highest average scores.

![image](https://github.com/user-attachments/assets/ba9d71f1-2e50-41f1-be46-4b90dcd72fe4)

**Problem solving ability:** the problem solving ability of TinyLlama was tested using the InstructEval benchmark. The benchmark includes tasks such as Massive Multitask Language Understanding (MMLU), BIG-Bench Hard (BBH), Discrete Reasoning Over Paragraphs (DROP), and HumanEval. These tasks are designed to measure the model's world knowledge and problem solving skills. The authors evaluated the model in 5-shot and 3-shot settings. The results show that TinyLlama has better problem solving skills than other existing models.

![image](https://github.com/user-attachments/assets/45299a1d-9b77-4dfa-9d05-c1f0d5b78277)

**Chinese Comprehension and Reasoning Skills:** The Chinese comprehension and reasoning skills of TinyLlama v1.1 were tested by tasks such as xwinograd, xstorycloze, xnli and xcopa. These tasks are multilingual multiple choice quiz tasks, but the authors only considered Chinese. The authors found that after continuing to pre-train the Chinese corpus, TinyLlama v1.1 Chinese outperformed the other models in most tasks. In addition, the authors found that involving more code data helped improve TinyLlama's multilingual capabilities.

![image](https://github.com/user-attachments/assets/91a1b5d8-e71c-4e82-b4bb-ee714eee1a13)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a small-scale language model called TinyLlama and demonstrates the potential of using smaller-scale language models on large-scale datasets by investigating its training process.
  2. The model employs the Transformer decoder architecture and uses the same architecture and tokenizer as Llama 2. Experimental results show that TinyLlama exhibits similar or even better performance than existing open-source language models in a variety of downstream tasks.
  3. And, the paper highlights the importance of targeting specific inference budgets rather than focusing solely on training computational budgets, which provides insights for future research on language models.

### 2. Innovative points
The main contribution of the paper is to explore the possibility of using small language models on large-scale datasets. The authors used the same architecture and tokeniser as Llama 2 to build TinyLlama and trained it to 3 trillion tokens, which is the first 100 million parameter model known to be trained using such a large amount of data. With this approach, the authors demonstrate that it is feasible to train smaller-scale language models on larger datasets and can achieve excellent performance on many downstream tasks. 

### 3. Future Works
Future research could further explore the effects of this strategy and try experiments with other types of models or different hyperparameters. It is also possible to apply this strategy to other areas such as computer vision or other tasks in natural language processing.     

