# GO-SLAM: Global Optimization for Consistent 3D Instant Reconstruction
[paper link](https://arxiv.org/pdf/2309.02436) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a deep learning visual SLAM framework called GO-SLAM that aims to achieve real-time global optimization and consistent 3D reconstruction.          | Deep Learning         |

## Methodology

### 1. Abstract
The method supports robust pose estimation through efficient loop closure and online full-beam adjustment, and performs per-frame optimization using global geometric information learned from the input frame history. Also, the method updates the implicit continuous surface representation in real time to ensure the consistency of the 3D reconstruction. Experimental results show that GO-SLAM outperforms existing methods in terms of tracking robustness and reconstruction accuracy, and can handle monocular, binocular and RGB-D inputs.

### 2. Method Description 
This paper proposes a keyframe based SLAM framework for achieving real-time, globally consistent 3D reconstruction. This framework utilizes keyframe tracking and real-time mapping capabilities for online drift correction to achieve this goal. This framework consists of two parts: **Forward Tracking and Backward Optimization**.

In forward tracking, the system calculates the optical flow between the current frame and the nearest keyframe by applying the RAFT algorithm, and determines whether to create a new keyframe based on the average optical flow size. Then, the system combines all the created keyframes into a keyframe graph and performs loop closure detection and global optimization based on it. Loop closure detection is the process of detecting whether there is a loop between adjacent keyframes within a local window, and if so, connecting them together to form a longer trajectory. Global optimization utilizes a Dense Beam Adjustment (DBA) layer to perform nonlinear least squares optimization on the position and depth of all keyframes, in order to correct camera pose and reverse depth.

In backward optimization, the system runs full BA to correct trajectory errors of historical keyframes and updates them to new keyframes in real-time tracking. In addition, to address the issue of global consistency, the system adopts a filtering strategy to select keyframes that need to be updated, and introduces a rendering network to accelerate the reconstruction of the scene.

![image](https://github.com/user-attachments/assets/0e3bc7c5-6454-4b83-af38-56740755829d)

### 3. Methodological improvements
This framework improves the robustness and stability of the system by combining loop closure detection and global optimization. In addition, by using the DBA layer for dense beam adjustment, it is possible to better handle issues such as local occlusion and echo. In addition, the system also adopts filtering strategies and rendering networks to accelerate the reconstruction speed of the scene, thereby achieving real-time performance.

![image](https://github.com/user-attachments/assets/f60984c5-5ec2-4442-be54-19037c207df6)

### 4. Issues addressed 
This framework solves important problems in SLAM, such as keyframe selection, loop closure detection, global optimization, and scene reconstruction, enabling the system to achieve real-time and globally consistent 3D reconstruction. In addition, due to its high robustness and stability, the framework is suitable for various environments and application scenarios.

## Experiments
This paper focuses on the Deep Learning SLAM system GO-SLAM proposed by the authors and compares it with several sets of experiments, including comparison with traditional SLAM methods and comparison with other deep learning SLAM systems. The details of each comparison experiment are described below:

**Comparison experiments on the TUM RGB-D dataset**
The authors compare GO-SLAM with traditional SLAM methods for point cloud representation as well as the recent NeRF-based RGB-D SLAM methods. The experimental results show that GO-SLAM has lower average trajectory errors for both monocular and RGB-D inputs, and better performance performance relative to other NeRF-based RGB-D SLAM methods.

**Comparative experiments on the EuRoC dataset**
The authors compare GO-SLAM with existing stereo SLAM methods. The experimental results show that GO-SLAM is able to produce camera trajectories that are comparable to the best existing stereo SLAM methods and is able to generate more complete and smoother 3D reconstruction models.

![image](https://github.com/user-attachments/assets/a9a92ad3-fe93-4608-84cf-d243538ce1d3)

**Comparative experiments on the ETH3D-SLAM dataset**
The authors compared GO-SLAM with methods based on point clouds, surface elements and voxels. The experimental results show that GO-SLAM has higher accuracy than the other methods with RGB-D inputs and is able to generate smoother and more plausible 3D reconstruction models.

**Comparative experiments on the ScanNet dataset**
The authors tested several short and long complex sequences and compared GO-SLAM with other methods such as DROID-SLAM. The experimental results show that GO-SLAM provides the best tracking performance and 3D reconstruction quality in all cases and can be run in real-time.

**Comparative experiments on the Replica dataset**
The authors compare GO-SLAM with existing RGB-D methods and monocular methods. The experimental results show that GO-SLAM performs well in terms of both accuracy and speed, and that real-time operation can be achieved without sacrificing accuracy.

## Conclusion

### 1. Advantages of the Thesis
  1. This thesis presents a deep learning-based SLAM algorithm that enables globally consistent 3D reconstruction in real-time and supports monocular, binocular or RGB-D inputs.
  
  2. The algorithm minimises trajectory errors by detecting loop closure and online full BA, while providing an efficient, compact and multi-resolution 3D representation using NeRF.

  3. Experimental results show that the algorithm is robust and reliable in handling large-scale scenes, and in particular achieves state-of-the-art performance in tracking long-range monocular trajectories without depth information.
 
### 2. Innovative points
  1. The paper presents a novel deep learning SLAM algorithm that enables real-time globally consistent 3D reconstruction and supports monocular, binocular or RGB-D inputs.

  2. The algorithm employs the Neural Radiation Field (NeRF) technique for efficient 3D representation and also implements an online full BA to optimise the 3D geometry throughout the keyframe history.
  
  3. The algorithm also introduces advanced techniques such as on-the-fly mapping and Neural Implicit Networks that allow the 3D reconstruction to be updated at a high frequency, thus ensuring global consistency and maintaining a high-quality 3D representation while capturing local details.
     
### 3. Future Works
  1. The deep learning SLAM algorithm proposed in this paper provides a new direction for future vision SLAM research, especially in monocular camera setups, which can better solve the drift problem.
  
  2. It can be further explored how the algorithm can be applied to more complex scenes, such as outdoor environments or multi-sensor fusion systems.
  
  3. Consideration could also be given to how other techniques, such as depth estimation or semantic segmentation, could be combined to improve the accuracy and robustness of the algorithm.
