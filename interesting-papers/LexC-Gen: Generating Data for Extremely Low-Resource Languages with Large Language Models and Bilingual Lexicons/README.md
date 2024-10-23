# LexC-Gen: Generating Data for Extremely Low-Resource Languages with Large Language Models and Bilingual Lexicons
[paper link](https://arxiv.org/pdf/2402.14086) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a data generation method called LexC-Gen, which aims to solve the problem of data scarcity in low-resource languages.          | Large Language Model (LLM)         |

## Methodology

### 1. Abstract
The method utilises a bilingual lexicon and a large-scale language model for task data generation, and translates the generated data into low-resource languages through lexical translation. Experimental results show that LexC-Gen-generated data performs competitively compared to expert-translated golden data in sentiment analysis and topic classification tasks, and improves by an average of 5.6 and 8.9 points over existing lexicon-based vocabulary translation methods. Through the ablation study, the authors demonstrated that the bilingual lexicon condition is a key component of LexC-Gen. In addition, LexC-Gen can serve as a potential solution for bridging the performance gap between open-source multilingual models (e.g., BLOOMZ) and commercial models (e.g., GPT-4).

### 2. Method Description 
This paper proposes LexC-Gen, a data generation method for low-resource language classification tasks. The method requires three inputs: labelled task data TH, a bilingual lexicon DHL for high-resource languages H to low-resource languages L, and a pre-trained model LLM supporting high-resource languages H. The key idea of the method is to use the LLM to generate task data TL using high-resource language vocabulary from the bilingual lexicon to improve the lexical overlap between the task data and the bilingual lexicon, and thus to more efficiently translation into the low-resource language L.

Specifically, the method consists of the following four steps:

  1. Randomly sample words wH and category labels c in the high-resource language H.

  2. Train the LLM using CTG to generate task data TH|D for the specified categories of the high-resource language based on the bilingual lexicon.

  3. The generated task data is filtered for input-label consistency to remove possible tagging errors.

  4. Finally, the words in the high-resource language task data are replaced with the corresponding low-resource language translations to obtain the final low-resource language task data TL.

![image](https://github.com/user-attachments/assets/8203de1a-df39-450c-b745-64dcfc713023)
  
### 3. Methodological improvements
The method improves the quality of the generated task data by introducing CTG to train the LLM, which enables the LLM to better generate high-resource language task data of specified categories based on the bilingual dictionary. In addition, the method employs input-label consistency filtering, which further reduces possible labelling errors and improves the accuracy of the generated task data.

### 4. Issues addressed 
The method solves the problem of lack of labelled data for classification tasks on low-resource languages. By utilising task data from high-resource languages and bilingual dictionaries, the method automatically generates task data with high lexical overlap for low-resource languages, thus allowing effective classification tasks to be performed on low-resource languages.

## Experiments
This paper describes LexC-Gen, a method for generating low-resource linguistic data using a language model, and evaluates its performance by comparing it to several benchmark datasets. Specifically, the authors conducted the following comparison experiments:

  1. **Comparing the size and performance of datasets for task classification and topic classification:** the authors used two datasets (NusaX and SIB-200) to test the performance of LexC-Gen on different datasets. The results show that the data generated using LexC-Gen significantly improves the accuracy of the model, especially when the amount of data is small.
     
![image](https://github.com/user-attachments/assets/53244e2b-758f-4dd3-b2d5-a6e719d66f63)

  2. **Comparing the quality of data generated using different methods:** the authors compare LexC-Gen with several other methods for generating data, including zero hints, several hints, and cross-language zero hints. The results show that the data generated using LexC-Gen is of higher quality and more accurate.

![image](https://github.com/user-attachments/assets/30370ddf-3d6f-4712-8a04-d07f876adb63)

  3. **Comparing the effect of using different types of dictionaries:** the authors used two different dictionaries (Gatitos and Panlex) to translate the generated data. The results show that using the Gatitos dictionary gives better results.

![image](https://github.com/user-attachments/assets/2be3b2a0-41f7-4312-bce3-fee79797f9b0)

## Conclusion

### 1. Advantages of the Thesis
  1. A method called LexC-Gen is proposed for generating task data for low-resource languages in the presence of scarce resources.

  2. The method uses existing lexical resources with additional training to learn how to incorporate lexical information into the generated data.

  3. The study shows that this approach can significantly improve performance on tasks such as sentiment analysis and topic classification, and that cost savings can be achieved through replication.

  4. The study also explores possible future research directions such as handling other types of natural language understanding tasks and extending to non-English languages.

### 2. Innovative points
  1. The LexC-Gen method introduces an additional step of training the language model using CTGs so that it can generate text that both maximises lexical usage and matches tags.

  2. The method uses existing lexical resources with additional training to learn how to incorporate lexical information into the generated data.

  3. The method can generate high-quality task data without the need for large amounts of labelled data.

### 3. Future Works
  1. The problem of word sense ambiguity and grammatical mismatch can be further explored to improve the quality of the generated data.

  2. Consideration can be given to applying the method to other types of natural language understanding tasks and extending it to non-English languages.

  3. Further research can be done to investigate how BLI can be utilised to extend lexicon coverage so that more words can be translated into low-resource languages. 
