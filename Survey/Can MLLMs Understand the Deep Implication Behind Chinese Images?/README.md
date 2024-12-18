# Can MLLMs Understand the Deep Implication Behind Chinese Images?
[paper link](https://arxiv.org/pdf/2410.13854) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | The aim of this paper is to evaluate the high-level perception and comprehension of Chinese images by a large-scale multimodal language model (MLLM), and to fill the gaps in existing work.          |  large-scale multimodal language model (MLLM)        |

## Methodology

### 1. Abstract
The authors propose the Chinese Image Implicit Understanding Benchmark (CII-Bench), which consists of manually-vetted real images and corresponding answers from the Chinese Internet, as well as images such as famous traditional paintings representing traditional Chinese culture. Through extensive experiments on multiple MLLMs, the authors found that there is a significant gap between the performance of MLLMs and humans on the CII-Bench, with a maximum accuracy of 64.4% compared to the average human accuracy of 78.2%. 

In addition, MLLM performs worse when processing traditional Chinese cultural images, suggesting a limited understanding of high-level semantics and a lack of a deep Chinese cultural knowledge base. Finally, most models show enhanced accuracy after incorporating emotional cues into the prompts. In conclusion, CII-Bench is expected to help MLLM better understand Chinese semantics and images with Chinese characteristics, and advance the development of expert artificial intelligence (AGI).

### 2. Method Description 
This paper presents CII-Bench, a new benchmark test set for evaluating the ability of multimodal learning models in comprehending Chinese culture and image information. The test set includes multiple types of visual content, such as traditional artworks, comics, posters, and Internet terrier images, and is accompanied by several multiple-choice questions to examine the model's ability to understand the deeper meanings in the images. 

During the data collection process, copyright and licensing regulations were followed, and high-quality data were filtered out through image similarity algorithms, optical character recognition techniques, and manual review. Meanwhile, in order to ensure the quality of annotation, multiple annotation and cross-validation were adopted, and the annotation content was refined and supplemented according to specific standards to ensure the consistency and comparability of the data.

![image](https://github.com/user-attachments/assets/c431fc0c-225a-4247-bb31-57ba90b4a175)

### 3.  Methodological improvements
Compared with the existing image understanding benchmark test set, CII-Bench focuses more on examining the model's ability to understand Chinese cultural and social contexts, and also provides more detailed and rich data annotation methods, making the test results more credible and reliable.

### 4. Issues addressed 
Current multimodal learning models have made great progress, but there are still some challenges in understanding and interpreting the deeper meanings in images. Therefore, designing a benchmark test set that specifically addresses this issue can better assess the capability of the models and advance related research.

## Experiments
This paper presents the authors' experimental study of the performance of multimodal large models for CII-Bench. The study includes natural challenges, gaps between human and multimodal large models, performance on different domain and sentiment dimensions, and problem-specific analyses.

**In terms of natural challenges**, the authors found that the multimodal large model performed poorly in handling tasks on the CII-Bench, with an accuracy of only 54.1%, which suggests that this benchmarking is challenging. In addition, the model also had difficulties in understanding traditional Chinese culture, showing low accuracy.

**In terms of the gap between humans and the multimodal large model**, the authors found that human participants achieved an average accuracy of 78.2% on the CII-Bench, while the best multimodal large model had an accuracy of only 60.9%. This suggests that although multimodal large-scale models have made great strides, they are still unable to fully understand the meaning of images.

![image](https://github.com/user-attachments/assets/3941f7e0-3e6f-402f-bd57-d6b5360daa54)

**In terms of performance across different domains and emotional dimensions**, the authors found that the models performed better in the environmental and political domains and worse in the life and social domains. In addition, the model performed better with images with negative emotions and worse with images with positive emotions.

![image](https://github.com/user-attachments/assets/fa2c6b9b-c123-46b2-a5ec-623b21d327c7)

Finally, **in terms of problem-specific analyses**, the authors conducted an in-depth analysis by understanding traditional Chinese paintings and developed an automated evaluation criterion based on a language model to assess the performance of the multimodal large-scale model in this area. The results show that although the models are able to observe surface information, there is still a large gap in deeply understanding complex cultural elements.

![image](https://github.com/user-attachments/assets/641cf135-bef7-4f13-9f0d-5e6c913ba1cc)

## Conclusion

### 1. Advantages of the Thesis
  1. A new rubric, CII-Bench, is proposed to assess the model's ability in understanding the deeper meaning in Chinese images.
  2. Diverse image types and question types are designed to comprehensively test the model's comprehension and reasoning abilities.
  3. The results of the comparative experiments show that there are still large gaps in the current large-scale language models to fully understand the cultural connotations of China.
  4. The performance of the model can be improved by introducing means such as emotional cues, but at the same time, it also exposes the model's shortcomings in emotional comprehension and interpretation of complex cultural elements.
 
### 2. Innovative points
   1. The CII-Bench evaluation criteria were designed for the deeper meanings embedded in Chinese images, making the evaluation more in line with practical application scenarios.
  2. Multiple types of images were used in the problem design, and the problem was divided into multiple subtasks to examine the ability of the model more comprehensively.
  3. Means such as emotional cues were introduced to assist the model performance, providing new ideas for subsequent research.

### 3. Future Works
  1. It is possible to further explore how other data sources or technical means can be used to improve model performance, such as increasing the amount of training data, using transfer learning, etc.
  2. Attempts can be made to extend CII-Bench to other languages or cultural domains in order to better compare the differences between different cultures.
  3. Deep learning techniques and traditional machine learning methods can be combined to build more integrated models for better performance improvement. 
