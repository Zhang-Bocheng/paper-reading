# Make a Cheap Scaling: A Self-Cascade Diffusion Model for Higher-Resolution Adaptation
[paper link](https://arxiv.org/pdf/2402.10491) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes an adaptive diffusion model called Self-Cascade that can be quickly adapted to higher resolution image and video generation tasks without requiring large computational resources.           | Diffusion Model         |

## Methodology

### Abstract
Traditional single-scale training data leads to the problem of incorrect object combinations when generating images, while large pre-trained models require significant computational and optimisation resources when adapting to higher resolutions. To address this problem, the authors propose a novel adaptive diffusion model based on the knowledge of the low-resolution model and use a reliable semantic guidance strategy to gradually exploit the knowledge of the low-resolution model for adaptation. 

In addition, the authors introduce a learnable multi-scale upsampling module to efficiently learn structural details from a small amount of newly acquired high-resolution training data. Experimental results show that the method offers faster training and fewer parameters than full fine-tuning, and only 10k steps of fine-tuning are required to achieve fast adaptation to higher-resolution image and video synthesis without additional inference time.

![image](https://github.com/user-attachments/assets/48b07b47-235a-43fb-bbe8-727811033256)

## Experiments
This paper mainly introduces the framework and improvement method of Self-Cascade Diffusion Model (SCDM), and conducts relevant experimental comparisons. Specifically, the authors firstly propose a method based on the Self-Cascade Diffusion Model for recycling low-resolution image synthesis model to achieve the goal of efficiently generating high-resolution images. Then, the authors further improve the performance of the model by introducing a time-aware feature upsampler with adjustable parameters. Finally, the authors experimentally compare the two versions of the proposed self-downscaling diffusion model and draw the corresponding conclusions.

On the experimental side, the authors used two metrics, Fréchet Inception Distance (FID) and Perceptual Path Length (PPL), to evaluate the quality of the generated images. FID is a commonly used metric to measure the difference between the distribution of the generated image and the real image, while PPL is a measure of the level of detail and realism of the generated image. In terms of experimental results, the authors found that the version that introduces temporal-aware feature up-sampling significantly improves the quality of the generated images compared to the version that only uses a pre-trained low-resolution model, especially when dealing with more complex scenes. In addition, the authors experimentally verified that the proposed method has better efficiency and stability relative to some other existing methods.

![image](https://github.com/user-attachments/assets/d8ba25d1-37b2-45ba-bc94-c860fd18dc09)

In summary, this paper proposes a new self-downscaling diffusion model and experimentally demonstrates its superiority in generating high-quality high-resolution images. This method can provide a reference and a lesson for future image generation tasks.

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a novel self-looping diffusion model for fast adaptation to higher resolution image and video generation tasks. The method achieves an efficient increase in resolution without additional training by introducing a central sample-guided noise rearrangement strategy.
  
  2. Also, the method proposes a lightweight time-aware feature upsampling module that can be fine-tuned with the help of small amounts of high-quality data, thus further improving the generation performance. Experimental results show that the method provides significant performance improvement at different resolutions and can be quickly adapted to new high-resolution domains.

### 2. Innovative points
  1. The self-recycling diffusion model proposed in this paper is a novel approach that utilises pre-trained low-resolution models to improve resolution, avoiding the problem of traditional super-resolution methods that require large amounts of high-quality data.
  
  2. In addition, the method introduces a time-aware feature upsampling module that can be fine-tuned with a small amount of high-quality data, further improving the generation performance. These innovations enable the method to achieve better generation results with less data and computational resources.

### 3. Future Works
Future research directions include how to better handle high-resolution data and how to further improve the generation performance.   
