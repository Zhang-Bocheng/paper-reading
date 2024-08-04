# PDiscoNet: Semantically consistent part discovery for fine-grained recognition
[paper link](https://arxiv.org/pdf/2309.03173) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents an algorithm called PDiscoNet for discovering partial features of objects in fine-grained classification.          | CNN         |

## Methodology

### 1. Abstract
Traditional fine-grained classification requires recognizing specific object parts, such as the shape of a bird's beak and wing patterns. PDiscoNet does this by using only image-level category labels and by encouraging the a priori conditions that parts are discriminative, compact, different from other parts, equivalent to rigid-body transformations, and active in at least some images to discover partial features of an object. 

In addition, the authors propose partial dropout and partial feature vector modulation methods to prevent individual parts from dominating the classification and to make the information from each part unique from the classifier's point of view. Experimental results show that this method provides better partial feature discovery performance than previous methods without requiring additional hyperparameter tuning and without compromising classification performance.

![image](https://github.com/user-attachments/assets/c750877a-be91-4e19-adb9-99b789a25af2)

### 2. Method Description 
This paper proposes a method called PDiscoNet for discovering K discriminative parts relevant to a fine-grained classification task based only on image-level category labels. The method uses a CNN base model fθ to extract feature vectors and computes K+1 attention maps, where each attention map represents a specific part or background element. Then, for each attention map, the corresponding part vectors are computed by weighted averaging. Finally, all the part vectors are combined into a single score vector and the final classification probability is obtained by softmax function.

![image](https://github.com/user-attachments/assets/f88d35de-4e9e-479c-bf3e-9f8708bada85)

### 3. Methodological improvements
In order to solve the problem that all parts are equivalent from the classifier's point of view, two improvements are proposed in this paper: **part vector modulation and part dropout**. part vector modulation is achieved by maintaining a modulation vector for each key point, multiplying it by each part vector before thereby achieving different classifier weights for different parts. part dropout, on the other hand, randomly discards a portion of the keypoints to encourage the model to find more discriminative parts.

In addition, in order to ensure that the learned attention graphs can meet a certain degree of interpretability and repeatability, four loss functions are introduced in this paper: concentration loss, orthogonality loss, equivariance loss, and presence loss, which are used to ensure the compactness, separability, consistency, and presence of the attention graphs, respectively, separability, consistency and presence.

### 4. Issues addressed 
  1. The PDiscoNet method proposed in this paper can effectively solve the key problem in fine-grained classification, i.e., how to discover discriminative local features. 

  2. Traditional CNNss may ignore some important local features, while PDiscoNet can emphasize the importance of these local features by using attention graph. Meanwhile, the improvement method proposed in this paper can also further improve the performance and robustness of the model.
     
## Experiments
This paper focuses on the experimental results of the PDiscoNet method for discovering shared parts in images and compares them with existing methods. Specifically, the authors use three different datasets (CUB, CelebA, and PartImageNet) to test PDiscoNet and three other methods (Dino ViT, Huang and Li's method, and a self-supervised pre-training method based on visual transformers). For each dataset, the authors used different evaluation metrics (e.g., keypoint regression error, NMI, and ARI, etc.) and reported the performance of each method.

On the CUB dataset, PDiscoNet performs better on all evaluation metrics compared to the other methods. For example, at K=4, PDiscoNet's keypoint regression error is 9.12%, while the average of the other methods ranges from 9.20% to 11.36%. In addition, PDiscoNet achieved higher NMI and ARI scores of 41.49 and 38.05, respectively, while other methods had lower scores. On the CelebA dataset, PDiscoNet also performed well, achieving the highest classification accuracy and the best NMI and ARI scores. On the PartImageNet dataset, PDiscoNet performed better compared to Dino ViT, especially in terms of NMI and ARI.

![image](https://github.com/user-attachments/assets/1569b2a1-84e1-468f-a6f8-690f6454493d)

In addition, the authors performed a sensitivity analysis on the different components of PDiscoNet to determine which factors have the greatest impact on its performance. The results show that Lorth, Lequiv, and part dropout are among the most important components, and they have the greatest impact on part quality. lconc, on the other hand, has a significant impact on the keypoint regression results. lorth and part eigenvector modulation have the greatest impact on the classification performance, whereas lpres has a lesser impact on the classification performance.  

![image](https://github.com/user-attachments/assets/2bf450c2-be96-4662-a146-03943f5730a0)

![image](https://github.com/user-attachments/assets/a1931a63-d293-44ce-9319-7c6e9b73508e)

## Conclusion

### 1. Advantages of the Thesis
This paper proposes a fine-grained visual categorization method based on a CNN that uses part representation as an information bottleneck and learns to detect semantically coherent parts that are relevant to the task, thus improving part localization and semantic coherence and requiring no additional annotation effort. The method provides unique supervised signals on fine-grained category labels, which can improve model interpretability without sacrificing accuracy in downstream classification tasks.
 
### 2. Innovative points
  1. the use of image-level partial annotations for discovering meaningful and discriminative parts to improve the interpretability and robustness of the model.
  
  2. By designing a CNN which is forced to use the discovered parts as a bottleneck for fine-grained categorization, the logits of the categories can be extracted independently from each discovered part and then combined for final categorization.
  
  3. This approach can also help to eliminate or compensate for biases caused by erroneous correlations.
 
### 3. Future Works
  1. Future research directions include improving the method to ensure that only the underlying region affects the information represented by the features of the corresponding part, avoiding the influence of background or neighboring parts.
  
  2. In addition, the degree of contour adherence in PDiscoNet can be further improved by adding self-supervised training on large datasets, leading to a better understanding of some aspects of the model's internal reasoning and enabling richer interactions between the model and the user.
