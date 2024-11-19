# Make-A-Shape: a Ten-Million-scale 3D Shape Model
[paper link](https://arxiv.org/pdf/2401.11067) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a novel 3D generative model called ‘Make-A-Shape’, which can efficiently generate high-quality 3D shapes under large-scale training and can be trained with 10 million publicly available 3D shapes.          | Diffusion Model         |

## Methodology

### 1. Abstract
The model employs an innovative waveform tree representation and diffusion model for efficient encoding and decoding, and also introduces a subband adaptive training strategy to improve model learning. In addition, the model can be controlled by additional input conditions, which enables the generation of data from a wide range of modalities, such as single/multi-view images, point clouds and low-resolution voxels. Experimental results show that the model achieves excellent performance in unconditional generation, shape complementation and conditional generation, and is capable of rapidly generating high-quality 3D shapes in a matter of seconds.

### 2. Method Description 
This thesis proposes a generative framework for large-scale 3D shape data that enables efficient training and storage through the use of a waveform tree representation. Firstly, each 3D shape is converted into a high-resolution discrete curvature field (TSDF), which is then decomposed into sub-band coefficients at multiple scales using the TSDF, and these coefficients are used to construct a waveform tree representation with a hierarchical structure. Second, an adaptive training strategy based on the relationship between parent and sibling nodes is designed in order to enable the model to learn the detail information effectively. Finally, to support condition generation, the input conditions are encoded as a series of latent vectors and injected into the generative network.

![image](https://github.com/user-attachments/assets/13146911-8259-4481-8793-0be86a0c9031)
 
### 3. Methodological improvements
  1. The main improvement of the method over traditional 3D shape generation methods is the adoption of a waveform tree representation, which makes the model more efficient and scalable when dealing with large-scale 3D shape data.
  2. In addition, an adaptive training strategy is designed, which can better balance the importance of detail information at different scales, thus improving the learning effect of the model. The method also supports conditional generation, which can generate corresponding 3D shapes based on different input conditions.

![image](https://github.com/user-attachments/assets/ce94ed6f-d157-498f-82cb-adcdb375ed10)

### 4. Issues addressed 
  1. How to efficiently process large-scale 3D shape data;
  2. How to learn the detail information in 3D shapes efficiently;
  3. How to support conditional generation to generate corresponding 3D shapes according to different input conditions.

## Experiments
This paper focuses on a 3D shape generation method based on diffusion modelling and verifies its performance and advantages through several comparative experiments. Specifically, the authors conducted the following comparison experiments:

**Comparison of shape generation under single/multiple view image conditions:** the authors use single/multiple view images as input conditions to compare with the traditional primitive model. The experimental results show that the authors' method outperforms the traditional method in metrics such as intersection and concurrency ratio (IoU) and light field distance (LFD).

![image](https://github.com/user-attachments/assets/77e7cf79-48b9-4ec6-92f3-8e0ab297cf6a)

**Comparison of shape generation under point cloud conditions:** the authors compare the authors' method with the traditional low-resolution voxel mesh method by using point cloud as an input condition. The experimental results show that the authors' method not only generates smoother and cleaner surfaces, but also has better performance for fewer points.

![image](https://github.com/user-attachments/assets/d1b739b3-a746-437c-a9df-6db01035c5d4)

**Comparison of shape generation under low-resolution voxel conditions:** The authors use low-resolution voxels as input conditions to compare with traditional linear interpolation methods. The experimental results show that the authors' method significantly outperforms the traditional method, achieving better results in metrics such as intersection and concurrency ratio (IoU) and light field distance (LFD).

![image](https://github.com/user-attachments/assets/a62a9ba7-f239-4593-b447-50b92011efac)

**Comparison of Shape Generation under Zero Sample Conditions:** the authors show that the method can perform the shape generation task under zero sample conditions and compare it with other methods. The experimental results show that the authors' method can generate diversified outputs and can be complementary for missing parts.

**Subband adaptive training strategy for 3D shape generation methods based on diffusion model:** the authors achieve the optimisation of 3D shape generation methods by adjusting the learning weights of different subband coefficients. The experimental results show that this adaptive training strategy can significantly improve the generation effect.

![image](https://github.com/user-attachments/assets/f4f3fd2f-859f-4e79-935d-1394591cdbcb)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a novel 3D generative framework called Make-A-Shape that can produce high-quality 3D shapes efficiently within seconds.
  2. The proposed framework uses a family of new techniques such as subband coefficient filtering scheme and a subband adaptive training strategy to ensure model training that can effectively attend to both coarse and sparse detail coefficients.
  3. The authors conduct extensive experiments demonstrating the superiority of their approach in terms of synthesizing high-quality 3D shapes across various challenging conditions.

### 2. Innovative points
  1. The paper introduces a family of new techniques such as the subband coefficient filtering scheme and the subband adaptive training strategy to ensure model training that can effectively attend to both coarse and sparse detail coefficients.
  2. The authors use a combination of various modalities such as single/multi-view images, point clouds, and low-resolution voxels to train their generative model.
  3. The authors also propose extending Make-A-Shape to take optional condition inputs of various modalities. 

### 3. Future Works
  1. The authors suggest that their work will pave the way for future research in other 3D representations to enable large-scale 3D model training.
  2. The paper opens up possibilities for future research in areas such as multimodal input conditioning for better control over generated shapes.
  3. The authors' work could potentially be extended to include other types of constraints such as semantic segmentation masks or user-defined labels for more fine-grained control over generated shapes.  
