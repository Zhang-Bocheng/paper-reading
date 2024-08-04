# NÜWA: Visual Synthesis Pre-training for Neural visUal World creAtion
[paper link](https://arxiv.org/pdf/2111.12417) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper presents a multimodal pretrained model called NU WA that can be used for a variety of visual synthesis tasks, including generating new or manipulating existing image and video data.          | Transformer          |

## Methodology

### 1. Abstract
The model employs a 3D Transformer encoder-decoder framework and incorporates a 3D neighborhood attention mechanism that is capable of processing speech, image, and video data simultaneously. Experimental results show that NU WA exhibits state-of-the-art performance on tasks such as text-to-image generation, text-to-video generation, and video prediction, and also shows impressive capabilities in the zero-sample case.

![image](https://github.com/user-attachments/assets/42601a2b-2526-4e5b-a536-d339428ae49c)

### 2. Method Description 
The paper proposes a unified 3D data representation that considers text, images and videos or their sketches as markers and defines a four-dimensional tensor X ∈ Rh × w × s × d to represent these markers. Where h and w denote the number of markers on the spatial axis (height and width), respectively, s denotes the number of markers on the temporal axis, and d is the dimension of each marker. 

For text, it is embedded into R1 × 1 × s × d using BPE; for images, it is encoded as continuous pixel values in R1 × 1 × s × d using VQ-VAE; and for videos, it is encoded using 2D VQ-GAN to obtain its 3D representation. In addition, a 3D neighborhood self-attention module based on 3D data representations supporting self-attention and cross-attention is proposed and trained on multiple tasks.

![image](https://github.com/user-attachments/assets/edbf6e65-dcdd-43df-9199-6b5955698a68)

### 3. Methodological improvements
The main contribution of this thesis is to propose a unified method for 3D data representation that can simultaneously process different types of data such as text, image and video with good performance. In addition, by introducing a 3D neighborhood self-attention module, the correlations and interactions between different types of data can be better captured, thus further improving the performance of the model.

### 4. Issues addressed 
This thesis addresses the problem of how to represent different types of data (e.g., text, images, and videos) in a unified way and use them for multi-task learning. By proposing a unified 3D data representation method and a 3D neighborhood self-attention module, the relationship between different types of data can be better handled, thus achieving better multi-task learning results.

## Experiments
This paper focuses on the performance of the NUWA model on several visual tasks, and several sets of comparison experiments are conducted to verify its effectiveness. Specifically, this paper includes the following four parts:

The first part is the **pre-training details**, which presents information about the input and output sizes of the NUWA model as well as the parameter settings during the training process.

The second part is **a comparison of the NUWA model with existing models on three tasks**: **text-to-image (T2I), video prediction (V2V), and image complementation (I2I)**. Among them, the NUWA model outperforms other models in both FID-0 and CLIPSIM metrics in the T2I task; in the V2V task, the NU¨WA model achieves the best performance in the FVD metrics; and the NU¨WA model is able to generate richer and more diverse images in the I2I task. 

![image](https://github.com/user-attachments/assets/435d77bc-aa8d-48cc-8e8b-a3658107c8c8)

The third section is **an application of the NUWA model to other tasks**. For example, in the S2I task, the NUWA model is able to generate more realistic buses; in the TI2I task, the NU¨WA model is able to generate high-quality results that are consistent with the original image; and in the S2V task, the NUWA model is able to realize the function of generating videos from 3D video data.

![image](https://github.com/user-attachments/assets/21c5e938-92c1-475f-8b3b-18f2073594e2)

The fourth part is **a further analysis of the NUWA model**. For example, this paper investigates the effect of different VQ-VAE settings on the model performance, and finds that using more discrete tokens improves the visual quality of the model; also, this paper proposes a new evaluation metric, Detected PA, to measure the semantic consistency of the model in the S2V task.

![image](https://github.com/user-attachments/assets/b112ff0d-b50e-491e-9135-906e7763fdea)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a unified pre-trained model called NUWA that can be used to generate new or manipulate existing images and videos supporting eight visual synthesis tasks.
  
  2. The model employs a generic 3D encoder-decoder framework that simultaneously considers three modalities: text, image, and video, and proposes a nearby sparse attention mechanism to take into account localized features on the spatial and temporal axes.
  
  3. In addition, the model is fully experimented on eight visual synthesis tasks with state-of-the-art results.

### 2. Innovative points
  1. NUWA, a generalized 3D encoder-decoder framework, is proposed to handle text, image and video modalities simultaneously;
  
  2. a nearby sparse attention mechanism is introduced to take into account local features on the spatial and temporal axes;
  
  3. full-scale experiments are carried out on eight visual synthesis tasks and state-of-the-art results are achieved. 

### 3. Future Works
  1. In the future, we can further explore how to apply NUWEA to more visual synthesis tasks and combine it with other technical tools (e.g., augmented learning) to improve its performance and application scope. 

  2. In addition, we can also try to combine NUWEA with techniques from other domains, such as NLP and audio processing, to realize more diverse application scenarios.   
