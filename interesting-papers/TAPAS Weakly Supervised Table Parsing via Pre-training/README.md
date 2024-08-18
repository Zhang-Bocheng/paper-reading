# TAPAS: Weakly Supervised Table Parsing via Pre-training
[paper link](https://arxiv.org/pdf/2004.02349.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper presents a weakly supervised table parsing method called TAPAS, designed to answer natural language questions and directly predict the denotation of tables without the need to generate logical forms.         |  BERT         |

## Methodology

### 1. Abstract
The method is based on the BERT architecture and is jointly pre-trained with text passages and forms crawled on Wikipedia, followed by end-to-end training. Experimental results show that TAPAS outperforms or is comparable to existing semantic parsing models on three different semantic parsing datasets, while having a simpler model structure. In addition, the article describes the application of cross-domain migration learning, where migration from WIKISQL to WIKITQ results in higher accuracy.

### 2. Method Description 
The paper presents a model called TAPAS for processing form quizzing tasks. The model is based on the BERT encoder with additional localization embeddings added to encode the form structure. Before questions and tables are fed into the model, they need to be preprocessed and converted into a sequence. The final answer is then predicted by adding a classification layer to select cells in the table and an aggregation operation. In addition, several techniques are used to improve the model performance, such as using different positional embeddings, introducing column selection, etc.

![image](https://github.com/user-attachments/assets/44f7e16d-e7e5-472f-8991-8537f764de71)

### 3. Methodological improvements
  1. Compared to the traditional table quiz model, TAPAS uses more positional embedding to better capture table structure information.
  
  2. Also, a new column selection mechanism is introduced, which enables the model to better select the correct columns for answer computation.
 
  3. In addition, data augmentation techniques are used to expand the training set and improve the generalization ability of the model.

### 4. Issues addressed 
The model addresses some of the challenges in table quizzing tasks, such as how to select the correct cells and aggregation operations and how to capture table structure information. TAPAS performs better on several benchmark datasets compared to traditional models, proving its effectiveness and usefulness.

## Experiments
This paper presents the performance of the TAPAS model on three different semantic parsing datasets and compares it with other approaches. Specifically, the authors use three datasets, WIKITQ, SQA and WIKISQL, to test the performance of TAPAS. Among them, WIKITQ is a complex Q&A dataset, SQA is a decomposed question sequence dataset constructed based on WIKITQ, and WIKISQL is a dataset based on text-to-SQL translation.

For each dataset, the authors used standard evaluation metrics to measure the performance of the models. For example, on WIKITQ, the authors used denotation accuracy as an evaluation metric, while on SQA and WIKISQL, metrics such as sequence accuracy and average question accuracy were used.

Through the experimental results, the authors found that TAPAS performed well on these datasets, especially on WIKITQ and SQA, where TAPAS even outperformed some previous state-of-the-art methods. In addition, the authors analyzed different components of TAPAS, including table, column and row embeddings, and position and ranking embeddings, and found that table and column/row embeddings are the most important. Also, the authors explore the interactions between different modules in TAPAS and find that pre-training can significantly improve the performance of the model.

![image](https://github.com/user-attachments/assets/dc9bb6a3-4f27-4d45-88a2-12bc6e8e032a)

## Conclusion

### 1. Advantages of the Thesis
  1. **Weakly supervised training**: TAPAS can learn from large amounts of unlabeled data, which makes it easier to train.
  
  2. **Structured pre-training**: The authors used a structured pre-training approach to improve the performance of the model, which can be trained on large-scale data, thus improving the model's generalization ability.
  
  3. **Handling Multiple Problem Types**: TAPAS can handle multiple problem types, including simple selection problems and complex aggregation problems.
 
### 2. Innovative points
  1. No need to generate logical forms: while traditional semantic parsing methods usually need to convert natural language questions into logical forms in order to get the answers, TAPAS can answer the questions by extracting information directly from the forms, thus avoiding the process of generating logical forms.
  
  2. Weakly supervised training: TAPAS can improve its performance by learning from a large amount of unlabeled data, which makes it easier to train.
  
  3. Structured Pre-training: The authors used a structured pre-training approach to improve the performance of the model, this approach allows training on large scale data, which improves the generalization ability of the model.
     
### 3. Future Works
  1. Handling large tables: current TAPAS can only handle smaller tables, and more efficient algorithms and technical support are needed if larger tables are to be handled.
  
  2. Relationships between multiple tables: In real-world application scenarios, it is often necessary to deal with relationships between multiple tables at the same time, and how to deal with these relationships is an important research direction.
  
  3. Broader application scenarios: Currently TAPAS is mainly used for question and answer tasks, but it may also have application prospects in other fields (e.g., text summarization, machine translation, etc.), so its scope of application needs to be further explored. 

