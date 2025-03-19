# Efficient Multimodal Fusion via Interactive Prompting
[paper link](https://arxiv.org/pdf/2304.06306) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents an efficient and flexible multimodal fusion method called PMF, which aims to address the problem of high computational cost of large-scale pre-trained models for downstream tasks.          | Multimodal Fusion         |

## Methodology

### 1. Abstract
The method employs a modular multimodal fusion framework and splits common cues into three types to learn different optimization objectives. What is more, the method adds cue vectors only in the deeper layers of the unimodal converter, which significantly reduces training memory usage. Experimental results show that the method achieves comparable performance compared to several other multimodal fine-tuning methods with less than 3% of trainable parameters and up to 66% savings in training memory usage.

![image](https://github.com/user-attachments/assets/81081dfe-3e2e-4c02-ada9-019e963f9047)

### 2. Method Description 
The Prompt-based Multimodal Fusion (PMF) strategy proposed in this paper is a learning framework for image-text multimodal tasks. The method is based on pre-trained visual Transformer and linguistic Transformer models and integrates two unimodal layers into a single multimodal layer through interactive prompts. In the unimodal feature extraction phase, the image input is processed and passed to the visual Transformer, while the text input is passed to the linguistic Transformer.These unimodal features are then passed to multiple multimodal fusion layers, each consisting of a query phase and a fusion phase. The query phase focuses on extracting the necessary information, while the fusion phase focuses on fusing information from other modalities together. In this process, we use three different types of cues: query cues, query context cues, and fusion context cues to dynamically learn different multimodal learning objectives.

![image](https://github.com/user-attachments/assets/38b3e3e4-761e-44da-9f0e-88d10b2acbe1)

### 3. Methodological improvements
  1. The use of interactive cues enables better control of information flow between different modalities.
  2. The use of nonlinear mapping functions to realize the transformation of cross-modal information improves the expressive power of the model.
  3. The use of three different types of cues to learn different multimodal learning objectives allows for more accurate capture of the relationships between different modalities.

![image](https://github.com/user-attachments/assets/f4cb2a57-24cc-47d2-97aa-c691de25a0e6)

### 4. Issues addressed 
The Prompt-based Multimodal Fusion strategy proposed in this paper mainly addresses the problem of information fusion in image-text multimodal tasks. Traditional methods are often difficult to accurately capture the relationships between different modalities, resulting in a degradation of model performance. In contrast, the method in this paper realizes the conversion and fusion of cross-modal information by using interactive cues and nonlinear mapping functions, which improves the expressiveness and prediction accuracy of the model. And, by using three different types of cues, this paper is also able to capture the relationship between different modalities more accurately, which further improves the performance of the model.

## Experiments
This paper focuses on the Prompt-based Multimodal Fusion (PMF) approach for multimodal classification tasks, and several comparative experiments are conducted to verify its performance and efficiency.

First, in terms of datasets and evaluation metrics, the authors used three multimodal classification datasets: UPMC Food-101, MM-IMDB, and SNLI-VE, and employed metrics such as accuracy and macro/microscopic F1 scores to evaluate model performance.

Then, the authors compared multiple baseline and existing methods, including Fine-tuning, VPT, P-BERT, LateConcat, MMBT, MBT, PromptFuse, and BlindPrompt. The results show that PMF improves performance while saving training memory compared to Fine-tuning only. In addition, PMF performs better and competitively compared to other prompt-based methods.

![image](https://github.com/user-attachments/assets/4cafbf3f-2616-4d4e-8818-b5d725258e6f)

Next, the authors conducted Ablation Study to explore the effects of different components and parameters. The results show that each module contributes to the quality of multimodal fusion, while adding more cues only harms the performance. In addition, deeper fusion layers and longer prompt lengths both improve performance, but too many prompts degrade performance.

![image](https://github.com/user-attachments/assets/4a2aa568-7eed-485d-8a45-788c2df8e86a)

Finally, the authors also explore the scalability and flexibility of PMF. By replacing the pre-trained models, the performance of PMF can be further improved while keeping the training memory consumption low. In addition, the authors tried the method of automatically searching for the best fusion structure and achieved better results.  

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new modular multimodal fusion framework, PMF, with high flexibility and bi-directional interaction capabilities and the ability to significantly reduce training memory usage.
  2. And, the authors propose three different types of interaction cues to dynamically learn different multimodal learning objectives to improve model performance.
  3. The superiority of PMF on multiple visual language datasets is verified through extensive experiments, proving it to be a very effective parameter-efficient method.

### 2. Innovative points
  1. The main contribution of the paper is to propose a new modular multimodal fusion framework, PMF, which enables bidirectional interaction between different modalities and is highly flexible.
  2. And, the authors categorize the cues into three different types in order to dynamically learn different multimodal learning objectives.
  3. This innovative approach allows the model to achieve comparable performance to traditional fine-tuning methods with fewer parameters and memory usage. 

### 3. Future Works
Future research directions include further investigating the application of PMFs in various multimodal understanding tasks, such as visual quizzing, and experimenting with different model architectures to improve the performance of PMFs. In addition, there is a need to further explore how to optimize the design of the cues to better adapt to different multimodal learning tasks.   
