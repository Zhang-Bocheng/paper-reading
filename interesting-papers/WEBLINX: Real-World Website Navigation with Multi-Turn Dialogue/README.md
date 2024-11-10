# WEBLINX: Real-World Website Navigation with Multi-Turn Dialogue
[paper link](https://arxiv.org/pdf/2402.05930) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper introduces a new conversational web navigation problem and presents a large-scale benchmark test set called WEBLINX containing 100,000 interactions from 2,300 expert demonstrations.         | Large Language Models (LLMs) & Multimodal    |

## Methodology

### 1. Abstract
The benchmark test set covers more than 150 real-world websites and multiple modalities that can be used to train and evaluate agents in a variety of scenarios. Large Language Models (LLMs) cannot process entire web pages in real time due to the large amount of information. To address this problem, the authors designed a retrieval-based model that efficiently prunes HTML pages by ranking relevant elements. Using selected elements, screenshots and operation history, various models were evaluated, ranging from small text models to proprietary multimodal models. 

Experimental results show that the fine-tuned small decoder outperforms the best zero-sample LLMs (including GPT-4V), but the larger multimodal model performs better on specific tasks. However, all fine-tuned models struggled to generalise to unseen sites. These findings highlight the need for large-scale multimodal models that can be adapted to new environments.

### 2. Method Description 
The model proposed in this paper is divided into two main parts: **candidate element selection and model prediction**. In the candidate element selection phase, the authors adopted the Dense Markup Ranking (DMR) method to quickly filter out the task-relevant elements and use MiniLM for finetune. For the case of exceeding the length limit of the model input, the authors designed a truncation strategy based on the HTML structure to reduce the information loss. In the model prediction phase, the authors tried three types of models: **text-only models, image-to-text models and multimodal models**. Among them, the plain text model uses pre-trained models such as Flan-T5 or LLaMA for finetune; the image-to-text model uses the Encoder-Decoder architecture of Pix2Act; and the multimodal model uses a unified architecture such as Fuyu-8B to process both image and text data.

![image](https://github.com/user-attachments/assets/6ad0b1c3-d773-482c-8724-baecd91c74a8)

### 3. Methodological improvements
  1. Compared to previous methods, the main improvement in this paper is the adoption of a more efficient DMR method in the candidate element selection phase, which enables the whole model to interact in real time.
  2. In addition, in the model prediction phase, the authors explored several different types of models to better adapt to different scenario requirements.

### 4. Issues addressed 
This paper addresses the problem of how to efficiently build intelligent agent programmes in the field of web manipulation automation. By introducing the DMR approach and multiple types of models, the authors have successfully improved the performance and efficiency of the models so that they can achieve better results in real-world applications.

## Experiments
This paper presents a study for multimodal dialogue systems, including comparative results and analysis of several experiments. Firstly, the authors compare different types of models, including text-only models, image-to-text models and multimodal models, and evaluate their performance on different tasks. Second, the authors also compare the effects of different training approaches on model performance, including zero-sample learning and fine-tuning learning. Finally, the authors also analyse behavioural predictions in some specific scenarios to further understand the performance and limitations of the models.

In the first experiment, the authors compared **the performance of different types of models in accomplishing specific tasks**. They used the DMR input representation to train the Flan-T5 model and compared it to the MindAct model. The results show that the DMR input representation plays an important role in improving the model performance. In addition, the authors compared the performance of the LLaMA model and the Flan-T5 model in completing the task. Although the LLaMA model is smaller than the Flan-T5 model, it performs better. This may be due to the fact that the LLaMA model was trained with a large number of instruction-following tasks, while the Flan-T5 model had no such training experience.

In the second experiment, the authors compared **the performance of the image-to-text model and the multimodal model in completing specific tasks**. They used two models, Pix2Act and Fuyu-8B, and compared them to the Flan-T5 model. The results show that the Fuyu-8B model performs better than the Pix2Act model because it can receive text as input and has a larger number of parameters. However, the Pix2Act model performed better than the Fuyu-8B model in terms of intent matching and text prediction.

In the third experiment, the authors compared **the performance of the multimodal model and the chat-based text model in completing specific tasks.** They used the Fuyu-8B model and the LLaMA-based text model and compared them to the Flan-T5 model. The results show that the LLaMA-based text model performs better than the Fuyu-8B model, suggesting that the multimodal model is still lagging behind the chat-based text model optimised for command following when trained using screenshots.

In the fourth experiment, the authors compared **the performance of open-source and commercial models when performing specific tasks.** They used models such as GPT-3.5T, GPT-4T, Sheared-LLaMA, and LLaMA-2 and compared them to a test dataset. The results show that the commercial models perform better in the zero-sample learning setting, but the open-source models (e.g. Sheared-LLaMA and LLaMA-2) perform better in the fine-tuned learning setting.

In the fifth experiment, the authors compared **the performance of the models on familiar and unknown websites**. They used two datasets, TESTOOD and TESTIID, and compared them with different models. The results show that although the models perform well on familiar sites, they may have difficulties on unknown sites. For example, the LLaMA-13B model performs poorly on the TESTCAT dataset, suggesting that the unknown subcategory is more challenging than a new website in the same category.

In the sixth experiment, the authors qualitatively evaluated two models, GPT-4V and LLaMA-2-13B. They chose three action types (clicking, text input, and speaking) and provided two examples to show how each model performed in these scenarios. The results show that even when models correctly predict intentions, they may make incorrect predictions. For example, in the clicking scenario, GPT-4V selects an incorrect tab, while in the text input scenario, it tries to enter a username instead of a password in the password field. In addition, in the say scenario, GPT-4V used a different writing style, while LLaMA-2 learnt the annotator's writing style. 

## Conclusion

### 1. Advantages of the Thesis
  1. An important research question is posed: how can existing large-scale models be used to implement conversational website navigation in the browser.
  2. A new benchmarking dataset, WEBLINX, is proposed, which contains 2337 presentations from 155 real websites and records over 100K actions and discourses.
  3. Designed a method called Dense Markup Ranking (DMR) for converting HTML pages into compact representations for use in LSTM.
  4. A series of evaluation metrics dedicated to specific types of actions were developed to more accurately assess model performance.

### 2. Innovative points
  1. The use of an expertly constructed dataset, WEBLINX, which provides a variety of task definitions, data representations and assessment metrics, provides a complete framework for researchers.
  2. Used Dense Marker Ranking (DMR) technique to effectively convert web pages into compact representations, enabling LSTM to better process web information.
  3. A set of evaluation metrics specifically for different types of actions was developed, allowing researchers to more accurately assess the performance of the model. 
### 3. Future Works
  1. It is recommended that multimodal architectures be designed to efficiently handle situations where visual input is combined with structured information.
  2. It is recommended that models be evaluated in environments that cover a wider range of scenarios, including complex websites and advanced browser events, etc.
  3. It is recommended to extend to tasks other than browsers, such as operating system level interactions.
  4. It is recommended to utilise reward-based methods such as RLHF and DPO.
  5. It is recommended to explore other training methods such as self-experiential learning and context-based synthesis.   
