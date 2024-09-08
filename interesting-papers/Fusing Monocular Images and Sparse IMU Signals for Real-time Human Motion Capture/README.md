# Fusing Monocular Images and Sparse IMU Signals for Real-time Human Motion Capture
[paper link](https://arxiv.org/pdf/2309.00310) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |  This paper presents a new motion capture method that fuses monocular images and sparse inertial measurement unit (IMU) signals to address occlusion, extreme lighting/texture, and out-of-view problems in visual motion capture, and also to mitigate the global drift problem in inertial motion capture.         | Deep Learning         |

## Methodology

### 1. Abstract
The authors propose a two-coordinate strategy to better estimate the body pose by utilising different targets of the IMU signals in each of the two branches, and also introduce a hidden state feedback mechanism to compensate for the drawbacks in the case of different inputs. Experimental results show that by carefully designing the fusion method, the technique significantly outperforms existing visual, inertial and combinatorial methods for global orientation and local pose estimation. 

### 2. Method Description 
This thesis presents a real-time motion capture system based on the fusion of vision and inertial sensors. The system utilises deep learning techniques and adopts a dual coordinate system strategy to improve the accuracy and robustness of the system. The system is able to provide reliable motion estimation results from inertial sensors when visual signals are unreliable or unavailable.

![image](https://github.com/user-attachments/assets/8f576f3f-9698-4645-a118-4fc10d645f39)

### 3. Methodological improvements
The system uses a dual-coordinate system strategy where the visual and inertial signals are processed and fused separately. When the visual signals are reliable, the system uses the visual signals for motion estimation; when the visual signals are unreliable, the system uses only the inertial signals for motion estimation. In addition, the system uses a hidden state feedback mechanism to further improve the accuracy and robustness of the system.

### 4. Issues addressed 
Conventional motion capture systems rely heavily on visual signals, but suffer from degraded accuracy due to problems such as occlusion and insufficient light. In contrast, the system combines information from vision and inertial sensors and is able to provide reliable motion estimation results when visual signals are unreliable or unavailable, thus solving the problems of traditional motion capture systems. Meanwhile, the system adopts deep learning technique and dual coordinate system strategy to improve the accuracy and robustness of the system.

## Experiments
This paper focuses on the authors' use of a new approach to motion capture and compares it with other methods. Specifically, they use a dual-coordinate strategy and a feedback mechanism to improve pose and translation accuracy. In addition, they evaluate key components, including the dual-coordinate strategy, hidden state feedback, and optimisation. Finally, they tested their approach in a variety of situations and show more results in a video.

On the quantitative side, the authors compare their approach to methods such as ROMP, PARE, TIP, PIP and VIP. The evaluation metrics they use include MPJPE, PA-MPJPE, PVE, and TE.The results show that their method provides significant improvements over other methods in terms of both pose and translation accuracy. For example, on the TotalCapture dataset, their method outperformed the other methods on all metrics.

![image](https://github.com/user-attachments/assets/513c003a-9416-4d70-bf4f-9646337f24dc)

On the qualitative side, the authors show how their method performs in different situations. For example, in some cases, the purely visual methods ROMP and PARE fail to estimate the position, while the IMU-based methods TIP and PIP suffer from drift. In contrast, the authors' method utilises both visual and IMU inputs more efficiently through a dual-coordinate strategy and a feedback mechanism, and thus allows for better pose and translation estimation in challenging motion, occlusion and field scenarios. 

![image](https://github.com/user-attachments/assets/2b1388f7-a9b3-433c-b798-bcadf3713e81)

## Conclusion

### 1. Advantages of the Thesis
  1. This thesis presents a method that fuses monocular images and sparse inertial measurement unit (IMU) signals for real-time human motion capture and enables highly accurate and robust motion estimation despite extreme lighting conditions, severe occlusion, or a person leaving the camera's field of view.
  
  2. The method employs a two-coordinate system strategy, which allows the neural network to better learn the inertial signals in different situations; meanwhile, a hidden state feedback mechanism allows information to be exchanged between the two coordinate systems, thus helping one branch with a higher confidence level to obtain better results.
  
  3. Quantitative and qualitative results show that the method can reconstruct motion more accurately than existing methods.

### 2. Innovative points
  1. The main contributions of this thesis include: an accurate and robust method for fusing monocular images with sparse IMU signals for real-time human motion capture;
  
  2. a two-coordinate-system strategy that allows the neural network to better learn inertial signals in different situations;
  
  3. and a hidden state feedback mechanism that exploits the joint results to improve the performance of individual components by using them.
 
### 3. Future Works
In future research, the modelling of magnetic disturbances could be considered in order to deal more comprehensively with the problem of sensor error accumulation. In addition, since the method ignores differences in body shape, the inclusion of a body shape factor could be considered for future experiments to obtain a more complete reconstruction.
