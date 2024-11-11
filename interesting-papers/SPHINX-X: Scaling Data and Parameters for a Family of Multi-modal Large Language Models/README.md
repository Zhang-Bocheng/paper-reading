# SPHINX-X: Scaling Data and Parameters for a Family of Multi-modal Large Language Models
[paper link](https://arxiv.org/pdf/2402.05935) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a family of large-scale multimodal language models called SPHINX-X, which is improved and extended from the SPHINX framework.          |   Multimodal Large Language Model (MLLM)      |

## Methodology

### 1. Abstract
To improve the architecture and training efficiency, the authors remove redundant visual coders, skip fully populated sub-images and use jump tokens, as well as simplify multi-stage training into a one-stage fully integrated approach. In addition, they constructed a comprehensive multi-domain and multi-modal dataset including publicly available resources in linguistic, visual and visual-linguistic tasks, and further enriched this collection by adding OCR-intensive and Set-of-Mark datasets. By training different base language models (e.g., TinyLlama-1.1B, InternLM2-7B, LLaMA2-13B, and Mixtral-8×7B), the authors obtain a wide range of multimodal language models with different parameter sizes and multilingual capabilities. Comprehensive benchmarking shows a strong correlation between multimodal performance and data and parameter sizes. 

![image](https://github.com/user-attachments/assets/b02dbc59-0120-4a26-9460-aebda241ddaf)

### 2. Method Description 
In this paper, a multimodal learning model called SPHINX-X is proposed for dealing with large-scale multitasking and multimodal instruction following problems. The model employs technical tools such as multiple visual coders, a learnable skip sub-image mechanism, and a single-stage training strategy to improve computational efficiency and performance performance. Specifically, SPHINX-X captures diverse visual representations by fusing four different visual coders (CLIP-ViT, CLIP-ConvNeXt, DINOv2, and Q-former), and uses two visual coders (MoV) to further provide complementary and refined visual knowledge. 

In addition, SPHINX-X introduces a learnable skip sub-image mechanism to replace fully populated sub-images, thereby reducing the input sequence length and saving computational resources. Finally, SPHINX-X employs a simplified one-stage training strategy that transforms all datasets into a multimodal multi-round dialogue format for an efficient training process.

![image](https://github.com/user-attachments/assets/ef8217fc-8776-4bdd-aabb-ec55584a9227)

![image](https://github.com/user-attachments/assets/a329a2b6-b391-488f-84cb-f208d6ac8592)

### 3. Methodological improvements
  1. **Streamlining of the visual coders:** the CLIP-ViT and Q-former encoders have been removed, and only the DINOv2 and CLIP-ConvNeXt encoders have been retained to improve computational efficiency.
  2. **Learnable skip sub-image mechanism:** a learnable skip sub-image mechanism is used instead of fully populated sub-images to reduce the input sequence length and save computational resources.
  3. **Single-stage training strategy:** A single-stage full-stage training strategy is used to transform all datasets into a multimodal multi-round dialogue format for an efficient training process.

These improvements enable SPHINX-X to better handle large-scale multitasking and multimodal instruction following problems with higher computational efficiency and performance.

### 4. Issues addressed 
  1. **Processing high-resolution images:** SPHINX-X improves computational efficiency by mixing multiple visual coders to process high-resolution images and introduces a learnable skip sub-image mechanism in place of fully populated sub-images.
  2. **Processing different types of visual data:** SPHINX-X can process visual data from different domains, such as object comprehension and comprehension of the entire image in computer vision tasks, as well as tasks such as visual quizzing and visual guidance.
  3. **Handling large-scale multitasking and multimodal instruction-following problems:** SPHINX-X employs a single-stage full-phase training strategy to transform all datasets into a multimodal multi-round dialogue format, which enables efficient large-scale multitasking and multimodal instruction-following problem solving.

## Experiments
This paper describes the performance of the SPHINX-X model on several visual language tasks and conducts comparative experiments with other models. Specifically, the following comparison experiments are conducted in this paper:

**On the Multimodal Language Model (MLLM) benchmark**, the SPHINX-X model is compared with models such as MathVista and CCbench, and the results show that the SPHINX-X model performs well on mathematical reasoning, complex scene comprehension, low-level visual tasks, and visual quality assessment, and is highly resistant to illusions.

![image](https://github.com/user-attachments/assets/1d1ad9f4-0249-456d-85cb-539b2d8426b2)

**On the Generalised Visual Questioning and Answering (VQA) benchmark**, the SPHINX-X model was compared with several benchmarks such as GQV, OK-VQA, VizWiz, etc., and the results showed that the SPHINX-X model performs well in general visual comprehension, relational reasoning, scientific context and symbolic visual reasoning.

![image](https://github.com/user-attachments/assets/3dd4a16f-affd-4bac-807c-ea2988f1d8cf)

**On text-oriented VQA benchmarks**, the SPHINX-X model is compared with several benchmarks such as TextVQA, OCRvQA, DocVQA, etc., and the results show that the SPHINX-X model is able to achieve good performance even with a small amount of OCR data.

![image](https://github.com/user-attachments/assets/9d38cff4-26ba-4a9e-bb8e-6f0653f4c366)

**On the referring object localisation task**, the SPHINX-X model is compared with benchmarks such as RefCOCO, RefCOCO+ and RefCOCOg, and the results show that the SPHINX-X model performs well in accurately recognising and understanding referring objects in images.

![image](https://github.com/user-attachments/assets/2577e507-1fe4-4544-ae73-53a8b210b359)

**On other MLLM benchmarks**, the SPHINX-MoE model was compared with benchmarks such as MathVerse, SciVerse, MMVP, HallusionBench, AesBench, MMMU, and ScreenSpot, and the results showed that the SPHINX-MoE model performed well in mathematical problem solving and scientific understanding and has better visual understanding and less verbal illusions.

![image](https://github.com/user-attachments/assets/253e7801-8414-47b7-a9f0-222c4815dfa2)

**On the video analysis task**, the SPHINX-Plus model was compared with models specifically designed for video tasks such as Jin et al. (2023), Su et al. (2023), and Zhang et al. (2023a), and the results showed that the SPHINX-Plus model performed well in video-exclusive comprehension and knowledge-based question answering, but was not successful in the challenging datasets where temporal relationships need to be modelled are slightly inferior to the best available methods. 

![image](https://github.com/user-attachments/assets/e52ebc56-11db-46bf-975a-24554168f634)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a new Multimodal Large Language Model (MLLM), called SPHINX-X, which improves the performance of the original SPHINX by improving three aspects of it: removing redundant visual coders, skipping fully populated sub-images and simplifying multi-stage training to single-stage holistic.
  2. The authors also collected a large-scale multi-domain dataset for MLLM training and demonstrated the superior performance of SPHINX-X in various benchmark tests.
  3. This research helps to advance the next generation of AI with a wide range of applications.
 
### 2. Innovative points
  1. SPHINX-X is proposed by improving SPHINX, thus enhancing its performance.
  2. A large number of multi-domain datasets were collected to support MLLM training, and two specialised datasets were constructed to enhance OCR-intensive and Set-of-Marks hinting capabilities.
  3. SPHINX-X was used in conjunction with base LLMs of different sizes to meet the needs of different scenarios.
 
### 3. Future Works
  1. This study provides a useful reference for future MLLM research, which can further improve the performance of MLLM by further optimising the model architecture and increasing the amount of data.
  2. MLLM can be applied to a wider range of domains, such as autonomous driving and graphical user interface agents.
  3. More MoV methods based on hybrid vision experts and other novel model architectures can be explored to improve the performance of MLLM.   
