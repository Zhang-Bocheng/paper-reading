# Do PLMs Know and Understand Ontological Knowledge?
[paper link](https://arxiv.org/pdf/2309.05936) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This thesis explores whether pre-trained language models (PLMs) are aware of and capture ontological knowledge.           | LLMs         |

## Methodology

### 1. Abstract
Existing PLM probing research has focused on factual knowledge and lacks systematic probing of ontological knowledge. The authors determine whether PLMs truly understand ontological knowledge by probing whether they are able to memorise information such as entity types, hierarchical relationships between classes and attributes, and domain and scope constraints, as well as whether they are able to reason logically according to ontological entailment rules. The results show that PLMs can memorise certain ontological knowledge and reason using the implicit knowledge, but both the memorisation and reasoning performance are imperfect, suggesting that their knowledge and understanding are not complete.

### 2. Method Description 
The paper presents two probe learning methods based on pre-trained models: **memory probes and inference probes**. For memory probes, they used manual templates and soft templates to design probes and evaluated the memory capability of the models by calculating the probability of candidate words in the masked input. While for inference probes, they used manually designed connectives and pseudo-words to construct the probes and assessed the inference ability of the model by classifying whether the premises were memorised by the model or not.

![image](https://github.com/user-attachments/assets/8d84f298-e318-483f-a7a9-07c9743cda6b)

### 3. Methodological improvements
Compared to the traditional method of manually designing probes, this method is more flexible and can automatically adjust the probe parameters to suit different task requirements. It is also better able to avoid the model remembering specific words by using techniques such as pseudo-words.

### 4. Issues addressed 
The method can help us better understand the learning process of pre-trained models, which can guide us on how to utilise these models in real-world applications. In addition, the method can also provide lessons for other fields, such as natural language generation and machine translation.

## Experiments
This paper focuses on the authors' comparative experiments on the performance of pre-trained language models (PLMs) in memory and reasoning tasks and analyses the results to arrive at a set of findings. The validity of different cues is also analysed.

Firstly, in the memory task, the authors used a frequency-based model as a baseline model to predict the labels that would appear in the training set and randomly selected candidate lists that were not prime labels. The results show that PLMs are better at remembering than the baseline model, outperforming the baseline model in all subtasks and under all metrics, except for the DM task, where the best performance is achieved. In addition, the BERT model also performs much better than the benchmark model under all subtasks and all metrics, with an average improvement of 43% to 198%. However, despite the significant improvement over the benchmark model, the results are not perfect and PLMs can only partially remember certain knowledge.

![image](https://github.com/user-attachments/assets/d737e4c2-6bb6-41d7-b1ed-203d04bf4ef9)

Second, in the inference task, the authors fixed the use of multiple masks and mean pooling methods and showed the performance of BERT-base-cased and RoBERTa-base in the TP and DM tasks. The results show that when P1 is given explicitly, the model is able to significantly improve the ranking of correct answers. When P1 is given implicitly, the models have higher MRR metrics, which suggests that PLMs can utilise the implicit ontology knowledge and select the correct inference rules for reasoning. However, no combination of antecedents resulted in near-perfect inference performance, implying that PLMs still have a limited understanding of ontological knowledge.

![image](https://github.com/user-attachments/assets/3c81e8f0-ce7c-4b51-be4e-fd287572d49e)

Finally, the authors also explored the impact of hint templates on performance. The results show that the use of soft cue templates improves the performance of memory tasks, especially in TP, SCO and SPO tasks. However, only a few models showed better results on the DM and RG tasks, possibly because the semantics of manual templates and domain range constraints are more complex and difficult to capture with the three soft tokens. In the inference task, the authors found that it was trainable conjunctions rather than soft cue templates describing ontological relations that improved performance.  

![image](https://github.com/user-attachments/assets/40ead862-132c-402c-ba97-23941d74e753)

## Conclusion

### 1. Advantages of the Thesis
  1. This study systematically investigates whether pre-trained language models can encode ontological knowledge and understand its semantics.
  
  2. The experimental results show that pre-trained language models can store a certain amount of ontological knowledge and make inferences through inference rules, suggesting that they have some degree of ontological awareness and comprehension.
  
  3. The study proposes that ChatGPT performs better in the experiments, which opens up possibilities for further development in the future.

### 2. Innovative points
  1. The study constructed a dataset for assessing the memory capacity and reasoning ability of pre-trained language models, including five subtasks: type, superclass, superproperty, domain constraints, and range constraints.
  
  2. For the reasoning task, the study proposed six inference rules based on the RDFS specification and designed corresponding schemas to describe the reasoning process.
  
  3. The study also explored the relationship between memory and reasoning ability of pre-trained language models and proposed some improvements.
 
### 3. Future Works
  1. The results of this study suggest that pre-trained language models still have limitations in terms of ontological knowledge and need to further improve their knowledge and comprehension.
  
  2. In future research, more data and more complex inference rules can be considered to test the ability of pre-trained language models.
  
  3. Also, ways to integrate ontological knowledge with natural language processing tasks could be explored to better support practical applications.  
