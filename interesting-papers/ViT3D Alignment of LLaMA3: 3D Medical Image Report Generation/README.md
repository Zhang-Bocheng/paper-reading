# ViT3D Alignment of LLaMA3: 3D Medical Image Report Generation
[paper link](https://arxiv.org/pdf/2410.08588) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper describes a new method for automatic medical report generation that utilises a large-scale language model and a 3D Vision Transformer (ViT3D) image encoder for processing.  | large-scale language model (LLMs)         |

## Methodology

### 1. Abstract
The authors use Asclepius-Llama3-8B as the language model and generate textual reports by autoregressive decoding. Experimental results show that the method achieves an average Green score of 0.3 and an average accuracy of 0.61 on the validation set, outperforming the benchmark model.

### 2. Method Description 
The paper presents an automatic medical report generation system based on a visual coder and a large language model. The system consists of a visual coder for processing raw image data and transforming it into an embedded representation, and a LLM for generating relevant reports related to the input images based on textual cues. The language module is a transformer model based on an attentional mechanism that predicts the logarithmic probability of the next marker by integrating information about the current marker sequence with the image embedded representation. The visual encoder is based on a 3D visual transformer that sequentially processes 3D image data to obtain an embedded representation. The visual coder and large language model were pre-trained on a large dataset and fine-tuned on a given dataset for medical report generation and visual quizzing tasks.

In this study, Asclepius-Llama3-8B was used as the linguistic processing module and the 3D ViT module from M3D-LaMed was used as the visual processing module. The whole text generation process is implemented through an autoregressive decoding process, where the model generates the text output of the next token based on the previous token. The loss function uses Cross-Entropy loss to minimise the negative log-likelihood of the given image embedded and generated text.

![image](https://github.com/user-attachments/assets/de46ddba-475d-4175-b1c2-7f7d359cd2ae)

### 3. Methodological improvements
The system proposed in this thesis has high accuracy and efficiency in the field of automatic medical report generation. The system uses a large-scale external dataset, CT-RATE, which makes it more generalisable and scalable. In addition, the system uses a named entity recognition technique to extract organ information from textual reports and categorises sentences into ‘chest’, ‘abdomen’ and ‘pelvis’ based on the organ mentioned.

### 4. Issues addressed 
The system proposed in this thesis addresses some of the challenges in the automatic generation of medical reports, such as how to efficiently handle a large number of medical images and corresponding text reports, and how to improve the accuracy and efficiency of the system. The system is capable of automatically generating detailed reports related to medical images, reducing the workload of doctors and improving the quality and efficiency of healthcare services.

## Experiments
In this paper, two comparative experiments are conducted to compare the effect of fine-tuning the model using LoRA and without LoRA and to compare the effect of fine-tuning the model using the CT-RATE dataset and a given dataset.

For the first experiment, the authors used Green score as an evaluation metric in the MRG task and accuracy in the VQA task. The results showed that the model using LoRA fine-tuning improved the average Green score from 0.25 to 0.30 in the MRG task and accuracy from 0.46 to 0.61 in the VQA task compared to the model without LoRA fine-tuning.Although the Green score for the Chest category did not improve, the overall improvement demonstrates the effectiveness of LoRA fine-tuning. In contrast, the model that used the CT-RATE dataset for fine-tuning achieved similar performance in the MRG task as the model that did not use any dataset for fine-tuning, which may be due to incompatibility between the datasets.

![image](https://github.com/user-attachments/assets/fa440170-485b-46be-97ad-3beb0051732b)

For the second experiment, the authors used both the given dataset and an external dataset for model fine-tuning and compared the results with the results of fine-tuning using only the given dataset. The results show that the model fine-tuning with external datasets performs slightly better than the model fine-tuning with only the given dataset in the MRG task, but slightly worse than the latter in the VQA task. This suggests that it is important to choose the right dataset for fine-tuning for different tasks.

![image](https://github.com/user-attachments/assets/a6461dec-8264-4d6c-9f6c-289b6e2ae81e)

## Conclusion

### 1. Advantages of the Thesis
  1. The method combines visual and textual information to efficiently interpret complex medical images and generate relevant and accurate textual descriptions. By using an external dataset for fine-tuning, the method is able to achieve better results compared to a benchmark model on limited data.
  2. In addition, the method demonstrates the effectiveness of combining Vision Transformer (ViT) and Large Language Modelling (LLM) to bridge the gap between image understanding and language generation in the medical field.

### 2. Innovative points
  1. The method embeds visual information into a feature map and passes it to Vision Transformer (ViT), which then connects the feature map with the cue embedding vectors, and finally inputs it into a large language model to generate the next tokens of the text to be generated.
  2. In addition, the approach uses a pre-trained model and a small amount of data to fine-tune the Asclepius-Llama3-8B language model to make it better suited for MRG tasks. This approach not only improves the capability of the model, but also reduces the amount of training data required. 

### 3. Future Works
  1. Expert reviews are needed to evaluate the performance of the model in future studies. In addition, the authors plan to introduce Reinforcement Learning from Human Feedback (RLHF) into their training process to further improve the quality and performance of the model.
  2. This approach will allow for better adaptation to real-world clinical scenarios and ensure that the generated reports have higher accuracy and reliability.    
