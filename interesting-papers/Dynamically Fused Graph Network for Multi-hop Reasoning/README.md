# Dynamically Fused Graph Network for Multi-hop Reasoning
[paper link](https://arxiv.org/pdf/1905.06933) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 | This paper introduces a new method called DFGN for answering questions that require multiple scattering of evidence and reasoning.         | Graph Networks          |

## Methodology

### 1. Abstract
  Most existing textual quizzing methods focus only on finding answers in a single passage, but many puzzles require multiple supporting evidence from two or more texts.DFGN achieves stepwise inference through a dynamic fusion layer that starts from entities in a given query, explores along dynamically constructed entity graphs in the text, and progressively finds the relevant supporting entities from a given document. Experimental results show that DFGN achieves competitive results with public boards on the HotpotQA dataset and produces interpretable inference chains.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/565134e9-6cd0-4284-93ef-eded117859dc)

### 2. Method Description 
  The Dynamic Fusion Graph Network (DFGN) proposed in this paper is a question and answer system based on human reasoning process. The system consists of five components: a paragraph selection subnetwork, an entity graph building block, a coding layer, a multi-step inference block, and a final prediction layer. Among them, the passage selection sub-network uses a pre-trained BERT model to select passages relevant to the question; the entity graph building module utilizes the Stanford CoreNLP toolkit to identify named entities extracted from the context and builds the entity graph in three ways; the coding layer stitches together the query and context and passes them to the pre-trained BERT model to obtain a representation; the multi-step inference block on the other hand, mimics human one-step reasoning behavior and is implemented through three processes, Tok2Ent, Dynamic Graph Attention, and Graph2Doc; and the final prediction layer uses an LSTM structure with four output dimensions to make predictions.

### 3. Key Concepts
  _Text-based Question Answering (QA)_: A NLP task where a system is designed to answer questions posed by users based on a provided text corpus. The goal of text-based QA systems is to comprehend the meaning of the questions and extract relevant information from the text to generate accurate answers.
  
### 4. Methodological improvements
 Compared to traditional Q&A systems, DFGN has been improved in the following three areas:

  1. An entity graph building module is introduced, enabling the system to better understand entity relationships in context;
  
  2. Adopting a multi-step reasoning mechanism with three processes, Tok2Ent, Dynamic Graph Attention and Graph2Doc, which is closer to the human reasoning process;
  
  3. Weakly supervised signaling is introduced in the prediction layer to improve the performance of the system.
     
### 5. Issues addressed 
  DFGN aims to address some of the problems in traditional Q&A systems, such as the lack of ability to understand entity relationships in context, the inability to simulate human reasoning processes, and the difficulty in optimizing system performance. By introducing an entity graph building block, a multi-step reasoning mechanism, and weakly supervised signals, DFGN can better deal with these problems and thus improve the accuracy and efficiency of Q&A systems.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/b0579b0e-4bfa-4670-9999-9fb3920f9f8c)

## Experiments
  This paper focuses on the experiments conducted by the authors on the HotpotQA dataset and compares them with other models. The experiment consists of four parts:

  **Experimental setup and implementation details**: the authors used the BERT tokenizer to encode paragraphs and questions, the Stanford CoreNLP Toolkit to extract named entities to construct entity graphs, and the pre-trained BERT model as encoder and decoder. In the experiments, the authors used a lower threshold to select support facts to maintain high recall and reasonable precision.

  **Main Results**: The authors compared their proposed DFGN with benchmark models and other unpublished models and achieved the second best results. In addition, the authors improved the model performance by modifying the way entities are recognized in the entity graph.

  **Ablation study**: The authors conducted an Ablation study of model components and dataset fragments and found that each component provides a relative improvement of 1% to 2% and that multi-layer fusion blocks can significantly improve model performance.

  **Graph structure analysis**: the authors evaluate the quality of graph structures and propose two metrics, ESP EM and ESP Recall, to assess the quality of multi-hop inference. The authors also show how the model works and its limitations through a case study.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/e75e8a5f-d6fe-447e-9598-fa9c5bed13c3)

## Conclusion

### 1. Advantages of the Thesis
 This paper proposes a new multi-hop text-based Q&A method, DFGN, which can effectively filter out useless information and extract useful information, as well as solve the inference problem in open-domain problems.DFGN uses dynamic entity graphs to support multistep inference, and predicts the mask of the entity graphs at each inference step to eliminate irrelevant entities. In addition, DFGN proposes a fusion process that combines document information with entity diagram information to improve the accuracy of the answer. Finally, the authors provide a method for interpreting and evaluating inference chains.
 
### 2. Innovative points
  The main innovation of DFGN is that it uses dynamic entity graphs for multi-step reasoning and a mask prediction module to filter out irrelevant entities. In addition, DFGN introduces a fusion process that combines document information with entity diagram information, thus improving the accuracy of the answers. These innovations enable DFGN to achieve better results in open domain problems.
  
### 3. Future Works
  1. Further exploration could be done on how to better construct entity maps and how to predict masks more accurately.
  
  2. And, combining DFGN with other models can be considered to improve its performance.

In conclusion, DFGN provides new ideas and methods for multi-hop text quizzing, which has a wide range of application prospects.
