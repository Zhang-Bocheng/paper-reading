# CM3: A Causal Masked Multimodal Model of the Internet
[paper link](https://arxiv.org/pdf/2201.07520) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper introduces a new model, CM3 (Causally Masked Multimodal Model), which can be trained on large-scale structured multimodal documents containing text and image tokens, and is capable of generating richly structured, multimodal output         |  Multimodal Modeling          |

## Methodology

### 1. Abstract
  Unlike traditional language models, CM3 employs causal masking to provide bi-directional contextual information by simultaneously masking out a small portion of long token strings during the generation process. The authors trained it on large-scale web articles and Wikipedia with excellent results.
  
  CM3 not only recovers the functionality of other models such as DALL-E, GENRE, and HTLM with zero samples, but also unconditionally generates images, describes them according to the text, and fulfills a variety of tasks.CM3 also sets new records for summarization, entity linking, and entity disambiguation, and in the fine-tuned settings to remain competitive.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/c59c2d8f-a64b-40cd-b161-d50b09c11dec)

## Conclusion
### 1. Advantages of the Thesis
  1. This paper proposes a new cross-modal pre-training model, CM3, which is trained on structured multimodal data at large scale and is capable of implementing a variety of zero/non-zero sample tasks.

  2. CM3 uses a novel "causal masking" technique, which allows the model to be trained in left-to-right order, and also allows bidirectional generation, which improves the model's performance.

  3. Through experimental verification, CM3 achieves excellent performance on several tasks, including image generation, image filling, text filling, and image classification.
     
### 2. Innovative points
 1. The CM3 model proposed in this paper is a new cross-modal pre-training model, which has higher flexibility and expressive power than existing models such as DALL-E.

 2. CM3 adopts the technique of "causal masking", which enables the model to be trained in left-to-right order, and also allows bidirectional generation, which improves the model's expressive ability.

 3. In terms of data processing, CM3 streamlines and filters HTML documents, removing useless information and improving the efficiency and performance of the model.
    
### 3. Future Works
  1. The CM3 model proposed in this paper performs well in cross-modal tasks, but there are still some issues that need to be solved, such as how to further improve the generalization ability and robustness of the model.

  2. In the future, considering combining CM3 with other models to form a more complex cross-modal system to cope with more complex application scenarios.

  3. More efficient training strategies and algorithms can also be explored to improve the training speed and effectiveness of the model.
