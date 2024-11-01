# CoLLaVO: Crayon Large Language and Vision mOdel
[paper link](https://arxiv.org/pdf/2402.11248) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper examines the current performance of large-scale visual language models (VLMs) in object-level image understanding and proposes a new visual cue tuning scheme, Crayon Prompt, to enhance the object-level image understanding of VLMs.          | Large Language Model (LLMs)         |

## Methodology

### 1. Abstract
It is shown that the current performance of VLMs is closely related to their zero-sample performance in visual language tasks, and thus improving basic image understanding is crucial for VLMs to perform well in VL tasks. By introducing a Dual QLoRA learning strategy, the approach allows for visual instruction tuning while maintaining object-level image understanding, resulting in significantly improved results for a wide range of VL benchmarks in the zero-sample setting. The code is available on GitHub.

### 2. Method Description 
The CoLLaVO model proposed in this paper is a visual question-answering model whose structure consists of a visual encoder, a Crayon Prompt, a multilingual base model (MLM), and a fully-connected multilayer perceptron (MLP) that connects the visual and linguistic components. Among them, CLIP is used as a visual encoder, while the MLM from InternLM-7B is used to process textual input. In addition, two fully-connected MLPs with GELU activation functions serve as bridge connectors. For CoLLaVO input, a prompting protocol is followed, where ‘’ denotes a special marker for image embedding features, ‘’ denotes a marker to stop text generation, ‘User:{}’ denotes a question template, and ‘Assistant:{}’ denotes an answer template.

![image](https://github.com/user-attachments/assets/1f9c33cd-ab78-4661-bc05-f17ab35d5c1e)

### 3. Methodological improvements
To ensure a full understanding of the objects in the whole image, CoLLaVO should be able to recognise all the different objects, including foreground (e.g. people, buses, bottles, hairdryers and handbags) and background (e.g. sky, road, river, ocean and snow) objects. To do this, the researchers used a panoptic segmentation model to generate panoptic colour maps to differentiate between the different object classes from the MS-COCO 2017 dataset and provide a visual cue for CoLLaVO to be able to focus on all the objects in the image.

To further improve CoLLaVO's object-level image understanding, the researchers proposed Crayon Prompt Tuning (CPT), which converts panoptic colour maps into vector quantitative features by learning semantic and numbered queries, and combines them with the backbone MLM to generate Crayon Prompts.Then, the Crayon Prompt-based Instruction Tuning (CIT) using crayon instructions, which processes complex visual instruction tasks by training semantic queries, numbered queries, and MLP connectors as well as backbone MLM.

### 4. Issues addressed 
The CoLLaVO model aims to implement visual question and answer, but traditional visual question and answer models have some problems, such as the inability to handle complex visual instruction tasks and the difficulty of maintaining both object-level image understanding and complex visual language performance. Therefore, the researchers proposed the CoLLaVO model, which solves these problems and improves the performance of CoLLaVO in visual question-answering tasks by introducing techniques such as Crayon Prompt and Crayon Prompt-based Instruction Tuning.

## Experiments
This article presents implementation details and experimental results of the CoLLaVO model. The model performs well in object-level image understanding tasks and outperforms several closed-source and open-source VLMs in zero-sample visual language understanding (VL) tasks.The article first describes five key technical details, including the implementations of QLoRA, Crayon Prompt, Image-CIT, and VL-CIT, as well as the training hyperparameters. Then, the article verifies the effectiveness of CoLLaVO through comparison experiments.

The first comparison experiment is **an accuracy comparison in an object-level image understanding task**. The authors used four powerful baseline models: BLIP2, InstructBLIP, Qwen-VL, and LLaVA1.5, which were evaluated on the MS-COCO 2017 dataset with 80 categories classified as ‘things’. The results show that CoLLaVO approaches or exceeds all benchmark models in terms of Top-20, Bottom-20 and average accuracy, and has the smallest performance gap between Top-20 and Bottom-20. This indicates that CoLLaVO performs well in object-level image understanding across multiple object classes.
![image](https://github.com/user-attachments/assets/f10e1c83-2598-434f-a6c3-42c1ec2a117a)

The second comparison experiment is **a performance comparison in a zero-sample VL task**. The authors used several well-known datasets to evaluate the performance of CoLLaVO, such as MME, MM-Bench, MM-Bench-Chinese and Q-Bench. The results show that CoLLaVO achieves excellent results in all these benchmark tests, especially in MME, MM-Bench, MM-Bench-Chinese and Q-Bench, which mainly assess visual perception and cognitive abilities.

The third comparative experiment was **an Ablation study of different factors of CoLLaVO**. The authors analysed the factors Crayon Prompt, Dual QLoRA, Image-CIT and VL-CIT for CoLLaVO. The results show that semantic embedding and numbering embedding in Crayon Prompt significantly improve the zero-sample performance of CoLLaVO on MME datasets. In addition, Dual QLoRA, Image-CIT and VL-CIT also positively affect the zero-sample performance of CoLLaVO, respectively. 

## Conclusion

### 1. Advantages of the Thesis
  1. The methodological innovation of the paper is the use of panoramic colour maps generated by the panoptic segmentation model as the base information of Crayon Prompt and embedded into CoLLaVO's multimodal language model in order to maintain the integrity of the original visual context.
  
  2. This approach is more efficient and accurate than drawing red circles directly on the image. The paper concludes with suggestions for future research directions, including further research into how to better utilise the Crayon Prompt and other visual cues to improve object-level image understanding, and exploring how these techniques can be applied to a wider range of natural language processing tasks.

### 2. Innovative points
  1. Crayon Prompt embeds object-level information into CoLLaVO's multimodal language model by using panoramic colour maps generated by the panoptic segmentation model to enhance object-level image understanding.
  
  2. The dual QLoRA learning strategy, on the other hand, allows CoLLaVO to learn from both Crayon Prompt and existing visual instruction tuning datasets, thus achieving an effective balance between object-level image understanding and complex VL problems.
 
### 3. Future Works
  1. Future research could further explore how Crayon Prompt and other visual cues can be utilised to improve object-level image understanding and apply it to a wider range of natural language processing tasks.
  
  2. In addition, attempts could be made to combine Crayon Prompt with other existing techniques (e.g., pre-trained models) to further improve the performance of CoLLaVO models. Alternatively, researchers may consider developing more zero-sample VL tasks in order to evaluate the potential of the CoLLaVO model for application in different domains.    
