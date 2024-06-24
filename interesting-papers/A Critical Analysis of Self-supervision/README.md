# A critical Analysis of Self-supervision
[paper link](https://arxiv.org/pdf/1904.13132.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |    This paper explores the effectiveness of self-supervised learning of deep convolutional neural networks using single images      |   Computer Vision        |

## Methodology

### 1. Abstract
   The authors critically analyze three different representative methods, BiGAN, RotNet, and DeepCluster, and demonstrate that, as long as powerful data augmentation techniques are used, these methods can learn the first few layers of a convolutional network as effectively as using millions of labeled images. However, for deeper layers, even training with millions of unlabeled images cannot bridge the gap with manual supervision.

### 2. Method Description 
  The paper focuses on the performance of deep learning models trained on different datasets and proposes three different unsupervised feature learning methods: **generative models, rotational networks, and clustering networks**. Among them, the generative model uses an adversarial generative network (GAN) to learn image distributions; the rotational network learns abstract features by predicting the vertical orientation of the image; and the clustering network alternates between clustering and feature learning to produce better feature representations.
  
### 3. Key concepts
  _Self-supervised learning_ :  A type of machine learning where the system learns from the data itself without the need for manually labeled examples. The data provides its own supervision in self-supervised learning. This approach is particularly useful for utilizing large amounts of unlabeled data to pre-train models, which can later be fine-tuned on smaller, labeled datasets.
  
### 4. Methodological improvements
  This thesis proposes a data enhancement strategy, i.e., expanding the dataset by performing operations such as random cropping, scaling, rotating, and contrast change on the original data, so as to control the change in the amount of information. Meanwhile, the paper also compares the effects of different data enhancement methods on model performance and finds that data enhancement can significantly improve the generalization ability of the model.
  
### 5. Issues addressed 
  The paper aims to explore the performance of deep learning models on different datasets, and proposes an effective data enhancement strategy as well as three different unsupervised feature learning methods. These methods can help us better understand how deep learning models work and provide more robust and reliable solutions for practical applications.
  
## Experiments
  This paper focuses on the experiments conducted by the authors in learning self-supervised learning methods and uses the results to answer several questions: are large datasets beneficial for unsupervised learning? Does the use of different data augmentation methods affect the representation of the learned features? and how can features learned from a single image be used for other tasks?

  First, the authors conducted linear probe experiments to assess the quality of the learned feature representations for different depths of convolutional layers. They used AlexNet as the base model and conducted experiments on ImageNet and CIFAR-10/100. The experimental results show that the DeepCluster and BiGAN models obtained by training with a single image perform quite similarly in the first two convolutional layers compared to the fully supervised ImageNet-trained model, while slightly falling short in the deeper layers.

  Second, the authors analyzed the effect of different data augmentation methods on the representation of the learned features. They found that random scaling was the most effective data enhancement method, while rotation and color dithering also had a role. These results show that data enhancement is still very important in the case of ultra-low sample sizes.

  Finally, the authors conducted some other experiments such as style migration using feature representations obtained from single image training. The results of these experiments show that the features learned from a single image can also be applied to other tasks with strong generalization ability.

  In conclusion, this paper verifies the effectiveness of feature representations learned from single images through a series of experiments and provides a valuable reference for the research of self-supervised learning.
  
## Conclusion
### 1. Advantages of the Thesis
  1. This paper investigates the effectiveness of self-supervised learning and explores its mechanisms by decomposing the information extraction capabilities of each layer.
     
  2. The authors conducted experiments using three different self-supervised methods (BiGAN, RotNet, and DeepCluster) and found that these methods can learn the first few layers of a deep network almost perfectly using a single image.
     
  3. The results of this paper provide new ideas for self-supervised learning, emphasize the importance of data augmentation in self-supervised learning, and raise the question of how to make better use of available data.
     
### 2. Innovative points
   1. This paper proposes a new self-supervised learning method, i.e., feature learning from a single source image, combined with data enhancement techniques to improve the model performance.

   2. By decomposing the information extraction capability at different levels, it reveals the learning approaches and limitations at different levels in self-supervised learning.

   3. This paper also compares the effectiveness of various self-supervised methods and demonstrates their applicability and limitations in different situations.
   
### 3. Future Works
  1. Self-supervised learning has a broad application prospect in the field of deep learning, and it needs to be further explored how to apply it to a wider range of scenarios in the future.

  2. Data enhancement techniques are one of the keys to self-supervised learning, and more efficient data enhancement methods need to be developed in the future to improve the generalization ability and robustness of the model.

  3. The method of decomposing the information extraction ability of each layer proposed in this paper provides a new idea for a deeper understanding of self-supervised learning, and the mechanism behind it and its application value need to be further investigated in the future.


