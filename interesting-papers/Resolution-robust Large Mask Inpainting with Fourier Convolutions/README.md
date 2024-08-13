# Resolution-robust Large Mask Inpainting with Fourier Convolutions
[paper link](https://arxiv.org/pdf/2109.07161) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper introduces a new image filling method, Large Mask Filling (LaMa)         | Convolutional Neural Network          |

## Methodology

### 1. Abstract
The paper uses Fast Fourier Convolution and a high perceptual field loss function to address the problems encountered by modern image filling systems when dealing with large missing regions, complex geometries, and high-resolution images. Experimental results show that LaMa achieves better performance than existing methods on multiple datasets and adapts well to scenes above the training resolution. In addition, LaMa has lower parameter and time costs than competitive benchmarks.

![image](https://github.com/user-attachments/assets/7baf4d3d-28c7-453f-86bf-9da2a43a3abe)

### 2. Method Description 
The paper presents a Fast Fourier Convolution (FFC) based fully convolutional network for the filling problem in high resolution images. The method improves the filling effect by using global contextual information and uses a wider receptive field in the early layers to capture the global structure. In addition, the method introduces loss functions such as High Receptive Field Perceptual Loss (HRF PL) and Adversarial Loss to optimize the model performance.

![image](https://github.com/user-attachments/assets/2313e119-d8d6-4b89-986b-fe5cde1ff4c6)
 
### 3. Methodological improvements
Compared to traditional fully convolutional networks, the method uses Fast Fourier Convolution (FFC) instead of traditional convolutional operations, allowing the model to better utilize global contextual information. Also, the method uses loss functions such as High Receptive Field Perceptual Loss (HRF PL) and Adversarial Loss to further optimize the model performance.

![image](https://github.com/user-attachments/assets/71c20174-7bb3-4157-98ac-6fc0d2c9203b)

### 4. Issues addressed 
The method solves the problem of insufficient global context information in high-resolution image filling and improves the filling effect. At the same time, the method also considers the impact of different training strategies on model performance and proposes a more reasonable training strategy.

## Experiments
This paper focuses on the performance of the LaMa network in image restoration tasks and conducts several sets of comparison experiments to verify its performance and advantages. Specifically, the authors conducted the following sets of comparison experiments:

**Comparing the performance of multiple baseline models**: the authors used several publicly available pre-trained models for comparison, including CoModGAN, MADF, etc., and the results show that the LaMa-Fourier model performs well in most of the cases with fewer parameters.

**User survey**: in order to eliminate selection bias, the authors also conducted a user survey, which showed that the LaMa method generates more acceptable filling results.

**Impact of model components**: The authors analyzed different components of the LaMa network, including the use or not of Fourier Convolution (FFC) in the residual block, the use or not of High Receptive Field (HRF) in the perceptual loss, and the impact of mask width. The results show that the use of FFC can significantly improve the filling quality under wide masks, while the use of HRF in perceptual loss can further improve the filling effect.

**Generalization ability at high resolution**: Since real-world editing scenarios usually require processing high-resolution images, the authors also tested the generalization ability of the LaMa network at higher resolutions. The results show that the model using FFC can maintain better quality and consistency at unseen high resolutions. 

![image](https://github.com/user-attachments/assets/5c5a88a0-020e-4e93-8000-615fd445e7c5)

![image](https://github.com/user-attachments/assets/8c85fea1-bb9b-4b29-acd2-27e5db911fa6)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a simple yet effective single-stage image filling method, called LaMa. The method is based on Fast Fourier Convolution (FFC) and perceptual loss, and uses an aggressive mask generation strategy to train the model.
  
  2. LaMa has excellent performance in dealing with large masks, captures and generates complex periodic structures, and can be generalized to high-resolution images without increasing training data or computational cost.
 
  3. In addition, LaMa has the advantage of fewer trainable parameters and inference time cost.

### 2. Innovative points
  1. The main innovation of LaMa is that it employs FFC as the basis of the network architecture, which allows the network to obtain a larger effective receptive field for better understanding of the global image structure.
  
  2. LaMa introduces a perceptual loss function and an aggressive mask generation strategy to further improve the fill quality. These innovations enable LaMa to achieve better performance compared to existing state-of-the-art baselines without the need for complex two-stage models.
     
### 3. Future Works
Future research directions include exploring other types of convolutional operations, such as vision transformers, and investigating how to extend this approach to other computer vision tasks.
