# InternLM-XComposer2: Mastering Free-form Text-Image Composition and Comprehension in Vision-Language Large Model
[paper link](https://arxiv.org/pdf/2401.16420) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |This paper presents an advanced visual language model called InternLM-XComposer2 that excels in free-form text image synthesis and comprehension.           |    Multimodal Learning      |

## Methodology

### 1. Abstract
Unlike traditional visual language comprehension, the model is able to flexibly interweave information from a variety of inputs (e.g., outlines, detailed text descriptions, and reference images) to enable highly customised content creation. The model employs an approach called Partial LoRA (PLoRA), specifically applied to image tagging, to preserve the integrity of pre-trained linguistic knowledge and strike a balance between accurate visual understanding and text combination. Experimental results show that the InternLM-XComposer2 model, based on InternLM2-7B, excels in producing high-quality multimodal content for long texts and has excellent cross-modal comprehension performance in various benchmark tests, not only significantly outperforming existing multimodal models, but also even surpassing GPT-4V in some evaluation metrics and the Gemini Pro.

![image](https://github.com/user-attachments/assets/0b88bbe1-3e9a-4bf8-9587-1a0e62f6ae3d)

### 2. Method Description 
The model proposed in this paper, called InternLM-XComposer2, consists of a visual coder and a language learning model (LLM), interconnected by an innovative low-rank adaptation module (Partial LoRA). Given a set of images and text, the LLM uses the output of the visual coder as visual tokens and the disambiguated text as linguistic tokens. These tokens are concatenated to form an input sequence. The visual coder is a lightweight model pre-trained on CLIP, while LLM employs the recently introduced InternLM-2.

In order to achieve effective modality alignment, the authors propose Partial LoRA, a pluggable module designed to align the knowledge of the new modality with the LLM. The module adopts the inspiration of the original LoRA and adapts the low-rank matrix for the input labelling of the new modal part. In the specific configuration, Partial LoRA is applied to all visual markers.

![image](https://github.com/user-attachments/assets/e9d900ea-8d8b-410d-81a8-75a6ec5885db)
  
### 3. Methodological improvements
The methodology proposed in this paper focuses on the use of a carefully curated dataset in the pre-training phase to enhance the model's capabilities, while a series of tasks are introduced in the supervised fine-tuning phase to further improve the model performance. In addition, in the free-form text-image combination task, the authors have collected a large amount of high-quality data covering a wide range of writing styles, flexible text editing, complex instruction following, and personalised materials.

### 4. Issues addressed 
The main contribution of this paper is to propose a new multimodal learning model that can effectively deal with the relationship between visual and linguistic information. By jointly training the visual coder and LLM, the model is able to achieve good performance on multiple tasks, such as image classification and text classification. In addition, by collecting a large amount of high-quality data, the model has some generalisation ability and can be applied to a variety of different application scenarios.

## Experiments
This paper focuses on the performance of InternLM-XComposer2 in several benchmark tests and compares it with existing SOTA models and APIs. Specifically, the authors conducted the following three comparison experiments:

**MLLM Benchmark results:** the authors used multiple benchmarks such as MathVista, MMMU, and AI2D to validate the performance of InternLM-XComposer2. The experimental results show that the model performs well in these benchmarks and even exceeds the performance of some closed-source APIs. For example, it achieved a score of 57.6% on MathVista and 78.9% on AI2D, which is better than the API performance. Also, the model is able to handle some challenging tasks, such as university-level MMMU tasks.

![image](https://github.com/user-attachments/assets/731a9068-6613-40ad-9746-5d0197799de8)

**Open source model comparison:** the authors also compared InternLM-XComposer2 with other open source MLLMs. The experimental results show that the model exhibits state-of-the-art results in all benchmarks, including MME-Perception. In addition, the model achieved close to 80% accuracy.

![image](https://github.com/user-attachments/assets/b8cbaff9-11e9-42eb-9ede-5026c1283492)

**Creativity Benchmark Results:** finally, the authors used the CreationBench benchmark test to evaluate the creativity capabilities of InternLM-XComposer2. The results show that the model not only performs well in terms of overall creativity, but also significantly outperforms previous open-source LLMs in key metrics.The model maintains a strong performance even in the presence of the GPT-4 reference answer, demonstrating its ability to generate highly creative and logically-structured responses, which is critical for user engagement and satisfaction. 

![image](https://github.com/user-attachments/assets/27def22c-4da4-4bae-bb1c-43bdaddf8bc3)

## Conclusion

### 1. Advantages of the Thesis
  1. The authors enhance the performance of the model by introducing the innovative Partial LoRA (P-LoRA) method, which adds additional LoRA parameters specifically for image tagging to balance accurate visual comprehension with literary composition capabilities. 
  2. In addition, the authors propose a high-quality and diverse data base that includes sophisticated instruction following, customised text and image content, high-quality and stylistically diverse writing, and flexible text editing. 
  3. Together, these design elements contribute to a model that outperforms existing open-source MLLM models on a variety of assessment metrics and meets or exceeds the performance level of state-of-the-art models such as GPT-4V and Gemini Pro.

### 2. Innovative points
**Partial LoRA:** The design passes the image tokens forward with additional LoRA parameters, while the linguistic tokens retain their original architecture. This selective enhancement ensures that the model maintains good performance in both the visual and textual domains.

**High-quality and diverse data base:** the authors collected a large amount of high-quality pre-trained and supervised fine-tuned multimodal data covering a wide range of genres and aspects, such as captioning, generic Q&A, scientific Q&A, chatty Q&A, mathematical Q&A, conceptual knowledge, dialogue, and textual image synthesis. The quality and diversity of these data is crucial for the model's visual language comprehension and authoring capabilities.

### 3. Future Works
  1. The authors believe that the potential of the model for free text image synthesis has not yet been fully realised, and that its visual-linguistic comprehension performance can be improved by further improving the model's detail perception and complex reasoning capabilities.
  2. In addition, the authors also point out that with the development of technology, the model can be applied to a wider range of application scenarios, such as automatically generating multimedia content and assisting creative design.
