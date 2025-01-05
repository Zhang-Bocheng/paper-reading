# Knowledge-Guided Short-Context Action Anticipation in Human-Centric Videos
[paper link](https://arxiv.org/pdf/2309.05943) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper explores how short video clips can be used to predict long-term human actions and provide better suggestions and stimulate creativity in video editing workflows by improving the effectiveness of the attention mechanism at runtime.          |  Transformer        |

## Methodology

### 1. Abstract
The approach uses symbolic knowledge graphs to augment the attention mechanism of the Transformer network, and is able to achieve a performance improvement of 9% over the current best method on two benchmark datasets.

### 2. Method Description 
The Knowledge Guided Attention Mechanism (KGAM) proposed in this paper is an approach to enhance the attention mechanism in the transformer model. The method enables the identification of objects present in the scene, the establishment of links between their respective operability and the most likely actions to be performed, by including symbolic knowledge in the ontology graph (KG) and combining it with the transformer model. This information is used to modify the weights of visual features in attention.

### 3. Methodological improvements
  1. The attention mechanism in the TRANSFORMER model is enhanced so that it can use symbolic knowledge to adjust the weights of visual features.
  2. Knowledge-guided correction matrices Re and Rd are obtained for the encoder and decoder, respectively, by processing the context vectors.
  3. The standard multi-head attention mechanism was modified to obtain separate knowledge-guided attention for the encoder and decoder of the transformer.

### 4. Issues addressed 
  1. How to make the transformer model better understand the objects in the scene and their manipulability?
  2. How to adjust the weight of visual features in attention based on the presence or absence of objects in the scene?
  3. How can symbolic knowledge be used to improve the performance of the TRANSFORMER model?

## Experiments
This paper focuses on the evaluation of a neurosymbolic action prediction method and compares it to existing benchmarks. Specifically, the authors use two publicly available datasets (50Salads and Breakfast) to evaluate the effectiveness of the method and compute three metrics (MoC accuracy, minimum number of actions, and instantaneous single next prediction). 

In these metrics, the authors' method outperforms the current best long-time action prediction method on all datasets and significantly improves in most cases. In addition, the authors show through an example how their method identifies future action sequences better than existing methods. Overall, the authors' method performs well in the task of long-time action prediction. 

![image](https://github.com/user-attachments/assets/41d9515d-f57f-4aa3-a1c1-11d9c3edd864)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a new knowledge-guided action prediction method that combines symbolic domain knowledge and video comprehension capabilities with the use of knowledge graphs to capture the relationships between entities present in a scene and the functions and tools they may have.
  
  2. With this approach, future actions can be accurately predicted even under short field of view observations. Furthermore, the authors demonstrate that their method outperforms the current best method on two common benchmark test datasets for long-term action prediction.

### 2. Innovative points
  1. The methodological innovation of this paper is to combine symbolic domain knowledge with video comprehension capabilities to improve the accuracy of action prediction.
  2. They use knowledge graphs to capture the relationships between entities present in a scene and the functions and tools they may have, and apply them in an attention mechanism to refocus the model on which features it should focus on for action prediction. 

### 3. Future Works
  1. In the future, it could be further explored how to better utilise symbolic domain knowledge to enhance video understanding, especially when dealing with complex scenes.
  2. In addition, consideration could be given to how other types of knowledge (e.g., affective knowledge) could be combined with video comprehension to achieve a more comprehensive understanding.
  3. Finally, attempts could be made to extend this approach to other types of prediction tasks, such as speech recognition or natural language processing.
