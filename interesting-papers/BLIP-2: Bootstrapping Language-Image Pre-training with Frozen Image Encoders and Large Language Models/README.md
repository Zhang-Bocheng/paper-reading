# BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
[paper link](https://arxiv.org/pdf/2301.12597) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes an efficient pretraining strategy called BLIP-2 for visual language pretraining         | LLMs          |

## Methodology

### 1. Abstract
  Since end-to-end training of large models is becoming increasingly expensive, the method uses an off-the-shelf frozen image encoder and a large language model for pre-training, and bridges the gap between the different modalities with a lightweight query converter. Experimental results show that BLIP-2 achieves state-of-the-art performance on a variety of visual language tasks and has fewer trainable parameters than existing methods. For example, on zero-sample VQAv2, BLIP-2 outperforms Flamingo80B by 8.7%, but has only 54 times its trainable parameters. In addition, the model demonstrates the ability to follow natural language instructions for zero-sample image-to-text generation.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/a6155144-2d43-4124-b4d9-feea359c3091)

### 2. Method Description 
  BLIP-2 proposed in this paper is a pre-trained model based approach for visual language understanding, the main idea of which is to achieve better performance by utilizing existing pre-trained models. The method uses a Querying Transformer (Q-Former), a learnable module to connect a frozen image encoder and a frozen language model. 
  
  During the pre-training process, the Q-Former is divided into two phases: a visual-linguistic representation learning phase and a visual-to-linguistic generation learning phase. In the first phase, the Q-Former is connected to a frozen image encoder for extracting visual features related to the text; in the second phase, the Q-Former is connected to a frozen language model for generating the text. In addition, the method employs several different self-attention mechanisms and pre-training objectives to improve the performance of the model.
  
### 3. Key concepts
  _Querying Transformer_: it uses self-attention as fundamental to the model's ability to handle sequential data. By computing attention scores between queries and keys and using these scores to aggregate information from values, Transformers can capture complex dependencies and relationships in the data, making them powerful tools for various AI applications.
  
### 4. Methodological improvements
  Compared to the previous BLIP method, BLIP-2 introduces more flexible query embedding and adds more pre-training tasks such as image-text comparison learning, image-generated text, and image-text matching. These improvements enable BLIP-2 to better handle complex visual language understanding tasks, thus improving the performance of the model.

### 5. Issues addressed 
  BLIP-2 aims to address the problems in existing visual language understanding methods, such as insufficient comprehension of complex scenes and difficulty in handling long texts. By introducing a more flexible query embedding approach and multiple pre-training tasks, BLIP-2 can better handle these problems, thus improving the performance of the model.
  
  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/33597857-f96c-4e8c-92e8-e6e896d40310)

## Experiments
  This paper presents the performance of the BLIP-2 model on several zero-sample visual language tasks and compares it with other methods. Specifically, the paper includes experiments in the following four sections:

  1. **Instruction-guided zero-sample image-to-text generation**: the ability to control image-to-text generation by adding a textual cue as input after a visual cue. The experimental results show that BLIP-2 achieves state-of-the-art results on the VQAv2 and GQA datasets, even though possessing 54 times fewer trainable parameters than Flamingo80B. Furthermore, this paper observes that either a stronger image encoder or a more powerful language model leads to better performance.

  2. **Image description generation**: the BLIP-2 model was fine-tuned for the image description generation task, which requires the model to generate textual descriptions for the visual content of an image. Experimental results show that BLIP-2 achieves state-of-the-art performance on the NoCaps validation set, exhibiting strong generalization capabilities.

  3. **Visual Q&A**: given labeled VQA data, the parameters of the Q-Former and image encoder are fine-tuned while keeping the language model frozen. Experimental results show that BLIP-2 achieves state-of-the-art results in open generative modeling.

  4. **Image-Text Retrieval**: directly fine-tuning the first stage pre-trained model without the language model for image-to-text retrieval and text-to-image retrieval. Experimental results show that BLIP-2 achieves state-of-the-art performance on the COCO and Flickr 30K datasets.

  In summary, the BLIP-2 model achieves state-of-the-art results on several zero-sample visual-linguistic tasks, demonstrating its ability to efficiently capitalize on the rapid advances in the visual and natural language communities. 
  
## Conclusion
### 1. Advantages of the Thesis
  1. A frozen image encoder and language model are used to reduce the computational cost.
 
  2. The Querying Transformer (Q-Former) is proposed for extracting useful visual features and feeding them into the frozen language model, which enables effective cross-modal semantic representation learning.

  3. State-of-the-art performance is achieved on several visual language tasks, including visual quizzing, image description, and image retrieval.
     
### 2. Innovative points
  1. A frozen image encoder and language model are utilized to avoid the problem of needing to use large models and datasets for end-to-end training.

  2. The Querying Transformer (Q-Former), which is a lightweight transformer for extracting useful visual features and feeding them into the frozen language model, is proposed to enable effective cross-modal semantic representation learning.

  3. During the pre-training process, a two-stage learning strategy is employed: the first stage is visual linguistic representation learning, and the second stage is visual-to-linguistic generative learning to further improve the model's expressive capabilities.
     
### 3. Future Works
  1. Further explore how to utilize more unlabeled data to improve the model's generalization ability and zero-sample inference.

  2. Investigate how to combine BLIP-2 with other techniques, such as self-supervised learning, transfer learning, etc., to further improve the model's performance capability.

  3. Explore how BLIP-2 can be applied to natural language processing tasks in other domains, such as machine translation and sentiment analysis.
