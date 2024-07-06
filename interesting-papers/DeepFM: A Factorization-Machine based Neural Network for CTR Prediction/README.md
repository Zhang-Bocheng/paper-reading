# DeepFM: A Factorization-Machine based Neural Network for CTR Prediction
[paper link](https://arxiv.org/pdf/1703.04247) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2017 | This paper presents a neural network model called DeepFM that combines the advantages of factorization machines and deep learning.         | Neural Network           |

## Methodology

### 1. Abstract
  The model emphasizes both low- and high-order feature interactions and does not require any feature engineering beyond the original features. Compared with Google's latest Wide& Deep model, DeepFM is better and more efficient in CTR prediction. The authors experimentally demonstrate the effectiveness and efficiency of DeepFM and apply it to business data.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/a17b574b-4795-4a00-a81d-c00042d7b864)

### 2. Method Description 
  The DeepFM proposed in this paper is a neural network and factorizer-based model for CTR prediction tasks. The model consists of two components: the FM component, which uses factorization machines to learn low-order interactions between features and is able to handle sparse data, and the Deep component, which uses a multilayer perceptron to capture high-order feature interactions. The two components share the same input vectors and combine their results through a fully connected layer. The final prediction is computed using a sigmoid function.
  
### 3. Methodological improvements
  1. **No pre-training required**: DeepFM does not require a pre-training process and therefore can converge faster compared to other similar models such as FNN.
  
  2. **Does not require domain expert knowledge**: DeepFM does not require domain expert knowledge for feature engineering as it automatically learns useful feature representations from raw features.
  
  3. **Able to handle sparse data**: Thanks to the FM component, DeepFM is able to handle sparse data efficiently, which is not possible with many other models.
     
### 4. Issues addressed 
  CTR prediction is an important problem that is widely used in areas such as ad recommendation and search engine ranking. However, CTR prediction faces some challenges, such as:

  1. **Large number of features**: In CTR prediction, there are usually thousands of features, most of which are sparse.
     
  2. **Complex interactions between features**: There may be complex interactions between different features, and these interactions are crucial for prediction accuracy.
  
  3. **Need for fast and accurate predictions**: CTR predictions often require real-time or quasi-real-time response times to be able to provide the best user experience in the shortest possible time.
     
DeepFM addresses these issues by making CTR prediction more accurate and efficient by taking into account both low- and high-order feature interactions and automatically learning useful feature representations.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/c5ee50fd-09b2-48a6-bf65-b9d58c086e28)

## Experiments
  This paper focuses on the performance of DeepFM model in the CTR prediction task and compares it with nine other models. The experimental data comes from two datasets, Criteo and Company, and the evaluation metrics are AUC and Logloss. The experimental results show that DeepFM outperforms the other models in terms of efficiency and effectiveness, with the AUC on the Criteo dataset improving by 0.86% and the Logloss decreasing by 4.18%, and on the Company dataset the AUC improving by by 4.18% and Logloss by 5.60% on the Company dataset. 
  
  In addition, this paper also tunes the parameters of DeepFM, including activation function, dropout rate, number of neurons, number of hidden layers and network shape. Through experiments, it is found that relu is a more suitable activation function for deep models, the dropout rate should be set between 0.6 and 0.9, the number of neurons should be between 200 and 400, the number of hidden layers should not be too many, and the constant shape network structure is the optimal choice.
  
  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/5d360c84-580b-4a5e-94c7-0fddf770a872)

## Conclusion

### 1. Advantages of the Thesis
  The paper proposes a new neural network model, DeepFM, which combines the architectures of FM and DNN, and is able to learn both low-order and high-order feature interactions without any feature engineering. Compared with the existing Wide&Deep model, DeepFM has higher efficiency and better performance performance. Experimental results show that DeepFM outperforms existing models in both AUC and Logloss metrics on two real datasets.
  
### 2. Innovative points
   DeepFM is a hybrid model based on FM and DNN, which achieves the learning of feature interactions by jointly training the depth part and the breadth part. Compared with existing models, the main innovation of DeepFM is that it can learn both low-order and high-order feature interactions without any feature engineering. In addition, DeepFM is designed with shared embedding vectors, which makes its input vectors smaller, thus improving the training efficiency.
   
### 3. Future Works
  Future research directions include exploring strategies (e.g., introducing pooling layers) to enhance the ability to learn the most useful higher-order feature interactions, and training DeepFM on GPU clusters to solve large-scale problems.
