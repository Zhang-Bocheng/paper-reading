# OmnimatteRF: Robust Omnimatte with 3D Background Modeling
[paper link](https://arxiv.org/pdf/2309.07749) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |This paper presents a new video keying method, OmnimatteRF, which combines a dynamic 2D foreground layer with a 3D background model.           |  Computer Vision        |

## Methodology

### 1. Abstract
While traditional video keying methods can only isolate foreground objects, OmnimatteRF is able to simultaneously preserve subject details and reconstruct more complex scenes. Experimental results show that the method is able to achieve better scene reconstruction in a variety of videos.

### 2. Method Description 
The Omni matte RF model proposed in this paper is a video matte extraction algorithm that represents a static background as a 3D radiance field and uses a foreground branch to predict an RGBA image to capture the object and its associated effects. The model consists of two independent branches: **foreground and background**. For a given frame, the foreground branch predicts an RGBA image (omnimatte) for each object, while the background branch renders a single RGB image. In the preprocessing stage, the optical flow between neighbouring frames is predicted using the RAFT model, which is used as an auxiliary input and supervisory signal. 

At the same time, the MiDaS depth estimator was used to predict the monocular depth map for each frame and used it as the ground truth for depth loss. Several regularisation losses such as image reconstruction loss, alpha regularisation loss, alpha distortion loss and optical flow reconstruction loss were used in optimising the model.

![image](https://github.com/user-attachments/assets/d639b224-f580-4b45-857c-a5b6dc1d9656)

### 3. Methodological improvements
The Omni matte RF model introduces the concept of 3D radiance field to better capture the effect of dynamic objects compared to the traditional RGBA video matte based method. In addition, the model employs several regularisation losses to improve the stability and accuracy of the model.

### 4. Issues addressed 
The Omni matte RF model solves the problem that traditional video matte extraction algorithms are unable to capture the effects of dynamic objects and improves the accuracy and stability of the model.

## Experiments
This paper focuses on a new approach in video background segmentation and synthesis, and conducts comparative experiments with some existing methods. Specifically, the authors first selected a new challenging dataset and then conducted comparative experiments with three other datasets, including two synthetic datasets and one real-world dataset. Among them, for the synthetic dataset, the authors used commonly used quantitative evaluation metrics (e.g., PSNR, SSIM, and LPIPS, etc.) and derived the corresponding method performance scores. 

For the real-world dataset, on the other hand, only a qualitative evaluation was performed since there was no clean background layer rendering available. In addition, the authors have analysed and experimentally validated the different loss terms used in the model. Finally, the authors summarise the advantages of their method over other methods and suggest some future research directions. 

![image](https://github.com/user-attachments/assets/e2026d1b-8020-4c4a-b2b7-d0c730dfded5)

## Conclusion

### 1. Advantages of the Thesis
  1. This article presents a new video editing method that can separate dynamic foreground objects and their associated effects from static backgrounds and can be extended to a wider range of application scenarios.
  
  2. The authors use deep learning techniques to achieve more accurate and complex scene modelling by combining a 2D foreground layer with a 3D background model.
  
  3. The method shows excellent results on multiple test datasets and is highly robust and scalable.
 
### 2. Innovative points
  1. The method employs deep learning techniques and radial field modelling, allowing foreground objects and their associated effects to be better captured and separated.
  
  2. The method combines a 2D foreground layer with a 3D background model, making it possible to handle more complex and non-planar background scenes.
  
  3. The method also provides a simple but effective retraining step to obtain clean static 3D reconstructions from videos with moving subjects.

### 3. Future Works
  1. The method opens up new possibilities in the field of video editing, which can be applied to more application scenarios, such as virtual reality and film production.
  
  2. Future research can further explore how the method can be combined with other techniques to achieve more sophisticated and high-quality video editing effects.
  
  3. Extension of the method to multi-targeted scenarios as well as handling larger datasets can be considered. 
