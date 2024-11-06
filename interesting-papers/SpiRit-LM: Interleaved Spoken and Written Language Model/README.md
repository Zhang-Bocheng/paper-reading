# SpiRit-LM: Interleaved Spoken and Written Language Model
[paper link](https://arxiv.org/pdf/2402.05755) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a multimodal language model called SPIRIT LM that freely mixes text and speech information. The model is based on a pre-trained textual language model and is extended to speech modalities by successive training.          | Multimodal         |

## Methodology

### 1. Abstract
Speech and text sequences are merged into a single streaming token and trained using a small, automatically constructed speech-text parallel corpus. There are two versions of the model: the basic version (BASE) uses speech phoneme units (HuBERT), while the expressive version (EXPRESSIVE) considers pitch and style units in addition to phoneme units. In either version, the text is encoded using subword byte alignment. The experimental results show that SPIRIT LM has not only the semantic capabilities of the text model but also the expressive capabilities of the speech model. In addition, the authors demonstrate the ability of SPIRIT LM to learn new tasks with a small number of samples in a cross-modal task. The article provides model weights and inference code for readers' reference.

### 2. Method Description 
This paper proposes a language model called SPIRIT LM, which is based on continuous pre-trained text and speech datasets. Specifically, the model uses LLAMA 2 as the base model and different types of inputs (e.g., text-only, speech-only, and data with speech-text correspondence) are added during the training process to enhance its generalisation capability. In addition, the model employs techniques such as HuBERT and HiFiGAN to improve the quality of speech synthesis.

![image](https://github.com/user-attachments/assets/b0c182e6-4440-4858-aefd-ad12492bada9)

### 3. Methodological improvements
  1. More complex input types are used: in addition to text-only and speech-only, data with speech-text correspondences are included to help the model learn better cross-modal representations.
  2. The HuBERT model was introduced in the speech encoder to capture information in speech.
  3. The HifiGAN model is used in the speech decoder to further improve the quality of speech synthesis.

### 4. Issues addressed 
  1. **Cross-modal understanding:** since humans usually process multiple sensory information simultaneously, being able to understand and process information from different modalities is crucial for building comprehensive AI systems. The SPIRIT LM model proposed in this paper is trained to better understand these different input types by combining text-only, speech-only, and data with speech-text correspondences, and is able to perform cross-modal transformations when needed.
  2. **Expressive power:** In speech synthesis tasks, it is a key challenge to preserve the emotional expression of the original audio. The SPIRIT LM model proposed in this paper not only learns the basic features of speech, but also improves the expressiveness of speech by incorporating additional stylistic information.

## Experiments
This paper describes SPIRIT LM, a generative model using natural language processing techniques, and conducts several comparative experiments to evaluate its performance and performance. Specifically, the paper includes the following comparison experiments:

**Cross-Language Task Comparison Experiment:** this experiment compares the performance of SPIRIT LM with other benchmark models by performing zero-shot and few-shot generative tasks across different languages. The results show that SPIRIT LM performs well in most tasks, especially in cross-language text generation.

**Cross-modal Task Comparison Experiment:** this experiment compares the performance of SPIRIT LM with other benchmark models by combining speech and text data in a generation task. The results show that SPIRIT LM can effectively handle cross-modal generation tasks and outperforms other benchmark models on some tasks.

**Expressive Power Experiment:** this experiment compares different versions of SPIRIT LM in terms of their expressive power and generation quality by training them. The results show that increasing expressiveness improves generation quality, but also reduces training efficiency.

![image](https://github.com/user-attachments/assets/9c11e9eb-755a-4e68-8074-6b5c710064b6)

**Cross-domain experiment:** this experiment compares the performance of SPIRIT LM in different domains by testing it on datasets from different domains. The results show that SPIRIT LM can show better performance in various domains.

**Interpretability experiment:** this experiment explores how SPIRIT LM works and how to improve its interpretability by analysing the key steps in the generation process.

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a new language model, SPIRIT LM, which can generate both text and speech and performs well in cross-modal tasks.
  2. The authors use an alternating training approach, where speech and text data are inserted alternately in the input sequence, enabling the model to learn transitions between the two modalities.
  3. The ability to extend the speech modality by introducing expression tokens allows the model to maintain sentiment consistency when generating speech.
  4. The authors also propose a new benchmark test, SPEECH-TEXT SENTIMENT PRESERVATION (STSP), for evaluating the ability of the generative model to retain emotion across modalities.

### 2. Innovative points
  1. The SPIRIT LM proposed in this paper is a new language model that is capable of generating not only text, but also speech, and of switching between different modalities.
  2. The authors use an alternating training approach that allows the model to learn the relationship between the two modalities and to maintain consistency of sentiment when generating speech.
  3. The authors also propose a new benchmark test, STSP, to evaluate the ability of the generative model to retain emotion across modalities.

### 3. Future Works
  1. The performance of the model can be improved in the future by further improving the model architecture and training methods, such as increasing the model size and optimising the training strategy.
  2. SPIRIT LM can be compared with other language models to evaluate its performance and effectiveness.
  3. Further research can be conducted to address the issue of harmful content that may be generated by the generative model to ensure user safety.    
