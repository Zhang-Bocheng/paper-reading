# End-to-End Adversarial Text-to-Speech
[paper link](https://arxiv.org/pdf/2006.03575.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper describes an end-to-end speech synthesis method that directly takes text or phoneme sequences as input and outputs raw audio output.         |  Neural Networks         |


## Methodology

### 1. Abstract
  The generator proposed by the authors is feed-forward, using a differentiable alignment scheme for training and inference, along with a combination of adversarial feedback and predictive loss to learn to produce high-quality audio. To capture temporal variations in the generated audio, the authors also employ a soft dynamic time warping technique.
  
### 2. Method Description 
  This paper presents a neural network-based text-to-speech conversion model that centers on mapping input sequences to audio signals and improving the quality of the generated audio through adversarial training. Specifically, the model consists of two main components: an "aligner" for mapping irregular-length input sequences to fixed-length audio signals, and a "decoder" for extending the output of the aligner to the full audio frequency range. In addition, the model uses multiple In addition, the model uses multiple random window discriminators to improve the effectiveness of adversarial training, and employs techniques such as text normalization and pinyinization in the preprocessing stage to improve the quality of the generated audio.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/0c3227e4-c4d2-4142-a9e0-6c998692b1b4)

### 3. Methodological improvements
 The model has the following advantages over traditional text-to-speech conversion models:

  1. The model can handle input sequences of different lengths without padding or truncation.
  
  2. Adversarial training makes the generated audio more realistic while avoiding the pattern seeking problem.
  
  3. Multiple random window discriminators improve the effectiveness of adversarial training.

  4. Preprocessing techniques such as text normalization and pinyinization further improve the quality of the generated audio.
     
### 4. Issues addressed 
  The model solves the problems that exist in traditional text-to-speech conversion models, such as the need to fill or truncate input sequences and the difficulty of generating realistic audio. It also provides a simple and effective solution that can be applied to a variety of different speech synthesis tasks.

## Experiments
  This paper focuses on the experimental results and analysis of the EATS model proposed by the DeepMind team. The model is an end-to-end speech synthesis system that uses an adversarial learning approach to generate high-quality speech signals. The experimental part consists of two main aspects:

First, the authors used a multi-speaker dataset in their experiments and trained multiple models for comparison. Among other things, the authors quantitatively evaluated the performance of the models by means of Mean Opinion Score (MOS) given by a human evaluator. Specifically, the authors compared the output of each model to real speech and had a human evaluator score their naturalness. Ultimately, the authors derived MOS scores for the different models and compared them to the results of other related studies.

Second, the authors also conducted a variety of different experiments on different components of the EATS model to explore their effects on speech quality. Specifically, the authors investigated the effects of the EATS model on speech quality by switching on and off the components of the model such as the Random Window Discriminators (RWD), Mel-spectrogram Discriminator (MSD), length prediction loss and other components were operated on and off to obtain a range of different models, which were evaluated for MOS. In addition, the authors compare the effects of using different input methods (e.g., characters or phonemes), different alignment methods (e.g., monotonic interpolation or attentional mechanisms), and whether or not Dynamic Time Warping (DTW) is used on the performance of the models.

Taken together, the experimental results in this paper show that the EATS model has better speech synthesis capabilities on the multi-speaker dataset, and that the model's performance varies for different components and parameter settings. These experimental results provide valuable references and insights for subsequent research.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/5ab9a7a7-83f6-40cf-a2ae-d601d906d46e)

## Conclusion

### 1. Advantages of the Thesis
  1. This study presents an end-to-end speech synthesis model that can be learned using relatively weakly supervised signals (normalized text or phonemes paired with corresponding audio).
  
  2. The model produces speech that matches a given conditional text and has the ability to generalize to unobserved text with a naturalness scored by humans close to the best systems for multi-stage training pipelines or multi-layer supervised systems.
  
  3. The system description in Section 2 is efficient and does not rely on autoregressive sampling or teacher coercion during either training or inference, avoiding problems such as exposure bias and reduced parallelism in inference.
     
### 2. Innovative points
  1. The EATS model proposed in this study eliminates the typical intermediate bottleneck present in most state-of-the-art TTS engines by maintaining a learned intermediate feature representation throughout the network.
  
  2. The model consists of two high-level sub-modules: an aligner processes the raw input sequences and generates low-frequency (200 Hz) alignment features; these features are fed into a decoder that up-samples them into 24 kHz audio waveforms via 1D convolution.
  
  3. The design of the aligner and the combination of guided training (adversarial feedback and domain-specific loss functions) allow the TTS system to learn almost end-to-end, producing a natural sound with high fidelity, close to that of state-of-the-art TTS systems.
     
### 3. Future Works
  1. The end-to-end speech synthesis model proposed in this study has great potential to operate on raw text that has not been text-normalized and phonemicized.
  
  2. Further exploration can be done to improve the performance of the model, such as adding more data and model capacity, and improving the design of aligners and decoders.
