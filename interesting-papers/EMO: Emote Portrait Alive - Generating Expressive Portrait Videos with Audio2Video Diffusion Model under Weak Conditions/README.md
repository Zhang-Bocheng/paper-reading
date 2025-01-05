# EMO: Emote Portrait Alive - Generating Expressive Portrait Videos with Audio2Video Diffusion Model under Weak Conditions
[paper link](https://arxiv.org/pdf/2402.17485) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new framework called EMO for enhancing the realism and expressiveness of human head videos.          |  Diffusion Model        |

## Methodology

### 1. Abstract
Traditional techniques often fail to capture the full range of human expressions and the uniqueness of individual facial styles. To address these issues, the authors propose a compositing method that directly converts audio signals to video without the need for intermediate 3D models or facial keypoints. The method ensures seamless transitions between video frames and maintains consistent identity features throughout the video, resulting in highly expressive and realistic animation effects. Experimental results show that EMO is capable of producing not only convincing speaking videos but also singing videos in a variety of styles, significantly outperforming existing state-of-the-art methods in terms of expressiveness and realism.

### 2. Method Description 
The study aimed to generate long-lasting, coherent and audio-synchronised speaker header videos by using Stable Diffusion (SD) as a base framework. They used the following steps:

  1. Map the original image features to the potential space z0 using a self-encoder in the SD model.
  2. Introduce Gaussian noise e into the potential space to produce a series of noise embeddings zt.
  3. Extract text features using the CLIP text encoder and integrate them into the noise embeddings for denoising operations.

![image](https://github.com/user-attachments/assets/45d4b038-33be-4b5c-ac3d-2a3c3c272061)

### 3.  Methodological improvements
  1. Replace the cross-attention layer in the SD model with a reference attention layer to better maintain the identity consistency of the target object.
  2. Introducing an audio layer to capture speech features and control the speaker's motion.
  3. Add ReferenceNet structure for extracting features and ensuring identity consistency in Backbone Network.
  4. Use temporal modules to handle dynamic content and enhance continuity across clips.
  5. Use face locator and speed layers to provide weak conditions to synchronise head rotation speed and frequency.

### 4. Issues addressed 
  1. How to generate a coherent and stable video of the speaker's head?
  2. How to drive the speaker's motion based on the audio signal?
  3. How to ensure the consistency of speaker identity and stability of head motion?

## Experiments
This paper focuses on four sets of experiments, namely dataset collection and preprocessing, method comparison, quantitative comparison and Ablation Study (stability analysis).

In the first set of experiments, the authors used about 250 hours of video data supplemented with two datasets, HDTF and VFHQ, to train the model. They used MediaPipe to acquire facial frames and labelled them by calculating the head rotation speed. These video clips were scaled and cropped to 512×512 size. In the first stage of training, they trained Backbone Network and ReferenceNet using reference images and target frames with batch size of 48. In the second and third stage, they set the length of the generated video to f = 12, the number of motion frames n = 4, the batch size to 4, the number of extra features m to 2, and the learning rate to 1e- 5. in the inference process, they used the DDIM sampling algorithm to generate the video clips in 40 steps, assigning a constant velocity value to each frame. The time consumption of this method is about 15 seconds per batch.

![image](https://github.com/user-attachments/assets/252fca91-c24a-4177-b3d8-1683101e3399)

![image](https://github.com/user-attachments/assets/0a8a6572-b557-4721-ab2f-aa7ca26e3ac8)

In a second set of experiments, the authors compared their method with a number of other previous methods, including Wav2Lip, SadTalker, DreamTalk, and MakeItTalk.In addition, they used the Diffused Heads method for comparison, but the results were not as satisfactory as they could have been because the model was trained on the CREMA dataset . They used Fréchet Inception Distance (FID) to evaluate the quality of the generated video, Facial Similarity (F-SIM) to evaluate the effect of preserving identity, Fréchet Video Distance (FVD) to evaluate the effect of video levels, SyncNet to evaluate lip synchronisation quality, and expression quality using Expression-FID (E-FID). The results show that their method performs better on several metrics.

In a third set of experiments, the authors further explored the ability to generate different styles of avatar videos. They used Civitai's reference image as input and synthesised characters with different styles such as realism, anime and 3D using different text-to-image models. Even though their models were only trained on realist videos, they were still able to generate avatar videos in a variety of styles.

![image](https://github.com/user-attachments/assets/cb98e41e-6059-4986-870a-bad24db4c7dd)

In the fourth set of experiments, the authors performed stability analyses to assess the impact of the velocity layer and the face localiser. For the velocity layer, they generated videos with different velocity values and measured metrics such as average velocity variance and rate of change of velocity mean. The results showed that the inclusion of a velocity layer significantly improved the consistency of head movements. For the face localiser, they tested the effect when using different sized face regions as inputs. The results show that a proper face region allows the character to exhibit less head movement, while a larger face region allows more head bobbing. At the same time, the input white mask does not provide specific guidance, allowing faces to be generated in arbitrary positions.  

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a novel expressive head video framework, EMO, based on a diffusion model, which does not require any intermediate representation or a priori pose information and is capable of capturing the complex relationship between audio and video to generate highly expressive and naturalistic head videos.
  2. And, the authors construct a large and diverse audio-video dataset to train the model, and demonstrate through experimental results that EMO outperforms existing state-of-the-art methods on a variety of metrics.

### 2. Innovative points
  1. EMO employs the Stable Diffusion technique, which combines the temporal module and 3D convolution to extend to the video domain, and introduces an audio feature extractor and an attention module to learn the correlation between audio and video.
  2. EMO introduces novel mechanisms such as a facial localiser and a velocity layer to provide weak conditions to guide the approximate position and speed of motion of the video without compromising expressiveness.
  3. EMO also uses a reference network to ensure the consistency of faces in the video and implements a motion frame module to maintain continuity between neighbouring video clips for seamless infinite video generation.

### 3. Future Works
Future research could consider how to further optimise the algorithm and improve efficiency. And, ways to extend EMO to other types of video generation tasks, such as full-body motion video generation, could be explored.  
