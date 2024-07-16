# Jointly Learning Explainable Rules for Recommendation with Knowledge Graph
[paper link](https://arxiv.org/pdf/1903.03714) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 | This thesis focuses on how to achieve both interpretability and effectiveness in recommender systems.     | Neural Networks         |

## Methodology

### 1. Abstract
Most of the traditional recommendation methods focus only on improving the prediction accuracy, ignoring the need for model interpretability. The authors propose a novel learning framework that combines rule learning from knowledge graphs with NN recommendation models to achieve effective and easy-to-understand recommendation results. Experiments show that the approach achieves significant improvements on real datasets and is robust to "noisy" knowledge graphs.

![image](https://github.com/user-attachments/assets/2e1eb6b2-d9de-4714-b796-4980d6025608)

### 2. Method Description 
This paper propose a recommendation system framework based on rule learning, including two modules: **rule learning module and recommendation module**. In the rule learning module, a randomized wandering algorithm is used to compute the probability of rules in a given item association and convert these rules into feature vectors. Then, the global rule set is constructed by selecting useful rules. In the recommendation module, the derived rule features are utilized to enhance the recommendation performance and the recommendation results can be interpreted.

![image](https://github.com/user-attachments/assets/06f0db5c-3095-4ae2-8ee4-59f91b7aa2c7)

### 3. Methodological improvements
Unlike traditional recommender systems, this method introduces the concept of rule learning, which makes the recommendation results more interpretable. At the same time, it combines the rule learning and the learning of the recommendation model through multi-task learning, which improves the effectiveness of the model.

### 4. Issues addressed 
The method solves the problem that traditional recommender systems have difficulty in interpreting the recommendation results, and also improves the accuracy and efficiency of the recommender system. In addition, the method is applicable to many types of recommendation models with high flexibility and scalability.

## Experiments
  This paper focuses on a knowledge graph-based recommender system and conducts several comparative experiments to validate its performance and effectiveness. Specifically, this paper uses two open datasets (Amazon Cellphone and Amazon Electronic) to conduct the experiments and employs multiple evaluation metrics to measure the performance of the recommender system. Also, this paper compares the performance of traditional matrix decomposition methods, NN methods, and knowledge graph-based methods in different domains, and draws the following conclusions from multiple sets of experiments:

  1. Knowledge graph-based methods can effectively improve the performance of recommender systems and perform well in tests in different domains;
  
  2. Multi-task learning is more effective than two-step learning and can better utilize the interaction between rule selection and recommendation models;
  
  3. The need to consider the limitations of entity types when using knowledge graphs in order to avoid introducing irrelevant entities;
  
  4. Different association types have different impacts on the recommendation results, so appropriate association types should be selected for different domains and user needs;
  
  5. For the recommendation of a single user, the most suitable set of rules can be selected based on the user's historical behavior and preferences, so as to improve the recommendation effect.
     
  ![image](https://github.com/user-attachments/assets/903f8599-43ab-4b6f-bd9f-d0b5fb6e9bd8)

  ![image](https://github.com/user-attachments/assets/3a4ed1a3-adc0-47ef-b24e-8680a51de5ca)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a novel and effective joint optimization framework for extracting rules from the knowledge graph and making recommendations based on these rules.

  2. The framework consists of two modules: a rule learning module and a recommendation module. The rule learning module is able to derive useful rules from different types of item associations, while the recommendation module introduces rules into the recommendation model to improve performance.
  
  3. The paper uses Freebase, a large-scale knowledge graph, to learn rules and can be used in conjunction with different recommendation algorithms, such as the classical matrix decomposition algorithm BPRMF and the state-of-the-art NN recommendation algorithm NCF.
  
  4. The effectiveness of the framework is demonstrated by experimental evidence that the proposed four augmented rule recommendation algorithms achieve significant results in several domains and outperform all benchmark models.
  
  5. In addition, the obtained rules are able to explain why we recommend an item to a user, thus improving the interpretability of the recommendation model.
     
### 2. Innovative points
  1. The thesis utilizes item association information from the knowledge graph to extract rules that make recommendation results more accurate and interpretable.
  
  2. The thesis proposes a joint optimization framework that can improve performance in learning rules and recommendation models simultaneously.
  
  3. The paper also used a multi-task learning approach to combine rules from different sources to further improve the recommendation results.

### 3. Future Works
  In future research, the authors plan to explore how to design a combinatorial algorithm that combines embedded learning in order to maintain the interpretability of the recommendation results and the information of the knowledge graph.
