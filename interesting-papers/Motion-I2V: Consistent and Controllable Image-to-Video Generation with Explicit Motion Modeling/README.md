# Motion-I2V: Consistent and Controllable Image-to-Video Generation with Explicit Motion Modeling
[paper link](https://arxiv.org/pdf/2401.15977) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a new framework called Motion-I2V for consistent and controlled image-to-video generation.         |  Diffusion-based Motion & Attention Modules        |

## Methodology

### 1. Abstract
Unlike traditional methods that learn complex image-to-video mappings directly, Motion-I2V decomposes I2V into two stages with explicit motion modelling. The first stage uses a diffusion-based motion field predictor that focuses on deriving the trajectories of reference image pixels. The second stage then proposes motion-enhanced spatio-temporal attention modules that augment the limited one-dimensional temporal attention, which can effectively propagate the features of the reference image in the video latent diffusion model. By training the first stage of the sparse trajectory control network, Motion-I2V supports the user to precisely control the motion trajectory and motion region, providing a more controllable I2V process than relying on textual commands only. In addition, the second stage of Motion-I2V naturally supports zero-sample video-to-video translation.

### 2. Method Description 
The Image-to-Video Synthesis (I2V) framework proposed in this paper, called ‘Motion-I2V’, is divided into two phases: the first phase **predicts the motion field**, and the second phase **synthesises video frames** using the predicted motion field. In the first stage, a pre-trained stable diffusion model is used to predict the corresponding coordinates of each source pixel in the target image. In the second phase, the encoded reference image is merged with the predicted motion fields from the first phase and new video frames are rendered by an enhanced version of the temporal attention mechanism.

![image](https://github.com/user-attachments/assets/87999a25-5536-4d96-b791-2e6a9884ad7e)

### 3. Methodological improvements
Compared to the existing diffusion model-based I2V methods, Motion-I2V introduces an additional stage of motion field prediction to improve the quality of the generated video. Meanwhile, in the second stage, an enhanced version of the temporal attention mechanism is used to expand the spatio-temporal sensory field and alleviate the pressure of directly predicting complex spatial-temporal patterns.

### 4. Issues addressed 
The method proposed in this paper aims to address the difficulty of maintaining temporal consistency and the lack of fine-grained control of existing diffusion model-based I2V methods while maintaining visual fidelity. By introducing motion field prediction and an enhanced version of the temporal attention mechanism, higher quality, more temporal consistency and controllable video synthesis results are achieved.

## Experiments
This paper focuses on the Motion-I2V approach for the image-to-video generation task and performs quantitative and qualitative comparison experiments with other approaches. Specifically, the authors used Stable Diffusion v1.5 and AnimateDiff v2 as the base models for the first and second phases of the experiments, trained on the WebVid-10M dataset. For evaluation, the authors constructed a test set containing the categories of human activities, animals, vehicles, natural scenes, and AI-generated images, and used ChatGPT-4V to generate cues to measure the consistency and motion magnitude of the generated videos. Quantitative evaluation results show that the Motion-I2V method outperforms other publicly available methods VideoComposer, I2VGen-XL, and DynamiCrafter on the prompt-following metrics.In addition, Motion-I2V generates more consistent videos even with large motion. Qualitative comparison results show that Motion-I2V can generate a larger range of motion compared to DynamiCrafter, while Pika 1.0 provides better visual quality but is limited by the type of motion. These results validate the superior performance of Motion-I2V in generating consistent results.

![image](https://github.com/user-attachments/assets/0086206c-2a8f-4a90-8b2c-7d21a62b0748)

In the Ablation Study section, the authors assessed the impact of key design choices. First, they trained a model without a first stage (i.e., learning temporal dependencies using only the 1D time module) and observed that the model was unstable and prone to generating collapsed results during inference. They then added the first stage and added the predicted motion field directly to the feature map, rather than using attention to adaptively inject deformation features into subsequent frames. By further changing the fusion method to attention, they obtained a final model with the highest consistency score.

![image](https://github.com/user-attachments/assets/0296a138-e667-45f6-beda-e4a92deb5976)

## Conclusion

### 1. Advantages of the Thesis
  1. A new I2V framework is proposed that divides the image-to-video generation process into two stages: motion field prediction and video rendering.
  2. In the first phase, a diffusion model is used to predict pixel-level trajectories, enabling more accurate dynamic modelling.
  3. In the second phase, a motion-guided spatio-temporal attention-based mechanism is proposed that enhances the capabilities of the video diffusion model and supports region-specific animation.
  4. A control network was also trained to enable the user to manipulate the motion of objects through sparse trajectory annotations.

### 2. Innovative points
  1. The I2V problem is decomposed into two subtasks dealing with motion field prediction and video rendering, improving the efficiency and accuracy of the model.
  2. A motion-guided spatio-temporal attention-based mechanism was introduced to increase the spatio-temporal awareness of the model and also support region-specific animation.
  3. A control network was trained to enable users to manipulate the motion of objects through sparse trajectory annotations, improving user controllability and interactivity.

### 3. Future Works
  1. Further research can be done to improve the generalisation ability and test set performance of the model using techniques such as zero signal-to-noise ratio scheduling.
  2. Consideration can be given to introducing more visual information, such as lighting and texture, into the video synthesis process to produce more realistic and natural videos.
  3. It is possible to explore how to combine techniques from other domains, such as GAN, VAE, etc., to enhance the expressiveness and diversity of the model.    
