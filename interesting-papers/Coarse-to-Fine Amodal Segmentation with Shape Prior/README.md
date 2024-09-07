# Coarse-to-Fine Amodal Segmentation with Shape Prior
[paper link](https://arxiv.org/pdf/2308.16825) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |  In this paper, a new method called Coarse-to-Fine Segmentation (C2F-Seg) is proposed for solving the modal object segmentation problem.         |  Multi-modal        |

## Methodology

### 1. Abstract
The method converts the learning space from pixel-level image space to vector quantised latent space by modelling modal segmentation step-by-step, and performs coarse-grained modal segmentation based on this. However, this method lacks the ability to process detailed information about objects, so a convolutional refinement module is proposed to inject finer-grained information and provide more accurate modal object segmentation. To aid the study of modal object segmentation, the authors also created a synthetic modal dataset, MOViD-Amodal (MOViD-A), which can be used for both image and video modal object segmentation tasks. Experimental results show that C2F-Seg outperforms other methods on two benchmark datasets, KINS and COCO-A, and demonstrates its potential for video modal object segmentation tasks.

### 2. Method Description 
The paper proposes a framework called C2F-Seg for solving the occluded object segmentation problem. Firstly, the visible part is estimated by a standard segmentation algorithm and image features are extracted as input using a pre-trained ResNet. Then, the input is combined with a coded mask to predict the occluded portion of the whole object using the Transformer model. Finally, the convolution module is used to refine the prediction and generate the final prediction of the occluded portion.

![image](https://github.com/user-attachments/assets/ddfa1652-9787-4954-b9fe-7da993d94b85)

### 3. Methodological improvements
  1. A vector quantisation (VQ) embedding space is used: by projecting the mask in the embedding space, the relationship between the visual features and the mask can be better captured.
  
  2. The mask-and-predict idea was introduced: by choosing the right proportion of masks, the task is made more challenging and generalisable.
  
  3. The iterative prediction process is added: the prediction of the masked part is done through several iterations, thus improving the accuracy.

### 4. Issues addressed 
The paper mainly addresses the problem of occluded object segmentation. Traditional segmentation algorithms can only deal with the visible part, but not the occluded part. Therefore, the thesis proposes a framework that can estimate both the visible part and the occluded part, improving the accuracy of segmentation. In addition, the framework can also be applied to video occluded object segmentation due to its scalability.

## Experiments
This paper presents experiments comparing the effectiveness of the C2F-Seg model in image and video scenarios, and analyses and validates several aspects.

Firstly, in image scenarios, the authors compare C2F-Seg with several competitors, including methods such as AISFormer and VRSP. The results show that C2F-Seg achieves the best performance on both the KINS and COCOA datasets, exceeding the AP and mIoU metrics of the other methods. In addition, C2F-Seg achieves better results by exploiting the shape prior compared to AISFormer.

![image](https://github.com/user-attachments/assets/97c8cbfb-79fc-4ad0-a424-bbf0175171af)

Secondly, in video scenarios, the authors further tested C2F-Seg using both FISHBOWL and MOViD-A datasets. The results show that C2F-Seg performs best above all baselines, achieving higher occluded mIoU metrics. Especially for MOViD-A, a more challenging dataset, C2F-Seg is still able to effectively handle multiple objects, lens distortion, and viewpoint changes.

![image](https://github.com/user-attachments/assets/5bf35326-ce2a-4e79-b0a0-396339277f79)

Finally, the authors also conducted experiments to validate the effectiveness of C2F-Seg in a number of areas, including a study of the effect of the convolutional refinement module, the effect of the parameter K, and the effect of the quality of the input visible mask on performance. The results of all these experiments show that C2F-Seg is an efficient and accurate method that can achieve good results in different scenarios.

## Conclusion

### 1. Advantages of the Thesis
This paper propose a novel coarse and fine network architecture, C2F-Seg, a framework that learns shape prior using transformers and predicts the masks of visible and non-visible regions through a two-branch refinement module. Experimental results show that state-of-the-art performance is achieved in both image and video.

### 2. Innovative points
The main contribution of this paper is the proposal of C2F-Seg, a new coarse and fine network architecture, whose core idea is to combine shape prior with visual features in order to generate accurate amodal segmentation step by step. Specifically, the framework performs a coarse segmentation in a low-dimensional vector quantised latent space, and then uses a convolutional refinement module to further inject detailed information. 

This coarse and fine structure is designed to allow the model to better capture the relationship between shape prior and visual features, resulting in more accurate amodal segmentation. In addition, the authors have created a new synthetic dataset called MOViD-A containing 838 videos and 12,299 objects to facilitate research in this area. 

### 3. Future Works
While C2F-Seg has achieved state-of-the-art performance on image and video amodal segmentation tasks, there are still some challenges that need to be addressed. For example, how to handle the case where objects are completely invisible and how to improve the generalisation of the model. Therefore, future research could focus on these aspects to further improve the performance and usefulness of amodal segmentation. 
