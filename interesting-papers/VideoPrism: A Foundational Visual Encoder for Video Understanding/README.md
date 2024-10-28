# VideoPrism: A Foundational Visual Encoder for Video Understanding
[paper link](https://arxiv.org/pdf/2402.13217) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a general-purpose video encoder called VideoPrism that is capable of handling a variety of video comprehension tasks and requires only a fixed model.          | Transformer         |

## Methodology

### 1. Abstract
The encoder improves on the mask autocoding approach by pre-training on a heterogeneous corpus containing high-quality video title pairs and noisy parallel text (e.g., ASR transcripts), using a global local distillation and token shuffling scheme for global local semantic video embedding, allowing VideoPrism to focus primarily on video modalities and to take advantage of the valuable textual information associated with the video. The authors conducted extensive testing on four broad video understanding task groups, ranging from Web video quizzing to scientific CV, achieving the best performance on 33 out of 31 video understanding benchmarks.

![image](https://github.com/user-attachments/assets/9c7edefb-7973-4142-b6f1-81f0f2571edd)

### 2. Method Description 

This paper proposes a video pre-training model called VideoPrism, whose architecture is based on the standard Vision Transformer (ViT). The model uses large-scale video text data for pre-training and learns the visual semantic information and motion information in the video through two phases of training.

In the first phase, the authors used video-versus-text learning by aligning the video encoder with the text encoder in order to enrich the visual semantic information using linguistic supervision. In this process, the authors use a Multi Attention Pooler (MAP) to aggregate features from the video encoder and introduce auxiliary datasets such as WebLI.

In the second phase, the authors focused on how to learn appearance and action information from pure video data. They employ a modified masked autoencoder to learn motion understanding while retaining the semantic knowledge learnt in phase one. Specifically, they continue to train the video encoder using pure video data in the second phase and employ some improvements such as random shuffling and global local distillation loss to effectively utilise the knowledge from the first phase.

![image](https://github.com/user-attachments/assets/04ff6bb4-6b52-42be-8582-0e26a8cda887)

### 3. Methodological improvements
The main improvement of VideoPrism over previous video pre-training models is that it uses richer video text data for pre-training and learns the visual semantic information and motion information in the video through two stages of training. In addition, the authors propose some improvements for the second stage of training, such as stochastic shuffling and global local distillation loss, in order to make better use of the knowledge learnt in the first stage.

### 4. Issues addressed 
The goal of VideoPrism is to be a basic video encoder capable of capturing visual semantic information and motion information in videos. To address this problem, the authors propose a two-stage training framework that incorporates a large amount of video text data for pre-training. This approach can help the model learn richer visual semantic information and motion information, thus improving video understanding.

## Experiments
This paper focuses on the performance of the VideoPrism model on a video comprehension task and compares it with other approaches. Specifically, the authors conducted experiments in the following four areas:

In **the VideoGLUE benchmark**, VideoPrism achieves better results on all datasets compared to the best available methods. This shows that VideoPrism has strong video comprehension capabilities and is able to handle multiple types of video signals, including different aspects such as motion and appearance.

![image](https://github.com/user-attachments/assets/fb479385-5844-4d5a-a334-4bc5206983c6)

VideoPrism also performs well in **the zero-sample video text retrieval and classification task**, achieving the best results on multiple datasets. This shows that VideoPrism can not only be trained on labelled data, but also improve its generalisation ability by learning unlabelled data from different domains.

![image](https://github.com/user-attachments/assets/9d6bc8e9-f90b-4832-b848-d2645cfa143f)

VideoPrism also performs well in **the zero-sample video generation task** and can be used in video-to-speech generation tasks.

Finally, the authors also analysed **the components of VideoPrism to verify its effectiveness**. They found that techniques such as two-stage pre-training, global distortion loss, and token shuffling are important for improving VideoPrism's performance.

![image](https://github.com/user-attachments/assets/e94f2bc5-291c-47c5-b3ea-e55a5695ad9a)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a general video encoder called VideoPrism that achieves state-of-the-art performance on a wide range of video understanding tasks. The authors employ a large scale pre-training dataset and develop an efficient method for learning appearance and motion information.
  
  2. In addition, the authors propose a unique two-stage pre-training approach to accommodate mixed data sources and utilise video vs. language comparison learning to gather semantic information.
  
  3. Finally, the authors conduct a comprehensive evaluation that demonstrates the broad applicability and superior performance of VideoPrism across multiple domains.

### 2. Innovative points
The design philosophy of VideoPrism is to approximate the ideal pre-training dataset by assembling high-quality video title pairs as well as video clips containing noisy text descriptions. At the same time, the authors employ a unique two-stage pre-training approach, where the first stage uses video-text pairs for video language comparison learning, and the second stage performs improved masked video modelling based on all video-only data. The innovation of this approach is the ability to leverage mixed data sources and learn semantic information efficiently.
 
### 3. Future Works
Future research could further explore how to handle longer video sequences and incorporate them into long-term video understanding systems. In addition, combining this pre-training approach with other visual or natural language processing techniques could also be considered to improve the performance and efficiency of the model.   
