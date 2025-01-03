# FMDLlama: Financial Misinformation Detection based on Large Language Models
[paper link](https://arxiv.org/pdf/2409.16452) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a financial misinformation detection method called ‘FMDLlama’, which is based on Large Language Models (LLMs) for training and optimisation.           | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
In the current research, most of the traditional methods are used for financial misinformation detection, and the advantages of LLM are not explored. Therefore, the authors propose a multi-task financial misinformation dataset (FMDID) that supports fine-tuning of LLM instructions, as well as a comprehensive Financial Misinformation Evaluation Benchmark (FMD-B) that includes classification and explanation generation tasks to test the financial misinformation detection capabilities of LLM.

### 2. Method Description 
The financial disinformation detection (FMD) model proposed in this paper is based on the open-source Large Language Model (LLM), parameterised using pre-training weights, and enables the processing of multiple financial disinformation detection tasks through multi-task learning. Specifically, the model uses an autoregressive language model as the base generator and is capable of simultaneously processing multiple financial disinformation detection tasks, including disinformation detection and explanation generation. 

Each task is represented by a set of context-target pairs, where the context contains the task description, the input text and the query, while the target is a sequence of further tokens containing answers to the query. The model is optimised on the merged dataset to maximise the objectives of conditional language modelling, leading to improved prediction and generation performance.

![image](https://github.com/user-attachments/assets/de13f29c-dfd3-4cc9-8cf0-d64fab3ed17f)

### 3.  Methodological improvements
This paper proposes a new dataset construction methodology that combines two existing financial disinformation datasets, FinFact and FinGuard, for the construction of the FMD's Directive Fine-tuning Dataset (FMDID). In addition, this paper presents the FMD benchmarking dataset (FMD-B) for evaluating the performance of the models on the financial disinformation detection task.FMDLlama2 and FMDLlama3 are constructed by fine-tuning LLama2-chat-7b and LLama-3.1-8B-Instruct3, which are models that are trained on the FMDID dataset for training. All models were trained on two Nvidia Tesla A100 GPUs, each with 80 GB of memory.

### 4. Issues addressed 
The main contribution of this paper is to provide a new approach to financial disinformation detection that is based on open-source large-scale language models, is able to handle multiple financial disinformation detection tasks at the same time, and achieves good results in experiments. This method can provide strong support for the detection of financial disinformation, which can help to protect the interests of investors and maintain the stability of the market.

## Experiments
This paper presents the results of comparative experiments using two approaches based on language models in the field of financial disinformation detection. One of them uses pre-trained language models (e.g., BERT and RoBERTa) and the other uses unsupervised learning language models (e.g., LLaMA and Mistral). The paper also describes the metrics used to evaluate the performance of these models, including accuracy, precision, recall, micro-average F1 values, and explanatory evaluation metrics such as ROUGE and BERTScore.

In terms of experimental results, this paper finds that language models using unsupervised learning such as LLaMA and Mistral can achieve better performance on financial disinformation detection tasks. LLaMA3, in particular, outperforms all other publicly available LLaMA models and the private ChatGPT model on the FMD-B dataset. While BERT and RoBERTa were fine-tuned for each classification task individually and had similar performance to FMDLlama3 on the simple FinGuard dataset, they did not perform as well as FMDLlama3 on the complex dataset FinFact.This may be due to the fact that PLMs with fewer parameters have difficulty in comprehending long and complex textual content. 

In contrast, for LLMs without fine-tuning, Mistral-7b, LLama3.1-8b and ChatGPT perform well. This is because most of the data points in FMD-B are long texts, while Mistral-7b, LLama3.1-8b and ChatGPT allow for longer input lengths and better comprehension of the corresponding long texts. The effectiveness of domain-specific instruction fine-tuning strategies can be recognised by comparing the results of FMDLlama2 and llama2-7b and FMDLlama3 and llama3.1-8b. The domain-specific instruction fine-tuning strategy enables LLMs to pay more attention to those domains, resulting in better performance.  

![image](https://github.com/user-attachments/assets/d171f62b-76cb-4aae-a1cc-1beaed9c1019)

## Conclusion

### 1. Advantages of the Thesis
This paper proposes the first language model (LLM) dedicated to financial disinformation detection (FMD) and construct the corresponding multi-task command adjustment dataset (FMDID) and evaluation benchmark (FMD-B). Experimental results show that the model performs well on FMD tasks and outperforms other open-source LLMs as well as ChatGPT.In addition, the authors plan to further expand the datasets of FMDID and FMD-B in order to improve the performance of FMDLlama and evaluate the FMD capabilities of LLMs more comprehensively. 

### 2. Innovative points
The main contribution of this paper is to propose a new approach to address the problem of false information detection in the financial domain. Specifically, the authors construct a multi-task instruction-tuned dataset that includes tasks such as classification and explanation generation to support fine-tuning of LLM. They then developed the first LLM dedicated to FMD, FMDLlama, and applied it to the FMD-B assessment benchmark. Experimental results show that FMDLlama performs well on FMD tasks and outperforms other open source LLMs and ChatGPT.
 
### 3. Future Works
Due to the limited publicly available financial disinformation datasets, the authors constructed instruction tuning datasets and assessment benchmarks based on only two datasets, which may affect the generalisation ability and reliability of the model. Therefore, in future research, expanding the size of the datasets to include data from different sources, platforms, domains, and languages could be considered to better assess the FMD capabilities of LLM. Also, the effect of larger models could be explored to further improve the performance of FMDLlama. 
