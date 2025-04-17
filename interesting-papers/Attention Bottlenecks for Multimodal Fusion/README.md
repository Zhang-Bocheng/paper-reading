# Attention Bottlenecks for Multimodal Fusion
[paper link](https://arxiv.org/pdf/2107.00135) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper presents a new multimodal fusion approach for video classification tasks. Traditional machine perception models are usually unimodal and optimized on a single benchmark test.          | Multimodal Fusion         |

## Methodology

### 1. Abstract
Therefore, in the multimodal case, a “late fusion” approach is usually used where the final representation or prediction of each modality is fused at the last stage. However, the novel architecture based on the attention mechanism proposed in this paper uses a “fusion bottleneck” to achieve modal fusion at multiple levels. In contrast to traditional bilateral self-attention, the model forces information between modalities to pass through a small set of bottleneck latent variables, which requires the model to collect and compress relevant information from each modality and share the necessary information. Experiments show that this strategy improves fusion performance while reducing computational cost. The authors conducted a comprehensive ablation study and achieved state-of-the-art results in several audio-visual classification benchmark tests.

### 2. Method Description 
The Multimodal Bottleneck Transformer (MBT) proposed in this paper is a deep learning model for audio-visual fusion classification tasks. The model is based on Vision Transformer (ViT) and Audio Spectrogram Transformer (AST), and achieves effective fusion of multimodal information by introducing bottleneck tokens and different token fusion strategies.

Specifically, MBT extracts the RGB image and audio spectrum into non-overlapping N pixel blocks, respectively, and converts them into a one-dimensional token sequence. These markers are then fed into an encoder consisting of multiple self-attention layers. In each self-attention layer, the MBT uses either standard self-attention blocks or cross-modal self-attention blocks for information interaction. And, MBT controls cross-modal information flow by introducing bottleneck tokens to improve computational efficiency and reduce complexity.

### 3. Methodological improvements
The main improvement of MBT over traditional multimodal deep learning models is the introduction of bottleneck tokens and different token fusion strategies. By restricting the cross-modal information flow to be passed only through bottleneck tokens, MBT is able to efficiently compress and share information from different modalities. In addition, MBT provides three different token fusion strategies, including “pure” self-attention, cross-modal self-attention with independent parameters, and cross-modal self-attention with bottleneck tokens. These strategies can be selected based on the task requirements for optimal performance.

### 4. Issues addressed 
MBT aims to address the problem of information fusion in audio-visual fusion classification tasks. Conventional multimodal deep learning models usually have difficulty in processing large amounts of information from different modalities simultaneously and often require significant computational resources. In contrast, MBT can process multimodal information more efficiently and significantly reduce computational complexity by introducing bottleneck tokens and different token fusion strategies. Therefore, MBT can provide better performance and efficiency in practical applications.

## Experiments
This paper focuses on MBT, a multimodal fusion model for video classification tasks, and performs several comparative experiments to validate its performance and effectiveness. Specifically, the paper first describes the three video classification datasets used (AudioSet, Epic-Kitchens-100, and VGGSound) as well as the evaluation protocols, and then discusses the implementation details, followed by an ablation analysis of multiple key design choices, and finally compares it with existing approaches.

In the experiments, the authors used ViT as the backbone network and performed different sampling strategies for image and audio data, including video clips of different lengths, random cropping of RGB frames, and extraction of log mel spectrograms. Also, the authors performed a comparison of various fusion strategies, including self-attention, cross-attention, and bottleneck fusion, etc., and finally identified the bottleneck fusion strategy and optimized its parameters. In addition, the authors performed an impact analysis of input sample size and training set size, and compared MBT with other unimodal benchmarks and previous fusion methods.

![image](https://github.com/user-attachments/assets/dd759b3c-be3a-4b16-9e21-be9eaf8c3b5b)

The experimental results show that MBT has better performance performance with respect to unimodal benchmarks and other fusion methods, especially when dealing with tasks in audiovisual related categories. In addition, the authors further explain the advantages and features of MBT by visualizing the attention map, which is able to better focus on audio-related motion regions rather than the whole object. In conclusion, the MBT model proposed in this paper provides a new idea and solution for the multimodal fusion task and achieves better experimental results.  

## Conclusion

### 1. Advantages of the Thesis
This thesis proposes a new audio-visual fusion model that uses a cross-modal attention mechanism and explores different fusion strategies. By introducing a bottleneck to limit cross-modal attention flow, performance is improved and computational cost is reduced. And, the authors consider the scalability and fairness issues of the model and make recommendations for future work.

### 2. Innovative points
The methodological innovation of the paper is the introduction of a bottleneck mechanism to limit cross-modal attention flow, thus avoiding the high computational complexity associated with fully paired attention. Also, the authors experimented with the effects of different types of input representations and dataset sizes, and applied the proposed model to several benchmark tests to obtain the latest best results. 

### 3. Future Works
Future work in this paper includes extending MBT to other modalities (e.g., text and optical flow) and further research on fusion strategies in the framework of self-supervised learning. What is more, the authors point out the problem of bias in the training dataset, which needs to be taken care of when deploying, analyzing, and constructing models.  
