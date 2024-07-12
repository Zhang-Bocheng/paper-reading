# Generative Pretraining from Pixels
[paper link](https://cdn.openai.com/papers/Generative_Pretraining_from_Pixels_V2.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 |This paper explores the possibility of unsupervised image representation learning using sequence converter autoregressive prediction of pixels.          |  Self-supervised Learning         |

## Methodology

### 1. Abstract
   The authors trained a GPT-2 scale model without labeling and tested it on low-resolution ImageNet. The experimental results show that the model is able to learn robust image representations, outperforming even the supervised pre-trained model on the CIFAR-10 dataset. Furthermore, the larger model was able to match the self-supervised benchmark on ImageNet after hybrid training. This study demonstrates that it is feasible to use an unsupervised approach to image representation learning similar to that used in NLP.

   ![image](https://github.com/user-attachments/assets/5312ae8d-bd19-4d8d-a2cf-09ad885f885c)

### 2. Method Description 
  The paper presents an image-based auto-regressive and BERT (Bidirectional Encoder Representations from Transformers) pre-training model for learning generic representations and applying them to downstream tasks. Specifically, the model employs the Transformer decoder architecture and uses two different objective functions in the pre-training phase： auto-regressive and BERT. In the fine-tuning phase, the model replaces the fully-connected layer with a classification header to adapt to a specific task.
  
### 3. Methodological improvements
 This method introduces the Transformer structure, which enables the model to better capture long-distance dependencies, thus improving its generalization ability. And, the method also takes into account the application of data enhancement and dimensionality reduction techniques, which further improves the effectiveness of the model.
 
### 4. Issues addressed 
  The main objective of the method is to address the problem in image pre-training of how to use large-scale unlabeled data to learn generic representations that can be easily applied to a variety of downstream tasks. By introducing autoregressive and BERT objective functions and using linear probes for evaluation, the method successfully addresses this problem and achieves good performance.
  
## Experiments
  This paper focuses on experimental results using autoregressive modeling in unsupervised learning and compares them with other methods. The experiment consists of the following four parts:

**Comparison of the quality of the representation at different depth layers**: the authors observe a tendency for the quality of the representation to first increase and then decrease as the depth increases. This suggests that the autoregressive model operates in two phases: the first phase is where each location gathers information from the surrounding context to construct a global image representation, and the second phase is where this contextual information is utilized to solve the conditional pixel prediction task.

**Comparison of linear probe accuracy on CIFAR and STL-10 datasets**: the authors found that their model achieved state-of-the-art results on CIFAR-10, CIFAR-100 and STL-10. For example, on CIFAR-10, their model performs better than SimCLR (pre-trained on ImageNet but without labels) and ResNet-152 (pre-trained on ImageNet with labels). Even at the same resolution, better validation loss is obtained with the deeper model.

**Comparison of linear probe accuracy on ImageNet**: not being able to efficiently train at standard ImageNet input resolution, the authors were only able to train at low resolution. Nevertheless, they were still able to match recent comparative learning methods. By connecting features from multiple layers, they can even achieve performance comparable to a model with 8192 embedding dimensions.

**Global fine-tuning: the authors also experimented with global fine-tuning to further improve accuracy**. On CIFAR-10, their model achieved 99% accuracy and 88.5% on CIFAR-100. On ImageNet, they achieved 66.3% accuracy at an MR of 322 and 72.6% accuracy at an MR of 482. While these results are slightly lower than Isometric Neural Nets (Sandler et al., 2019), it is still an important benchmark point.

![image](https://github.com/user-attachments/assets/394359ad-d31d-4dff-b730-13cc3db6f118)

## Conclusion

### 1. Advantages of the Thesis
 1. The method uses a self-encoder and predictive pixel approach for pre-training and achieves better results than other self-supervised learning methods.
 
 2. In addition, the authors compare the performance at different resolutions and propose several optimization methods to improve the model performance.
    
### 2. Innovative points
  1. This method performs better on multiple datasets compared to the traditional self-encoder and comparison learning methods.
  
  2. Also, the authors compare the performance at different resolutions and propose some optimization methods to further improve the model performance.
     
### 3. Future Works
  1. The self-supervised learning method proposed in this paper provides a new idea for the pre-training of image models, which can be considered to be applied to other fields, such as NLP in the future. In addition, more complex self-supervised learning tasks can be explored to further improve the model performance.
     
