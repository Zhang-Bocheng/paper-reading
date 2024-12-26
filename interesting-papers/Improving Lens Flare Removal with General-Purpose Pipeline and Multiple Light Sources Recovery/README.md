# Improving Lens Flare Removal with General-Purpose Pipeline and Multiple Light Sources Recovery
[paper link](https://arxiv.org/pdf/2308.16460) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | The aim of this paper is to address the heterogeneous halo problem that occurs when images are captured under strong light sources, which can seriously affect image quality and the effectiveness of computer vision tasks.          |  Computer Vision        |

## Methodology

### 1. Abstract
Although existing methods can synthesise data by direct addition, these methods do not take into account automatic exposure and tone mapping in the signal processing pipeline, resulting in limited data for depth model training. In addition, existing methods have difficulty dealing with multiple light sources because various light sources have different sizes, shapes, and luminance. To address these issues, this paper proposes a solution to improve the performance of lens halo removal by revisiting the signal processing pipeline and designing a more reliable light source recovery strategy. 

The new pipeline distinguishes between local and global illumination through convex combinations to avoid global illumination bias and local oversaturation. The recovery strategy for multiple light sources uses convex combination based on the input-output average of light levels, thus avoiding the need for hard thresholding for identifying light sources. Also, this paper contributes a new lens halo test dataset containing halo contamination images captured by ten consumer electronics products

![image](https://github.com/user-attachments/assets/6b216bf0-4774-4191-a0d1-3a6506c5a1c1)

### 2. Method Description 
This paper proposes two methods to process images with halos: Flare-Corrupted Image Generation and Light Source Recovery.

In **Flare-Corrupted Image Generation**, the authors mix the two images together by calculating the light matrices of the halo image and the scene image and assigning weights to each pixel according to the light matrices, and then using convex combination. This approach avoids the problem of training data distribution bias and makes the deep model better adapt to the real situation.

In **Light Source Recovery**, the authors use the same process as Flare-Corrupted Image Generation, but choose a more powerful convex function as the weighting function to ensure that only the light source is restored to the final image. This approach allows the parameters in the weighting function to be adjusted as needed to recover light sources in different situations.

![image](https://github.com/user-attachments/assets/91ab096e-1f21-4fdb-b741-1c2a0184c091)

### 3. Methodological improvements
Compared to the traditional method of halo removal, the method in this paper is able to better preserve the light source information in the original image, thus improving the performance of the deep learning model.

### 4. Issues addressed 
The Flare-Corrupted Image Generation and Light Source Recovery methods proposed in this paper address the problem that exists when capturing images with halos, i.e., how to preserve the light source information in the original image and avoid the problem of shifting the training data distribution. These methods can be applied to various computer vision tasks such as object recognition, target detection, etc.
  
## Experiments
This paper focuses on the following comparison experiments:

**Flare Removal Comparison:** this experiment compares the traditional method, the depth model, and the method in this paper, and uses the full reference metrics PSNR and SSIM to evaluate the performance. The results show that this paper's method has a better spot removal effect at night, while the spot removal effect during daytime is slightly inferior to that of the method proposed by Wu et al. but better than that of the method proposed by Dai et al.

**Light Source Recovery Comparison:** This experiment compares the performance of the current method and the method in this paper in the case of a single light source and multiple light sources. The results show that this method can better recover light sources of different sizes and locations, while the current method can only recover the most obvious light sources.
![image](https://github.com/user-attachments/assets/30e615ae-1f1b-4466-8824-c67c1949689d)

**Generalisation Comparison:** This experiment compares the generalisation ability of the current method and the method in this paper under different camera models, different spot shapes and different light source types by collecting a test set of consumer electronics products. The results show that the method in this paper can effectively remove different light spots in a wider range of scenarios.

![image](https://github.com/user-attachments/assets/7f5416c7-66b0-40c9-b595-101dbf203bfc)

**Flare Removal for Object Detection:** This experiment uses a pre-trained YOLOv5 detector to process images with and after removal of flares and compares their effects on object detection. The results show that light spots affect the accuracy of the object detector, and the method in this paper can improve the accuracy of the object detector.  

## Conclusion

### 1. Advantages of the Thesis
  1. The method generates more realistic images with scattered and reflected halos in inverse gamma space using pixel-level convex combinations and avoids the problem of shifting global illumination distributions by redesigning the optical synthesis principle in ISP.
  
  2. In addition, the method naturally recovers multiple light sources without the hard thresholding problem. Experimental results show that the method removes lens halos and restores multiple light sources better than existing methods.

### 2. Innovative points
  1. The method redesigns the principle of optical synthesis in ISP to generate more realistic images with scattered and reflected halos using pixel-level convex combinations in inverse gamma space and avoids the problem of shifted global illumination distributions.
  
  2. And, the method naturally recovers multiple light sources without the hard thresholding problem. These innovations enable the method to better remove lens halos and recover multiple light sources. 

### 3. Future Works
The method in this paper provides a new idea for removing lens vignetting and restoring multiple light sources. However, the method still has some limitations, such as the inability to handle complex light paths and multiple types of halos. Therefore, future research can further explore how to solve these problems and apply the method to a wider range of scenes.  
