# Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots
[paper link](https://arxiv.org/pdf/2402.10329) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper describes a data collection and strategy learning framework, called the Universal Manipulation Interface (UMI), that allows direct transfer of human demonstrations in the field to deployable robotic strategies.         |  Data Collection Framework        |

## Methodology

### 1. Abstract
The UMI uses handheld grippers in conjunction with a well-designed interface to enable portability of challenging bimanual and dynamic manipulation demonstrations, low-cost and information-rich data acquisition. To facilitate deployable strategy learning, UMI incorporates a well-designed strategy interface, as well as a design that matches inference time delays and relative trajectory action representations. With these features, the UMI framework unlocks new robot manipulation capabilities, enabling zero-sample generalisation to new environments and objects with dynamic, bimanual, accurate and long time-series behaviours, simply by changing the training data for each task. This paper demonstrates the versatility and effectiveness of UMI through comprehensive real-world experiments, in which strategies learned through UMI are able to generalise to new environments and objects after diverse training with different human demonstrations.

### 2. Method Description 
This paper presents the Universal Manipulation Interface (UMI), a handheld  designed to enable the transfer of robotic manipulation strategies directly from live human demonstrations. The UMI is designed to be a trigger-activated, handheld 3D-printed and parallel jadata collection frameworkw pincer with soft fingers, used in conjunction with a GoPro camera as the sole sensor and recording device. The system has the following features:

Captures enough information to perform a wide range of complex tasks, not just grab and place.

  1. Is scalable and can be used for a wide range of robot arms.
  2. The data collected contains enough information to learn effective robot strategies and is virtually unaffected by specific robots.
  3. The hardware design of the UMI consists of a wrist-mounted camera and a 3D print with soft finger grips of the same position and size.

  The camera is mechanically fixed and stable with respect to the position of the finger, which eliminates the need for camera-robot-world calibration when deployed on a robot. In addition, because the camera is in a fixed position, the observed visual difference between the human demonstration and the robot deployment is minimised, thus reducing the sensitivity of the strategy inputs to changes in the external environment.

![image](https://github.com/user-attachments/assets/42b662e7-300a-40c0-b4a2-1ae520837143)
  
### 3. Methodological improvements
In order to address the problems with traditional data collection methods, UMI has made improvements in the following areas:

  1. The use of wrist-mounted cameras rather than external still cameras avoids the problem of relying on an external camera setup.
  2. Using Fisheye focal length lenses to provide a wider field of view and reduce the impact of background structures.
  3. Utilises IMU data for motion capture to improve the accuracy of dynamic movements.
  4. Use of continuously controlled pincer widths to expand the task range.
  5. Use relative trajectory representation to make the system more robust to tracking errors or camera displacement.

### 4. Issues addressed 
  1. While traditional methods require expensive external camera setups, UMI uses wrist-mounted cameras, which are cheaper and easier to deploy.
  2. Traditional methods rely on precise motion capture, while UMI uses IMU data for motion capture, improving the accuracy of dynamic movements.
  3. Traditional methods are limited by fixed camera positions, resulting in large visual discrepancies between observed human demonstrations and robot deployments, whereas UMI's cameras are fixed in fixed positions, eliminating this problem.
  4. Discrete motion capture used by traditional methods limits the task range, whereas the UMI uses continuously controlled pincer widths to extend the task range.

## Experiments
This paper focuses on four experiments conducted by the authors on robot learning using the UMI framework, which are evaluated and compared in detail. Specifically, these experiments include:

**Cup Arrangement task (Cup Arrangement)**: this task was designed to test the UMI's ability to capture and transfer one-handed, two-armed, dynamic, and long-time-domain manipulations. The results of the experiments showed that the UMI could successfully complete 20 of all 20 test cases with more efficient data collection compared to using a human hand presentation.

**Dynamic Tossing:** This task requires the robot to throw multiple objects into corresponding containers to test its ability to capture and transfer fast human hand movements, precise hand-eye coordination, and time synchronisation. Experimental results showed that UMI was able to achieve a success rate of 87.5%, but when delayed matching was disabled, the success rate dropped to 57.5%.

**Bimanual Cloth Folding task:** This task required two robotic arms to coordinate folding the sleeves of a jumper and placing them in a bag to test the ability to handle high degree of freedom deformable objects. Experimental results showed that UMI was able to successfully complete this task in 70% of the cases.

**Dish Washing:** This task requires the robot to perform a series of sequential actions to clean plates and sponges to test its ability to perform complex liquid manipulations on ultra-long time scales. Experimental results show that UMI was able to achieve a 70% success rate.

![image](https://github.com/user-attachments/assets/e771c5bb-65fc-4185-a6aa-dc40f9e35f0b)
In addition, the article evaluates data collection efficiency and accuracy. The experimental results show that data collection using the UMI is much faster than traditional human demonstration methods and that the SLAM system is more accurate.

![image](https://github.com/user-attachments/assets/655b0f37-0a26-4766-b03e-8b09edd8cf07)
  
## Conclusion

### 1. Advantages of the Thesis
  1. The framework uses a hand-held data collection interface that enables easy sharing and distributed data collection by recording all information in a standard MP4 file.
  2. In addition, the framework has the advantage of being scalable and flexible for tasks in a variety of environments and allows for zero-sample generalisation across different environments.

### 2. Innovative points
  1. **Physical interface design:** the authors used Fisheye lenses and side mirrors to provide more visual context and combined them with GoPro's IMU sensor to improve tracking performance.
  2. **Policy interface design:** the authors used inference time matching to deal with the problem of different sensor observation and execution delays, used relative trajectories as action representations to eliminate the need for accurate global actions, and applied the Diffusion Policy model to model multi-modal action distributions.
  3. **Data collection approach:** the authors propose the use of a wrist camera for data collection, which captures enough information to perform some complex operations while maintaining a high transfer rate.

### 3. Future Works
Future directions for improvement include the development of a somatosensory-aware strategy learning framework capable of transferring valid but hardware-unfeasible motions to actual robots; there is also a need to explore lighter materials as well as further improvements in the mechanical design and ergonomics of UMI, or to build robotic hands and strategies robust and flexible enough to be directly transferable from human motions.   
