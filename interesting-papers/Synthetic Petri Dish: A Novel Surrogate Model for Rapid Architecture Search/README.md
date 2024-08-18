# Synthetic Petri Dish: A Novel Surrogate Model for Rapid Architecture Search
[paper link](https://arxiv.org/pdf/2005.13092.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a new model called “synthetic petri dish” for accelerating the most expensive step in the Neural Network Architecture Search (NAS) process - training and evaluating each architecture on a real dataset.         | Neural Network          |

## Methodology

### 1. Abstract
The model predicts the performance of different architectures by instantiating them in very small networks and evaluating them using a small number of synthetic data samples. Unlike traditional neural network-based prediction models, the synthetic petri dish is trained on real architectures to predict their performance, so that predictions can be inferred from their true intrinsic properties. Experiments show that synthetic petri dishes can significantly improve prediction accuracy for new architectures, especially in the absence of real data. This work provides a new research direction for exploring the performance of model components aimed at optimizing synthetic diagnostic environments to provide informative evaluations.

![image](https://github.com/user-attachments/assets/a3c419ac-c5a7-4d70-a0a3-16e0bfa3c0dd)

### 2. Method Description 
This study proposes the Synthetic Petri Dish (SPD) method, which aims to create a miniature environment training model that allows the performance of small-scale patterns in it to be a good predictor of their performance in real evaluations. The main idea of the SPD method is to extract a number of sub-modules from a real network and put them into a small network for training and evaluation. This data is then used to optimize the synthetic data for SPD in order to better simulate the training and evaluation process in real situations.

![image](https://github.com/user-attachments/assets/0b52758f-2818-43e7-8632-740ae2e8dcec)

### 3. Methodological improvements
Compared to traditional search-based methods, the SPD method can search for optimal architecture combinations more efficiently by introducing the concept of Petri nets. Meanwhile, the SPD method also utilizes the technique of data augmentation, which increases the diversity of data by transforming the original data, thus improving the generalization ability of the model.

### 4. Issues addressed 
The method solves two main problems: first, how to search for the optimal architecture combinations efficiently; second, how to improve the generalization ability of the model. By using the SPD method, the optimal architecture combinations can be searched quickly on smaller datasets, and the generalization ability of the model can be further improved by data enhancement techniques. This method is of great significance for the design and optimization of large-scale NN.

## Experiments
This paper describes two experiments on the task of searching for the optimal slope of a sigmoid activation function and architectural search for use as a recursive unit. 
<br>&emsp;In the first experiment, the authors used a synthetic Petri dish to predict the network performance corresponding to different sigmoid slopes and compared it to a NN model. The results show that synthetic petri dishes can more accurately predict the effect of sigmoid slope on network performance.
<br>&emsp;In a second experiment, the authors combined the synthetic petri dish with a genetic algorithm and a neural architecture optimizer to accelerate the architecture search for recursive units. The results show that this approach can discover high-performance recursive unit architectures with a limited number of data points.

![image](https://github.com/user-attachments/assets/a0a0a480-d71d-4201-a3aa-69a57beb79e7)

## Conclusion

### 1. Advantages of the Thesis
  1. By using the method of learning synthetic data, the training cost of real networks is reduced to an acceptable level and a large number of experiments can be done in a short period of time.
  
  2. Since Synthetic Petri Dish runs in a simplified environment, it is better able to capture key factors in real networks, thus improving the accuracy of predictive models.
  
  3. Compared to traditional black-box models, Synthetic Petri Dish is able to provide more prior knowledge, which is extracted from real networks, and can help improve the accuracy of prediction results.

### 2. Innovative points
  1. Utilizing machine learning techniques to extract key factors from real networks and applying them to Synthetic Petri Dish to help speed up network architecture search.
  
  2. Simple activation functions such as sigmoid are used in Synthetic Petri Dish to better understand the behavior of the network and extract useful prior knowledge from it.
  
  3. The effectiveness and feasibility of this approach is demonstrated by evaluating the performance of Synthetic Petri Dish.

### 3. Future Works
  1. how to apply this method on more complex tasks is still an issue. 
  
  2. how to further improve the performance of Synthetic Petri Dish is also an important research direction.
  
  3. In conclusion, future research should continue to explore and develop this novel neural network architecture search method to help solve the challenges and problems currently faced.
