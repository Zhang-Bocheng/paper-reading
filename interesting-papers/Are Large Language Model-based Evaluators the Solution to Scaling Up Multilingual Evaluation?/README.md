# Are Large Language Model-based Evaluators the Solution to Scaling Up Multilingual Evaluation?
[paper link](https://arxiv.org/pdf/2309.07462) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores the performance of Large Language Models (LLMs) in natural language processing tasks and proposes the use of LLMs as evaluators to address the limitations of existing benchmarks and metrics.          | Large Language Models (LLMs)        |

## Methodology

### 1. Abstract
Using an LLM such as the GPT-4 as an evaluator, the authors tested it in three text generation tasks, five metrics, and eight languages, and calibrated it against 20K native speaker judgements. The results show that using LLMs as evaluators improves multilingual evaluation, but more accurate calibration is needed for languages with low-resource and non-Latin characters to avoid bias.

![image](https://github.com/user-attachments/assets/de6afd92-cfe0-4c3e-aac1-fd91a457fb16)

## Experiments
This paper describes the authors' experiments using the GPT-4 model for a text generation task and provides a comparative analysis of various aspects of it. Specifically, the authors conducted the following comparative experiments:

  1. **Comparison of different prompting styles**: the authors tried two different prompting styles, single prompting and multiple prompting, and also provided detailed descriptions and examples for each task to ensure that the model could understand the requirements of the task correctly.
  
  2. **Comparison of model evaluation with human evaluation**: the authors constructed an evaluation model by providing clear and simple evaluation criteria and compared it with human evaluation results. They use percentage agreement (PA) to measure consistency and class distribution, and weighted F1 scores to measure internal consistency.
     
 ![image](https://github.com/user-attachments/assets/54460fd8-9c34-4127-9734-e542af221e30)
 
  3. **Effect of tuning hyperparameters**: the authors tested the performance of the model at different temperatures and found that it performed best at a temperature of zero.

![image](https://github.com/user-attachments/assets/575974b0-980d-4714-8227-3dcfa6e28f81)

  4. **Effect of a small number of samples**: the authors tested the performance of the model in small sample situations and found that a small number of samples may have an effect on the model's performance in some cases.
