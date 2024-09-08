# OpenIllumination: A Multi-Illumination Dataset for Inverse Rendering Evaluation on Real Objects
[paper link](https://arxiv.org/pdf/2309.07921) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper presents a real-world dataset called OpenIllumination that contains over 108,000 images of 64 objects in different materials and shooting angles with accurate camera parameters, illumination truths and foreground segmentation masks.         | Dataset         |

## Methodology

### 1. Abstract
The dataset can be used to evaluate the performance of various inverse rendering and material decomposition methods on real objects. The authors also tested and compared the performance of several state-of-the-art inverse rendering methods. The paper describes how to recover the camera parameters by using COLMAP to improve the performance of the inverse rendering method. And the paper also presents a chrome sphere-based lighting calibration method for obtaining realistic lighting information, which is important for evaluating the effects of relighting.

### 2. Method Description 
This paper focuses on the acquisition process of the OpenIllumination dataset and some of the key techniques included in it. The dataset contains more than 108K images of 64 objects with different materials, and each object was photographed by 48 DSLR cameras in 13 different illumination modes. In addition, 20 objects were photographed by 24 high-speed cameras at 142 OLAT settings. Twenty-four different material categories were included in the dataset, such as plastics, glass, fabrics, ceramics, and so on. 

### 3. Methodological improvements
  1. Compared to the traditional method of image capture with a handheld camera and estimating the camera parameters using COLMAP, this paper takes advantage of light staging by fixing the camera internal and external parameters while capturing different objects, thus avoiding the challenges posed by problems such as lack of texture of the object or specular reflections in certain viewpoints.
  
  2. In addition, this paper proposes a chrome sphere-based illumination calibration method for accurately estimating the true lighting information, thus improving the accuracy of evaluating the relighting effect.

### 4. Issues addressed 
This paper addresses the challenges of using COLMAP to estimate camera parameters on handheld cameras, such as the lack of texture on objects or specular reflections in certain viewpoints. Also, the chrome sphere-based illumination calibration method proposed in this paper effectively addresses the problem of inaccurate illumination information in relighting effect estimation. The application of these techniques can improve the performance of inverse rendering methods and provide more accurate results for relighting effect evaluation.

## Experiments
This paper focuses on four main areas of experimentation:

**Inverse rendering evaluation**: the authors selected six learned inverse rendering methods and three methods supporting multi-lighting optimisation for their experiments and evaluated them using images from our dataset. In the single illumination condition, the authors selected images with all lights on as the training and test sets. In the multi-illumination condition, the authors chose three sets of images with different illumination modes. The experimental results show that NeRD suffers from high instability, while TensoIR performs best but still has problems with highly glossy surfaces.

![image](https://github.com/user-attachments/assets/e9bced83-6a1e-43a3-9a11-738087a4c347)

**Photometric stereo**: The authors used OLAT images to reconstruct normal and diffuse colour maps of objects. Experimental results show that OLAT images can be used for photometric stereo.

![image](https://github.com/user-attachments/assets/2f65ea27-afb9-4c40-8ea0-e0f26dbf3b24)

**Novel view synthesis**: The authors validated the data quality using several neural radiation field methods and obtained high PSNR scores.

![image](https://github.com/user-attachments/assets/d7cb22a9-b960-467a-8c66-c50e72c92f22)

**Ablation study**: The authors compare the quality of data captured by a handheld camera and a fixed camera and find that the handheld camera tends to lead to inconsistent illumination, while the fixed camera provides a more complete reconstruction.

![image](https://github.com/user-attachments/assets/3b1b293a-e218-4742-97e1-6931f58b8476)

## Conclusion

### 1. Advantages of the Thesis
  1. The dataset provides key components such as accurate camera parameters, realistic illumination information, and segmentation masks for all images, providing researchers with a valuable resource for quantitatively evaluating the effectiveness of inverse rendering and material decomposition techniques on real objects.
  
  2. In addition, the authors use the dataset to evaluate multiple state-of-the-art inverse rendering and novel view compositing methods and effectively compare their performance.

### 2. Innovative points
The methodological innovation of this paper lies in proposing a capture approach similar to a traditional light stage, whereby a dense distribution of cameras and controllable lights fixed on a static frame allows for precise pre-calibration of all cameras and reuse of the same camera parameters, thus not only improving calibration accuracy but also providing a consistent evaluation process for all scenes. In addition, the authors have designed an efficient semi-automatic labelling method to provide high quality object segmentation masks. 

### 3. Future Works
  1. The future outlook of this paper is to further explore and advance the research in this area. Since this dataset only contains objects with sizes between 10 and 20 cm, future research could consider expanding to larger sizes.
  
  2. In addition, due to the limited camera density, future research could also consider increasing the camera density to improve the efficiency of data collection.
  
  3. With the development of computer vision technology, future research could also consider applying deep learning techniques to areas such as inverse rendering and material decomposition to improve the performance and robustness of the algorithms.  
