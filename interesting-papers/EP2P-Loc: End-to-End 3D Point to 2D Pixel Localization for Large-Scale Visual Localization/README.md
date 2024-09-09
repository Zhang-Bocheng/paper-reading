# EP2P-Loc: End-to-End 3D Point to 2D Pixel Localization for Large-Scale Visual Localization
[paper link](https://arxiv.org/pdf/2309.07471) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper introduces a new large-scale visual localisation method, EP2P-Loc.          | Computer Vision         |

## Methodology

### 1. Abstract
The method increases the correctness of matching by removing invisible 3D points and not detecting keypoints, and employs coarse-to-fine-grained feature extraction to reduce memory usage and search complexity. In addition, the method applies a differentiable PnP algorithm for end-to-end training for the first time. Experimental results show that the method outperforms existing visual localisation and image-to-point cloud registration methods on new datasets based on 2D-3D-S and KITTI.

### 2. Method Description 
The paper presents a method called EP2P-Loc for predicting the 6-DoF camera pose of a given 2D image in a 3D global reference map. The method assumes that the global map is divided into multiple sub-maps and gives information about the 2D image, the positive sample point cloud sub-map, the negative sample point cloud sub-map, the camera pose matrix, and the camera internal reference matrix during the training process.

In the testing phase, the method first extracts the feature vectors of the 2D image and the point cloud sub-map, then removes the invisible points using the IPR algorithm, followed by obtaining the local and global feature vectors of the point cloud sub-map through the Fast Point Transformer network. Finally, the feature vectors of the 2D image and the point cloud sub-map were fed into different classifiers to determine if each point belonged to the image and projected into the image coordinate system. Ultimately, these matched points are placed into a differentiable PnP layer to learn the best 2D-3D correspondence and estimate the camera pose.

![image](https://github.com/user-attachments/assets/339552ff-020e-4f8b-9599-eb404dab7952)

### 3. Methodological improvements
Compared to traditional SLAM methods for monocular vision, the EP2P-Loc method introduces the concept of point cloud sub-maps, which can more accurately capture the geometrical structures in the scene and can effectively deal with occlusion problems. In addition, the method employs an IPR algorithm to remove invisible points, which improves the matching accuracy. The method also uses a differentiable PnP layer to optimise the estimation results of the camera pose, making the whole system more stable and reliable.

### 4. Issues addressed 
The EP2P-Loc method mainly solves some challenging problems in monocular vision SLAM, such as occlusion, light variation, scale variation, etc. By introducing point cloud sub-maps and IPR algorithms, the method can better handle these problems and improve the estimation accuracy of camera pose. In addition, the method can be applied to real-time SLAM and multimodal SLAM, etc., which has a wide range of application prospects.

## Experiments
This paper focuses on image- and point cloud-based visual localisation methods and conducts several comparative experiments to verify their performance. Specifically, the authors compare the performance of the method with six existing image-to-image, image-to-RGB-D and RGB-D-to-RGB-D localisation methods on three different datasets, and the results are analysed and discussed in detail.

Firstly, in the visual localisation task, the authors compare the method with six other methods, including DSAC*, SfM methods (e.g. COLMAP and Kapture), and local feature extraction based methods such as Super-Point, D2-Net and HLoc. The experimental results show that the method outperforms and outperforms other methods on all three datasets and has a faster runtime.

![image](https://github.com/user-attachments/assets/b83cda70-55c8-41c5-abf8-baba4c4928c2)

Second, in the image-to-point cloud registration task, the authors compare the method with two existing methods, namely 2D3D-MatchNet and DeepI2P. The experimental results show that the method shows better performance on the KITTI dataset, outperforms the other methods, and can more accurately estimate the relative pose between the camera and the point cloud.

![image](https://github.com/user-attachments/assets/50065aad-42c0-433e-b1b0-ddef5ac55b41)

In addition, the authors conducted several sub-experiments to further validate the effectiveness of the method. For example, they tested the IPR algorithm and found that it can significantly reduce the number of redundant points in the point cloud and can improve operational efficiency without degrading performance. They also analysed the performance of the method by varying the parameters in terms of the number of global matching candidates, 2D pixel coordinate calculation and 2D pixel classification, and drew relevant conclusions. 

![image](https://github.com/user-attachments/assets/7a1f320f-d5d0-4d47-9748-9e9b3a743773)

## Conclusion

### 1. Advantages of the Thesis
  1. This research presents a novel approach to solving problems in large-scale visual localisation tasks.
  
  2. The researchers employed effective strategies to reduce memory usage and computational cost, and were able to handle invisible 3D points.
  
  3. The researchers also employed an end-to-end trainable PnP solver for high-quality 6-DoF pose estimation.
  
  4. The method demonstrated state-of-the-art performance in benchmark tests on large indoor and outdoor environments.

### 2. Innovative points
  1. The method solves the problem of discrepancies between different representations by efficiently learning the features of 2D pixels and 3D points.
  
  2. The method is able to select relevant subgraphs at the coarse-grained level and find accurate 2D-3D correspondences at the fine-grained level.
  
  3. The method also employs a visible 3D point removal algorithm that can handle invisible 3D points.
  
  4. The method also employs an end-to-end trainable PnP solver for high quality 6-DoF attitude estimation.

### 3. Future Works
  1. The method has high practical value for large-scale visual localisation tasks and can be widely used in areas such as autonomous driving, robot navigation and augmented reality.
  
  2. Future research can explore how to further improve the accuracy and efficiency of the method and how to apply it to more complex scenes and environments.
  
  3. Combining the method with other techniques, such as deep learning and machine learning, can be considered to achieve better performance and results. 
