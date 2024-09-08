# Dynamic Hyperbolic Attention Network for Fine Hand-object Reconstruction
[paper link](https://arxiv.org/pdf/2309.02965) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |  This paper introduces a new hand object reconstruction method, Dynamic Hypersphere Attention Network (DHANet)         | graphical convolutional network        |

## Methodology

### 1. Abstract
The method exploits the intrinsic properties of hypersphere space by projecting image and mesh features into a uniform hypersphere space and using two modules - the -Dynamic Hypersphere Convolution and Image Attention Hypersphere Convolution, to learn representative feature information. Experimental results show that the method outperforms most existing methods on three public datasets, providing a promising alternative for fine-grained hand object reconstruction.

### 2. Method Description 
This paper presents a method called Dynamic Hyperbolic Attention Network (DHANet) for hand object reconstruction task. The method is based on image and 3D mesh data and uses a dynamic graph convolution network in hyperspherical space to learn feature representations. Specifically, DHANet consists of three main steps: **image-to-mesh estimation, dynamic hyperspherical map convolution, and attentional hyperspherical map convolution**.

![image](https://github.com/user-attachments/assets/9f7f6761-af7d-4b4f-97eb-bd39df47efcd)

In the **image-to-grid estimation phase**, each branch employs an encoder-decoder architecture, where the encoder consists of two pre-trained ResNet-18s and the decoder predicts the hand and object grids, respectively. The hand reconstruction decoder uses the MANO model to predict hand parameters from image features, while the object reconstruction decoder uses AtlasNet as its decoder.

In the **dynamic hyperspherical graph convolution stage**, the authors propose a three-step process: projection, graph construction and hyperspherical graph convolution. Firstly, the vertices are mapped onto the hypersphere and then the local graph structure is constructed by the hypersphere k-nearest neighbour algorithm. Finally, hyperspherical graph convolution is performed to learn node features.

In the **attention hypersphere graph convolution phase**, the authors introduce an image attention mechanism to capture the relationship between images and hand-object interactions. Specifically, the module consists of four steps: projection, graph construction, feature transformation and image attention. Firstly, the image features are mapped onto a hypersphere and then four different types of neighbours are computed based on the distance. Next, a Moebius layer is used to fuse the neighbour features with shallow and deep image features, and multimodal geometric-image features are learned through the image attention mechanism.

![image](https://github.com/user-attachments/assets/51ac5785-db53-4231-83b6-2e99bd450cb1)

### 3. Methodological improvements
  1. The DHANet method proposed in this paper improves the traditional graphical convolutional network by applying it to the hand-object reconstruction task dealing with tree-graph structures.
  
  2. The authors introduce dynamic hyperspherical graph convolution and image attention mechanisms, which enable better capture of hand-object interaction information.
  
  3. In addition, the authors employ the Moebius transform in hyperspherical space in order to reduce distortions while preserving local geometric information.

### 4. Issues addressed 
The DHANet method proposed in this paper aims to solve the hand-object reconstruction task, which is a challenging computer vision problem. Conventional methods often struggle to capture hand-object interaction information, making it difficult to achieve accurate reconstruction. However, by applying graphical convolutional networks to the hand-object reconstruction task that deals with the structure of tree diagrams, the method proposed in this paper can better capture the hand-object interaction information and thus achieve more accurate reconstruction.

## Experiments
This paper focuses on a deep learning approach to hand object reconstruction and conducts several comparative experiments to validate its effectiveness. Specifically, the authors use three publicly available datasets (Obman, FHB, and HO-3D) to conduct experiments and compare them with existing single-image hand object reconstruction methods. 

Among them, the authors' method belongs to the category of unknown object models and uses two modules, dynamic hyperspherical convolution and image-attentive hyperspherical convolution, to enhance feature expressiveness. In their experiments, the authors used metrics such as hand error, object error, and contact metrics to evaluate the reconstruction quality and came up with the following conclusions:

<br>&emsp; On the Obman dataset, the authors' method performs better than the benchmark method with smaller hand error and object error;
![image](https://github.com/user-attachments/assets/718c744c-da21-4f47-8e78-83db768f5d27)

<br>&emsp; On the FHB dataset, the authors' method also achieved SOTA results with smaller hand and object errors;
![image](https://github.com/user-attachments/assets/f829f306-f06f-440f-8f87-055f9b14df71)

<br>&emsp; On the HO-3D dataset, the authors' method also achieved SOTA level with smaller hand and object errors;
![image](https://github.com/user-attachments/assets/23e48ff1-e0ef-48e2-b54f-bebd2ef46df7)

<br>&emsp; The experimental results show that the authors' method is applicable not only to synthetic data but also to data from real scenes;
<br>&emsp; Hyperspherical space can better preserve geometric information, thus improving feature representation and model performance;
<br>&emsp; Dynamic hyper-spherical convolution and image-attentive hyper-spherical convolution can effectively enhance the feature expression ability and further improve the model performance.  
![image](https://github.com/user-attachments/assets/81b5c8ad-3bbe-485c-ae1f-47d7ce3f661d)

## Conclusion

### 1. Advantages of the Thesis
In this paper, a method based on Dynamic Hyperspherical Attention Network (DHANet) is proposed to solve the hand object reconstruction problem. The method employs hyperspherical space in processing hand object images or meshes, which results in better preservation of geometric information and the ability to learn more representative multimodal features. Experimental results show that the method achieves better performance on three public datasets compared to existing methods.

### 2. Innovative points
The main contributions of the paper are the first application of hyperspherical space to the task of hand object reconstruction, and the proposal of new modules such as dynamic hyperspherical map convolution and hyperspherical attention map convolution for effective modelling of hand object geometric information and learning of interaction relations. These innovations provide new ideas and directions for subsequent research.

### 3. Future Works
Although this paper has achieved some successes, there are still some challenges that need to be further explored. For example, there are issues such as how to take advantage of other properties in hyperspherical space to improve the model performance, and how to effectively deploy and optimise the model in real-world applications. Therefore, future research can further explore these issues and try to propose more effective and practical methods for hand object reconstruction.  
