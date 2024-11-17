# CreativeSynth: Creative Blending and Synthesis of Visual Arts based on Multimodal Diffusion
[paper link](https://arxiv.org/pdf/2401.14066) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents an innovative framework called CreativeSynth, which is based on the diffusion model and is capable of coordinating multimodal inputs and multitasking for a wide range of applications in the field of artistic image generation.          | Diffusion model         |

## Methodology

### 1. Abstract
By integrating multimodal features and custom attention mechanisms, CreativeSynth enables precise manipulation of image style and content while maintaining the integrity of the original model parameters. Experimental results show that CreativeSynth excels in enhancing the realism of artistic images and preserving their intrinsic aesthetic nature. The framework provides new ideas for combining generative models with artistic techniques as a custom digital palette.

### 2. Method Description 
This research presents an image synthesis framework called CreativeSynth, which is capable of generating customised artwork based on given textual prompts and reference images. The framework includes the following main components:

  1. Conditional Encoding: integrates text and image features through a pre-trained Stable Diffusion model.
  2. Sentiment Maintenance: a style alignment processor is introduced to tune the attention mechanism and normalisation layer for adaptive fusion between artistic and semantic images.
  3. Semantic fusion: text and image features are processed using a decoupled cross-attention mechanism and merged to produce the final modified image features.
  4. Sample process: inverse reconstruction using a deterministic denoising diffusion implicit modelling (DDIM) technique to recover the original image and ensure consistency with the input text.

### 3. Methodological improvements
Compared to the existing U-Net cross-attention architecture, CreativeSynth employs separate paths dedicated to text or image features, thus avoiding mutual interference between different features. In addition, CreativeSynth introduces the IP-Adapter module, which uses the embedding information of the reference image to guide the generation process, improving the quality of the synthesised image.

### 4. Issues addressed 
CreativeSynth solves the problem of the difficulty of considering both textual cues and reference images in traditional image synthesis methods. The framework automatically generates artwork that meets given conditions, providing artists with a more efficient creative tool.

## Experiments
This paper conducts several comparative experiments to evaluate and validate the performance and effectiveness of the Creative Synth method. Specifically, the following four experiments are conducted in this paper:

**Experiment 1: Benchmark comparison experiment in the image fusion task.** This experiment aims to evaluate the effectiveness of Creative Synth in comparison with existing models such as Image Mixer, Kosmos-G and VD. The results show that Creative Synth excels in stylistic rendering and is able to effectively incorporate semantic information into the synthesis results, generating harmonious fusion results with artistic quality and aesthetic value.

**Experiment 2: Benchmark Comparison Experiment in a Text-Based Single Image Editing Task.** The purpose of this experiment is to evaluate the effectiveness of Creative Synth in comparison with several state-of-the-art benchmark models (e.g., IP-Adapter, ProSpect, DreamBooth, etc.). The results show that while IP-Adapter produces higher quality results, it fails to retain the non-editing information of the target image. In contrast, Creative Synth is able to implement editing operations for personalised text descriptions while maintaining the content of the original image, while ensuring content fidelity and style consistency.

![image](https://github.com/user-attachments/assets/646b2c2c-db1c-4fcb-a6de-3f9e1e3a4bc6)

**Experiment 3: Quantitative Evaluation Experiment.** This experiment uses three key metrics (i.e., Aesthetic Score, CLIP-T, and CLIP-I) to quantitatively compare Creative Synth with other existing methods. The results show that Creative Synth achieves excellent results on all evaluation metrics, especially on the Aesthetic Score metric, which has an average score of 7.563, which is significantly better than other methods.

![image](https://github.com/user-attachments/assets/6c26906d-cf23-480a-93b0-c81eab33b522)

**Experiment 4: User Research Experiment.** This experiment was conducted by asking participants to vote on the results of multiple image generation techniques to determine which method generated the most popular art results. The results showed that Creative Synth was particularly popular for ink drawings, oil paintings, and digital art.

## Conclusion

### 1. Advantages of the Thesis
  1. The approach is not only popular in terms of visual effects, but also very effective in enforcing user-specific art editing intentions. Specifically, the article proposes two core mechanisms: aesthetic maintenance and semantic fusion to ensure that the original intent of the artist and the original style of the artwork are not lost, and to enhance the ability to humanely customise the work to reflect the user's intent and narrative.
  2. In addition, the method has multiple applications, including image variation, image editing, style transformation, image fusion and multimodal blending.

### 2. Innovative points
  1. The main contribution of this paper is the proposal of a novel creative art framework, CreativeSynth, which is capable of integrating multimodal inputs and digital artworks, focusing not only on generating images with a sense of realism, but also preserving essential artistic elements such as conceptual integrity, stylistic fidelity, and visual symbolism.
  2. At the same time, the method employs advanced aesthetic maintenance, semantic fusion, and inverse coding techniques that enable the integration of multimodal semantic information while preserving the intrinsic expression of the artwork, thus greatly increasing the degree of consistency and individuality of the work. 

### 3. Future Works
In future work, the authors plan to apply this approach to different image generation architectures and extend it to other types of media, such as video. With subsequent improvements and applications, this approach will help creators achieve creative expression like never before.    
