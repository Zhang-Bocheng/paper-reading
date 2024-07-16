# Jukebox: A Generative Model for Music
[paper link](https://arxiv.org/pdf/2005.00341.pdf)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper describes a model called Jukebox that generates music with singing in the raw audio domain.         | Transformer          |

## Methodology

### 1. Abstract
The model uses multi-scale VQ-VAE to compress long sequences of raw audio and is modeled using an autoregressive Transformer. The authors show that combining this model over a wide range of scales can generate high-fidelity and diverse songs lasting up to several minutes. In addition, the model can control musical and vocal styles based on artist and genre, and achieve more controllable singing effects with mismatched lyrics.

### 2. Method Description 
The paper proposes a Variational Autoencoder (VAE)-based approach to compress raw audio data and learn a representation of music in the compressed low-dimensional space. Specifically, they use a Variational Auto-Encoder (VQ-VAE) with embedding vectors, where the embedding vectors are obtained by randomly restarting to avoid the codebook collapse problem. In addition, they used a separated self-encoder to train different levels of the model to maximize the amount of information stored at each level. Finally, they used conditional models to control the style of music generated and provided lyrics as additional conditional signals.

![image](https://github.com/user-attachments/assets/9a530042-aecf-4fe3-a129-f0e5f15c34ab)

### 3. Methodological improvements
  Compared to traditional variational self-encoders, this method uses more techniques to improve its performance. First, they used random restarts to avoid the codebook collapse problem, which allowed all embedding vectors to be utilized efficiently. Second, they used separated self-encoders to train different levels of the model to better capture the different hierarchies of the audio. Finally, they used conditional models to control the style of music generated and provided lyrics as additional conditional signals, which enabled more flexible music generation.
  
  ![image](https://github.com/user-attachments/assets/eb3b3464-87dd-418d-9fd0-b7b1bde83648)

### 4. Issues addressed 
  The main goal of this approach is to generate high-quality and diverse musical compositions. To address this problem, they use a variety of techniques to improve the performance of their models, including random restart, separated self-encoders, and conditional models. These techniques allow them to better capture the different hierarchies of audio and enable more flexible music generation. As a result, their approach can be used to generate a wide variety of types of musical compositions, thus satisfying the needs of different users.
  
## Experiments
This paper describes the training and performance of the Jukebox music generation model, and conducts several comparison experiments to verify its effectiveness. Specifically, this paper focuses on the following comparison experiments:

**Audio reconstruction experiment**: this experiment compares the effects of different codebook sizes, skip sizes, and L2 losses on audio reconstruction. The results show that a larger codebook can improve the reconstruction quality, while a smaller skip size and joining spectral loss can increase the ability to encode high-frequency information, but also introduce some noise.

**Music Sample Generation Experiment**: this experiment compares the effects of music sample generation using different datasets and conditions. The results show that using larger and more diverse datasets and conditions can improve the quality and diversity of the music generated.

**New Styles and New Lyrics Generation Experiment**: This experiment compares the effects of generating new styles and lyrics given a vector of artist embeddings. The results show that in some cases the generated new styles and lyrics can resemble the original song, but in other cases they are less successful.

**New Sound Generation Experiment**: This experiment compares the effects of generating new sounds by mixing the sounds of two artists. The results show that this method can achieve new sound generation to some extent, but not always successfully.

  ![image](https://github.com/user-attachments/assets/b490575c-e865-451d-8ffd-d69c69527710)

## Conclusion

### 1. Advantages of the Thesis
  This paper presents a model called Jukebox that generates raw audio music in many different styles and artists, and can be conditioned to specific artists and genres. The model also has the option to specify lyrics to generate samples and is capable of generating songs with natural sounding vocals that last up to several minutes. The model has longer duration and higher recognizability than previous work.
  
### 2. Innovative points
This paper use a deep learning-based autoregressive sparse transformer and layer-by-layer compression to compress audio data into a discrete space and train the model with MLE to retain as much musical information as possible. In addition, the authors developed an automatic upsampler to reconstruct the information lost at each compression level. This approach allows for efficient compression and decompression without loss of musical information, thus improving the efficiency and accuracy of the model.

![image](https://github.com/user-attachments/assets/81751be0-ae23-43b5-8ad2-cfbf2805912c)

### 3. Future Works
  The Jukebox model proposed in this paper provides a new way of thinking in the field of music generation, which can generate high-quality musical works. Future research directions include further improving the performance of the model and expanding its application scope, such as in the fields of movie soundtracks and game sound effects. There is also a need to explore how to better utilize the existing music knowledge base to guide the learning process of the model, as well as how to deal with legal and technical challenges such as copyright issues.


