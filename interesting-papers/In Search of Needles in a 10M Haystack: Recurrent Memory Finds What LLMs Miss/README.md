# In Search of Needles in a 10M Haystack: Recurrent Memory Finds What LLMs Miss
[paper link](https://arxiv.org/pdf/2402.10790) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores the challenges faced when using generative converter models to process long documents and presents a new benchmark test called BABILong to evaluate the capabilities of different approaches.          |  Neural Network        |

## Methodology
The authors found that existing methods are only suitable for sequences up to 10^4 elements in length, whereas by fine-tuning GPT-2 and adding a cyclic memory enhancement, it was made capable of handling tasks up to 11 x 10^6 elements in length. This result marks a significant advance in neural network modelling for processing long sequences.

![image](https://github.com/user-attachments/assets/36e19688-4120-4c26-8b3b-5156d586b726)

## Conclusion

### 1. Advantages of the Thesis
  1. The BABILong benchmark test is proposed to evaluate the ability of NLP models in processing documents of arbitrary length.
  2. Real-world information acquisition tasks are modelled by mixing background text with problem sentences, and datasets such as PG19 are used as a source of background text.
  3. Experiments are conducted on GPT-4 and RAG to demonstrate their limitations in processing long sequences, and the Recursive Memory Augmentation Model (RMT) and its extended version (RMT-R) are proposed as a solution.
  4. The experimental results show that RMT and RMT-R perform well in handling sequences up to millions of markers long and have good generalisation ability.
 
### 2. Innovative points
  1. A new benchmark test (BABILong) is proposed to evaluate the ability of NLP models in processing documents of arbitrary length.
  2. Using the recursive memory mechanism, RMT and RMT-R models are designed to handle long sequences efficiently and improve performance.
  3. Different NLP models and different background text sources (e.g., PG19) were used in the experiments to increase the diversity of the experiments.
 
### 3. Future Works
  1. Further exploration can be done to optimise the RMT and RMT-R models to make them more applicable to different types of long text processing tasks.
  2. Attempts can be made to combine recursive memory mechanisms with other techniques, such as attention mechanisms or reinforcement learning, to achieve better performance gains.
  3. Consideration can be given to applying recursive memory mechanisms to other domains, such as natural language generation, machine translation, etc.  
