# Towards Practical Capture of High-Fidelity Relightable Avatars
[paper link](https://arxiv.org/pdf/2309.04247) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents a new framework called Tracking-free Re-lightable Avatar (TRAvatar) for capturing and reconstructing high-fidelity 3D avatars.          |   Computer Vision       |

## Methodology

### 1. Abstract
 TRAvatar works in a more practical and efficient setup than previous approaches. It uses dynamic image sequences trained in Light Stage to achieve realistic re-lighting effects under different lighting conditions and provides real-time animation of avatars in various scenes. In addition, TRAvatar allows trackless avatar capture, removing the need for accurate surface tracking under different lighting conditions. 
 
The main contributions of this paper are twofold: first, the authors present a novel network architecture that explicitly establishes and ensures the fulfilment of linear illumination. Based on simple group light source capture, TRAvatar can predict real-time appearance and achieve high-quality relighting effects under arbitrary environment mapping with only one-way forward passes. Second, they jointly optimise facial geometry and relightable appearance from scratch based on image sequences, where tracking is implicitly learned. This tracking-free approach leads to robustness to temporal correspondences between frames under different lighting conditions. Extensive qualitative and quantitative experiments show that our framework achieves superior performance in realistic avatar animation and relighting.

![image](https://github.com/user-attachments/assets/44111880-97ce-4d3f-a465-3771e8377c0f)

### 2. Method Description 
The paper presents a novel framework called TRAvatar for learning high-fidelity 3D virtual avatars that are animatable, relightable and renderable. The method is based on the variational autoencoder (VAE) architecture and uses a hybrid voxel representation to construct the 3D model. During training, they use multi-view image sequences as well as dynamic expression capture data under different lighting conditions to achieve separated motion and expression-related motion through self-supervised learning. In addition, they designed a special appearance decoder for linear illumination properties to enable real-time relighting.

![image](https://github.com/user-attachments/assets/369b2db7-20a9-4ee8-93ad-29905d7266b1)

### 3. Methodological improvements
Compared to the previous method, the method does not need to track geometric information for training. Also, they used customised capture devices including 356 lighting units and 24 machine vision cameras to capture dynamic expressions under various lighting conditions. In addition, their special appearance decoder is able to strictly satisfy the linear illumination property, which improves the generalisation ability.

![image](https://github.com/user-attachments/assets/0f2a6344-e58e-4137-8fc3-a6ee112a806b)

### 4. Issues addressed 
The approach addresses the problem of creating animatable, relightable and renderable high-fidelity 3D virtual avatars in real-time. Through self-supervised learning, they successfully separate motion from expression-related motion and achieve high-fidelity reconstruction with linear illumination. This approach has a wide range of promising applications in areas such as game development, virtual reality and digital humans.

## Experiments
This paper conducts several comparative experiments to verify the effectiveness of its proposed 3D face modelling method based on hybrid voxel representation. Specifically, the authors conducted the following four experiments:

**Quality evaluation experiments**: by showing two examples of humanoid models using hybrid voxel representations, it is demonstrated that the method is able to achieve separation of light and motion and can be naturally used in applications such as video-driven animation and relighting.

![image](https://github.com/user-attachments/assets/560d55a3-1f6b-4237-92f5-cd6775198e03)

**Experimental Comparison with MVP Method**: The proposed method is compared with the MVP method on the publicly available Multiface dataset. The results show that even without the computationally intensive tracking process, the quantitative reconstruction error of the proposed method is slightly lower than that of MVP+ and avoids information loss.

**Comparison experiments with Deep Portrait Relighting (DPR) method**: the proposed method is compared with the DPR method under the same input conditions. The results show that DPR cannot predict the correct relighting effect, while the proposed method can achieve portrait relighting more realistically.

**Ablation Study Experiment on Linear Illumination Branching Design**: The proposed method was compared with four other alternative design options to evaluate the effectiveness of linear illumination branching. The results show that linear illumination branching significantly improves the generalisation performance, making the method more suitable for relighting.  

## Conclusion

### 1. Advantages of the Thesis
  1. A new framework, called TRAvatar, is proposed for capturing and reconstructing high-fidelity and relightable 3D avatars in practical and efficient settings.
  
  2. The framework is trained with dynamic image sequences to achieve natural relighting and video-driven animation under different lighting conditions.

  3. Experimental results show that the framework achieves superior performance in realistic avatar animation and relighting, facilitating 3D avatar content creation.
Methodological Innovation Points

Future Perspectives
 
### 2. Innovative points
  1. A network architecture is designed to satisfy linear illumination properties, enabling real-time appearance prediction and high-quality relighting effects.
  
  2. Proposes to jointly optimise facial geometry and relightable appearance based on image sequences, implicitly learning base mesh deformations.
  
  3. Robustness is provided using a tracking free scheme to establish inter-frame correspondences under different illumination conditions.
  
  4. The proposed method provides higher efficiency and flexibility compared to traditional graphical pipeline methods.
     
### 3. Future Works
  1. With data capture devices being expensive, there is a need to explore more affordable devices to create relightable avatars.
 
  2. The study indicated that the lack of sufficient surface constraints makes precise manual control difficult, so more flexible control methods can be further investigated.
 
  3. Research into near-field and high-frequency relighting and accessories such as glasses are also directions worth exploring. 
