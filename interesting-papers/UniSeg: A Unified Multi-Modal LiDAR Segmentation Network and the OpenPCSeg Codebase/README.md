# UniSeg: A Unified Multi-Modal LiDAR Segmentation Network and the OpenPCSeg Codebase
[paper link](https://arxiv.org/pdf/2309.05573) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents a multimodal LiDAR segmentation network called UniSeg, which can perform both semantic and panoramic segmentation tasks and is able to utilise information from three representations (i.e., point, voxel and distance) of RGB images and point clouds.          | Computer Vision         |

## Methodology

### 1. Abstract
The authors designed two modules: the **Learnable cross-Modal Association (LMA)** module is used to automatically fuse the voxel view and distance view features with the image features so as to fully utilise the rich semantic information of the images, while the **Learnable cross-View Association (LVA)** module is used to combine the enhanced The Learnable cross-View Association (LVA) module is used to transform the enhanced voxel view and distance view features into the point space and further adaptively fuse the features of the three point cloud views.

The experimental results show that UniSeg achieves excellent performance on three public benchmark datasets, with top rankings on SemanticKITTI, nuScenes and Waymo Open Dataset (WOD). In addition, the authors have built a codebase called OpenPCSeg, which contains the most popular outdoor LiDAR segmentation algorithms with reproducible implementations. The codebase will be made publicly available for use.

![image](https://github.com/user-attachments/assets/e481751b-5af7-4d80-a506-2e39e0e6fe41)

### 2. Method Description 
The paper presents a single network semantic segmentation and panoramic segmentation method called UniSeg. The method uses point clouds, RGB images and range maps as inputs and performs semantic segmentation and panoramic segmentation tasks in a single network. UniSeg employs adaptive cross-modal fusion and cross-view correlation modules to achieve multi-view feature fusion, which improves segmentation accuracy. 

Specifically, the method firstly corresponds the point cloud to the RGB image through a camera calibration matrix, and then uses an adaptive cross-modal fusion module to fuse the point cloud and range map features with the image features. Finally, the cross-view correlation module is used to fuse the features of the three views to obtain the final segmentation result.

![image](https://github.com/user-attachments/assets/de1843cd-7d6f-4245-b484-e2bf520afc44)

### 3. Methodological improvements
Compared to other multi-view fusion methods, UniSeg uses an adaptive cross-modal fusion module and a cross-view association module, which can better deal with the number mismatch problem and dynamically select the most important features to be fused between different views, thus improving the segmentation accuracy.

### 4. Issues addressed 
UniSeg mainly solves the quantity mismatch problem and the selection problem of feature fusion in multi-view data fusion, thus improving the segmentation accuracy. Also, the method is applicable to semantic segmentation and panoramic segmentation tasks in multiple scenarios.

## Experiments
This paper focuses on the performance of UniSeg, a multimodal fusion network, on the LiDAR semantic segmentation task and compares it with several baseline approaches. Specifically, the authors employ three popular baseline datasets (nuScenes, SemanticKITTI, and Waymo Open) to test UniSeg's performance and use the intersection-to-union ratio (IoU) and the overall average intersection-to-union ratio (mIoU) as evaluation metrics. In addition, the authors compare the unimodal and multimodal performances at different distances and analyse the effect of each module as well as the impact of different fusion strategies.

First, in terms of quantitative results, UniSeg achieves excellent performance on all three datasets. For example, on the SemanticKITTI dataset, UniSeg's mIoU score of 69.6 exceeds the 2.2 IoU points of SPVCNN. In addition, UniSeg also obtained a panoptic quality (PQ) of 78.4 on the Waymo Open dataset, which is comparable to its competitor SPVCNN++. Overall, these results show that UniSeg is an effective multimodal fusion network that can significantly improve the accuracy of LiDAR semantic segmentation.

![image](https://github.com/user-attachments/assets/dddbc9c8-7f26-4678-9c87-f24ed35995ee)

Second, in a comparison of efficiency and accuracy, UniSeg has the best accuracy when compared to other methods in terms of parameters and latency. Specifically, when reducing the parameters to 0.2 times of the original, UniSeg still achieves faster speeds while maintaining higher accuracy. This demonstrates that UniSeg can provide efficient solutions in real-world applications.

![image](https://github.com/user-attachments/assets/fb308f5e-55f5-4bbd-a350-301aaa68e69f)

Finally, UniSeg shows strong robustness and stability in various experiments. For example, UniSeg's LMA module is more robust than other methods in the face of errors caused by imperfect calibration matrices. In addition, by adding Gaussian noise to simulate errors in real environments, UniSeg also shows better immunity to interference.  

![image](https://github.com/user-attachments/assets/21198079-fe67-4cc0-86a5-f3c2bd18d579)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes UniSeg, a unified multimodal LiDAR segmentation network that is capable of simultaneous semantic and panoramic segmentation and utilises RGB images and point clouds of three views as input data.
  
  2. To fully utilise the information from different modal data, the article proposes a cross-modal association module (LMA) and a learnable cross-view association module (LVA), and achieves impressive performance, ranking first in three popular LiDAR segmentation benchmarks.
  
  3. In addition, the article builds the OpenPCSeg codebase with the aim of providing reproducible and consistent implementations to facilitate the development of related research.

### 2. Innovative points
  1. The main contribution of this article is to propose a new multimodal fusion framework that jointly processes RGB images and point clouds from three views, thus improving the accuracy and robustness of perception.
  
  2.  Specifically, the cross-modal association module (LMA) and the learnable cross-view association module (LVA) proposed in the article are able to effectively fuse data from different modalities and achieve leading performance in several benchmark tests.
  
  3.  In addition, the authors have built a codebase called OpenPCSeg, which aims to provide reproducible and consistent implementations to help researchers better evaluate different LiDAR segmentation algorithms.

### 3. Future Works
Future research directions include further optimising the model structure to improve its efficiency and accuracy; exploring more multimodal data sources, such as cameras and radars; and combining multimodal fusion techniques with other perception techniques to build more complete and reliable perception systems. 
