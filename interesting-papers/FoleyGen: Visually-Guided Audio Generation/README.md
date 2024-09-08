# FoleyGen: Visually-Guided Audio Generation
[paper link](https://arxiv.org/pdf/2309.10537) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a video-to-audio generation system called FoleyGen, which is based on a linguistic modelling approach and uses a neural audio codec for bidirectional transformation.          |  Transformer        |

## Methodology

### 1. Abstract
The generation of audio tokens is performed through a single Transformer model and features extracted by a visual coder. In order to address the problem of mismatch between actions in the video and the generated audio, the authors explored three new visual attention mechanisms and thoroughly evaluated multiple visual coders. Experimental results show that FoleyGen outperforms previous systems on the VGGSound dataset, achieving better results in all objective metrics and human evaluations.

### 2. Method Description 
The paper presents FoleyGen, a video-to-audio generation system for generating semantically consistent and temporally aligned audio clips based on video content. The system consists of three main components: **a neural audio codec, a visual encoder, and an audio-lingual decoder**. In particular, the Neuro-Audio Codec converts waveforms into discrete tokens using EnCodec and compresses the waveforms during training; the Visual Codec extracts the feature vectors of the video frames; and the Audio Linguistic Decoder autoregressively generates discrete audio tokens based on the extracted visual features using the Transformer model.

![image](https://github.com/user-attachments/assets/a0af26e8-6157-4c19-934e-ccb8b563875c)

### 3. Methodological improvements
In order to improve the temporal alignment of the visual input and generated audio, the paper proposes three different visual attention mechanisms, namely full-frame visual attention, causal visual attention, and frame-specific visual attention. These mechanisms can help the model to better synchronise audio and visual cues.

### 4. Issues addressed 
The approach addresses challenges in video-to-audio generation, including how to maintain semantic consistency and how to achieve temporal alignment. The quality of audio generation can be further improved by using different visual attention mechanisms.

## Experiments
This paper focuses on the authors' proposed FoleyGen system for the open-domain visually guided audio generation task, and conducts several sets of comparative experiments to verify its performance. Specifically, the authors used the following three comparison experiments:

The first comparison experiment compares FoleyGen with two previous state-of-the-art approaches, SpecVQGAN and IM2WAV. The authors used the objective evaluation metrics Fréchet Audio Distance (FAD), Kullback-Leibler Divergence (KLD) and ImageBind (IB) scores as well as subjective evaluation metrics to assess the performance of the three methods. The results show that FoleyGen outperforms SpecVQGAN and IM2WAV on all objective and subjective metrics and significantly reduces the FAD score. This improvement can be attributed to the integration of EnCodec, which improves the compression ratio of audio tokens and enhances the reconstruction quality, while avoiding the need for multiple Transformer models.

The second comparison experiment was to compare the effects of different visual coders on FoleyGen performance. The authors trained four different visual coders and applied them to FoleyGen. The results show that the visual coders pre-trained by multimodality (e.g., CLIP and ImageBind) exhibit comparable or even better performance than the unimodal pre-trained visual coders. ViT, on the other hand, outperforms VideoMAE due to its pre-training on the discrimination task.

![image](https://github.com/user-attachments/assets/cc9a419b-08ab-4fb0-9e3b-16840cb005a5)

The third comparison experiment tested the effect of different attention mechanisms on FoleyGen performance. The authors tried full-frame visual attention, causal visual attention, and frame-specific visual attention and evaluated them both objectively and subjectively. The results show that full-frame visual attention outperforms the other two in terms of both objective metrics and human evaluation, but frame-specific visual attention performs better in terms of human evaluation because it is better able to capture important actions in the video. 

![image](https://github.com/user-attachments/assets/e6241122-89a9-48a3-8e1b-18c265f7b357)

## Conclusion

### 1. Advantages of the Thesis
  1. The framework employs three main components: **a bi-directional waveform marker converter, a visual coder, and a conditional transformer**, where a neural audio coder (EnCodec) is introduced to achieve better reconstruction quality and to eliminate distortion loss during spectrogram-to-waveform conversion.
  
  2. In addition, the authors propose three different visual attention mechanisms to enhance the temporal coherence between audio and video.
  
  3. Finally, the experimental results show that FoleyGen has a higher performance performance compared to other systems.

### 2. Innovative points
  1. The methodological innovation of this paper is the adoption of a language modelling approach for video-to-audio generation, which overcomes the difficulty of processing both visual and auditory data in traditional methods.
  
  2. Also, the authors introduce a neural audio codec (EnCodec) and explore three different mechanisms of visual attention to improve the temporal consistency between generated audio and video. These innovative approaches allow FoleyGen to excel in both objective metrics and human assessment.

### 3. Future Works
  1. Future research should explore more deeply how to improve the temporal consistency of video-to-audio generation systems.
  
  2. In addition, deep learning techniques can be considered for a wider range of application scenarios in areas such as virtual reality and film production.  
