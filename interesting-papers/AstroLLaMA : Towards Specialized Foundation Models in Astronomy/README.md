# AstroLLaMA: Towards Specialized Foundation Models in Astronomy
[paper link](https://arxiv.org/pdf/2309.06126) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |  This paper describes a model called AstroLLaMA, obtained by fine-tuning LLaMA-2, for processing natural language tasks in astronomy.         |  NLP        |

## Methodology

### 1. Abstract
The model was trained using over 300,000 astronomical abstracts from the arXiv and optimised for traditional causal language modelling. The results show that AstroLLaMA reduces confusion by 30% compared to LLaMA-2 and generates more insightful and scientifically relevant text completion and embedding extractions. Furthermore, despite a significantly smaller number of parameters, AstroLLaMA still performs better than the existing base model. The model can be used as a robust, domain-specific model with extensive fine-tuning potential. Its public release is intended to facilitate astronomy-focused research, including aspects of automated literature abstraction and dialogue agent development.

### 2. Method Description 
This paper describes a method called AstroLLaMA for performing text categorisation tasks in the field of astronomy. The method uses a dataset from the arXiv repository and focuses it on articles in the category of astrophysics. A corpus containing about 95 million words is formed by extracting the abstracts of these articles. For the model architecture, the authors chose LLaMA-2 developed by Meta as the base model and fine-tuned it for the task of text categorisation in the field of astrophysics.

### 3. Methodological improvements
Compared to traditional rule-based or hand-designed feature approaches, AstroLLaMA takes advantage of pre-trained models that automatically learn patterns and regularities in the data, thus improving the accuracy and efficiency of text classification. In addition, by using large-scale datasets for pre-training and fine-tuning, AstroLLaMA has better generalisation capabilities and adaptability.

### 4. Issues addressed 
AstroLLaMA primarily addresses the challenges faced when performing text categorisation in the field of astronomy, including the lack of sufficiently large datasets and the need to deal with complex domain-specific terminology and knowledge. By using large-scale datasets for pre-training and fine-tuning, as well as choosing model architectures that are appropriate for the field of astronomy, AstroLLaMA is able to effectively address these issues and improve the accuracy of text classification.

## Experiments
This article focuses on the performance of three models in completing astronomy-related abstract tasks, and compares and analyses them. Specifically, the article uses three different models, GPT-4, LLama-2 and AstroLLaMA, and evaluates their text generation capabilities and embedding space quality.

Firstly, in terms of text generation capability, the article applies the three models to complete an astronomy-related abstracting task and gives an example. The results show that LLama-2 performs relatively poorly, tending to go off-topic and produce irrelevant content. In contrast, GPT-4 was able to generate more coherent text, but its responses were too generic to capture domain-specific knowledge in astronomy. 

However, AstroLLaMA demonstrates excellent contextual awareness, showing a deep understanding of astronomical concepts and the ability to complete texts accurately. For example, when processing information related to nebulae, AstroLLaMA was able to recognise the presence of the SE Stream and explore metal abundance differences to determine their origin.

Secondly, in terms of embedding spatial quality, the article assesses the performance of the model by calculating the similarity between abstractions. The results show that the embedding space of GPT-3 is too generic, resulting in a lack of differentiation as the similarity is concentrated between relatively high values (0.7-0.9). The embedding space of AstroLLaMA, on the other hand, exhibits higher variance and is more representative of the particular semantic variations in the field of astronomy, thus potentially facilitating a finer representation of astronomical content as well as better document retrieval and semantic analyses. 

## Conclusion

### 1. Advantages of the Thesis
  1. The model uses abstracts from over 300,000 astronomical research papers as training data and fine-tunes on these data to improve its performance in the astronomical domain.
  
  2. Compared to its base model, LLaMA-2, and the current state-of-the-art general-purpose language model, GPT-4, AstroLLaMA has significant advantages in generating high-quality abstracts.
  
  3. The model's ability to better understand relevant information contributes to its performance in tasks such as Q&A, scientific summarisation and hypothesis generation.
 
### 2. Innovative points
  1. By using abstracts from over 300,000 astronomy research papers as training data, the model is able to perform well in the field of astronomy.
  
  2. The model has a higher number of parameters than some of the existing small-scale models and is therefore better able to handle complex astronomical problems.
The model also employs a multimodal learning approach, which allows it to process both text and other types of data, such as images or audio.
 
### 3. Future Works
  1. The authors plan to extend AstroLLaMA's training data to include the full LaTeX source code to further improve its performance.
  
  2. They will also endeavour to balance the model's ‘conviction’ (respect for scientific evidence and accuracy) and ‘creativity’ (ability to formulate interesting hypotheses) to better meet the needs of the astronomical field.
  
  3. The model has been publicly released and is available for researchers to use, as well as providing a model for other domain-specific languages.
