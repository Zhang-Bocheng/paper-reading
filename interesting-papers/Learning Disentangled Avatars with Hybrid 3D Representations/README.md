# Learning Disentangled Avatars with Hybrid 3D Representations
[paper link](https://arxiv.org/pdf/2309.06441) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This thesis presents Disentangled Avatars (DELTA), a hybrid explicit-implicit 3D representation method for learning animatable and realistic human avatars.          | Computer Vision         |

## Methodology

### 1. Abstract
DELTA uses monocular RGB video as input and produces a human avatar with separated body and clothing/hair layers. The method allows the human avatar to be modelled as a body or face versus clothing or hair, where the body or face is modelled using an explicit parameter-based 3D model and the clothing or hair is modelled using an implicit neural radiation field. 

DELTA has also designed an end-to-end differentiable renderer that integrates meshes into volumetric rendering, allowing it to be learnt directly from a monocular video without any supervision. Experimental results show that DELTA exhibits good performance on tasks such as decoupled reconstruction, virtual clothing fitting, and hairstyle transfer. In addition, DELTA can transfer hair and clothes to arbitrary body shapes. Finally, the authors have released an open source pipeline to facilitate future research.

### 2. Method Description 
The paper presents a system called DELTA for learning discrete head and body representations. The system captures elements such as faces, hair and clothing by using a hybrid explicit-implicit 3D representation and is able to recombine them in a high-quality manner. Specifically, the system uses the SMPL-X model as an explicit 3D representation of the human body shape and the NeRF model as an implicit 3D representation of hair and clothing. In addition, the system uses dynamic pose-dependent morphing techniques to capture human motion in the video.
![image](https://github.com/user-attachments/assets/3214b7af-8ad0-4202-bab9-6a74c302ee9c)

### 3. Methodological improvements
Compared to existing hybrid explicit-implicit 3D representations, DELTA employs a more flexible and expressive NeRF model for representing hair and clothing. In addition, the system introduces dynamic pose-dependent deformation techniques, making it possible to better capture human motion in videos.

### 4. Issues addressed 
The main goal of DELTA is to address the problem of how to reconstruct high-quality discretised head and body representations in monocular video. While traditional hybrid explicit-implicit 3D representations often struggle to accurately capture detail-rich elements such as hair and clothing, DELTA solves this problem by using the more flexible and expressive NeRF model. In addition, DELTA introduces dynamic pose-dependent morphing, which allows it to better capture human motion in video, thus further improving its reconstruction quality.

## Experiments
This paper focuses on the authors' method of capturing the clothing and hair of the characters in a video using a deep learning approach, and conducts comparative experiments with other existing methods. Specifically, the authors divide the clothing and hair in the video into two parts, which are captured and reconstructed using different NN models. 
![image](https://github.com/user-attachments/assets/1fa98599-abbb-4dbe-a678-43897f01e67d)

For clothing capture, the authors used a hybrid representation based on Neural Radiation Field (NeRF), which can efficiently capture different types of clothing and is capable of repositioning and changing shapes. As for hair capture, a hybrid representation based on a multilayer perceptron (MLP) is used, which can accurately capture a character's hair and enables hair transfer and shape change.

In terms of experiments, the authors first validated the effectiveness of the method using public datasets, including the People's Photo Studio, iPer and SelfRecon datasets. Then, the authors compared the method with existing methods, including NB, SMPLpix, Neural Body and Anim-NeRF. The results show that the authors' method is more accurate than the other methods, and especially performs better in clothing capture. In addition, the authors show some applications of the method, such as repositioning, facial expression capture, and virtual fitting. 
![image](https://github.com/user-attachments/assets/9d15edd2-a196-42dd-8f1e-7b92740801f3)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a method called DELTA, which enables the separate reconstruction of a human avatar and the human body by representing the face and body using a triangular mesh, while the hair and clothing are modelled using a Neural Radiation Field (NeRF).
  
  2. The method is effective in capturing the geometry of the different parts and is able to automatically extract the 3D model in a single video.
  
  3. In addition, the method has good visualisation and can be used in application areas such as virtual reality and virtual fitting.

### 2. Innovative points
  1. This approach not only captures the geometry of the different parts better, but also allows learning directly from a single video without introducing any 3D supervision.
  
  2. In addition, the paper devised a new volumetric renderer that not only drives the separation of different parts, but also enables end-to-end differentiable learning.
     
### 3. Future Works
Further research is needed to better handle lighting and material properties to improve realism. In future research, it would like to see more work focussed on these aspects in order to further improve and extend the range of applications of the method.  
