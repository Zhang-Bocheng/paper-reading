# ChatQA: Building GPT-4 Level Conversational QA Models
[paper link](https://arxiv.org/pdf/2401.10225) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a new model called ChatQA that outperforms GPT-4 in Retrieval Augmented Generation (RAG) and Conversational Question and Answer (QA) based on retrieval          |   Question and Answer (QA)       |

## Methodology

### 1. Abstract
In order to improve generation, the authors propose a two-stage instruction fine-tuning method and introduce a dense retriever dedicated to Conversational QA, which significantly improves the performance of RAG. In addition, the authors present CHATRAG BENCH, an evaluation platform with ten datasets covering a comprehensive evaluation of scenarios involving RAG, form-related QA, arithmetic calculations, and questions involving unanswerable questions. Experimental results show that the ChatQA-1.0-70B model built using Llama2 as the base model can slightly outperform GPT-4-0613 and GPT-4-Turbo-2024-04-09 on CHATRAG BENCH without relying on any synthetic data from OpenAI GPT models. In particular, the Llama3-ChatQA-1.5-70B model outperforms the accuracy of GPT-4-Turbo-2024-04-09, achieving a 4.4% improvement.

### 2. Method Description 
The paper presents two approaches for improving the performance of conversational Q&A systems: two-stage instruction tuning and retrieval enhancement based on human-annotated datasets. The first approach aims to improve the instructive and generative capabilities of the model through two stages of training. The second stage involves merging data from single rounds of Q&A and multiple rounds of dialogue into the training set to enhance the model's ability to process information in documents. The second approach uses the human-annotated dataset to build a high-quality conversational Q&A dataset and uses it to further train the retriever to improve the model's multi-round Q&A performance.

 ![image](https://github.com/user-attachments/assets/e97ab81f-38e4-4e23-a800-2e6f290311a9)
 
### 3. Methodological improvements
The main innovation of the paper is to propose a new conversational Q&A dataset, i.e., a dataset annotated by humans, which helps to improve the performance of the model. In addition, they propose a retrieval enhancement method based on the human-annotated dataset, which can significantly improve the model's multi-round Q&A performance.

### 4. Issues addressed 
The paper focuses on solving the problem of multi-round question and answer performance in conversational question and answer systems. By introducing a human-annotated dataset and a retrieval enhancement method based on this dataset, the solution proposed in this thesis can effectively improve the model's multi-round question and answer performance. This is important for achieving smarter and more natural human-computer interaction.

## Experiments
This paper focuses on the performance of the ChatQA model based on the GPT-{8B, 22B} pre-trained model on multi-round dialogue and Q&A tasks, and compares it with some cutting-edge large-scale language models. Specifically, the authors constructed CHATRAG BENCH, consisting of 10 long and short document datasets covering various types of questions and answers. They then evaluate the performance of their models using several benchmark tests, including F1 scores, human ratings, etc.

First, the authors compared different model variants with the OpenAI model. The results show that Llama3-ChatQA-1.5-8B/70B outperforms Llama2-Chat and Llama3-Instruct on most of the datasets.In addition, these models also perform better than GPT-4-0613 and GPT-4-Turbo.

![image](https://github.com/user-attachments/assets/c656df3a-ae7a-4398-9c7f-8a0707ea9c25)

Secondly, the authors analysed the impact of some key factors on model performance. For example, they found that training from stage 1 to stage 2 improves the model's multi-round dialogue capability. In addition, the addition of single-round dialogue datasets also helps to improve the model's performance. Finally, the authors also compare different types of text datasets and the model performance under different conditions.  

![image](https://github.com/user-attachments/assets/5ec49a86-dd97-41d5-a24a-6d0b78302efd)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a family of models called ChatQA that can outperform GPT-4 on conversational Q&A and RAG tasks, and does so using a relatively weak base model. 
  2. In addition, the paper devises a benchmark test (CHATRAG BENCH) containing ten conversational Q&A datasets and demonstrates the excellent performance of the ChatQA model on these datasets.
 
### 2. Innovative points
  1. The use of a two-stage instruction fine-tuning methodology and data processing flow improves the ability of the base model in integrating user-supplied or retrieved context;
  2. For the retrieval problem, it demonstrates that the fine-tuning of a single-round Q&A retriever is comparable to that of a query rewriting model based on the LLM, and also shows the potential of training a customised retriever from synthetic data.

### 3. Future Works
Future research directions include, but are not limited to, further improving the performance of the model, exploring more application scenarios, and optimising the interpretability and security of the model.   
