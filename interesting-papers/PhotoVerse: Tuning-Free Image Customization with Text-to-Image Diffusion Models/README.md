# PhotoVerse: Tuning-Free Image Customization with Text-to-Image Diffusion Models
[paper link](https://arxiv.org/pdf/2309.05793) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents a new approach called PhotoVerse for personalised text-to-image generation.         | Diffusion Models         |

## Methodology

### 1. Abstract
The approach provides effective control over the image generation process by introducing a two-branch conditional mechanism in both the text and image domains, and also introduces facial identity loss as a new component that enhances the preservation of identities. In addition, PhotoVerse eliminates the need for test-time adjustment, requiring only a single facial photograph of the target identity, significantly reducing the resource costs associated with image generation. After a single training phase, the method generates high-quality images in seconds and can produce diverse images for a variety of scenes and styles.

### 2. Method Description 
The paper presents a method called Dual-branch Concept Extraction for personalised concept extraction in image synthesis tasks. The method consists of two branches: **textual conditioning and visual conditioning.** In the preprocessing stage, a face detection algorithm is used to identify faces in the input image and a mask is applied to remove non-facial elements to ensure the effectiveness of subsequent identity feature extraction. For the textual condition, the features of the reference image are extracted using the CLIP image encoder and these features are converted into multi-word embeddings to form a pseudo-word set S* using a multi-adapter architecture. At the same time, the features extracted using the image encoder are mapped onto the image adapters to capture identity-related visual cues. Finally, information from the two branches is merged using a stochastic fusion strategy and regularisation terms are introduced to retain important information and eliminate redundant information.

![image](https://github.com/user-attachments/assets/cfdbe130-9639-471e-8884-52af1b50ed44)

### 3. Methodological improvements
This method improves the traditional diffusion model by increasing the expressive power of the model through the addition of new concept-injecting branches. Specifically, it adjusts only the weights in the cross-attention module instead of the entire U-Net network, which allows for more efficient training of the model and reduces the risk of overfitting. In addition, the method employs a stochastic fusion strategy and regularisation terms to further optimise model performance.

### 4. Issues addressed 
The method mainly addresses the problem of implementing personalised concept extraction in image synthesis tasks. While traditional diffusion models may not provide enough details to construct novel concepts, the method enhances the model's expressiveness by injecting new concepts and fine-tuning the weights in the cross-attention module. In addition, the method can quickly personalise the image generation based on the text provided by the user, thus meeting the user's individual needs.

## Experiments
This paper focuses on the performance of the PhotoVerse method in an image generation task and compares it with other related methods. Specifically, the authors fine-tuned the model using three public datasets and evaluated it on a self-collected dataset. In the evaluation phase, they measured the model's performance capabilities by generating five images similar to the input photos. In addition, the authors explored some parameter tuning and techniques to meet different application requirements.

In terms of **quantitative results**, the authors used the facial recognition model Arcface to calculate the similarity of identity information in the generated images. The results show that the PhotoVerse method performs consistently and robustly across the entire racial group, with a mean value of 0.696. Identity similarity for certain races (e.g., brown and white) exceeds 0.7, with white ethnicity having the highest identity similarity. Despite some minor variations, overall the method was highly effective.

In terms of **qualitative results**, the authors compared the PhotoVerse method with four other personalisation techniques, including DreamBooth, Textual Inversion, E4T and ProFusion.They found that while these methods require fine-tuning over test time, they all require a significant amount of time and storage space for personalisation. In contrast, the PhotoVerse method can synthesise five images in as little as 25 seconds, which is extremely efficient and user-friendly. In addition, the PhotoVerse method does a good job of preserving key features of the reference image, such as facial features, expression, hair colour and hairstyle. It also produces clearer and more natural images, avoiding problems such as artefacts.

![image](https://github.com/user-attachments/assets/32b51a6a-cba5-4db6-979e-ddf1410699e1)

Finally, the authors also conducted a series of ablation studies to explore the effects of visual conditional branching, regularisation, and facial ID loss on model performance. The results show that visual conditional branching is crucial for maintaining identity consistency, while regularisation promotes sparse representations, thus improving the generalisation ability of the model. In addition, facial ID loss also plays an important role in maintaining identity information. 

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents a novel approach that combines a two-branch conditional mechanism and facial identity loss to improve the quality of personalised text-to-image synthesis.
  2. Compared to existing methods, the method does not require adjustments at test time and requires only a single facial photograph to complete the synthesis process, significantly reducing resource costs.
  3. In cases where only a single conceptual image is used, the method generates high-quality images quickly, typically in about 5 seconds.
  4. The method not only preserves identity information, but also has good editing capabilities, supporting diverse stylisation, image editing and new scene generation.
  
### 2. Innovative points
  1. The paper proposes a two-branch conditional injection method based on the Stable Diffusion model, which achieves better conditional injection in both text and image domains by combining improved identity text embedding with spatial conceptual cues.
  2. The method introduces a facial identity loss component to enhance identity retention in training.
  3. The method balances high identity similarity with strong editing capabilities, effectively improving the quality of synthesis. 

### 3. Future Works
  1. The method provides an effective approach for personalised text-to-image synthesis, but there are still challenges that need to be addressed, such as how to further improve the generation speed and handle more complex scenes.
  2. Possible research directions include extending the input by utilising more data sources (e.g. audio, video, etc.) and exploring new conditional injection techniques for higher levels of control and interaction.
