# DeepSeek-VL: Towards Real-World Vision-Language Understanding
[paper link](https://arxiv.org/pdf/2403.05525) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper describes an open source visual language model called DeepSeek-VL, designed to support real-world visual and language understanding applications. The approach is centred around three key dimensions: data construction, model architecture and training strategy.         |  Large Language Model (LLMs)       |

## Methodology

### 1. Abstract
In terms of data construction, the model works to ensure that the data is diverse, scalable, and covers a wide range of real-world scenarios, including web page screenshots, PDF files, OCR, diagrams, and knowledge-based content (e.g., expert knowledge and textbooks), to achieve a comprehensive representation of real-world contexts. In addition, they created a use case classification system and constructed an instruction fine-tuning dataset based on this system, which greatly improved the user experience of the model in real-world applications. In terms of model architecture, taking into account efficiency and the needs of most real-world scenarios, DeepSeek-VL employs a hybrid visual coder that efficiently processes high-resolution images (1024 x 1024) and maintains a relatively low computational overhead within a fixed-labelling budget. 

This design choice ensures that the model is able to capture semantic and detailed information that is critical in a variety of visual tasks. In terms of training strategy, the authors believe that a proficient visual language model should first and foremost have strong linguistic capabilities. To ensure that LLM capabilities are preserved during pre-training, they explore an effective VL pre-training strategy by integrating LLM training and carefully managing the dynamics of competition between visual and linguistic modalities. Starting from text, the ratio is gradually adjusted to promote a balanced integration of the two modalities. Experimental results show that the DeepSeek-VL family (1.3B and 7B models) exhibits a superior user experience in real-world visuo-linguistic chatbot applications, achieving state-of-the-art or competitive performance on a wide range of visuo-linguistic benchmarks, while maintaining robust performance on language-centric benchmarks.

### 2. Method Description 
The DeepSeek-VL proposed in this paper is a multimodal pre-training model based on a visual coder, a language model and a visual language adapter. It includes a hybrid visual coder, a visual adapter and a language model. Among them, the hybrid visual coder contains two different visual coders: the SigLIP and the SAM-B. The SigLIP is responsible for processing high-resolution images, while the SAM-B is used for processing low-resolution images. In addition, two different datasets are introduced to train the model: image-text pairs and pure speech sequences.

<br>&emsp;**Visual-linguistic adapter pre-training phase**: the goal of this phase is to establish the connection between visual and linguistic elements and to improve the comprehension of the LLM.
<br>&emsp;**Co-visual-linguistic pre-training phase**: this phase further enhances the multimodal comprehension and linguistic capabilities of the model by co-training the linguistic model with the visual-linguistic adapter.
<br>&emsp;**Supervised fine-tuning phase**: this phase uses fine-grained fine-tuning with instructions to enhance the model's performance in dialogue.

### 3. Methodological improvements
  1. **The design of the hybrid visual coder**: by utilising both SigLIP and SAM-B for coding, visual information at different resolutions can be better captured, thus improving model performance.

  2. **Choice of datasets**: The authors chose a variety of datasets for training, such as ShareGPT4V and Document OCR, to ensure that the model can adapt to multimodal inputs in various scenarios.

  3. **Optimisation of training strategy**: By adjusting the training ratio and introducing SFT data, the model can achieve better results with limited computing resources.

### 4. Issues addressed
  1. **Enhancing the model's linguistic ability and multimodal comprehension**: the training of visual language adapters enables the model to better understand the relationship between visual elements and linguistic elements, thus enhancing the model's linguistic ability and multimodal comprehension.
  
  2. **Handling of low-resolution images**: traditional visual coders are difficult to handle low-resolution images, while SAM-B can effectively solve this problem, thus enabling the model to better handle low-resolution images.
  
  3. **Balancing the development of the model**: By optimising the training ratio and the dataset, the model is able to achieve better results with limited computational resources, thus balancing the development of the model.
      
![image](https://github.com/user-attachments/assets/662d58a7-5526-466e-836f-833d1f18379b)

## Experiments
This paper focuses on the authors' comprehensive evaluation and comparative experiments on the multimodal capabilities of the deep learning model DeepSeek-VL. Specifically, the authors evaluated the model on a public benchmark test dataset and compared it to models with publicly available source code. In addition, the authors evaluated the model linguistically and humanly, and analysed and optimised its components.

For public benchmarking datasets, the authors used several multimodal datasets, including MMMU, CM-MMU, and MMMBench, as well as the diagram comprehension dataset OCR bench, the hallucination dataset POPE, and the scientific question datasets ScienceQA and MathVista. The authors used a generative evaluation approach, allowing the model to automatically generate text and parsing results and compare them to known answers. Experimental results show that DeepSeek-VL performs well in these benchmarks, even outperforming some open source and proprietary models.

![image](https://github.com/user-attachments/assets/7c434e10-f45f-464a-81ac-5370ac1d90a3)

For linguistic and human evaluation, the authors independently constructed a dataset for manual evaluation of DeepSeek-VL's capabilities. The dataset contains 100 questions divided into seven categories, each covering a specific task. The authors combined this dataset with task and image material from existing reports to form similar image material and prompt statements. With this approach, the authors ensured that the dataset was comprehensive and representative. The authors compare DeepSeek-VL with models such as InternLM-XComposer2-VL, CogVLM, and GPT-4V and demonstrate their performance on various dimensions. The authors also conducted a comparative evaluation using GPT-4V to determine which model was better or declared a tie. The experimental results show that DeepSeek-VL outperforms the other models in most cases, especially in commonsense reasoning.

![image](https://github.com/user-attachments/assets/637a9edc-2315-41c4-988d-ca953d5eeb30)

Finally, the authors analysed and optimised different parts of DeepSeek-VL. They found that increasing the amount of data in the first phase of projector warm-up training does not improve performance, suggesting that the capacity of the projector is limited. In terms of training phases, the authors found that combining the first, second and third phases gave better results than combining only the first and third phases. When mixing data from different modalities, the authors found that direct mixing leads to inefficiency and therefore proposed a batch-by-batch grouping approach to solve this problem. In addition, the authors propose a progressive modality warm-up strategy that can effectively prevent significant language proficiency decline in the early stages of training.

![image](https://github.com/user-attachments/assets/81e2c737-bf4d-4e7d-b88b-70eff5fcb316)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents the DeepSeek-VL family of models, which addresses the problems of traditional pre-trained models in understanding multimodal data by prioritising the visual data processing stage.
  
  2. The model performs well in several benchmark tests and demonstrates superior linguistic and visual capabilities. In addition, the authors open source code and related datasets to facilitate further exploration and application by other researchers.

### 2. Innovative points
  1. Compared with traditional pre-trained models, DeepSeek-VL employs joint visual and linguistic pre-training to improve the model's performance on multimodal tasks. Meanwhile, the model introduces the concept of hybrid embedding space, which enables the model to better handle different types of input data.
  
  2. In addition, the authors propose a novel data augmentation method to increase the sample diversity by randomly cropping the images, which improves the generalisation ability of the model.

### 3. Future Works
It is foreseeable that research based on the DeepSeek-VL model will continue to grow in the coming years, and more researchers will also try to use similar hybrid embedding space approaches to solve challenges in multimodal tasks.    
