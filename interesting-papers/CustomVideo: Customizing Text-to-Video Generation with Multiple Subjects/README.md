# CustomVideo: Customizing Text-to-Video Generation with Multiple Subjects
[paper link](https://arxiv.org/pdf/2401.09962) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a new framework called CustomVideo, designed to enable personalised text-to-video generation guided by multiple topics.          |         Diffusion Model |

## Methodology

### 1. Abstract
The approach utilises multiple topics for combination and devises a simple but effective attention control strategy to separate different topics in the potential space of the diffusion model. In addition, to help the model focus on specific regions of the object, the researchers also segmented the objects in a given reference image and provided corresponding object masks for attentional learning. Finally, the researchers collected a multi-topic text-to-video generation dataset containing 63 different categories of individual subjects and 68 meaningful pairs as a comprehensive benchmark test.

### 2. Method Description 
The paper presents a method called CustomVideo for generating videos containing multiple topics given textual cues. CustomVideo is based on a pre-trained Video Diffusion Model (VDM) and introduces a new learnable vocabulary to represent each topic and achieves separation between topics through a cross-attention mechanism. In the training phase, CustomVideo is co-trained using images with multiple topics to ensure that all topics appear simultaneously in the video. In the inference phase, the user simply provides a textual cue containing a specific topic to generate a high-quality video.

![image](https://github.com/user-attachments/assets/f7bff45f-3ae0-47f8-8d7c-51dfa683ac23)

### 3. Methodological improvements
  1. New learnable vocabulary: Introduces a new learnable vocabulary for each topic to better separate different topics in the cross-attention mechanism.
  2. Cross-attentional control: using cross-attentional maps to directly regulate the topic learning process, allowing the model to focus on the correct topic areas more effectively.
  3. Positive and negative guidance: in addition to positive guidance, negative guidance is introduced to avoid the influence of irrelevant regions and improve the quality of generated topics.

### 4. Issues addressed 
CustomVideo solves the problems in traditional multi-topic video generation methods, such as difficulty in accurately capturing topic features and difficulty in achieving topic separation. By introducing a new learnable vocabulary, cross-attention control, and positive and negative steering, CustomVideo generates high-quality videos with high diversity and preserved topic characteristics.

## Experiments
This paper focuses on the performance of the CustomVideo approach in a multi-topic driven video generation task and compares it with several related approaches. Specifically, the following comparison experiments are used in this paper:

**Comparison with DreamBooth and CustomDiffusion:** these methods are methods for converting images of a single subject to video, so this paper applies them to multi-subject scenarios and compares them with other methods.
**Comparison with DisenDiff+SVD-XT:** This is a multi-concept-driven image-to-video conversion method, so this paper applies it to multi-subject scenes and compares it with CustomVideo.
**Comparison with DreamVideo:** this is the current state-of-the-art single-topic-driven video personalisation method, so this paper uses it as a control group and compares it with CustomVideo.

![image](https://github.com/user-attachments/assets/9bb36c53-2049-42c9-99c1-bb3bf31a1507)

For each experiment, this paper uses both quantitative and qualitative evaluation metrics to measure the results. Among them, quantitative metrics include CLIP text alignment, CLIP image alignment, DINO image alignment, and timing consistency. While the qualitative metrics visualise the performance of each method by showing the generated videos.

![image](https://github.com/user-attachments/assets/9fd3eb32-ac1a-4654-ac4b-95e280869d92)

From the experimental results, CustomVideo performs well in the multi-topic driven video generation task. Compared with DreamVideo, CustomVideo achieves significant improvements in both CLIP image alignment and DINO image alignment. In addition, CustomVideo has better temporal consistency and is able to better preserve the identity of the subject. CustomVideo also received the highest rating in terms of human evaluation, indicating that it generates higher quality videos.  

## Conclusion

### 1. Advantages of the Thesis
  1. The framework utilises simple co-occurrence and attention control mechanisms to separate similar topics and retain the corresponding identity information.
  2. Evaluated using the customised dataset CustomStudio and compared to state-of-the-art SOTA methods, the results show that CustomVideo performs well in both quantitative and qualitative experiments, significantly outperforming other methods.

### 2. Innovative points
  1. CustomVideo proposes a flexible and efficient training process that generates the desired video by providing only the subject image instead of the video.
  2. CustomVideo employs a cross-attentional layer extraction strategy, where intermediate-sized cross-attentional layers are used for attentional control.
  3. CustomVideo also provides a human interface for user study to better understand user needs and feedback. 

### 3. Future Works
  1. In the future, further exploration can be done to improve the model's ability to handle special cases such as small faces and large numbers of subjects.
  2. Consideration can be given to introducing more a priori knowledge such as scene, time, etc. to improve the quality and realism of the generated video.
  3. Attempts can be made to apply the framework to a wider range of application areas such as virtual reality, game development, etc.    
