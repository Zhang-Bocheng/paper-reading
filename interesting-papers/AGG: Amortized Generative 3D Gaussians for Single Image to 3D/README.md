# AGG: Amortized Generative 3D Gaussians for Single Image to 3D
[paper link](https://arxiv.org/pdf/2401.04099) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper describes a method called ‘Amortised Generative 3D Gaussians’ for converting single images into 3D models.         |  Generative Model        |

## Methodology

### 1. Abstract
While traditional optimisation-based methods require many computationally intensive fractional refinement steps, this approach eliminates the need for optimisation at each instance by using intermediate hybrid representations and joint optimisation, and utilises a hierarchical pipeline to generate rough 3D data and process it at high resolution.

![image](https://github.com/user-attachments/assets/fb8e6187-4109-4319-afcb-3cdaadc6d990)
### 2. Method Description 
The paper presents a neural network based image to 3D point cloud generation framework AGG (Amortised Generative 3D Gaussians). The framework is implemented through two stages: a coarse stage and a fine stage. In the coarse stage, AGG uses a hybrid generator to produce a hybrid representation as an intermediate generation target and decodes it into an explicit 3D Gaussian distribution. In the fine level, AGG uses a super-resolution module to introduce more 3D Gaussian distributions to improve resolution.

![image](https://github.com/user-attachments/assets/e702adff-99cb-49c6-ba0d-829191f98162)

### 3. Methodological improvements
Compared to traditional optimisation methods, the method uses automatic generation to avoid a tedious optimisation process. Also, the method extracts key information by using a pre-trained DINOv2 image encoder and increases the number of 3D Gaussian distributions by using feature expansion operations. In addition, the method utilises rich texture information to aid detail generation.

### 4. Issues addressed 
The method solves the problem in single image to 3D point cloud generation and is able to generate high quality 3D point cloud models quickly and efficiently. The method is applicable to a wide range of object types and has high generalisation capabilities.

## Experiments
This paper focuses on the authors' proposed AGG model and conducts comparative experiments with existing baseline methods. Specifically, the authors used the OmniObject3D dataset to train the model and performed quantitative and qualitative comparative analyses in a test set. Also, the authors conducted Ablation Studies on different components of the model to validate its effectiveness.

Firstly, the authors compared the AGG model with other sampling-based 3D generation methods such as Point-E and One-2345, as well as DreamGaussian. The authors use the CLIP distance to measure the similarity between multi-view rendered images and find that the AGG model performs very well in this regard. In addition, the AGG network is very fast in reasoning.

![image](https://github.com/user-attachments/assets/df4f94ca-842f-4b90-b3c3-f642d90039e2)

Secondly, the authors also conducted Ablation Study to compare the model performance after removing two components, Super Resolution and Texture Field, respectively. The results showed that the full AGG model produced the best results when rendered from a new viewpoint. In contrast, the model without Super Resolution resulted in low resolution and blurring due to the inability to obtain sufficient Gaussians, while the model without Texture Field resulted in erroneous geometry due to excessive pressure to predict texture information.  

![image](https://github.com/user-attachments/assets/5350f24c-e344-4fd9-9392-9b0a8aaf7d08)

## Conclusion

### 1. Advantages of the Thesis
The paper proposes a new single-image to 3D Gaussian distribution generation framework, AGG, which is capable of generating high-quality 3D Gaussian distributions quickly and learning all parameters at once in the training phase. Compared to existing optimisation and sampling methods, AGG has higher speed and better performance performance.
 
### 2. Innovative points
  1. AGG adopts a layered approach to generate 3D Gaussian distributions by first generating rough Gaussian distributions through a hybrid generator and then super-resolving them using a CNN to improve accuracy.
  
  2. What is more, AGG introduces two different transformers to predict geometric shape and texture information respectively, allowing the location and properties of the Gaussian distribution to be optimised simultaneously. 

### 3. Future Works
In future research, the authors would like to further extend AGG to be able to handle multiple objects and consider issues such as occlusion. And, the authors plan to explore how AGG can be used in conjunction with other 3D representations to better support larger scale 3D scene generation. 
