# REALM: Retrieval-Augmented Language Model Pre-Training
[paper link](https://arxiv.org/pdf/2002.08909) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a new approach to pre-training language models, REALM (Retrieval-Augmented Language Model), which enhances the ability of a language model to retrieve and attend to documents from large corpora such as Wikipedia) of documents.         | Pre-train model          |

## Methodology

### 1. Abstract
The method uses masked language modeling as a learning signal and considers millions of documents in a backpropagation process. The authors demonstrate the effectiveness of REALM by fine-tuning it for an open-domain quizzing task and achieve significant performance gains (4-16% absolute accuracy) in three popular open-domain quizzing benchmarks compared to existing state-of-the-art models for storing explicit or implicit knowledge. In addition, REALM offers the advantages of interpretability and modularity.

### 2. Method Description 
This paper proposes a knowledge-enhanced pre-training model called REALM, which performs a prediction task by combining input text with documents from a knowledge base. REALM consists of two key components: **a neural knowledge retriever and a knowledge-enhanced encoder**. 

In the pre-training phase, REALM uses a masked language modeling (MLM) task to learn how to retrieve information from the knowledge base and use this information in the prediction task. In the fine-tuning phase, REALM uses the Open Question and Answer (OpenQA) task to learn how to answer questions and utilize information from the knowledge base.

### 3. Methodological improvements
  1. Use techniques such as mask entity recognition and date recognition to select mask tokens that require world knowledge to predict.
  
  2. Add an empty document as a "consistency penalty" during the pre-training process to prevent oversimplified retrieval results.

  3. For the case of the same pre-training dataset and knowledge base, exclude simple retrieval results that could lead to overfitting.
 
  4. Use the inverse closure task and BERT pre-training to initialize the embedding function to avoid cold-start problems.

### 4. Issues addressed 
The REALM model proposed in this paper aims to solve the problem of knowledge enhancement in NLP. It is able to retrieve relevant information from a knowledge base and apply it to various tasks such as masked language modeling, open quiz, etc. By introducing different strategies and techniques, REALM can better capture world knowledge and avoid problems such as overfitting and cold-start. 

![image](https://github.com/user-attachments/assets/8f363ba1-3235-4f66-b73b-d77a9c8ad002)

## Experiments
This paper focuses on the authors' experiments on the Open-QA task and compares them with other methods. Specifically, the authors use three different datasets (NaturalQuestions-Open, WebQuestions, and CuratedTrec) to evaluate their model and compare the results with existing methods. Among others, the authors also compare two different pre-training methods (Wikipedia and CC-News), as well as models of different sizes (Base, Large and 11B). 

In addition, the authors analyze the effects of some key components, such as encoders, retrievers, and masking schemes. Finally, the authors conclude that their proposed REALM method is one of the best Open-QA systems available, with better performance and smaller model size.

![image](https://github.com/user-attachments/assets/1a5c82c3-c771-4f84-bc2a-f48016c4f5b5)


