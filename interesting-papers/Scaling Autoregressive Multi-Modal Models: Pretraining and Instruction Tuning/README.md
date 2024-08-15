# Scaling Autoregressive Multi-Modal Models: Pretraining and Instruction Tuning
[paper link](https://arxiv.org/pdf/2309.02591) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents a multimodal language model called CM3Leon that can generate both text and images with high quality.          | Multi-Modal Models         |

## Methodology

### 1. Abstract
The model employs a training method of large-scale retrieval-enhanced pre-training and multi-task supervised fine-tuning, which enables high-quality text-to-image and image-to-text generation. Experimental results show that CM3Leon outperforms similar methods in text-to-image generation and exhibits extremely high controllability across multiple tasks.

### 2. Method Description 
This paper proposes a pre-training method for text-to-image generation based on token-based decoder-only model. The method explores the potential of token-based decoder-only models in the text-to-image domain by simplifying the RA-CM3 model, modifying the dataset, and applying multimodal scaling laws. 

Specifically, the method uses images licensed on Shutterstock as a data source and employs the image disambiguator proposed by Gafni et al. to encode a 256 × 256 image into 1024 tokens. For the text part, the method uses a custom tokenizer with a vocabulary size of 56320 and introduces a special token " " to indicate transitions between modalities. In addition, the method employs a retrieval enhancement technique, which consists of two parts: intensive retrieval and retrieval strategy, to improve the generation results.

![image](https://github.com/user-attachments/assets/e1c8251b-cbc8-42e4-881a-cc743a52d36b)

### 3. Methodological improvements
  1. **Data source**: legal images on Shutterstock were used to avoid ownership and citation issues.
  
  2. **Image sorter**: the image sorter proposed by Gafni et al. (2022a) was used to encode a 256 × 256 image into 1024 tokens.
  
  3. **Text tokenizer**: a custom tokenizer with a vocabulary size of 56320 is used and a special token " " is introduced to indicate inter-modal transitions.
  
  4. **Retrieval Enhancement**: a retrieval enhancement technique, which consists of two parts: intensive retrieval and retrieval strategy, is used to improve the generation.
     
### 4. Issues addressed 
The method addresses the problem of how to effectively utilize large-scale data for pre-training in the field of text-to-image generation. Also, the method improves the generation effect by using retrieval enhancement techniques.

## Experiments
This paper focuses on the performance of the CM3Leon model in an image generation task and compares it with other models. Specifically, the authors conducted the following three comparison experiments:

**Comparison of different decoding strategies**: the authors used three different decoding strategies (Temperature Sampling, TopP Sampling and Contrast Decoding) to train the CM3Leon model and quantitatively evaluated its generation results. The results show that all of these decoding strategies positively affect the model's performance, with contrast decoding being the most effective.

**Comparison of CM3Leon with SOTA model**: the authors compared the CM3Leon model with several other text-to-image models, including DALL-E, PARTI, Make-A-Scene, etc., and evaluated their performance through FID metrics. The results show that the CM3Leon model achieves the best FID score in the zero-sample case, proving its better generalization ability.

![image](https://github.com/user-attachments/assets/21ad73d4-7398-4ef2-a93a-c7b59bcef793)

**Comparison of supervised fine-tuning**: the authors also performed supervised fine-tuning of the CM3Leon model and applied it to several visual language tasks, such as image description and visual question and answer. The results show that the CM3Leon model performs well on many tasks and even outperforms some previous state-of-the-art models.  

![image](https://github.com/user-attachments/assets/b5617031-b8bd-48a4-bce2-f260ae44444e)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a multimodal language model called CM3Leon that can efficiently and flexibly generate and populate text and images. The model demonstrates its potential to compete with or even surpass diffusion models in terms of cost-effectiveness and performance by extending the scope of autoregressive models.
  
  2. CM3Leon employs a comprehensive training strategy that includes a large-scale retrieval-enhanced pre-training phase with a diverse Shutterstock dataset as well as a second multi-task supervised fine-tuning phase.
  
  3. In addition, the model introduces a new self-contained contrast decoding method that improves the quality of text and image generation. The experimental results show that CM3Leon has a wide range of applications and encourage further exploration of this approach.

### 2. Innovative points
  1. CM3Leon is a retrieval-enhanced autoregressive multimodal language-based model that can efficiently generate and populate text and images.
  
  2. The model employs a comprehensive training strategy that includes a large-scale retrieval-enhanced pre-training phase with a diverse Shutterstock dataset and a second multi-task supervised fine-tuning phase.
  
  3. The model introduces a new self-contained contrast decoding method to improve the quality of text and image generation.
     
### 3. Future Works
  1. Explore more efficient retrieval enhancement methods to improve the efficiency and generalization ability of the model.
  
  2. Investigate how autoregressive models can be applied to other types of multimodal generation tasks, such as audio-image generation.
  
  3. Investigate how to combine autoregressive models with other types of generative models to achieve better performance and results.
