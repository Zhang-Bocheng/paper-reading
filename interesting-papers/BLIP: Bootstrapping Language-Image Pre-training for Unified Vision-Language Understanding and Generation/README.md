# BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation
[paper link](https://arxiv.org/pdf/2201.12086) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This paper introduces BLIP, a new visual language pre-training framework that can be flexibly applied to visual language comprehension and generation tasks.         | Vision-Language Pre-training(VLP)            |

## Methodology

### 1. Abstract
  While traditional visual language pre-training models usually only excel at one direction in either comprehension or generation tasks, BLIP can handle both. In addition, BLIP effectively reduces the impact of noise on model performance by utilizing network datasets for bootstrap learning. Experimental results show that BLIP outperforms other methods on tasks such as image text retrieval, image description, and visual quizzing, and has a strong generalization ability that can be directly applied to video language tasks.
  
### 2. Method Description 
  The paper presents a unified visual language pre-training framework called BLIP for learning data from noisy image-text pairs. The framework includes a multimodal hybrid encoder-decoder model called MED, and a dataset filtering method called CapFilt.

  The MED model uses Visual Transformer as its image encoder and introduces three features: a unimodal encoder, an image-based text encoder, and an image-based text decoder. During pre-training, three objectives are simultaneously optimized: comprehension-based and generation-based. 
  
  Specifically, ITC loss is used to encourage positive image-text pairs to have similar representations, while the opposite is true for negative image-text pairs; ITM loss is used to learn multimodal representations that capture fine-grained relationships between vision and speech; and LM loss is used to maximize the probability of generating a text sequence when given an image.

  The CapFilt method aims to improve the quality of text corpora. It consists of two modules: a generator for generating captions based on Web images, and a filter for removing noisy image-text pairs. Both modules are initialized from the same pre-trained MED model and fine-tuned separately for the COCO dataset.
  
### 3. Key concepts
  _Knowledge distillation_: A technique in machine learning where a smaller, simpler model (referred to as the "student") is trained to replicate the behavior and performance of a larger, more complex model (referred to as the "teacher"). The goal of knowledge distillation is to transfer the knowledge from the teacher model to the student model, thereby creating a more efficient and lightweight model that can achieve similar performance levels.
  
### 4. Methodological improvements
  The main improvement of the approach is the proposed BLIP framework, which is a unified VLP framework that can be used to learn data from noisy image-text pairs. In addition, the CapFilt method is proposed, which is a new approach to improve the quality of the text corpus, thus further improving the model performance.
  
### 5. Issues addressed 
  The method solves the following problem: how to learn data from noisy image-text pairs? And how to improve the quality of text corpus?
  
  By proposing the BLIP framework and the CapFilt method, the method successfully solves these problems and achieves significant performance improvement.
  
  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/262503e4-d6f9-42ad-9cad-47c893ffac03)

## Experiments
  This paper focuses on the authors' comparison experiments of several visual language tasks on the pre-trained model BLIP. Specifically, the authors compare the following six tasks:

1. **Image-Text Retrieval (ITR)**: this task involves retrieving the image from a library of images that best matches a given textual description. The authors used two datasets, COCO and Flickr30K, and fine-tuned the model with ITM and ITC loss functions. Experimental results show that BLIP outperforms existing methods in terms of average recall.

2. **Image Captioning**: this task requires generating a natural language description for a given image. The authors used two datasets, No-Caps and COCO, and fine-tuned the model with the LM loss function. The experimental results show that BLIP significantly outperforms other methods when using the same amount of pre-training data.

3. **Visual Question Answering (VQA)**: this task requires answering questions about a given image. The authors used the VQA dataset and fine-tuned it by considering the questions as an answer generation task. Experimental results show that BLIP outperforms ALBEF on the test set.

4. **Natural Language Visual Reasoning (NLVR)**: this task requires determining whether two sentences describe the same set of images. The authors made a simple modification to this task and fine-tuned it as a more computationally efficient architecture. Experimental results show that BLIP performs well on this task.

5. **Visual Dialog**: This task is visual Q&A in a natural dialog environment. The authors used the VisDial dataset and employed a ranking strategy for fine-tuning. The experimental results show that BLIP achieves the best performance on the validation set.

6. **Zero-shot Transfer to Video-Language Tasks**: this task applies the image language model to video-language tasks. The authors performed zero-shot transfer directly on COCO retrieval and VQA datasets and obtained impressive results.

Overall, the experimental results show that BLIP achieves excellent performance on several visual language tasks, proving the effectiveness of the CapFilt technique used in its pre-training phase. In addition, the authors conducted additional AB experiments to further validate the effectiveness of CapFilt.

## Conclusion
### 1. Advantages of the Thesis
  The paper proposes a new VLP framework, BLIP, which achieves broader downstream task performance improvements by using the Bootstrapping Language-Image Pre-training approach. BLIP employs a multimodal hybrid encoder-decoder model (MED) and introduces captioning and filtering methods to learn data from noisy image-text pairs. Experimental results show that BLIP achieves state-of-the-art performance on a variety of visual language tasks.
  
### 2. Innovative points
  1. The main contribution of this paper is to propose a new VLP framework BLIP, which employs a multimodal hybrid encoder decoder model (MED) and captioning and filtering methods.
  
  2. The MED model is a new model architecture that enables effective multi-task pre-training and flexible transfer learning. 
  
  3. The captioning and filtering method provides a new data enhancement method to learn more information from noisy image-text pairs, which improves the performance of the model.
     
### 3. Future Works
  1. The pre-trained corpus can be further expanded by iterating the dataset Bootstrap multiple times, generating multiple synthetic annotations, etc.

  2. it can also be CapFilt, etc., by training multiple different annotators and filters and combining their power.
