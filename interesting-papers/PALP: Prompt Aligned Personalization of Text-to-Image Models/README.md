# PALP: Prompt Aligned Personalization of Text-to-Image Models
[paper link](https://arxiv.org/pdf/2401.06105) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper presents a new approach, Prompt Aligned Personalization (PALP), for personalising text-to-image models.         |  Prompt Engineering        |

## Methodology

### 1. Abstract
Existing personalisation methods may sacrifice personalisation capabilities and adaptability to complex textual cues, thus failing to meet users' needs. PALP addresses this problem by maintaining the consistency of the personalisation model with the target cue using additional score distillation sampling terms. The method demonstrates flexibility in both multiple and single cue settings and can combine multiple themes or reference images for inspiration. The authors compare the method quantitatively and qualitatively with existing baselines and state-of-the-art techniques, and show that PALP achieves complex textual cues and personalisation needs better than other methods.

### 2. Method Description 
The image generation method proposed in this paper is called PALP (Personalised and Prompt-Aware Learning), whose main goal is to achieve the generation of images related to a new topic based on a given textual prompt, and to consider both personalisation and prompt matching goals in the generation process. Specifically, the method is implemented through the following steps:

  1. For a given topic S, a small number of representative samples are first fine-tuned for personalisation using a small number of representative samples.
  2. Along with personalisation, a fractional sampling technique is used to adjust the model predictions to focus more on the cues. Specifically, the clean cue yc is used for score sampling so that the noise prediction xhat0 is derived as a value closer to the cue yc.
  3. Use the Delta Denoising Score (DDS) variant to avoid oversaturation and pattern collapse problems. This can be achieved by calculating the direction of the residual between the personalised model prediction GβθLoRA (xhat0, yP) and the pre-trained model prediction Gαθ (xhat0, yc).

![image](https://github.com/user-attachments/assets/295f2f37-ac9e-4025-a43c-b023a1fac276)

### 3. Methodological improvements
  1. Emphasis on balancing the goals of personalisation and cue matching to ensure that the generated images accurately reflect the given subject matter while also meeting personalisation requirements.
  2. The use of advanced techniques such as fractional sampling and DDS variants improves the quality and diversity of the generated images.

### 4. Issues addressed 
  1. **The problem of balancing personalisation and cue matching in image generation:** traditional image generation methods tend to focus on only one of these goals, resulting in generated images that may not adequately reflect a given subject or satisfy personalisation needs.
  
  2. **Problems of oversaturation and pattern collapse:** the quality of the generated image is degraded due to focusing on only one of the targets, or problems such as repetition and homogeneity occur.

## Experiments
This paper focuses on a text-to-image personalisation generation method based on the Prompt-Adaptive Loss Personalization (PALP) framework, and evaluates and compares its performance through several comparative experiments.

Firstly, in ablation study, the authors constructed the final method by adding different components step-by-step from early stopping, SDS guidance, and replacing SDS for PALP guidance. The results show that using the same noise helps to improve PALP alignment, while multiplying the SCORE sampling equation by √α¯t/√1 - α¯t can further improve performance.

![image](https://github.com/user-attachments/assets/b119f049-a965-497d-a4a0-db21e9e5cb24)

Second, in a comparison with existing methods, the authors compare this paper's method with other multi-frame methods as well as single-frame methods such as TI+DB. The results show that this paper's method achieves the best text alignment while maintaining high image alignment, while TI+DB performs best on class prompt but worse on style prompt. In addition, the user survey also shows that this paper's method obtains higher user preference for prompt alignment and personalisation.

Finally, in terms of application, the authors applied this paper's method to single-frame and multi-concept personalisation scenarios and compared it with other methods. The results show that this paper's method not only achieves prompt and identity alignment, but also outperforms other methods in terms of the success rate of high-quality results.

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a new personalisation method that achieves better cue-to-topic consistency and is applicable to complex cues that include multiple topics. The method learns a given topic by fine-tuning a pre-trained model, while using score sampling to maintain consistency with the target cue.
  2. Experimental results show that the method achieves good results in terms of cue and topic consistency and can handle the case of one topic containing a single reference image. In addition, the method can be applied to multi-theme personalisation and provide immediate temporal personalisation for specific cues.

### 2. Innovative points
The authors use the knowledge of the pre-trained model to constrain the predictions of the personalisation model to maintain consistency with the pre-trained model by means of score distribution guidance. This approach not only allows for personalisation on small datasets, but also better captures the unique characteristics of new topics, thus generating richer scenarios that are more consistent with user expectations.

### 3. Future Works
Future research directions could consider how to extend the cue consistency constraints to more domains, such as audio or video generation. It is also possible to explore how personalisation can be further improved, e.g. by introducing more contextual information or using more complex model structures. 
