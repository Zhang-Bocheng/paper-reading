# Predicting Dynamic Embedding Trajectory in Temporal Interaction Networks
[paper link](https://arxiv.org/pdf/1908.01207) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 | This paper introduces a model called JODIE for predicting the dynamic trajectories of users and items in the embedding space.         |  recurrent neural networks         |

## Methodology

### 1. Abstract
The model uses two recurrent neural networks to update the user's embedding at each interaction and introduces a projection operator to estimate the user's embedding at any future point in time. With this approach, future user-item interactions can be predicted and state change predictions can be made. Experimental results show that JODIE outperforms six state-of-the-art algorithms in predicting future interactions and state changes.

![image](https://github.com/user-attachments/assets/ac976e45-ff5d-4a88-b77d-76dcea290d89)

### 2. Method Description 
The JODIE algorithm proposed in this paper is a method for learning the dynamic embedding trajectories of users and items. The algorithm uses two mutually recursive RNNs to update the dynamic embeddings of users and items, and predicts future interactions through projection operations.

JODIE combines the static embeddings of users and the dynamic embeddings of items to better capture long-term relationships and short-term behavioral changes between users and items. During training, JODIE uses batch processing techniques to maintain temporal order and optimizes model parameters by minimizing prediction error and regularization loss.

![image](https://github.com/user-attachments/assets/314b54e2-64bf-4dc3-8aad-f7ef7a5f9371)

### 3. Methodological improvements
  1. In contrast to existing RNN-based methods, JODIE employs a novel projection operation to predict future trajectories of user behavior, rather than simply keeping the user embedding unchanged.
  
  2. In addition, JODIE directly predicts the embedding vector of the next item instead of calculating the probability of interaction between the user and the item. This design allows JODIE to make recommendations more efficiently and has faster speed in inference.

### 4. Issues addressed 
JODIE reduces the computational effort by predicting the embedding vectors of users and items, and avoids overfitting by regularizing the loss. Experimental results show that JODIE has better recommendation results and faster training speed than existing methods.

## Experiments
This paper presents the results of the experimental validation of the JODIE algorithm on two tasks and compares them with six strong baselines. The experiments include two tasks, **future interaction prediction and user state change prediction**, which were tested using three different datasets. The experimental results show that JODIE significantly outperforms all the baseline methods on all datasets, with an average ranking of at least 20% higher than the best baseline method in the future interaction prediction task and an average recall of at least 12% higher than the best baseline method in the user state change prediction task. In addition, JODIE has a fast runtime speed and robustness to training data scale and embedding dimension size.

![image](https://github.com/user-attachments/assets/203ee66b-2063-4f25-ba95-1b4f47065c79)

## Conclusion

### 1. Advantages of the Thesis
  1. The model accomplishes this by using an update operation, which consists of two RNNs to generate embeddings of users and items, and a projection operation to predict future embedding trajectories of users.
  
  2. Additionally, the paper proposes a new batch algorithm called t-Batch that creates independent but time-consistent batches of data as training data, resulting in JODIE that is 9.2 times faster than the closest baseline.
  
  3. Finally, experimental results show that JODIE outperforms six state-of-the-art algorithms in predicting the next user interaction and predicting user state changes.

### 2. Innovative points
  1. The methodological innovation of this thesis is the proposed JODIE model, which is a coupled RNN model for learning the dynamic embedding trajectories of users and items and accurately predicting future user interactions and user state changes.
  
  2. The model achieves this by using an update operation, which consists of two coupled RNNs to generate user and item embeddings, and a projection operation to predict future embedding trajectories of users.
  
  3. In addition, the paper proposes a new batch algorithm, t-Batch, which creates independent but temporally consistent batches of data as training data, resulting in a JODIE that is 9.2 times faster than the closest baseline.

### 3. Future Works
Future research directions include learning the trajectories of groups of users to reduce the number of parameters, and clustering entity trajectories to identify similar entities. Also, designing new items to be recommended to many users based on missing predictors is a promising direction.  
