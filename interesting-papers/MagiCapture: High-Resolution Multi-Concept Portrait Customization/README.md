# MagiCapture: High-Resolution Multi-Concept Portrait Customization
[paper link](https://arxiv.org/pdf/2309.06895) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a portrait customization method called MagiCapture, which is capable of synthesizing high-quality, high-resolution portraits using a small number of reference images and allows for conceptual integration of different styles and themes.          | Attention         |

## Methodology

### 1. Abstract
The method mainly addresses the problem of unnatural faces in portrait generation, and also employs techniques such as attentional refocusing loss and auxiliary prior to make the model perform more robustly in weakly supervised learning environments. Experimental results show that MagiCapture outperforms other baseline methods in both quantitative and qualitative evaluations and can be extended to non-human object generation tasks.

### 2. Method Description 
The paper presents an image synthesis method based on textual cues and stylized images for integrating source content with reference styles given a small number of source and reference stylized images. The method is primarily used to generate portrait images, but can be applied to other types of images with simple modifications. The method utilizes a customization process for each concept and uses a combination of cues in the inference phase to generate multi-concept images. 

The method consists of two optimization phases: the first phase **optimizes the text embedding by reconstructing the target**; the second phase **optimizes both the text embedding and the model parameters for better reconstruction and generalization capabilities**. The method also proposes a mask reconstruction loss function for separating the identity information of the source subject from the information in other non-facial regions, as well as an attentional refocusing (AR) loss function for ensuring that the special markers focus only on the desired regions. Finally, the method also includes some post-processing steps such as super-resolution and face repair to further improve the quality of the generated samples.

![image](https://github.com/user-attachments/assets/cfa8ca5f-4d10-47d2-8145-ab16e5749677)

### 3. Methodological improvements
  1. The method employs two optimization stages to balance the relationship between reconstruction and generalization capabilities.
  
  2. In addition, it introduces a mask reconstruction loss function and an attentional refocusing (AR) loss function to ensure that the special markers focus only on the desired region. These improvements help to improve the quality and stability of the generated images.

### 4. Issues addressed 
  1. How to integrate the source content with the reference style given a small number of source and reference style images?
  
  2. How to ensure that special markers focus only on the desired region to avoid information leakage?
  
  3. How to improve the quality and stability of the generated images?
     
## Experiments
This paper focuses on the authors' experimental results using their own method to compare it with other personalization generation methods. Specifically, they selected a number of existing personalization generation methods (e.g., DreamBooth, Textual Inversion, and Custom Diffusion) as benchmarks and tested these methods using the same source and reference images. In addition, they manually selected 10 style concepts, resulting in 100 person-style pairs, each of which trained each benchmark model and generated 100 images, resulting in a total of 10,000 samples.

For evaluation, the authors used three metrics to measure the performance of the different methods: **facial similarity, style retention and overall image quality**. By calculating the cosine similarity of the facial embedding vectors between the source and generated images, the authors assessed the face similarity between the generated and source images. Also, they calculated the cosine similarity of the CLIP embedding vectors between the generated image and the reference image to assess whether the generated image preserves the style of the reference image. Finally, they used the LAION aesthetic predictor to assess the overall image quality.

![image](https://github.com/user-attachments/assets/d1d43fa5-33d0-44ff-9cdb-fb5c81dd404d)

Experimental results show that the authors' method outperforms other benchmark methods on all three metrics. A user study also showed that their method scored highest in ID preservation, style preservation, and image quality. In contrast, DreamBooth tends to overfit to reference style images, resulting in high style scores but low CSIM scores. In contrast, Textual Inversion tended to underfit both source and reference images, resulting in low-fidelity images that failed to preserve appearance details. Custom Diffusion better preserved source identity but still did not consistently perform well when dealing with composite cues, resulting in identity shifts and unnatural images.

![image](https://github.com/user-attachments/assets/0649f430-21a7-4e09-ac4c-7539a35f0f75)

Additionally, the authors conducted a pruning experiment and found that applying Attention Refocusing loss in the second stage of training was effective in preventing the attention map from focusing on unwanted regions, reducing information leakage and promoting information separation. The experimental results show that in the absence of compositional cue learning, the generated images often exhibit undefined behavior in which only one set of source or reference images appears in the image without blending.

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a method called MagiCapture for generating high-quality portraits using only a few reference images. The method solves the problems in traditional personalization methods by learning the source content and reference styles separately and generating a combined output.

  2.  MagiCapture employs pseudo-labeling and auxiliary loss learning to enhance the fusion effect between the source content and the reference styles; it also introduces attentional refocusing loss and mask reconstruction objectives to achieve information separation and prevent information leakage. Experimental results show that MagiCapture outperforms other benchmark methods, achieving excellent performance in both quantitative and qualitative evaluations.

### 2. Innovative points
  1. The main innovation of the MagiCapture method is its optimized design for the special needs in portrait photo generation. Specifically, the method employs a multi-concept customization approach that allows for the flexible synthesis of concepts from multiple themes or styles to generate more realistic and diverse photos.
  
  2. In addition, MagiCapture utilizes technical tools such as attentional refocusing loss and mask reconstruction of the target, which effectively solves the problems in traditional personalization methods and improves the quality and reliability of the generated photos.

### 3. Future Works
  1. Further exploring how to improve the efficiency and speed of portrait photo generation to meet the needs of large-scale applications;
  
  2. Combining the research results in the fields of natural language processing technology and affective computing, injecting more affective factors and semantic information into the generation of portrait photos;
  
  3. Strengthening the considerations of privacy protection and ethics and morality to ensure that the portrait photo generation applications do not violate the rights and dignity of users.
     
