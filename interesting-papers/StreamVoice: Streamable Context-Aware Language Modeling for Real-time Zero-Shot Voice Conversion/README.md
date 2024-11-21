# StreamVoice: Streamable Context-Aware Language Modeling for Real-time Zero-Shot Voice Conversion
[paper link](https://arxiv.org/pdf/2401.11053) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a novel language model called StreamVoice for real-time zero-sample speech conversion.          |    Large Language Modeling      |

## Methodology

### 1. Abstract
Traditional language model-based speech conversion methods require complete source speech data for offline conversion, limiting their deployment in real-time applications. StreamVoice, on the other hand, uses a fully causal context-aware language model and a time-independent acoustic predictor, which enables real-time conversion at the cue of any speaker and requires only a single utterance from a single speaker to complete the conversion. To enhance context-awareness, the model employs two strategies: teacher-guided context foresight and semantic masking strategies. Experimental results show that StreamVoice is capable of real-time conversion and achieves zero-sample performance comparable to non-streaming speech conversion systems.

### 2. Method Description 
The speech conversion model StreamVoice proposed in this paper uses a streaming architecture and improves the conversion quality by introducing contextual enhancement techniques. Specifically, the model uses a pre-trained ASR model and a speech codec model to represent the input speech features as semantic and acoustic features. Then, using context enhancement techniques, masked autoregressive projections and teacher-guided future projections are introduced into the language model to capture historical and future contextual information. Finally, the hidden states are mapped to the acoustic coding space by continuous or discrete projections to achieve speech transformation.

![image](https://github.com/user-attachments/assets/eee0f3f1-1472-42c7-8f77-dd910e45d6ff)

### 3. Methodological improvements
Compared to traditional speech conversion models, StreamVoice adopts a streaming architecture that enables real-time speech conversion. Meanwhile, the introduction of context enhancement technology can alleviate the performance degradation problem due to incomplete semantic input and lack of future information, which further improves the conversion quality.

![image](https://github.com/user-attachments/assets/70bf8dbf-00bc-4d54-9fa4-f3caa99cd469)

### 4. Issues addressed 
StreamVoice addresses two major challenges in real-time speech conversion: how to achieve real-time conversion while maintaining high quality; and how to overcome the performance degradation caused by incomplete semantic input and lack of future information. By applying context enhancement techniques, StreamVoice is able to achieve real-time speech conversion while maintaining high conversion quality.

## Experiments
This paper focuses on two experiments conducted by the authors in the field of speech conversion: a zero-observation experiment and an internal dataset experiment, and analyses and summarises the results.

First, in **the zero-observation experiment**, the authors used two different approaches to compare the performance differences between their proposed StreamVoice model and other existing speech conversion systems. One approach is to compare the StreamVoice model with a language model-based zero-observation speech conversion system (LM-VC), and the other approach is to use non-streaming ASR for semantic extraction in the StreamVoice model and compare it with another zero-observation speech conversion system (NS-StreamVoice). The experimental results show that the StreamVoice model achieves a performance close to or exceeding the existing system in both subjective and objective evaluations, and in particular, even exceeds the existing system in some aspects. In addition, the StreamVoice model has the advantages of real-time performance and causality.

![image](https://github.com/user-attachments/assets/6a182453-a4c0-48b2-b68b-51eb541c56aa)

Second, in **an in-house dataset experiment**, the authors compared the StreamVoice model with three other speech conversion systems, including an any-to-many-person non-streaming speech conversion system (NS-VC), a recently proposed streaming speech conversion system, IBF-VC, and a dual-streaming speech conversion system, DualVC.2 The results of the experiment showed that although the StreamVoice model uses a smaller ASR block size than other streaming speech conversion systems, it is still able to achieve similar performance as these systems, which indicates that the StreamVoice model has good conversion capabilities. In addition, Fine-tuning can further improve performance when there is available speech from the target speaker.

![image](https://github.com/user-attachments/assets/42bc997f-e190-4da5-a8ea-6c24246f9756)

Finally, the authors also conducted several **Ablation studies** to see how the different components of the StreamVoice model affect its performance. The experimental results show that different components in the StreamVoice model have a significant impact on its performance, e.g., Teacher-guided Contextual Foresight helps to capture linguistic content, while Semantic Masking helps to enhance contextual learning and improve speaker timbre capture. Also, the integrated bottleneck conditioner helps to prevent source speaker information leakage and has little impact on speech quality.

![image](https://github.com/user-attachments/assets/07b8ace9-2da0-42ad-8000-55c511b07162)
 
## Conclusion

### 1. Advantages of the Thesis
The paper presents a novel zero-shot speech conversion system called StreamVoice, specifically designed for applications in streaming scenarios.StreamVoice employs a single-stage language model and acoustic predictor framework, and improves its performance by augmenting contextual learning with input history and using instructor-guided contextual foresight. Experimental results show that StreamVoice is able to achieve streaming speech conversion while maintaining comparable performance to non-streaming speech conversion systems, and requires only 124 ms latency to complete the conversion, which is 2.4 times faster than real-time.

### 2. Innovative points
  1. It introduces teacher-guided contextual foresight;
  2. secondly, it employs a semantic masking technique that encourages acoustic prediction from preceding acoustic and contaminated semantic inputs.
  
  These approaches enable StreamVoice to better capture the source speaker's information and produce high-quality speech conversion results. 
  
### 3. Future Works
Future research could explore how to further optimise the design of StreamVoice for higher performance and faster speeds. For example, the use of more efficient speech encoders or improved language modelling architectures could be considered to increase the efficiency of the system. In addition, ways to combine StreamVoice with other speech processing techniques, such as emotion recognition or accent conversion, could be explored to extend its application scenarios.  
