# Emerging Properties in Self-Supervised Vision Transformers
[paper link](https://arxiv.org/pdf/2104.14294) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper explores whether self-supervised learning provides Vision Transformer (ViT) with new features that are different from convolutional neural networks (CNNs). |   Self-supervised Learning   |

## Methodology

### 1. Abstract
  Self-supervised learning methods adapted to this architecture very well and the following two important conclusions were found: first, the ViT features obtained from self-supervised learning contain explicit information about the semantic segmentation of images, which is not apparent with supervised ViTs and CNNs; second, these features are also excellent k-NN classifiers, and using a small ViT it is possible to achieve 78.3% of the ImageNet top-1 accuracy. 
  
  In addition, the article points out the importance of momentum encoders, multi-tailoring training, and the use of small blocks for ViTs. The authors apply these findings to a simple self-supervised method, DINO, and interpret it as a form of unlabeled self-distillation. By using DINO with ViT-Base, the authors achieved an ImageNet top-1 accuracy of 80.1%.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/5c49eac8-ac59-4be9-a485-4c0201769bdc)

### 2. Method Description 
  This paper proposes a self-supervised learning framework DINO (Distilled Input-Output Network) based on knowledge distillation for image feature learning. The framework draws on the idea of knowledge distillation by training a student network to match the output of a given teacher network. Specifically, the framework uses a multi-view strategy to construct different image perspectives and feeds these perspectives into the "student network" for feature extraction. Meanwhile, only two global views are passed to the "teacher network" to encourage "local-to-global" correspondence. Then, the parameters of the "student network: are learned by minimizing the cross-entropy loss function. 

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/94d0374a-1941-4b5c-90f8-0c24a315896d)

### 3. Methodological improvements
  1. First, it introduces the concept of knowledge distillation, which allows the student network to learn better from the teacher network.
  
  2. Second, the framework uses a multi-view strategy to increase data diversity, which improves feature representation.
  
  3. Finally, the framework uses centering and sharpening operations to avoid the model collapse problem, which makes the framework more stable and reliable.

### 4. Issues addressed 
  The framework addresses two major problems in traditional self-supervised learning: **data diversity and model stability**. By using a multi-view strategy, the framework can increase data diversity and improve feature representation; while by employing centering and sharpening operations, the framework can avoid the model collapse problem and improve model stability.
  
## Experiments
  This paper focuses on the performance of a self-supervised learning method based on the DINO framework on image classification and feature extraction tasks, and compares it with other self-supervised learning methods. Specifically, the authors used the ViT architecture as a model, conducted experiments on the ImageNet dataset, and compared the results with ResNet-50 and other self-supervised learning methods. The authors also analyzed the different components of the DINO framework and explored their impact on performance. In addition, the authors investigate the impact of different training parameters (e.g., batch size, multiple views, etc.) on model performance. Finally, the authors also explore some of the special properties of the DINO framework, such as the preservation of object position information and the ability to migrate to downstream tasks. Overall, this paper provides useful insights on self-supervised learning methods and offers some valuable references for researchers in related fields.
  
  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/1732dc1b-0f94-4942-8288-837d1b36a9f0)

## Conclusion

### 1. Advantages of the Thesis
  1. Compared with traditional labeled pre-training methods, DINO uses less data and computational resources, and also effectively avoids the problem of model overfitting.
  
  2. In addition, the article discusses some important features of DINO and ViT models, such as the inclusion of scene layout information and object boundaries, which have important application value for tasks such as image retrieval and weakly supervised image segmentation.

### 2. Innovative points
  1. DINO is a simple but effective self-supervised learning method that trains student networks by predicting the output of an unlabeled TEACHER network. This method does not require any additional regularization or contrast loss functions, thus reducing model complexity and improving stability.
  
  2. In addition, the authors have identified some important factors that affect the performance of DINO, such as the use of techniques such as small block sizes and multi-crop enhancement that can further improve the quality of features.

### 3. Future Works
  With the development of DL techniques, more and more researchers are focusing on how to use self-supervised learning to improve the generalization ability and efficiency of models. The DINO method proposed in this paper provides a new idea and tool in this direction. In the future, we can expect more researchers to combine DINO with other self-supervised learning methods to explore more efficient and intelligent visual recognition systems.
