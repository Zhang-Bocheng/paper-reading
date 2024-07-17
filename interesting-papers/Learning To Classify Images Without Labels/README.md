# SCAN: Learning To Classify Images Without Labels
[paper link](https://arxiv.org/pdf/2005.12320v2.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper presents a new unsupervised image classification method, SCAN (Self-Supervised Clustering with Attention Network).         | Unsupervised Learning          |

## Methodology

### 1. Abstract
 The method proceeds in two steps: first, semantically meaningful features are obtained using a self-supervised learning task; then these features are utilized as a priori to perform clustering in a learnable clustering method. Experimental results show that the method outperforms existing methods in terms of classification accuracy on several datasets and is the first unsupervised image classification method that performs well on large-scale datasets.

### 2. Method Description 
  The method uses representation learning in self-supervised learning to obtain semantic features and performs clustering by mining neighbor information. Specifically, the method first uses a pre-trained NN model to learn an embedding function that maps the input image into a low-dimensional space. Then, for each sample, it finds K samples with its nearest neighbors and uses them as its neighbors. Finally, the method defines a loss function such that each sample and its neighbors are correctly assigned to the same category.

### 3.  Methodological improvements
  1. Compared to traditional clustering methods based on the K-Means algorithm, the method introduces neighbor information, which can better handle noisy and locally varying situations.
  
  2. In addition, the method uses an adaptive objective function in self-supervised learning, which can automatically learn useful features without labels.
     
### 4. Issues addressed 
  This method solves two major problems in traditional unsupervised image classification methods: 
  <br>&emsp;first, due to the lack of labeling information, traditional methods tend to obtain only rough clustering results; 
  <br>&emsp;second, traditional methods are often susceptible to noise and local variations, resulting in poor clustering results.

  ![image](https://github.com/user-attachments/assets/bddeb7dc-13e2-41d5-9236-e74383f8ae39)

## Experiments
  In the experimental section, the authors used four datasets (CIFAR10, CIFAR100-20, STL10, and ImageNet) for their experiments with different settings and comparisons for each dataset. In particular, for the first three datasets, the authors divided the data into a training set and a validation set and used the same settings and hyperparameters for training and testing. For the ImageNet dataset, on the other hand, the experiments were conducted by dividing it into subsets of different sizes.

**Impact of hyperparameters**: the authors investigated the impact of different number of nearest neighbors K and different data enhancement strategies on the model performance. The results show that increasing the number of neighbors improves the accuracy of the model, while using the SimCLR data enhancement strategy is more effective than using RandAugment.

**Effectiveness of the method**: the authors demonstrate the effectiveness of the SCAN method by removing mis-matched sample pairs and using a larger number of neighbors. The results show that the method can effectively cluster images without relying on predefined categories.

**Performance on ImageNet**: the authors conducted experiments on the ImageNet dataset and compared it with other semi-supervised learning methods. The results show that their method outperforms other methods on metrics such as Top-1 accuracy, Top-5 accuracy, NMI and ARI.

![image](https://github.com/user-attachments/assets/a164eb37-1373-44d7-9033-3e80dc06f491)

![image](https://github.com/user-attachments/assets/b0092d9c-9233-4ff3-9517-e18860352d01)

![image](https://github.com/user-attachments/assets/85442923-08e0-4091-9886-1114290f9064)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a novel unsupervised image classification framework that has the following advantages over existing end-to-end learning methods: (1) it does not require expensive semantic annotations; (2) it can be applied to large-scale datasets; and (3) it can be scaled up to other domains such as semantic segmentation, semi-supervised learning, and few-sample learning.
 
  2. Experimental results show that the method performs better than existing work on multiple datasets, and its performance on ImageNet demonstrates its applicability to large datasets.
  
  3. The framework proposed in the paper combines feature learning and clustering, avoiding the initialization problem and the problem of low-level features, as well as eliminating the need for specific preprocessing operations.

### 2. Innovative points
 1. A two-step approach is proposed to achieve unsupervised image classification, which consists of first learning the feature representation through a self-supervised task, and then using nearest neighbors as a priori information for clustering.
 
 2. Unlike traditional end-to-end learning methods, the method does not need to rely on network architecture, but instead utilizes meaningful features for clustering, which improves the clustering results.

 3. In the experiments, the method uses nearest neighbors instead of the traditional K-mean clustering method, which effectively avoids the problem of clustering degradation.
    
![image](https://github.com/user-attachments/assets/50d38845-c97b-4143-b26b-a48d9ab635e7)

### 3. Future Works
  1. Further exploration can be done to apply the method to more complex visual tasks, such as target detection and semantic segmentation.
  
  2. One can try to combine the method with other unsupervised learning techniques, such as self-encoder and variational self-encoder, to improve the clustering effect.

  3. Different self-supervised tasks can be considered to learn feature representations for different types of datasets and application scenarios.
