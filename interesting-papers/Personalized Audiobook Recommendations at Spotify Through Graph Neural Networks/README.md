# Personalized Audiobook Recommendations at Spotify Through Graph Neural Networks
[paper link](https://arxiv.org/pdf/2403.05185) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents an approach to personalised recommendation using graph neural networks to improve the quality of recommendations for audio books on the Spotify platform.           | Graph Neural Networks (GNNs)         |

## Methodology

### 1. Abstract
Since audio books are a newly introduced content type that users know little about, a model that can quickly and accurately provide users with relevant recommendations is needed. This approach achieves an efficient recommendation system by combining user preferences for music and podcasts and using a heterogeneous graph neural network (HGNN) and a two-tower (2T) model. 

Experimental results show that this approach significantly improves the quality of personalised recommendations, resulting in a 46% increase in new audio book starts and a 23% increase in streaming playback rates. Moreover, the impact of this model is not limited to audio books, but also positively affects existing products such as podcasts.

### 2. Method Description 
The paper proposes a model called 2T-HGNN to solve the problem in recommender systems. The model consists of two parts: the Heterogeneous Graph Neural Network (HGNN) and Two Towers (2T). First, HGNN is used to learn relationships between audio books and podcasts and embed them into a common space. Then, 2T uses these embedding vectors to compute the similarity between a user and an audio book, and provides personalised recommendations to the user based on this similarity.

Specifically, HGNN captures user preferences for audio books and podcasts by constructing a co-listening graph and generating a low-dimensional representation using a multilingual Sentence-BERT model. It then uses a graph convolutional neural network called GraphSAGE to update node features and generate embedding vectors. Finally, the number of different types of edges is balanced by designing a multi-link neighbour sampler to avoid bias during training.

In 2T, the authors used two towers dealing with user and audio book features respectively. For the user tower, it takes into account demographic information such as age and country of the user as well as the user's historical interactions with music, podcasts and audio books. For the audio book tower, on the other hand, metadata of audio books, such as language and genre, and HGNN embedding vectors of audio books are used. Finally, by minimising the distance loss function between users and audio books, 2T can generate personalised recommendation lists.

![image](https://github.com/user-attachments/assets/7f8d9404-9a36-44f4-a9cb-0cd4522f8230)

### 3. Methodological improvements
  1. The ability to take into account the content features of both audio books and podcasts, thus better capturing user preferences.
  
  2. Ability to automatically learn relationships between audio books and podcasts without having to manually define correlations.
  
  3. Can handle sparse data, since audio books typically have fewer interactions.

  4. In addition, 2T-HGNN can avoid the problem of unbalanced data distribution through multi-linked neighbourhood samplers and can be trained on different time scales to improve efficiency and accuracy.
     
### 4. Issues addressed 
The main goal of the 2T-HGNN model is to provide personalised recommendation services to users. Since the relationship between audio books and podcasts is usually unknown, traditional collaborative filtering algorithms and content-based recommendation algorithms may not be able to capture user preferences well. The 2T-HGNN model, on the other hand, is able to take into account the content characteristics of both audio books and podcasts and automatically learn the relationship between them to better satisfy users' needs. In addition, since audio books usually have fewer interactions, 2T-HGNN is also able to handle sparse data, which improves the accuracy and efficiency of the recommender system.

## Experiments
This paper presents the authors' experiments on optimising an audio book recommendation system using a multi-hop graph neural network (HGNN) model. In an offline evaluation, the authors compare four different recommendation algorithms and evaluate their performance through three standard metrics (HR@K, MRR, and coverage). The results show that using the HGNN model significantly improves recommendation results, especially for cold-start users and long-tail recommendations.

Next, the authors conducted an online A/B test, applying the HGNN model to the ‘Audiobook for you’ page on the Spotify platform, and compared it with existing production recommendation systems. The results show that the HGNN model significantly increases new user initiation and streaming rates, while the 2T model has a relatively weak effect.

Overall, this paper shows how the HGNN model can be used to optimise an audio book recommender system and validates its effectiveness through offline evaluation and online A/B testing. These experimental results help improve the performance of existing recommender systems and provide a reference for future research on recommender systems.

![image](https://github.com/user-attachments/assets/1a1621ec-2fed-4174-a271-ced86c704b26)

![image](https://github.com/user-attachments/assets/4be809cf-e9f9-4e80-9bdc-e4005c3b414a)

## Conclusion

### 1. Advantages of the Thesis
  1. The system offers advantages in solving the cold-start problem, data scarcity and scalability, and improves prediction accuracy by using implicit signals.
  
  2. In addition, the authors introduce a balanced sampler to optimise HGNN training and reduce training time.
 
### 2. Innovative points
  1. The main contribution of the paper is to propose a modular recommender system architecture that combines the advantages of HGNN and 2T models. HGNN is used to capture complex relationships between items, while 2T models are able to provide scalable recommendation services for all users.
  
  2. In addition, the paper exploits the user's consumption behaviour of podcasts to understand the user's audiobook preferences and uses weak signals to augment the user representation. These innovative approaches make the system outperform other alternatives.
     
### 3. Future Works
In future research, new techniques and algorithms need to be further explored to meet the needs of different users and to continuously improve the performance and user experience of the recommender system.  
