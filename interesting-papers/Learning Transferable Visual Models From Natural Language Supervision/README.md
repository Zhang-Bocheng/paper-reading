# Learning Transferable Visual Models From Natural Language Supervision
[paper link](https://arxiv.org/pdf/2103.00020) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper describes a model called CLIP that learns image features from natural language descriptions and performs zero-sample migration learning without additional labeling data.         |  Transformer         |

## Methodology

### 1. Abstract
 The model uses large-scale Internet images and corresponding text descriptions for pre-training, and then learns downstream tasks by referring to learned visual concepts or describing new concepts through natural language. Experimental results show that the model performs well on several computer vision tasks, and even rivals models trained under full supervision. In addition, the paper provides code and pre-trained model weights for use by other researchers.

 ![image](https://github.com/user-attachments/assets/a261790c-e191-4c51-8111-503c6cb7e1c3)

### 2. Method Description 
This paper propose a pre-training model called CLIP (Contrastive Language-Image Pre-Training) for learning the semantic relationship between vision and natural language. The model predicts the correspondence between images and text by jointly training an image encoder and a text encoder, and uses a contrast loss function to optimize the similarity in the multimodal embedding space. 

1. **Constructing the dataset**: A large amount of image and text data are collected using web crawlers and paired into "image-text" pairs.

2. **Train the model**: Firstly, preprocess the image and text separately, and then train the model by comparing the loss function. Specifically, for each "image-text" pair, the model needs to predict whether the pair matches or not, and also needs to learn the representation of the image and text in the multimodal embedding space.

3. **Inference stage**: In the inference stage, given an image or a piece of text, the model can convert it into the corresponding multimodal embedding vector and calculate its similarity score with other images or texts, so as to realize the tasks of image classification and text retrieval.

![image](https://github.com/user-attachments/assets/a91d8a05-5b85-4e67-a527-c186324660a9)

### 3. Methodological improvements
  Unlike traditional supervised learning-based image classification methods, CLIP employs unsupervised learning and utilizes a large amount of unlabeled data for pre-training, avoiding the cost of manually labeling a large number of samples. In addition, CLIP introduces a contrast loss function, which enables the model to better learn the semantic relationship between images and text, thus improving the performance of the model.
  
### 4. Issues addressed 
The multimodal embedding space proposed by CLIP provides a bridge for cross research between these two fields. By learning the semantic relationship between images and texts, CLIP can help computers understand human linguistic expressions, which can be better applied to tasks such as image categorization and text retrieval. In addition, CLIP can be used as a base model for other NLP tasks, such as machine translation and dialog systems.

## Experiments
  This article mainly introduces the concept and method of zero-shot transfer, and demonstrates its effectiveness in the field of CV by comparing with Visual N-Grams and further analyzing the CLIP model. Specifically, the article conducts the following comparison experiments:

1. **Zero-shot transfer versus Visual N-Grams**: The authors used datasets such as ImageNet to compare the performance differences between the CLIP model and the Visual N-Grams model. The results show that the CLIP model achieves 76.2% accuracy on ImageNet, while the Visual N-Grams model can only achieve 11.5% accuracy. In addition, the CLIP model is able to match the performance to other datasets such as YFCC100M, CIFAR-10, etc.

2. **Zero-shot transfer capability of CLIP model**: the authors used several datasets to test the zero-shot transfer capability of CLIP model and analyzed its performance in detail. The results show that the CLIP model is able to achieve good performance on most datasets, especially on some fine-grained classification tasks. However, the performance of CLIP model is relatively weak on some complex tasks, such as satellite image classification and self-driving related tasks.

3. **Further analysis of the CLIP model**: the authors conducted a more in-depth study of the CLIP model, including exploring the role of its language model, exploring how to optimize the effect of zero-shot transfer, and other aspects. Meanwhile, the authors also propose some improvements, such as using a better pre-trained model, adjusting the cue text and other ways to improve the performance of the CLIP model.

![image](https://github.com/user-attachments/assets/9e8b5e03-62ca-48e5-bede-32284125a36d)

![image](https://github.com/user-attachments/assets/dea7329e-1767-480a-8110-8865a4dd526b)

![image](https://github.com/user-attachments/assets/d61a758c-5fbd-4852-a720-393fbad14700)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new visual text retrieval model, CLIP, which outperforms existing state-of-the-art techniques for zero-sample classification on multiple natural image distributions.
  
  2. CLIP has a wide range of applications and can be used for many tasks such as multi-label classification, detection and segmentation.
  
  3. The authors also conducted extensive experiments to evaluate the performance of CLIP and identified some potential problems and limitations.

![image](https://github.com/user-attachments/assets/bfcfc080-7026-4e7f-8fa4-fe4a635929b3)

### 2. Innovative points
  1. CLIP is a model based on the Transformer architecture that combines image features and text embedding vectors for more accurate visual text retrieval.
  
  2. CLIP uses a large scale pre-training dataset consisting of over 4 billion images and millions of text descriptions to improve its generalization ability and robustness.
  
  3. CLIP also introduces a novel learning objective that optimizes model parameters by minimizing the distance between two independent training processes.
     
### 3. Future Works
  1. CLIP is a very promising research direction that can be applied to many fields, such as computer vision, natural language processing, etc.
  
  2. In future work, it can be further explored how to improve the performance and scalability of CLIP and how to combine it with other techniques to solve more practical problems.

