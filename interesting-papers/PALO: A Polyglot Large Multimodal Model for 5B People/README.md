# PALO: A Polyglot Large Multimodal Model for 5B People
[paper link](https://arxiv.org/pdf/2402.14818) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a large-scale multilingual multimodal model called PALO that provides visual reasoning capabilities in ten major languages including English, Chinese, Hindi, Spanish, French, Arabic, Bengali, Russian, Urdu, and Japanese, covering a population of about 5 billion people (65% of the world's total population).          |  Multimodal Model        |

## Methodology

### 1. Abstract
The approach uses a semi-automatic translation technique to convert a multimodal instruction dataset from English to the target language and adapts it using a fine-tuned large-scale language model, which ensures high linguistic accuracy and allows scalability with minimal human effort. By introducing a diverse instruction set, the model's performance is improved on multiple languages, especially those that are less represented, such as Hindi, Arabic, Bengali, and Urdu. The study also presents the first multilingual multimodal benchmark test to evaluate the cross-linguistic visual-linguistic reasoning capabilities of future approaches.

### 2. Method Description 
This paper presents a multilingual model called PALO that understands and generates content in ten major languages for nearly two-thirds of the global population. The model employs the LLaVA architecture and has been adapted for different computational settings, including a large-scale model of 7/13B and a mobile-efficient model of 1.7B. For the large-scale model, CLIP ViT-L/14 was used as the visual coder and projected into the input embedding space via a two-layer MLP, while for the mobile-efficient model, a lightweight downsampling projector (LDP) was used to reduce the number of visual tokens by using depth-separable convolution to significantly reduce training and inference time.

Next, the authors detail how to build a high-quality, multilingual instruction-tuned dataset to further improve the model's capabilities. They first selected a state-of-the-art LMM model and used it to develop a semi-automatic translation pipeline to translate the English dataset into the target language, creating a robust and diverse multilingual dataset. They then hired teams of native speakers to provide detailed review and correction for each language to address linguistic issues specific to each language, gender accuracy, and overall linguistic integrity. Finally, they manually validated and corrected approximately 1,000 dialogues, which they used to fine-tune the LMM model to improve translation accuracy and adapt to different language attributes such as tone and spelling.

![image](https://github.com/user-attachments/assets/6ccf7462-ce17-487f-b359-349e993235e4)

### 3. Methodological improvements
  1. The multilingual model (PALO) proposed in this paper is one of the closest models available to achieve a globalised vision. It is not only capable of handling multiple languages, but also capable of understanding and generating richer and more challenging examples, which helps to improve the model's comprehension and generation capabilities. 

  2. In addition, they propose a semi-automatic translation pipeline that allows them to quickly and efficiently translate English datasets into the target language, thus extending the applicability of the model. In addition, they proposed a lightweight downsampling projector (LDP), which makes the mobile model more parametric and computationally efficient.

### 4. Issues addressed 
The main contribution of this paper is to propose a comprehensive and high-quality tuned dataset of multilingual visual language instructions that effectively extends the model's ability to better understand and generate content in multiple languages. In addition, they propose a semi-automatic translation pipeline that can quickly and efficiently translate an English dataset into the target language, thus extending the applicability of the model. All these improvements address the limitations of existing models in multilingual processing and improve the performance and usability of the models.

## Experiments
This paper presents experimental results and analyses of a multilingual visual-linguistic model (VLM). The authors conducted four experiments to compare the effectiveness of different training methods and used a variety of metrics to evaluate model performance.

The first experiment is **a model pre-training and fine-tuning experiment**. The authors pre-trained the model using the CC-595K dataset and then fine-tuned it on a dialogue set containing 10 languages. In this experiment, the authors used accuracy as an evaluation metric and compared the performance of different model sizes (1.7B, 7B, and 13B) on different languages. The results show that the authors' proposed multilingual extension model performs well on high-resource languages and significantly improves on low-resource languages.

The second experiment is an analysis of resource allocation for different languages. The authors classified 10 languages into two categories, high-resource and low-resource, and analysed the differences in their performance in the model. The results show that high-resource languages perform relatively well, while low-resource languages require more training data to get better results.

![image](https://github.com/user-attachments/assets/92af607f-c94d-4334-ba94-2f748d7e3b2f)

The third experiment was to evaluate the model on a high-quality test set. The test set consists of 24 challenging images, each with a detailed description and a series of questions. The authors used accuracy as an evaluation metric and compared performance between different model sizes and languages. The results show that the authors' proposed multilingual extended model achieves good performance on all languages, especially on low-resource languages.

![image](https://github.com/user-attachments/assets/e2c055d5-4b07-4310-9ff6-b972da77764a)

The fourth experiment compares different strategies for multilingual training. The authors tried both language-specific training based and joint training based approaches and compared their performance on different languages. The results show that joint training can further improve performance on low-resource languages, but language-specific training can also achieve good results in some cases. 

## Conclusion

### 1. Advantages of the Thesis
  1. The paper describes a multilingual model called PALO that is capable of processing multiple languages and providing accurate text responses. The model demonstrates its cross-language comprehension and generation capabilities across multiple high- and low-resource languages, and shows its sense of humour and cultural sensitivity through dialogue in different scenarios.
  
  2. In addition, the paper describes the dataset and model training process and highlights the importance of data privacy protection.
 
### 2. Innovative points
  1. The methodological innovation of the thesis is the development of a multilingual model that is able to perform visual understanding and text generation in different linguistic contexts.
  
  2. At the same time, the model employs a semi-automated translation process, which makes the model more widely applicable and efficient.
  
  3. In addition, the paper proposes a training strategy based on a multilingual dataset, which can improve the performance and generalisation of the model.
 
### 3. Future Works
In the future, the model can be further improved to make it more adaptable to low-resource language environments and enhance the understanding of their cultural context. In addition, the model can be applied to more domains, such as natural language reasoning, image classification, etc., to achieve more AI applications.  
