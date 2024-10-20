# Gen4Gen: Generative Data Pipeline for Generative Multi-Concept Composition
[paper link](https://arxiv.org/pdf/2402.15504) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper explores how to address two problems in personalised text-to-image diffusion models: the mismatch between complex scenarios and simple text descriptions and the lack of holistic metrics for assessing multi-concept personalisation performance.         | Diffusion Models         |

## Methodology

### 1. Abstract
To this end, the authors propose a semi-automated dataset creation pipeline (Gen4Gen) that uses a generative model to combine personalisation concepts into complex images with detailed text descriptions for each image. With this approach, they created a dataset called MyCanvas that can be used to test the performance of a multi-concept personalised text-to-image diffusion model. In addition, the authors devised a comprehensive metric that includes both CP-CLIP and TI-CLIP scores to better quantify the performance of the multi-concept personalised text-to-image diffusion approach. Finally, the authors demonstrate that the quality of multi-conceptual personalised image generation can be significantly improved by improving data quality and cueing strategies without modifying the model architecture or training algorithms.

### 2. Method Description 
The aim of this research was to construct a dataset for personalised image generation tasks and to design an automated data generation process called ‘Gen4Gen’. The process consists of three main stages: **object association and foreground segmentation, LLM-guided object combination, and background recolouring and image retelling**. 

First, a collection of objects is acquired from sources such as DreamBooth and Custom Diffusion and foreground information is extracted using the DIS algorithm. Then, the LLM model is used to provide possible bounding boxes for each object combination, based on which the objects are placed in the appropriate scene. Next, the generated layouts are adjusted to reflect real-world scale relationships using textual cues. Finally, the background is filled using a diffusion model such as Stable-Diffusion-XL, and the image is ‘recoloured’ after filling to improve the quality of the generation.

![image](https://github.com/user-attachments/assets/8267c635-9141-4942-ad70-fcdc008684d1)
  
### 3. Methodological improvements
The researchers introduced the following three improvement strategies to further enhance the generation results:

  1. **Introducing Global Composition Token**: Drawing on the abstract style learning mechanism in DreamBooth, global composition tokens are combined with individual tokens to enhance the model's ability to describe complex scenes.

  2. **Repeated Concept Token Cueing during Training**: For complex multiple concept combinations, in order to avoid missing a concept, each concept token is cued repeatedly to ensure that each specified concept appears in the generated image.

  3. **Fusion of background cues**: to avoid confusion between background and composite features composed of concepts, it is ensured that the background only appears in textual cues, thus allowing the model to focus only on object identity.
     
### 4. Issues addressed 
  1. **Design principles of the dataset**: detailed text description and image pairing, reasonable object layout and background generation, and high resolution are proposed to meet the needs of personalised image generation tasks.

  2. **Automated data generation process**: Through the ‘Gen4Gen’ process, multiple stages of object association and foreground segmentation, LLM-guided object combination, and background recolouring and image recapitulation are automated to improve the quality and scale of the dataset.

  3. **Model performance evaluation metrics**: two new performance evaluation metrics, Composition-Personalisation-CLIP (CP-CLIP) score and Text-Image Alignment CLIP (TI-CLIP) score, were designed, respectively are used to assess the scene composition and personalisation accuracy of the model as well as the generalisation ability of the model to avoid overfitting.

     ![image](https://github.com/user-attachments/assets/50ad94f8-03b2-4d45-b3eb-f1a4363ac8ad)

## Experiments
This paper focuses on the experimental design and result analysis of a personalised image generation model. The authors first describe the basic setup of the experiments, including the model used (Custom Diffusion), the dataset (OWL-ViT), and the evaluation metrics (CP-CLIP and TI-CLIP). The authors then conducted three sets of comparison experiments:

**Baseline experiment**: learning the original conceptual images and the MyCanvas dataset consisting of multiple conceptual images separately using the Custom Diffusion model, and comparing their performance in generating new images. The results show that using the MyCanvas dataset significantly improves the quality of the generated images compared to learning the original conceptual images.

**Experiments with cueing strategies**: based on the use of the MyCanvas dataset, the authors further propose a cueing strategy that involves adding a different contextual description for each combination of concepts. With this approach, the generalisation ability of the model can be better analysed. Experimental results show that the cueing strategy further improves the accuracy and consistency of the generated images.

![image](https://github.com/user-attachments/assets/fd405648-b718-4662-a166-f68d3b788e2a)

**Post-processing experiments**: the authors also performed post-processing on the generated images to improve their quality and usability. Specifically, they developed a filtering tool to assess the quality of the generated images and selected only the high-scoring images to be added to the MyCanvas dataset. The experimental results show that the likelihood of generating high-quality images is greater with fewer than four concepts. 

## Conclusion

### 1. Advantages of the Thesis
  1. The MyCanvas dataset is presented and studied and evaluated in detail.

  2. Improved data filtering methods are proposed in the dataset study to improve the data quality.

  3. Various modifications of training cues are studied and overall evaluation metrics are proposed which help to improve the quality of image generation.

  4. The research in the paper provides important insights into personalised text-to-image generation and automated data creation.

### 2. Innovative points
  1. The quality of image generation is improved by using some guidance information provided by LLM to adjust the object position.

  2. A semi-automated screen process is proposed to solve problems in some challenging scenarios.

  3. Some solutions are proposed for dataset quality problems, such as improved data screening methods.
     
### 3. Future Works
  1. Further exploration can be done to improve the quality of image generation using higher level language models such as GPT-4.

  2. More data enhancement techniques can be considered to increase the diversity of the dataset to improve the generalisation of the model.

  3. Further research could be done on how to apply this approach in different domains, such as video generation or virtual reality.  
