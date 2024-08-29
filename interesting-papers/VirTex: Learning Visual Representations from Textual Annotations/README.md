# VirTex: Learning Visual Representations from Textual Annotations
[paper link](https://arxiv.org/pdf/2006.06666.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper describes a new visual representation learning method, VirTex, that uses semantically dense annotations to train convolutional neural networks and achieves results comparable to or better than ImageNet-based pre-trained models in downstream tasks.         | Representation Learning          |

## Methodology

### 1. Abstract
This approach is more efficient than traditional classification-based supervised pre-training and allows learning on less data. Experimental results show that VirTex is able to produce high-quality feature representations in tasks such as image classification, target detection, and instance segmentation.

![image](https://github.com/user-attachments/assets/9fee23e9-6437-42f1-9b50-22b256f6b571)

### 2. Method Description 
The paper proposes a dataset based on image subtitle pairing to train a visual model and apply it to a downstream visual recognition task. Specifically, they use an image caption pairing dataset to pre-train a visual encoder and use this encoder to predict the captions of a given image. During the pre-training process, they used a bidirectional language model for prediction, which contains both forward and backward models. Eventually, they applied the pre-trained visual encoder to downstream visual recognition tasks such as object detection, semantic segmentation, etc.

![image](https://github.com/user-attachments/assets/5164af8a-237e-4e70-917a-e72fba8d20ac)

### 3. Methodological improvements
Compared to traditional methods for image classification and object detection, this approach can better utilise contextual information in images, thus improving the performance of downstream tasks. And they use a large-scale image caption pairing dataset to train the model, which makes the model have better generalisation ability.

### 4. Issues addressed 
This approach addresses the problem of ‘isolation’ that exists in traditional visual recognition tasks, where each image contains only one label or category and no other contextual information can be exploited. By introducing a paired dataset of image captions, the method is able to learn richer image features, which improves the performance of downstream tasks.

## Experiments
This paper focuses on VirTex, a natural language-based visual feature learning method, and conducts several comparative experiments to verify its effectiveness and data efficiency. Specifically, the following four experiments are conducted in this paper:

**Linear model classification experiments**: different types of pre-training methods such as MoCo-COCO, multi-label classification, and instance segmentation are used to compare with VirTex on two tasks, PASCAL VOC and ImageNet-1k. The results show that VirTex performs better on the same number of images and achieves better performance on fewer images, illustrating its higher data efficiency.

![image](https://github.com/user-attachments/assets/a73b9eaa-f131-49d0-9e0f-eda71ce3c05d)

**Model selection experiments**: the size and depth of the text header in VirTex were adjusted, and it was found that increasing the width and depth of the text header could improve the performance of the downstream task.

![image](https://github.com/user-attachments/assets/ebca18f5-3f9f-4169-bcdc-9c0835a459e1)

**Pre-training task experiment**: The pre-training task of VirTex was changed from a bidirectional encoder-decoder task to a unidirectional forward encoder task, and the results showed that the bidirectional task outperforms the unidirectional task.

![image](https://github.com/user-attachments/assets/9f2a87f0-af6d-4333-a1b7-69dae22b1d2b)

**Downstream task experiment**: comparing VirTex with other pre-training methods on four tasks: COCO instance segmentation, LVIS instance segmentation, PASCAL VOC detection and iNaturalist 2018 fine-grained classification. The results show that VirTex performs better on the same number of images and achieves better performance on fewer images, illustrating its higher data efficiency. 

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new visual representation learning method, VirTex, which uses text annotations to train models and achieves comparable or better performance than ImageNet pre-training on downstream tasks.
  
  2.  Compared to traditional image classification pre-training methods, VirTex can utilise the data more efficiently as it can learn high-quality visual features from a large number of weakly correlated images and text.
  
  3.  In addition, the data collection process is simpler since text annotation does not require an explicit category architecture.

![image](https://github.com/user-attachments/assets/2d42163d-99ab-4874-a2a8-0937da85166b)

### 2. Innovative points
The main innovation of VirTex is that it uses text annotations as supervised signals to train the model. By jointly training a CNN and a Transformer model, it automatically generates image labels described in natural language. This approach has a higher semantic density compared to other methods based on unsupervised contrast learning and supervised classification, and thus can learn high-quality visual features with less amount of data. 

### 3. Future Works
Future research could explore how to extend this approach to more downstream tasks and further improve its efficiency and accuracy. Also, it can be investigated how to deal with noisy large-scale image-text pair datasets to further extend the application of the method.  

