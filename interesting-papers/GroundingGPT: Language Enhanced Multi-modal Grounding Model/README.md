# GroundingGPT: Language Enhanced Multi-modal Grounding Model
[paper link](https://arxiv.org/pdf/2401.06071) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a language-enhanced multimodal localisation model called Grounding-GPT, which aims to address the limitations of current large-scale language models when dealing with fine-grained information          | Large Language Models（LLMs）|

## Methodology

### 1. Abstract
The model is capable of fine-grained localisation of images, video and audio, and employs a coarse-to-fine training strategy as well as diverse dataset construction methods to improve its performance. Experimental results show that the model is able to achieve fine-grained understanding of multimodal inputs while maintaining or improving global understanding. The authors make the code, dataset, and model publicly available to facilitate further research.

### 2. Method Description 
The paper presents a multimodal pre-training model called GroundingGPT for establishing semantic associations between different modalities such as image, video and audio. The model employs a CLIP visual coder, a ViT-L/14 network structure, and an adaptive mapping approach to process the inputs from different modalities, and achieves a finer-grained representation by combining spatial location information with temporal information. In addition, the model introduces a text-based representation of coordinates and timestamps to help the model better understand the spatial and temporal information in the input.

![image](https://github.com/user-attachments/assets/ba01f10b-5953-47b6-b48f-036ba9bf34aa)

### 3. Methodological improvements
The main improvements of the model are its multi-stage coarse- and fine-grained training strategy and data construction pipeline. In the first stage, the model is pre-trained multimodally using a public pre-training dataset to improve the model's understanding of various inputs. In the second stage, the model is trained at a finer granularity for spatial location and temporal information to further improve the model's performance. In the third phase, the model is fine-tuned using instructions that enable the model to generate responses that are more in line with human expectations and enhance multimodal interactions.

### 4. Issues addressed 
The model mainly addresses the problem of semantic association in multimodal scenarios, i.e., how to establish effective connections between different input modalities. By introducing multiple representations and training strategies, the model can better understand and process different types of data and generate more accurate and natural responses. This has important implications for many real-world application scenarios (e.g., intelligent customer service, speech recognition, etc.).

## Experiments
This paper presents an experimental study of a multimodal comprehension task. Firstly, in a multimodal localisation task, the authors conducted experiments using three datasets and compared them with previous end-to-end multimodal models and multimodal models based on language models. The results show that GroundingGPT performs well on multiple datasets and is even comparable to models trained specifically for the image region perception module. Second, in the video quiz task, the authors conducted experiments using the Charades-STA dataset and compared it with other video MLLMs. 

The results show that GroundingGPT performs well in the time-range retrieval task and has better performance than other video MLLMs. Finally, in terms of multimodal comprehension and suppression of object illusions, the authors conducted experiments using several visual quiz benchmarks and four benchmarks specifically designed for visual instruction tuning. The results show that GroundingGPT achieves state-of-the-art performance in all of these tasks and is able to effectively suppress object hallucinations.

Specifically, for the multimodal localisation task, the authors used the Reference Expression Understanding (REC) task to evaluate the model's image localisation capabilities. The authors used three datasets, RefCOCO, RefCOCO+, and RefCOCOg, and used previous end-to-end multimodal models, MDETR, UniTAB, and language model-based multimodal models as a baseline. The results show that GroundingGPT exhibits good performance on multiple datasets, even comparable to models trained specifically for the image region perception module.

![image](https://github.com/user-attachments/assets/ccaaa16f-cdfa-41a6-857d-e57e3c7705c0)

For the video quizzing task, the authors conducted experiments using the Charades-STA dataset and compared it with other video MLLMs. The results show that GroundingGPT performs well in the time-range retrieval task and has better performance than other video MLLMs.

![image](https://github.com/user-attachments/assets/7ee246be-e3bc-410b-9081-0e1ea762158e)

For experiments in multimodal understanding and suppression of object illusions, the authors conducted experiments using several visual quiz benchmark tests and four benchmark tests specifically designed for visual instruction tuning. The results show that GroundingGPT achieves state-of-the-art performance in all these tasks and is able to effectively suppress object hallucinations. 

![image](https://github.com/user-attachments/assets/b0315587-8e46-4eb9-ab88-61bde67a6c92)

## Conclusion

### 1. Advantages of the Thesis
  1. Accurate understanding of multiple input modalities: GroundingGPT is able to simultaneously process multiple input modalities such as image, video, and audio, and accurately capture the relationships between them.
  2. Multi-stage training strategy: The authors adopted a three-stage coarse-fine training strategy to gradually improve the model's performance capability, enabling the model to understand and process multi-modal data at different levels.
  3. Open source code and dataset: in order to promote the further development of the field, the authors release the model, code and dataset openly for other researchers to use and improve.

### 2. Innovative points
  1. The methodological innovation of this paper is that a multimodal bigram model is proposed, which is able to accurately capture the relationship between multiple input modalities for multimodal understanding and processing.
  2. In addition, the authors adopt a three-stage coarse-fine training strategy to adapt to different task requirements by gradually improving the model's performance capabilities. These innovations provide new ideas and methods for the research of multimodal learning.

### 3. Future Works
  1. Improving long video processing: exploring better modelling approaches to minimise information loss.
  2. Addressing multimodal input challenges: exploring how to perform multimodal tasks with multimodal inputs, such as simultaneous processing of spatial and temporal localisation in video.
  3. Extending grounding capabilities: extend the model's task scope to support a wider range of grounding requirements, such as pixel-level localisation and segmentation.
