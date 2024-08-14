# RippleNet: Propagating User Preferences on the Knowledge Graph for Recommender Systems
[paper link](https://arxiv.org/pdf/1803.03467) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2018 |  This paper presents a framework called RippleNet for propagating user preferences in a knowledge graph to improve recommender system performance.          | Knowledge Graph         |

## Methodology

### 1. Abstract
Traditionally, researchers have used side information such as social networks or item attributes to address sparsity and cold-start problems in collaborative filtering. This paper considers knowledge graphs as a source of side information and naturally incorporate them into recommender systems by automatically and iteratively expanding users' latent interests along links in the knowledge graph. Experimental results show that RippleNet achieves significant improvements over multiple baseline models in a variety of scenarios such as movie, book, and news recommendations.

![image](https://github.com/user-attachments/assets/8302f16c-daa5-4c8b-8a4c-b7f26c4e4467)

### 2. Method Description 
This paper proposes a knowledge graph-based recommender system that combines the user-item interaction matrix and the entity-relationship triples in the knowledge graph to predict the user's interest level in untouched items. Specifically, the system constructs a user-item interaction matrix using the user's historical behavioral data and enriches the feature representations of the items using the entity information associated with the items in the knowledge graph. Then, personalized recommendation is achieved by learning a prediction function that maps the user's interest degree into a probability space.

![image](https://github.com/user-attachments/assets/45eff0ec-6124-4274-a2f3-38fac81d6c96)

### 3. Methodological improvements
Compared with the traditional collaborative filtering or content recommendation based methods, this method is improved in the following aspects:

  1. utilizes the entity-relationship information in the knowledge graph, which is able to better capture the semantic similarity and relevance between items.
  
  2. For new users or cold-start problems, this method can utilize the existing entity information in the knowledge graph to infer the user's preference, thus improving the recommendation effect.
  
  3. During model training, a gradient descent based optimization algorithm is used to converge faster and achieve better performance.
     
### 5. Issues addressed 
  1. How to utilize the entity relationship information in the knowledge graph to enhance the accuracy of the recommender system?
  
  2. How to deal with the new user or cold start problem so that the recommender system can make reasonable recommendations even in the absence of historical data?

## Experiments
This paper focuses on RippleNet, a knowledge graph-based recommender system, and conducts comparative experiments with traditional collaborative filtering methods and matrix decomposition-based methods. In the experiments, the authors use two public datasets for evaluation, **MovieLens and LastFM**. where MovieLens is a movie rating dataset, including users' rating information of movies and basic attribute information of movies; while LastFM is a music social network platform, including users' listening records and basic attribute information of songs.

  1. the authors compared **RippleNet with two other traditional recommendation algorithms**. The results show that on the MovieLens dataset, RippleNet has better performance relative to the collaborative filtering approach and the matrix decomposition-based approach, with lower mean absolute error (MAE) and root mean square error (RMSE). And on the LastFM dataset, RippleNet also performs better relative to the other two methods, but the gap is not as significant as on the MovieLens dataset.

  2. the authors also **conducted experiments for different parameter settings to explore the performance variation of the RippleNet model**. Specifically, the authors adjusted hyperparameters such as the maximum hop number H and the negative sampling ratio and evaluated them. The results show that the performance of RippleNet improves when H increases, but the performance enhancement diminishes as H increases further. In addition, the performance of RippleNet decreases when the proportion of negative sampling is high.

  3. the authors also **demonstrate the prediction process of RippleNet through visualization**. They plotted the relationship between the items of a user's historical clicks and compared it with the related items predicted by RippleNet. The results show that RippleNet is able to accurately capture users' potential points of interest and give relevant recommendations.

 ![image](https://github.com/user-attachments/assets/e362179d-7d3f-4b5f-b30d-0b568cafb091)
    
## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new recommender system framework, RippleNet, that naturally incorporates knowledge graphs into recommender systems and automatically explores users' latent and hierarchical interests through preference propagation.
  
  2. The strength of the paper is that it proposes a novel approach to solve the KG-aware recommendation problem, while proving its effectiveness through experiments.
  
  3. In addition, the paper explains and discusses the design idea of RippleNet in detail, enabling readers to better understand how the method works.

![image](https://github.com/user-attachments/assets/58b13c70-b3e1-4ed5-b405-0df5979f9e17)

### 2. Innovative points
  1. The main innovation of the paper is the concept of preference propagation, which is a recommendation strategy based on users' historical behavior and knowledge graph.
  
  2. The method not only automatically discovers a user's potential interests, but also predicts the items that the user may be interested in based on the user's click history and the entity relationships in the knowledge graph.
  
  3. In addition, the paper introduces a KGE loss function to constrain the learning process of the model, which improves the generalization ability of the model.

### 3. Future Works
  1. Problems such as data sparsity and cold start may be encountered in practice, which require further research and improvement.
  
  2. In addition, the paper also mentions some directions for future research, such as designing non-uniform samplers to better explore users' potential interests.
 
  3.  All these directions are expected to promote the further development of the KG-aware recommendation field. 
