# Generative Image Dynamics
[paper link](https://arxiv.org/pdf/2309.07906) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | The paper presents a deep learning based video prediction system for converting single images into video sequences with natural fluctuating motion.           |  Deep Learning        |

## Methodology

### 1. Abstract
This paper presents a method for modelling scene motion based on an image-space prior. The method learns a motion prior by extracting motion trajectories from real video sequences and represents dense, long-term motion as a spectral volume. This approach is suitable for diffusion modelling during prediction and can transform individual images into motion textures for the whole video. In addition, the motion representation can be used for downstream applications such as converting static images into seamlessly looping videos or allowing users to interact with objects in the actual image to produce realistic simulated motion effects.

### 2. Method Description 
The system consists of two modules: **a module for predicting motion and a module for rendering images**. In the motion prediction module, a frequency space representation is used to model the natural motion with a power spectrum distribution dominated by low frequency components. In the image rendering module, future frames are synthesised by mapping the predicted motion texture onto the input image and using the feature pyramid soft interpolation technique.

![image](https://github.com/user-attachments/assets/bd4d0c60-a878-4465-97d4-f9c61659df6a)

### 3. Methodological improvements
Compared to the traditional pixel space diffusion model, this paper uses a more efficient frequency space representation for motion prediction. In addition, in order to avoid the problem of over-smoothing due to an excessive number of channels in the training data, a frequency-coordinated noise reduction strategy is proposed, which coordinates the prediction results of all frequency bands in the frequency domain to produce more accurate motion prediction results.

### 4. Issues addressed 
  1. Converting a single still image into a video sequence with natural fluctuating motion.
  
  2. Producing videos with slow motion or zoomed-in animation effects.
  
  3. Producing videos with seamless looping.
  
  4. Implementing interactive motion simulations using a single image.

## Experiments
This paper focuses on the use of a continuous spectral volume representation to generate periodic motion videos in natural scenes and compares it with other methods. Specifically, the method employs LDM as the backbone of the predicted spectral volume and is trained using VAE. In addition, 2D U-Net was used for iterative denoising and frequency-coordinated denoising, and was run on DDIM for 250 steps to obtain better results. For quantitative evaluation, the authors trained all the methods on images of the same size 256x160 and evaluated them using metrics such as FID and KID. Whereas for qualitative evaluation, it was evaluated by visualising the generated future frames and comparing them with a real reference video.

![image](https://github.com/user-attachments/assets/ecd20f27-02fd-4d12-8c6b-5e3da17c43b6)

In comparison with single image animation and video prediction methods, the method significantly outperforms the others, both in terms of image synthesis quality and video synthesis quality. Specifically, its FVD and DT-FVD distances are lower, indicating that the generated videos are more realistic and more temporally consistent. In addition, the authors also evaluated the sliding-window FID and sliding-window DT-FVD distances for the generated videos of the different methods, and found that no temporal degradation occurs using the global spectral volume representation. 

![image](https://github.com/user-attachments/assets/0e724c24-7119-4fd0-9f5e-d9b52802fb29)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a new method to simulate oscillatory dynamics in nature that uses a frequency-domain representation that can effectively predict low-frequency vibrations and can be solved for non-oscillatory motions or high-frequency vibrations by learning motion primitives.
  
  2. In addition, the authors experimentally demonstrate that the method can produce realistic animation effects and has potential application in several downstream applications.

### 2. Innovative points
  1. The methodological innovation of this paper lies in the adoption of a frequency-domain representation to model the oscillatory dynamics of nature and the ability to improve the generalisation of the model by learning the motion primitives.
  
  2. Also, the authors propose an attention module that coordinates predictions between different frequency bands, enabling the model to capture the dynamic characteristics of the object more accurately.
     
### 3. Future Works
  1. Future research directions can be taken from the following aspects: firstly, further research can be conducted on how to apply the method to other types of scenes, such as water flow, clouds, etc.;
  
  2. It can be explored how to combine the method with other techniques, such as object detection and tracking algorithms based on deep learning, in order to achieve more complex and realistic animation effects;
  
  3. It can be attempted to extend the method to the three-dimensional space object motion modelling in 3D space to achieve a more realistic and vivid virtual reality experience.  
