# Audiosr_ Versatile Audio Super-Resolution at Scale
[paper link](https://arxiv.org/pdf/2309.07314) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a diffusion model called AudioSR that allows super-resolution processing of many types of audio, including sound effects, music, and speech.          |  Diffusion Model        |

## Methodology

### 1. Abstract
The model is capable of upsampling an input signal over a bandwidth range of 2kHz to 16kHz to a high-resolution audio signal with a 24kHz bandwidth and 48kHz sample rate. Experimental results show that this approach can achieve excellent performance in a variety of audio super-resolution benchmark tests and can be used to enhance the quality of other audio generation models by means of plug-ins. The authors provide code and demos for reference.

### 2. Method Description 
This study presents an Audio Super Resolution (AudioSR) system for converting low resolution audio signals into high resolution audio signals. The system consists of two main steps: **high-resolution Mel spectrum estimation and Mel spectrum-to-waveform reconstruction using a neural vocoder**. Firstly, the low resolution audio signal X<sub>l</sub> is converted to a high resolution audio signal X<sub>h</sub> by interpolation. Then the Mel spectra of X<sub>h</sub> and Y<sub>h</sub> are computed and a pre-trained latent diffusion model is used to learn the process of estimating the high-resolution Mel spectrum Y<sub>h</sub>. Finally, a neural vocoder is used to convert the estimated high-resolution Mel spectrum into a high-sampling rate audio signal Y<sub>h</sub>.

![image](https://github.com/user-attachments/assets/dd9362ac-cf70-4ba4-bfa3-630a66c8b74c)

### 3. Methodological improvements
  1. Optimised training of the latent diffusion model using a pre-trained variational auto-encoder (VAE) as a latent space learner.
  
  2. Modified the noise scheduling by using cosine scheduling instead of the common noise scheduling to ensure a Gaussian distribution for the final diffusion step.
  
  3. A velocity prediction objective was introduced to reflect the new noise scheduling.
  
  4. A multi-resolution discriminator for HiFiGAN was used to address the spectral leakage in the original HiFiGAN.

### 4. Issues addressed 
The main objective of this research is to solve the problem of missing information present in the audio super-resolution task. This problem was effectively solved by decomposing the original audio super-resolution task and dividing it into two steps, i.e., high-resolution Mel spectrum estimation and Mel spectrum-to-waveform reconstruction using a neural vocoder. This approach not only improves the audio super-resolution but also makes the whole process more efficient.

## Experiments
This paper focuses on the AudioSR model for audio noise reduction and super-resolution tasks, and verifies the effectiveness of AudioSR in music synthesis and speech synthesis by comparing it with baseline models such as NVSR.

Specifically, the authors used several datasets for training and testing, including speech datasets from MUSDB18-HQ, MoisesDB, MedleyDB, FreeSound, and OpenSLR3. Also, the authors used NVSR as the main baseline model for comparison. For objective evaluation, the authors used LSD metrics and performed two types of subjective evaluations, i.e., overall quality score and preference comparison. In addition, the authors conducted subjective preference tests on the outputs of MusicGen, AudioLDM and FastSpeech2.

The experimental results show that AudioSR achieves state-of-the-art performance in music synthesis, outperforming the NVSR model at all cut-off frequency settings. As for speech synthesis, AudioSR-Speech achieved the best performance in the upsampling task from 24kHz to 48kHz. In addition, the authors found that LSD metrics do not always agree with perceived quality and further research is needed. 

![image](https://github.com/user-attachments/assets/0320809c-233b-429b-a8ab-d93aa4df6070)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents an audio super-resolution model called AudioSR that is capable of handling various types of audio and supports arbitrary sample rate settings.
  
  2. Evaluated by several audio super-resolution benchmarks, AudioSR shows excellent and robust performance and works efficiently with different types of audio and sample rates.
  
  3. In addition, the authors have performed subjective evaluations that demonstrate AudioSR's ability to improve the quality of audio generation models in a plug-in fashion, including models such as AudioLDM, MusicGen, and Fastspeech2. 

### 2. Innovative points
  1. Firstly, AudioSR is able to handle various types of audio, including music, speech and sound effects.
  
  2. Secondly, AudioSR is able to handle a flexible range of input sample rates from 2kHz to 16kHz and extends the bandwidth up to 24kHz.In addition, AudioSR employs a neural waveform synthesiser to synthesise audio signals, which makes use of the a priori knowledge learnt by the neural waveform synthesiser to reconstruct high frequency components.
  
  3. Finally, AudioSR can also be used as a plug-in module to enhance the quality of a wide range of audio generation models.

### 3. Future Works
Future work includes extending AudioSR to real-time applications and exploring appropriate audio super-resolution evaluation protocols for the general audio domain. This will further advance audio super-resolution technology and provide better solutions for a wider range of audio application scenarios.
