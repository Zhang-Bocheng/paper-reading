# Distilling the Knowledge in a Neural Network
[paper link](https://arxiv.org/pdf/1503.02531) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2015 |  This paper describes a method to improve the performance of machine learning algorithms by compressing the knowledge of multiple models into a single model.          |  Machine Learning (ML)       |

## Methodology

### 1. Abstract
This approach can be achieved by training several different models and averaging their predictions, but using the entire integrated model for prediction may be too cumbersome and computationally intensive. Therefore, the authors propose another technique for compressing knowledge and experiment on the MNIST dataset with surprising results. 

In addition, they show how the acoustic model of a commercial system can be significantly improved, thus increasing its performance. The authors also introduce a new hybrid model consisting of one or more full models and a number of specialised models that can be trained quickly and in parallel to discriminate between tiny categories confounded by the full model.

### 2. Method Description 
The paper proposes a NNs knowledge transfer method called ‘distillation’. In this method, knowledge from a larger, complex model (called a ‘bulky model’) is transferred to a smaller, simpler model (called a ‘lightweight model’). This process is achieved by training the lightweight model to learn probability distributions similar to those of the bulky model. Specifically, the logits of the bulky model are converted to a probability distribution using a softmax function at high temperature and passed as a soft label to the lightweight model. The lightweight model is then trained by minimising the cross-entropy loss between the two. Eventually, when the lightweight model is trained, its softmax temperature is reduced to 1 for more accurate results.

### 3. Methodological improvements
One of the methods is to use not only soft labels but also take the correct labels into account when training the lightweight model. Specifically, two different objective functions can be used: **one based on soft labels and the other based on correct labels**. By weighted averaging these two objective functions, better results can be obtained. What is more, the softmax output of the lightweight model can be normalised to ensure that the gradient produced is relatively constant across temperatures.

### 4. Issues addressed 
The method of distillation addresses the problem of knowledge transfer in NNs. The distillation method does not require such a priori knowledge, and it can directly use the knowledge of existing large models to train small models, thus simplifying the process of transfer learning. Therefore, the distillation method requires only a small amount of data to complete the knowledge transfer, it can also be applied in data-scarce situations.

## Experiments
This paper presents three sets of comparison experiments:

The first set of experiments**compares the effects of training models using soft and hard labels on the MNIST dataset**. The authors trained a NN with two hidden layers and compared it to a single large neural network trained using hard labels. The results showed that using soft labels reduced the test error from 67 to 74, whereas using hard labels only reduced the test error to about 146. This suggests that soft labels are better able to transfer knowledge to the student model, including translating categories that are not present in the dataset.

![image](https://github.com/user-attachments/assets/177b0242-7e85-4fdc-abfd-8d7e4c4dbba9)

The second set of experiments was **conducted on an internal Google dataset, JFT, for a speech recognition task**. The authors used a DNN with 8 hidden layers to predict HMM states, trained with a relatively small dataset and using 10 different models to make predictions. They then trained a new single model using the average predictions of these models as soft labels. The results show that the new model performs better than the separate models in terms of both frame classification accuracy and WER, achieving an improvement of about 80%. This suggests that using soft labels can improve model performance, especially when using multiple models.

![image](https://github.com/user-attachments/assets/64129413-a016-4bf4-8593-d31fe1ca3acf)

The third set of experiments was **conducted on a larger dataset to explore how large models can be trained using less data**. The authors used an approach called ‘expert’, which involves training a specialised model for each category, rather than a generic model. They find that this approach reduces the number of parameters that need to be trained while maintaining accuracy. And, they show how soft labelling can be used to prevent overfitting and recover most of the information in small samples. They also compared this technique to a hybrid expert system and found that using multiple independent expert models is easier to parallelise, thus increasing efficiency.  

![image](https://github.com/user-attachments/assets/f05f0548-45f0-4209-8210-6e787450917a)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new approach to ML model training, ‘knowledge distillation’, which improves the performance of small models by transferring knowledge from large models to small ones.
  2. The researchers used a variety of experiments to validate the effectiveness of this method and achieved good results on multiple datasets.
  3. The paper describes in detail the exact implementation of the method and proposes multiple improvement strategies to further enhance model performance.
  
### 2. Innovative points
  1. The ‘knowledge distillation’ method proposed in this study is a new ML model training method, which can improve the performance of small models by transferring knowledge from large models to small models.
  2. Compared with traditional model training methods, the ‘knowledge distillation’ method has higher efficiency and better generalisation ability, and can be applied to a variety of different tasks and datasets.
  3. The researchers also proposed some improvement strategies, such as the use of temperature tuning and other techniques, to further enhance the model performance. 

### 3. Future Works
  1. The ‘knowledge distillation’ method proposed in this study provides a new way of thinking and methodology in the field of ML, which can be used as a reference for future ML research.
  2. In practical applications, researchers can choose appropriate models and parameter settings according to specific needs and scenarios to achieve the best performance.
  3. Future research can explore more complex data structures and task types, as well as how to combine the ‘knowledge distillation’ method with other ML algorithms to further improve the model performance and application scope.  
