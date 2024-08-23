# Tracking Anything with Decoupled Video Segmentation
[paper link](https://arxiv.org/pdf/2309.03903) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a method called ‘Decoupled Video Segmentation’, which aims to solve the problem of expensive training data in video segmentation tasks.          | Computer Vision         |

## Methodology

### 1. Abstract
The method consists of two modules: **task-specific image-level segmentation** and **class/task-independent bidirectional time propagation**. In this way, only one image-level model needs to be trained for the target task (cheaper), as well as a generic temporal propagation model (one training for all tasks). In order to efficiently combine these two modules, bidirectional propagation was used for semi-online fusion of segmentation hypotheses from different frames to generate coherent segments. Experimental results show that this split approach performs better than the end-to-end approach for several data-scarce tasks, including large vocabulary video panorama segmentation, open-world video segmentation, referential video segmentation, and unsupervised video object segmentation.

### 2. Method Description 
The paper proposes a video segmentation method called ‘Decoupled Video Segmentation’, which is divided into two main parts: **an image segmentation model** and **a generalised temporal propagation model**. 
<br>&emsp;The image segmentation model provides task-specific image-level segmentation assumptions by training a model specific to the target task. 
<br>&emsp;The generic temporal propagation model, on the other hand, correlates and propagates these assumptions throughout the video by training on a class-independent occlusion propagation dataset. 
This approach separates task-specific segmentation learning from general video object segmentation learning, enabling a robust framework even when target domain data is scarce and insufficient for end-to-end learning.

![image](https://github.com/user-attachments/assets/3bf6fed8-34ab-40a3-927e-d0f67e0ea666)

### 3. Methodological improvements
The main improvement of the method is the decoupling of the image segmentation model from the temporal propagation model, which improves the robustness and generalisation of the algorithm. In addition, the method introduces the concept of in-clip consensus, which reduces the impact of single-frame segmentation errors by voting on the image segmentation results of a small set of future frames and further improves the segmentation accuracy by fusing the propagation results with the consensus results.

### 4. Issues addressed 
This method solves two problems in traditional video segmentation methods: task specificity and timing consistency. Traditional video segmentation methods usually need to design image segmentation models individually for each specific task, which leads to algorithm non-generality and difficulty in adapting to new tasks. In contrast, this method achieves a balance between generality and adaptability by using a combination of an image segmentation model specific to the target task and a generalised temporal propagation model. Meanwhile, since video sequences have temporal consistency, traditional video segmentation methods may suffer from inconsistency between time steps, while the method solves this problem by introducing the concept of in-clip consensus, which makes the segmentation results more accurate and reliable.

![image](https://github.com/user-attachments/assets/d609649b-8364-453f-90d1-b91513e2b1df)

## Experiments
This paper focuses on the results of comparative experiments using a new method in a video segmentation task. The approach treats image segmentation and video segmentation separately and uses a generalised temporal propagation module for long distance correlation. Specifically, the following four comparative experiments are conducted in this paper:

  1. The performance is evaluated and compared with other methods on the large-scale video semantic segmentation dataset VIPSeg in combination with three different image segmentation models (PanoFCN, Mask2Former and Video-K-Net). The results show that using our method significantly improves the effectiveness of long-range correlation, especially at larger k values.

![image](https://github.com/user-attachments/assets/9786f6e3-f4cf-423b-9b5e-5a2db4839096)

  2. On the open-world video segmentation dataset BURST, new objects can be better discovered and tracked using our method compared to traditional methods such as tracking detection.

  3. On the referring video segmentation datasets Ref-DAVIS17 and Ref-YouTubeVOS, better performance can be obtained using our method.

  4. On the single/multi-target video segmentation datasets DAVIS-16 and DAVIS-17, better performance can be obtained using our method.

![image](https://github.com/user-attachments/assets/fab91bdf-c8b9-4994-a8fc-3a2f2295bcb8)
 
## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a video segmentation method called DEVA that achieves the goal of ‘tracking anything’ by combining task-specific image-level segmentation with task-independent temporal propagation.
  
  2. The method effectively extends image segmentation methods to video data using bidirectional propagation techniques and utilises external task-independent data to reduce dependence on the target task, thus better adapting to tasks with scarce data.
  
  3. In addition, the method is combined with existing general-purpose image segmentation models to achieve state-of-the-art performance in large vocabulary and open-world video segmentation.

### 2. Innovative points
  1. The main contribution of the paper is the proposal of a video segmentation method based on task-specific image-level segmentation and task-independent temporal propagation.
  
  2. The method uses bi-directional propagation techniques to improve the detection accuracy and consistency of objects in the video and reduces the dependency on the target task by introducing external task-independent data.
  
  3. This approach is also able to seamlessly integrate existing general-purpose image segmentation models such as ‘Segment Anything’ (SAM) to achieve better performance.
     
### 3. Future Works
Future research could further explore how to improve this hybrid approach to make it more applicable to a variety of different video segmentation scenarios. For example, its performance could be improved by refining the time propagation algorithm or adding more external data sources. It could also be investigated how to combine this approach with other video processing techniques for a wider range of applications. 
