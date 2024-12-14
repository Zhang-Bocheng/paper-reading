# Multi-Layer Ranking with Large Language Models for News Source Recommendation
[paper link](https://arxiv.org/pdf/2406.11745) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new task, expert recommendation, designed to identify reliable sources of information based on previously cited sources.          |  Recommendation System       |

## Methodology

### 1. Abstract
The authors build a new dataset called NewsQuote containing 23,571 quoter pairs from news articles. The authors treat the recommendation task as an expert in retrieving quotes based on the relevance of a given query to the querent and propose a multi-layer ranking framework that uses a large language model to improve recommendation performance. Experimental results show that a large language model classifier and a multilayer ranking filter based on contextual learning significantly improve the prediction quality and behavioural quality of the recommender system.

### 2. Method Description 
The source recommendation method proposed in this paper is divided into three main parts: **candidate expert retrieval, multilayer ranking filter, and large-scale language model rearrangement.** 

First, the candidate expert retrieval method searches for expert sources in news stories that can comment on the topic based on the keywords in the query and evaluates their relevance through historical citations. Second, a multilayer ranking filter utilises a large-scale language model (LLM) as a component to extend the initial candidate pool to a wider range. Finally, the average repetition frequency of each filter layer is calculated using predefined weights and the candidate with the highest weighted occurrence score is returned.

![image](https://github.com/user-attachments/assets/c26b42d5-ace8-44d9-8214-ffe97bdb51f9)

### 3. Methodological improvements
Compared to traditional probabilistic base methods, the method proposed in this paper overcomes the limitations of the document corpus, making it more flexible in dealing with unknown topics. In addition, by introducing a large language model, the method improves the performance of the recommender system.

### 4. Issues addressed 
This method addresses the problem of finding reliable sources of information related to a query in a news recommender system. By taking into account the conditional independence and relevance of the query and the candidates, the method is able to effectively identify and rank the sources that are most likely to provide relevant information.

## Experiments
This paper focuses on experiments for recommending information sources in news stories and conducts several comparative experiments to evaluate the effectiveness of different approaches.

Firstly, the authors use different methods to recommend information sources using documents in the training set as a database and article titles in the test set as queries. Among them, the Document-based Retrieval method performs better than the Candidate-based Retrieval method, with 7% to 8% higher recall, average precision and NDCG@10 score. Additionally, the authors experimented with methods using GPT-3.5-Turbo and GPT4-Turbo as LLM rankers and combined them with multilayer ranking filters to further improve recommendation results.

![image](https://github.com/user-attachments/assets/6271450b-86da-47ae-b8c0-ef16d45a4ab1)

Next, the authors provide a detailed analysis and summary of the results of each experiment. For different evaluation metrics, such as recall, average precision, NDCG@10, etc., the authors give specific scores and explain their results. For example, when using GPT-4 as an LLM ranker, the MAP and NDCG@10 scores improved by 2%, but the recall did not improve significantly. This may be due to the fact that GPT-4 has a more advanced knowledge base and recall is more affected by random generation.

![image](https://github.com/user-attachments/assets/bc51caff-5553-47cb-9ff5-88532eeb9476)

In addition, the authors focused on the diversity and comprehensiveness of the recommendation results. By applying a multi-layered ranking filter, the authors found a significant decrease in the popularity of recommendations, suggesting that the method is able to avoid over-reliance on popular sources. However, this approach may sacrifice some ranking precision to improve recall and mitigate popularity bias.

Finally, the authors point out that the experimental results may be underestimated. Because the number of sources cited in actual news stories is small, uncited sources may also be valuable and deserve higher scores. 

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents an expert recommendation system based on news articles that is able to identify credible sources of information based on query information.
  2. The authors use a pre-trained Large Language Model (LLM) to enhance the recommendation capability of the system and demonstrate the effectiveness and accuracy of this approach in experiments.
  3. The construction process of the dataset is described in detail in the paper, including steps such as de-weighting, keyword extraction, and entity recognition, which allows the researcher to better understand the characteristics and quality of the dataset.
 
### 2. Innovative points
  1. This paper presents a novel dataset, NEwsQuoTE, which contains quotes from news articles and their sources, which provides an important basis for expert recommendation tasks.
  2. In traditional recommender systems, only the user's interest preferences are usually taken into account, whereas in this paper, historical quotes are used as inputs, which improves the accuracy and reliability of recommendations.
  3. By introducing a multi-layer ranking filtering mechanism, this paper further improves the performance of the recommender system and also mitigates the effect of popularity bias.

### 3. Future Works
  1. It can try to use more text features to improve the accuracy of the recommender system;
  2. It can explore how to enrich the dataset by using external data sources, such as social media;
  3. and lastly, It can consider how to apply the system to a wider range of domains, such as finance and healthcare.    
