# Group Normalization
[paper link](https://arxiv.org/pdf/1803.08494.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2018 | This thesis focuses on a new deep learning technique, Group Normalization (GN), and compares it with the existing Batch Normalization (BN).          |  Deep Learning         |

## Methodology

### 1. Abstract
  Since the error of BN increases rapidly as the batch size decreases, the effectiveness of BN is limited in tasks that require training with smaller batches. In contrast, GN divides channels into groups and normalizes them by calculating the mean and variance within each group, is computationally independent of batch size and has stable accuracy across batch sizes. 
  
  Experimental results show that GN has better performance than batch normalization on the ImageNet dataset and can be an effective alternative to batch normalization in a variety of tasks, including object detection, segmentation, and video classification. In addition, GN can be naturally transferred from the pre-training to the fine-tuning phase. Thus, GN is a simple and effective DL technique that can replace BN in many tasks.

  ![image](https://github.com/user-attachments/assets/3364c7f3-29e9-4259-9480-400d8504d601)

### 2. Method Description 
  This paper proposes a new DNN feature normalization method, Group Normalization (GN). The method differs from existing methods such as BN, layer normalization and instance normalization in that it groups pixels within the same channel and calculates the mean and variance within each group to achieve channel-level normalization processing.
  
  ![image](https://github.com/user-attachments/assets/ba6385f0-7f62-42d2-8222-f3f8b812dc9c)

### 3. Methodological improvements
  Compared with traditional methods such as BN, layer normalization and instance normalization, GN has the following advantages:

  1. **Better generalization ability**: Since GN considers the correlation between channels, it can better adapt to different data distributions and improve the generalization ability of the model.
  
  2. **Less computation**: Compared with instance normalization, GN does not require independent normalization operations for each sample, thus reducing the amount of computation.
  
  3. **Higher efficiency**: Compared with layer normalization,GN only needs to perform normalization operations on each set of channels, so the normalization process can be completed faster.

     ![image](https://github.com/user-attachments/assets/c8cc8802-a18f-401d-8d77-6df24971e94a)

### 4. Issues addressed 
  GN mainly solves the problem of interdependence between channels in DNN, and by grouping and normalizing pixel points within the same channel, it enables the network to make better use of the correlation between channels, and improves the performance and generalization ability of the model. Meanwhile, GN also has the advantages of less computation and higher efficiency, which further optimizes the training and inference speed of DNN.
  
## Experiments
  This paper focuses on the performance of GN in the tasks of image classification, target detection and segmentation, and video classification, with comparative experiments with BN.

First, in the image classification task of ImageNet, the authors used the ResNet model and replaced BN with GN for the experiments. The results show that GN can better handle the case of small batches of data and has a lower error rate on the validation set relative to BN. In addition, the authors tuned the number of groups and channels of GN and found that different settings affect the performance.

Second, in the target detection and segmentation task, the authors used the Mask R-CNN model and replaced BN with GN for their experiments. The results show that GN can improve detection accuracy with smaller batch sizes relative to BN and does not suffer from the problems of BN under non-independent distributions.

Finally, in the video classification task, the authors used the Inflated 3D (I3D) convolutional network and replaced BN with GN for the experiments. The results show that GN can better handle input sequences of different lengths and maintain high accuracy for smaller batch sizes compared to BN.

![image](https://github.com/user-attachments/assets/c28f3470-3471-4e56-bdfb-8110f06c4a4c)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new normalization layer GN and compares it with the existing BN. The experimental results show that GN exhibits good performance in various applications and can better adapt to different batch sizes. 
  
  2. In addition, the authors explore the relationship between GN and LN (Layer Normalization) and IN (Instance Normalization), and propose the idea of applying it to reinforcement learning tasks.
     
  ![image](https://github.com/user-attachments/assets/d93a73ad-4d8f-4201-aeb4-a05613e3c613)
 
### 2. Innovative points
  1. The main contribution of the paper is to propose a new normalization layer GN that computes the normalization parameters by grouping all feature mappings in each small batch, thus avoiding the use of global mean and variance.
  
  2. This approach not only improves the generalization ability of the model, but also reduces the risk of overfitting. And, the authors compare GN with other normalization methods and demonstrate its superiority.

### 3. Future Works
  1. This paper provides a new direction in the study of the normalization layer, i.e., how local information in small batches can be used to compute normalization parameters.
  2. Future work can further explore this direction and apply it to a wider range of deep learning tasks. In addition, the authors mention the idea of applying GN to reinforcement learning tasks, which is also a direction worth investigating.
