# Question Aware Vision Transformer for Multimodal Reasoning
[paper link](https://arxiv.org/pdf/2402.05472) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper presents a visual language model called QA-ViT for multimodal reasoning.         |  Multimodal        |

## Methodology

### 1. Abstract
Traditional visual language models usually consist of a visual encoder, a large language model and a projection module, but these models ignore the impact of user queries on the image encoding process. Therefore, this method introduces a QA-ViT approach in which problem awareness is directly embedded into the visual encoder to dynamically focus on image aspects relevant to the question posed. Experimental results show that applying this approach to a variety of multimodal architectures significantly improves performance and demonstrates its potential to enhance visual and scene text understanding.

### 2. Method Description 
This paper proposes a generic, lightweight method for any visual attention model (VL) architecture, aiming at efficiently converting trained image encoders into problem-aware encoders. The method consists of two basic components: firstly, questions are fed into a ‘question encoding’ module, which processes and projects natural language cues to bridge the linguistic and visual feature domains; secondly, text-encoded features are integrated into a frozen visual model via a ‘question fusion’ module; and secondly, text-encoded features are integrated into a frozen visual model via a ‘question fusion’ module. Secondly, text-encoded features are integrated in the frozen visual model through the ‘Question Fusion’ module to produce text-aware visual features. Finally, these visual features are projected together with the instruction embedding vectors and fed to a pre-trained language model (LLM) to process and produce the output of the whole system.

![image](https://github.com/user-attachments/assets/c2445c88-af85-4bea-a008-198bc3601e2b)

### 3. Methodological improvements
The method focuses on improving the existing visual attention model by modifying only the visual encoder and keeping the rest of the architecture unchanged. At the same time, a parameter-efficient problem fusion mechanism is proposed, which allows for the integration of cross-modal information in the frozen ViT architecture without significantly changing the overall performance.

### 4. Issues addressed 
The main goal of this approach is to improve the multimodal comprehension of visual attention models so that they can better handle visual tasks containing problems. Specifically, it addresses the problem of how to enable a visual encoder to perceive problem information without changing the structure of the original model. By using this approach, the performance of visual attention models in multimodal scenarios can be effectively enhanced.

## Experiments
This paper focuses on the performance of the QA-ViT model in a visual question-answering task, and conducts several comparative experiments to verify its effectiveness and applicability.

Firstly, the authors conducted multiple sets of experiments on the QA-ViT model, including the use of pre-trained models of different sizes (e.g., ViT+T5 and LLAVA-1.5), different fusion positions (e.g., early, late, sparse, and all layers), and different question representations (e.g., embedding-only versus using a specialised language model). The results of these experiments show that QA-ViT is able to improve performance in a variety of situations and that choosing appropriate parameter settings can further improve performance.

![image](https://github.com/user-attachments/assets/552c5329-33f2-430c-a8f9-80eef7787231)

Second, the authors also compare QA-ViT with other state-of-the-art general-purpose methods (e.g., mPLUG-DocOWL, OpenFlamingo-9B, Shikra, etc.) and demonstrate that QA-ViT outperforms the other methods on the VizWiz dataset. In addition, the authors analysed the effect of different components of the training data on QA-ViT and found that adding natural image description data to the visual quiz data significantly improves performance.

![image](https://github.com/user-attachments/assets/ec45be00-80b6-4c96-94fc-bf5670e09bc1)

## Conclusion

### 1. Advantages of the Thesis
This paper proposes a new method, QA-ViT, which improves the performance of multimodal inference models by introducing textual information into the visual coder and achieving better alignment between visual features and queries. Experimental results show that the method achieves significant improvements on various benchmark tasks and is highly general and adaptable.
   
### 2. Innovative points
The core idea is to incorporate textual information directly into the visual encoder, enabling the visual features to better respond to user queries. This is achieved by adding a cross-modal attention mechanism to the visual encoder, enabling the visual encoder to focus on both image and text information. This approach not only preserves the original visual comprehension ability of the visual coder, but also enhances its ability to understand user queries. 

### 3. Future Works
  1. further explore the effects of different types of textual information on the visual encoder
  2. explore the design of more complex cross-modal attention mechanisms
  3. incorporate information from other modalities, such as audio or haptics, to enhance multimodal reasoning. 
