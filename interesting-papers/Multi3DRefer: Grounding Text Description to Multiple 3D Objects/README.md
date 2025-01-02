# Multi3DRefer: Grounding Text Description to Multiple 3D Objects
[paper link](https://arxiv.org/pdf/2309.05251) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |  This paper presents a new task - localising multiple objects in the real world using natural language descriptions.          | Multimodal & Transformer         |

## Methodology

### 1. Abstract
Existing 3D visual localisation tasks focus on locating a unique object based on a textual description, but this strict situation is not realistic, as multiple objects need to be located in real scenes and robotics tasks. To address this problem, the authors propose Multi3DRefer, which is a generic dataset and task containing 61,926 descriptions of 11,609 objects, where each description can refer to zero, single or multiple target objects. In addition, they introduce a new evaluation metric that draws on previous work to facilitate research in multimodal 3D scene understanding.

### 2. Method Description 
The Multi3DRefer dataset presented in this paper is based on an enhanced version of the already existing ScanRefer dataset containing descriptions of zero-target, single-target, and multi-target scenes, and is designed to study multi-target visual localisation tasks. To increase data diversity, the authors used automated tools to generate more data samples and ensured their quality through manual validation. In addition, they used the GPT-3 model to reformulate the original text to increase the diversity and naturalness of the descriptions.

![image](https://github.com/user-attachments/assets/ea4b0858-0bdc-4ee4-a27f-261c7b1acce2)

In terms of model design, the authors used a two-stage CLIP-based architecture, where PointGroup acts as a detector, CLIP acts as a text encoder, and a Transformer-based fusion module combines object features with token-level embedding. During training, they introduce a contrast loss to help learn better multimodal embeddings and use a binary cross-entropy loss to supervise the matching module in selecting objects that satisfy the description. Finally, they also introduce two different settings for the construction of positive and negative samples and the selection of prediction thresholds.

![image](https://github.com/user-attachments/assets/141275a6-de13-4e9c-9133-ba64f21a4ec6)

### 3. Methodological improvements
Compared to traditional visual localisation tasks, the goal of this study is to locate multiple objects and therefore needs to deal with more complex situations. To address this issue, the authors used an automated tool to generate more data samples and ensure their quality through manual validation. In addition, they used the GPT-3 model to reformulate the original text to improve the diversity and naturalness of the descriptions. These improvements helped to improve the performance of the model and reduce the risk of overfitting.

### 4. Issues addressed 
The main problem in this study is multi-target visual localisation, i.e. given a 3D scene and a free-form linguistic description, predicting the bounding boxes of all objects that match the description in terms of axis alignment. To address this problem, the authors propose a two-stage CLIP-based architecture with automated tools and GPT-3 models to enhance the diversity and naturalness of the dataset. Experimental results show that the method can effectively perform multi-target visual localisation tasks at different difficulty levels.

## Experiments
This paper focuses on the performance of the M3DRef-CLIP model on the ScanRefer and Multi3DRefer datasets, and performs several comparative experiments to analyse the performance and effectiveness of the model.

First, on the ScanRefer dataset, the authors compare M3DRef-CLIP with a number of recent models, including models with joint input of additional data. The results show that M3DRef-CLIP outperforms all previous work in terms of accuracy, both using predictive and true frames. The authors attribute this to the use of two key factors, the CLIP text encoder and a powerful 3D object instance segmentation network (PointGroup) as an object detector.

Secondly, on the Nr3D dataset, the authors found that M3DRef-CLIP performed slightly worse than ScanRefer due to its weak real frame encoder. However, the use of 2D image information is helpful for the two-stage approach compared to other methods.

Next, the authors also examined the dataset of the Multi3DRefer task (Multi3DRefer) by dividing it into two subsets, single target and multi-target, and compared the use of additional multi-target descriptive data when training the model. The results show that the use of rewritten multi-target descriptive data improves performance on the ScanRefer dataset, whereas the models under the task setting (i.e., using prediction frames) using the Multi3DRefer dataset have good generalisation.

![image](https://github.com/user-attachments/assets/0b6ccd83-786f-438f-9683-03a579331d2a)

In addition, the authors conducted several comparative experiments to further analyse the performance and effectiveness of M3DRefer-CLIP. For example, they compared the use of pure CLIP only and the combination of CLIP and 3D features and observed that using the CLIP text encoder improves the performance while combining CLIP and 3D features gives the best performance. Additionally, they tested the need to use contrast learning in M3DRef-CLIP and found that the benefits of contrast loss were observed on the ScanRefer, Nr3D and Multi3DRefer datasets.

![image](https://github.com/user-attachments/assets/df2a9c6d-b33f-4278-9677-7b553e96eab0)

Finally, the authors analyse the descriptions of different attributes in the Multi3DRefer dataset to better understand how M3DRef-CLIP solves the task. They divided the descriptions into four categories: spatial, colour, texture and shape and compared the differences between M3DRef using GRU and PointGroup features and the full M3DRef-CLIP model. The results show that adding features from CLIP helps to recognise all these attributes, with hybrid 3D and CLIP performing best. In addition, the authors found that descriptions with spatial terms were more challenging than descriptions with texture or shape, while adding CLIP image features helped the most for colour and shape descriptions.

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a new task - using natural language descriptions to locate a flexible number of objects in a real-world 3D scene - and devises a simple yet effective data generation pipeline to create more diverse datasets by utilising existing linguistic data and ChatGPT.
  2. In addition, the authors explore an end-to-end fundamentally linear approach to this new task, which enables online rendering of the proposal object to generate 2D cues, and demonstrate the usefulness of CLIP and multimodal contrast loss.
  3. Multi3DRefer will bring additional challenges and practical value to the task of bridging vision and language, especially in the context of robotics and entity AI tasks.

### 2. Innovative points
The main contribution of the thesis is the presentation of an enhanced dataset and task, Multi3DRefer, in which a flexible number of target objects (zero, one, or more) can be localised in a 3D scene and a natural language description is given. Also, the paper provides a method based on CLIP embedding and online rendering of object proposals for multi-target visual localisation tasks.

### 3. Future Works
Future work could consider the use of positional coding to improve the model's ability to handle spatial relationships. It would be a good direction to investigate whether the use of positional coding can improve the model and which positional coding works best.  
