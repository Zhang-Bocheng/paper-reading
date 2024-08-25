# Typical Decoding for Natural Language Generation
[paper link](https://arxiv.org/pdf/2202.00666v3) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2022 | This thesis explores the problem of the representation of probabilistic models in natural language generation and proposes a new sampling method, typical sampling.         | Natural Language Generation          |

## Methodology

### 1. Abstract
While traditional sampling of high probability regions leads to problems such as text monotony and repetition, typical sampling selects words with information close to the conditional entropy for sampling, which is more in line with the way humans use language. Experimental results show that typical sampling is competitive in terms of quality and reduced repetition compared to kernel and pre-k sampling.

### 2. Method Description 
This thesis proposes an information theory-based approach to natural language generation, aiming at generating languages that are more compatible with human habits. The approach begins by considering a probabilistic model as a communication channel and establishing a relationship between its distribution and actual natural language strings. Then, by estimating the information content of each word in the model, the assumption is made that any given word should have an information content close to the expected information content. Finally, this control of information content is achieved by limiting the sampling space to achieve better text quality.

![image](https://github.com/user-attachments/assets/43ec897c-6cd4-4ba4-8e9a-b3c2c5a2c4df)

### 3. Methodological improvements
The method provides a new perspective on the natural language generation problem by introducing the concept of information theory. It not only explains why high probability texts tend to be boring or generic, but also provides guidance on how to design better decoding strategies. Specifically, the approach uses a new decoding strategy called typical sampling, which ensures that the generated text is more human-friendly by limiting the sampling space.

### 4. Issues addressed 
The method addresses some common problems in natural language generation, such as low quality and repetition. By considering the probabilistic model as a communication channel and controlling its information content, the method generates texts that are more compatible with human habits. In addition, by introducing a typical sampling strategy, the method can improve decoding efficiency and text quality. Therefore, the method has important application value in the field of natural language generation.

## Experiments
This paper presents the results of experiments on five natural language generation tasks, including two tasks, abstract summarisation and story generation. In the experiments, the authors used the Hugging Face framework and employed different random sampling strategies to generate text, including nucleus sampling, top-k sampling, temperature sampling, beam search and Mirostat methods. In addition, the authors tuned the model with hyperparameters and used automatic quality metrics and human evaluation metrics to assess the effectiveness of the different sampling strategies.

Specifically, in the abstract summarisation task, the authors used the BART model and fine-tuned it to the CNN/DAILYMAIL dataset. In this task, the authors used perplexity as an automatic quality metric and computed MAUVE scores to measure the similarity between the generated text and the reference text. Also, the authors invited five annotators to rate 200 examples under each sampling strategy on criteria including fluency and relevance. The final results show that TYPICAL Sampling performs the best, and its generated texts have high quality and diversity.

![image](https://github.com/user-attachments/assets/e94eaedb-1b05-4343-92af-1701b3753a2a)

In the story generation task, the authors used the GPT-2 model and fine-tuned it to the WRITINGPROMPTS dataset. In this task, the authors also used perplexity and MAUVE scores as automated quality metrics and invited five annotators to rate 200 examples under each sampling strategy on the criteria of fluency, coherence, and interestingness. The final results show that TYPICAL SAMPLING remains the best choice, generating stories that are more coherent and interesting than the other sampling strategies.  

![image](https://github.com/user-attachments/assets/daff9f9f-1475-4a81-9784-177a0196a5e0)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper presents an information theory-based approach to evaluate and improve decoding strategies for probabilistic language models.
  
  2. The method provides a new criterion for evaluating and generating sample texts that are closer to human texts by taking into account the efficiency criterion used by humans in natural language communication.
  
  3. Experimental results show that the use of typical sampling strategies reduces repetition and improves text quality comparable to human evaluation.
Methodological Innovations

Future Outlook.
 
### 2. Innovative points
  1. This study proposes a new criterion based on information theory for evaluating and generating sample texts that are closer to human texts.
  
  2. By applying information theory to the study of natural language communication, this research provides new ideas for solving the problem of decoding strategies for probabilistic language models.
     
### 3. Future Works
  1. This study provides a basis for further exploration of information theory applications in natural language communication.
  
  2. The method can be further extended by applying it to other natural language processing tasks and comparing it with other decoding strategies.
  
  3. Consideration can be given to how the method can be applied to practical application scenarios such as real-time speech recognition. 
