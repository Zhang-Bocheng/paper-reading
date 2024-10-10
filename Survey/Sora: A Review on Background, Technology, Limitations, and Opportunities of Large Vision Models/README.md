# Sora: A Review on Background, Technology, Limitations, and Opportunities of Large Vision Models
[paper link](https://arxiv.org/pdf/2402.17177) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper provides a comprehensive review and analysis of Sora, a text-to-video generation AI model released by OpenAI in 2024.          |  SORA        |

## Methodology

### 1. Abstract
It first describes the development history and technical foundations of Sora, and describes in detail its applications and potential impact in multiple industries. The main challenges and limitations that need to be addressed, such as ensuring secure and unbiased video generation, are then discussed. Finally, the future direction of Sora and video generation modelling is explored as well as how it can facilitate interactions between humans and AI to improve productivity and creativity in video generation.

### 2. Method Description 
Sora is a video generation technique based on diffusion transformer, the core idea of which is to map the original video into the latent space and compress it into a low-dimensional representation by a time-space compressor. These tokenised potential representations are then processed using a visual attention mechanism (ViT) and the denoised potential representation is output. 

Finally, user instructions and possibly visual cues are used to guide the diffusion model to generate videos with a specific style or theme. After several denoising steps, the latent representation of the generated video can be obtained and mapped back into pixel space by the corresponding decoder.

![image](https://github.com/user-attachments/assets/ad99e4a8-5476-430a-8b88-ec4efde86d4e)
 
### 3. Methodological improvements
The main advantage of Sora over traditional video generation techniques is its flexibility and scalability. Not only can it generate high-quality videos, but it can also automatically generate videos with a specific style or theme based on user instructions and visual cues. In addition, Sora uses the latest deep learning techniques and computer vision algorithms to improve the quality and efficiency of video generation.

### 4. Issues addressed 
Sora primarily addresses some of the limitations and challenges of traditional video generation techniques. For example, while traditional techniques usually require a large amount of computational resources and training data to generate high-quality videos, Sora can achieve efficient video generation with a small amount of data and computational resources. In addition, Sora can automatically generate videos with specific styles or themes based on user commands and visual cues, thus meeting the needs of different users.

## Models
This paper presents an experimental study addressing three aspects of the video generation model Sora: variable duration, resolution and aspect ratio, unified visual representation, and video compression networks. In each aspect, the authors present specific experimental methods, which are explained and analysed in detail.

Firstly, in terms of the variables duration, resolution and aspect ratio, the authors conclude that the use of videos in their original size and format improves the quality of the generated videos by comparing the effects of models trained using videos of different sizes and formats. Specifically, they compared Sora with a model that cropped the video to fit a square shape, and found that using the original size and format of the video better maintains the integrity and proportions of the scene, resulting in a more natural and coherent visual narrative.

![image](https://github.com/user-attachments/assets/19a8975a-c9b3-4cb0-a159-2075647d0e4e)

Second, in the area of unified visual representations, the authors propose a method for converting a variety of visual data, including images and videos, into unified representations for large-scale training of generative models. They propose to process videos with different sizes and aspect ratios using a spatio-temporal convolutional neural network, which decomposes the video into spatio-temporal feature blocks and encodes them. These spatio-temporal feature blocks are then organised into a spatio-temporal embedding representation for subsequent model training.

Finally, in terms of video compression networks, the authors discuss two different compression methods: spatial chunk compression and spatio-temporal chunk compression. Both methods can effectively handle videos with different resolutions and durations, and the compression can be further optimised by utilising pre-trained visual coders. The authors also mention a solution called PNP, which allows for efficient training by packing multiple video clips into a single sequence without increasing the computational cost.

![image](https://github.com/user-attachments/assets/6649f86b-712b-443d-9329-dbd27bc1640b)

Overall, this paper provides an in-depth analysis and experimental study of the Sora video generation model, showing how the quality of generated videos can be improved using videos of the original size and format, a unified visual representation, and an effective video compression network. These findings are important for improving existing generative models and advancing artificial intelligence techniques. 

![image](https://github.com/user-attachments/assets/9254dbb3-5b1e-4f63-89d5-fbe343ec3ae6)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper details the technical details of OpenAI Sora, including data preprocessing, model architecture, instruction following, and hint engineering.

  2. The paper provides readers with a deeper understanding and comparison by analysing methods and techniques from other related studies.

  3. The paper uses clear language and diagrams to explain the technical details, making it easier for readers to understand.

### 2. Innovative points
  1. Sora uses a new video compression technique and diffusion transformer model to improve the quality and efficiency of the generated video.

  2. Sora used trained descriptors to improve textual cues to improve their understanding of user intent.

  3. Sora also developed a way to extend the video cues so that the model can better understand and edit the video.
     
### 3. Future Works
  1. As technology evolves, we can expect more innovations and improvements to further enhance the performance and reliability of AI.

  2. More domain-specific applications are likely to emerge, such as healthcare, finance, etc.

  3. One of the future challenges is how to ensure the security and privacy protection of these technologies.  
