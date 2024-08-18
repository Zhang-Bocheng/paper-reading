# SyncDreamer: Generating Multiview-consistent Images from a Single-view Image
[paper link](https://arxiv.org/pdf/2309.03453) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a novel diffusion model called SyncDreamer that generates multi-view consistent images from a single viewpoint image.          | Diffusion         |

## Methodology

### 1. Abstract
SyncDreamer achieves multi-view consistency by synchronizing the intermediate states of multiple generated images and using a 3D perceptual feature attention mechanism to correlate corresponding features between different views. Experimental results show that SyncDreamer can generate highly consistent images in a variety of 3D generation tasks.

![image](https://github.com/user-attachments/assets/1d552382-aef3-4e58-872b-5edac6957ed0)

### 2. Method Description 
This paper proposes Multiview Diffusion, a model for multi-view image generation of a single object. The model treats the image generation process for multiple object views as a synchronized set of noise predictors and maintains multi-view consistency by associating the state of each view. Specifically, the model uses a shared U-Net to process all noise predictors and exchanges information at each time step to achieve synchronization. In addition, to ensure that the model is able to perceive the spatial relationships between multiple generated views, the authors propose a feature attention module based on a deep attention mechanism for extracting features that are relevant to the current view.

![image](https://github.com/user-attachments/assets/a2a8875c-4b39-43ff-92bf-da5433982e81)

### 3. Methodological improvements
The main contribution of this paper is to propose a multi-view diffusion model that can generate multi-view images of a single object while maintaining multi-view consistency. The traditional single-view diffusion model cannot guarantee multi-view consistency and thus is difficult to be applied to multi-view image generation tasks. The multi-view diffusion model in this paper, on the other hand, can effectively solve this problem.

![image](https://github.com/user-attachments/assets/3294891c-fe7e-4f0d-a490-3511c84e6584)

### 4. Issues addressed 
This paper mainly solves the multi-view consistency problem in multi-view image generation of a single object. In the traditional single view diffusion model, the lack of consistency between the generated multi-view images is caused by not considering the information of other views. In contrast, the multi-view diffusion model in this paper achieves better multi-view consistency by associating the states of multiple target views and utilizing the deep attention mechanism to enhance the connection between different views. This approach can provide higher quality results for multi-view image generation tasks.

## Experiments
This paper focuses on experiments using the SyncDreamer algorithm for multi-view image synthesis and single-view 3D reconstruction, and compares it with several baseline methods. Specifically, the authors used the Google Scanned Object dataset as the evaluation dataset and randomly selected 30 objects of different types for testing. In the experiments, the authors used a variety of commonly used evaluation metrics such as PSNR, SSIM, and LPIPS to measure the quality of new-view image synthesis, as well as metrics such as CD and Volume IoU to measure the quality of single-view 3D reconstruction. Meanwhile, the authors also analyzed the multi-view consistency of the model and further verified its multi-view consistency by calculating the number of points of the generated images through the MVS algorithm COLMAP.

![image](https://github.com/user-attachments/assets/cd22e953-0d81-40d1-ac01-d1e2b1049ea8)

In terms of experimental results, the authors found that Zero123 was able to produce visually reasonable images but not multi-view consistency, while RealFusion had strong multi-view consistency but was unable to produce visually reasonable images. In contrast, SyncDreamer was able to produce both visually reasonable images and strong multi-view consistency. Furthermore, in the single-view 3D reconstruction task, the authors found that methods such as Point-E and Shap-E tended to produce incomplete shapes, while the One-2-3-45 method, which learns directly from the Zero123 output, loses detail information. In contrast, SyncDreamer is able to capture detailed geometric information while maintaining a smooth surface, achieving better reconstruction quality.

In addition to this, the authors conducted several experiments to further validate the effectiveness of SyncDreamer. For example, the authors show that SyncDreamer is still able to produce reasonable 3D geometries when working with non-real-world images such as hand-drawn designs; the authors also show that initializing from Zero123 can better leverage its 3D prior knowledge by comparing the results of different initialization strategies, which improves the stability of the model; and lastly, the authors also tested the runtime of the model and found that SyncDreamer takes about 40 seconds to generate 64 images (4 instances) on an A100 GPU, slightly longer than the Zero123 runtime. 

![image](https://github.com/user-attachments/assets/65a45262-cb8f-4bd1-be0d-35199f8226ad)

## Conclusion

### 1. Advantages of the Thesis
  1. A simple yet effective framework that generates multi-view consistent images for single-view 3D reconstruction tasks is presented.
  
  2. Multi-view consistency is improved by using a simultaneous multi-view diffusion model to model the joint probability distribution between multiple view images.
  
  3. A novel architecture is designed that uses Zero123 as the backbone and introduces a new volume conditioning module to model cross-view dependencies.
  
  4. Experimental results show that SyncDreamer not only efficiently generates multi-view images with strong consistency, but also achieves better reconstruction quality based on the baseline approach and good generalization ability for various input styles.

### 2. Innovative points
  1. The diffusion model is applied to directly generate multi-view images to solve the multi-view consistency problem in single-view 3D reconstruction.
  
  2. Improve multi-view consistency by synchronizing the multi-view diffusion model to model the joint probability distribution among multiple view images.
  
  3. Introducing a new volume conditioning module to model cross-view dependencies and enhance the performance of the model.
     
### 3. Future Works
  1. Apply the method in a wider range of scenarios, e.g., achieving higher quality 3D reconstruction in virtual reality, game development, etc.
  
  2. Investigate how to further optimize the model so that it can achieve better performance when dealing with complex shapes.
  
  3. Explore how to combine the method with other techniques, such as deep learning, computer vision, etc., to achieve higher-level 3D reconstruction tasks.  
