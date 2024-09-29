# Enhance Audio Generation Controllability Through Representation Similarity Regularization
[paper link](https://arxiv.org/pdf/2309.08773) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents a novel approach to enhance the control of audio generation by emphasising the alignment between audio and textual representations. In language model-based audio generation, the approach utilises both text and audio token representation inputs to predict subsequent audio tokens.          |  Audio Generation        |

## Methodology

### 1. Abstract
The current configuration lacks explicit regularisation to ensure consistency between the selected textual representation and the predictions of the language model. Therefore, the authors propose an approach that combines audio and textual representation regularisation, in particular during the Classifier Free Guidance (CFG) phase, in which cross-attention to textual conditions is excluded during language model training. This approach aims to minimise audio and text similarity differences compared to other samples in the same training batch. 

### 2. Method Description 
The paper proposes a language model-based approach to audio generation that consists of three key elements: **a compression model, a text encoder, and a language model component**. Firstly, the compression model is used to encode the raw audio data into a discrete multi-stream sequence of tokens; secondly, a pre-trained text encoder is introduced to convert the input text into a set of embedding representations; and finally, the language model component is utilised to predict the probability distribution of the next audio token by combining the previous audio tokens and the text embedding representations. During the training process, the effective sequence length is reduced by training multiple streams of audio tokens in parallel, thus improving the training efficiency.

![image](https://github.com/user-attachments/assets/56fba599-fce8-499f-95ae-c5f224091c3f)

### 3. Methodological improvements
The paper proposes a new method called ‘representation regularization’, which aims to strengthen the correlation between audio and text representations while maintaining the effectiveness of the Classification Free Guidance (CFG) method to unconditionally train language models. Specifically, in each batch, a pooling method is used to obtain text sequence representations and audio sequence representations and to minimise differences in audio and text similarity compared to other samples. 

### 4. Issues addressed 
  1. Traditional cross-entropy loss cannot force audio token predictions to match the provided text conditions.
  
  2. When training a language model using the CFG method, the correlation between text and audio may become loose, resulting in a mismatch between the generated audio and the text.
     
## Experiments
This paper describes two experiments, music generation and sound effect generation. For music generation, the authors used a dataset with a total of 20K hours of licensed music and employed MusicCaps benchmarking to evaluate the effectiveness of the model. For sound effect generation, the authors used a dataset containing 4k hours of training data and employed datasets such as AudioCaps for training. 

In their experiments, the authors compared different model settings and parameter combinations and performed a human preference evaluation. The final results show that the effectiveness of the model and user satisfaction can be significantly improved by introducing representation regularisation.

![image](https://github.com/user-attachments/assets/81285b05-8bc2-442d-a757-51b5f0b76260)

![image](https://github.com/user-attachments/assets/6fc61bb4-6c33-47bc-9c79-283897f970f7)

## Conclusion

### 1. Advantages of the Thesis
  1. The method achieves this by minimising the similarity difference between text and audio representations, and its effectiveness is demonstrated by experimental validation on several music and sound effect generation tasks.
  
  2. In addition, the paper introduces some state-of-the-art neurogenerative models, such as diffusion probabilistic models and transformer-based language models, and demonstrates their excellent performance in the field of audio generation. These studies provide an important reference value for the development of the audio generation field.
 
### 2. Innovative points
  1. The main contribution of this paper is to propose the idea of representation regularisation, i.e., to enhance the connection between text and audio representations by minimising the similarity difference between the two during the training process.
  
  2. This approach not only improves the controllability and consistency of audio generation, but also can be applied to many different audio generation tasks with high generality.
  
  3. In addition, the paper introduces some recent neurogenerative models, such as diffusion probabilistic models and transformer-based language models, and demonstrates their excellent performance in the field of audio generation. These studies provide important reference value for the development of the audio generation field.
     
### 3. Future Works
  1. Explore more efficient representation learning methods to further improve the quality and controllability of audio generation;

  2. Investigating how to combine multimodal information (e.g., images, videos, etc.) to generate richer and more realistic audio;

  3. Developing more flexible and extensible audio generation frameworks that can be easily applied to real-world scenarios;

  4. Exploring how techniques such as reinforcement learning can be used to optimise decision-making and control strategies during audio generation.  
