# Unsupervised Translation of Programming Languages
[paper link](https://arxiv.org/pdf/2006.03511.pdf) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper introduces a new approach - a neural network based unsupervised programming language translation system. While traditional compilers need to write rules manually, this approach automatically learns the mapping relationship between source and target code to achieve high-quality translations.         | Unsupervised  Learning       |

## Methodology

### 1. Abstract
The authors used source code from the open-source GitHub project for training and demonstrated the model's high accuracy when translating functions between programming languages such as C++, Java and Python. The model shows significant advantages over traditional rule-based commercial benchmarks. In addition, the approach does not require expertise in the source or target language and is easily generalisable to other programming languages. Finally, the authors provide the dataset containing 852 parallel functions used for testing and unit tests to ensure the correctness of the translations.

### 2. Method Description 
This paper proposes a programming language translation method based on the sequence-to-sequence (seq2seq) model, using the attention mechanism and the Transformer architecture. The method employs three main principles of unsupervised machine translation: **initialisation, language modelling and back translation**. Specifically, the approach begins with cross-programming language model pre-training, using a Cross Language Model (XLM) on a single source code dataset with a Masked Language Modelling (MLM) objective. Next, the model is trained by using the Denoising Auto-Encoding (DAE) objective to enable it to predict the original input based on noisy inputs and to make the encoder more robust to handle input noise. Finally, back-translation techniques are used to further improve the translation quality.

![image](https://github.com/user-attachments/assets/8530a5c5-c354-4848-b6c4-ffae9ecfbd58)

### 3. Methodological improvements
The method in this paper has the following improvements over traditional machine translation methods:

  1. Cross-programming language model pre-training is used, which enables the model to learn the similarities between different programming languages.
  
  2. A DAE objective was used, enabling the model to generate accurate translation results in noisy environments and improving the robustness of the encoder.
  
  3. Back-translation techniques were used to further improve the quality of the translations.

### 4. Issues addressed 
The method in this paper solves the problem of translation between programming languages by providing programmers with a convenient tool to convert code from one programming language to another. In addition, the method provides a new idea for research in the field of NLP on how to use unsupervised learning methods for cross-language text modelling.

## Experiments
This paper presents the performance of the TransCoder model on a source code translation task and compares it with two other existing frameworks. C++, Java and Python files from the GitHub public dataset were used in the experiments to train the model by extracting functions and using them as training data. The authors also designed a new evaluation metric, computational accuracy, to measure whether the generated code can output the results correctly. 

![image](https://github.com/user-attachments/assets/e51137be-4dcf-437d-9d5c-c3102aaccac7)

Experimental results show that computational accuracy more accurately reflects the performance of the model than the traditional BLEU score. In addition, using beam search decoding can significantly improve computational accuracy, but it should be noted that decoding considering only the highest probability may lead to performance degradation. Finally, TransCoder performs well in terms of computational accuracy compared to the two existing frameworks, especially when dealing with standard library functions. 

![image](https://github.com/user-attachments/assets/a527a469-b023-45d2-b988-93ca6efc6eb5)

## Conclusion

### 1. Advantages of the Thesis
  1. The study proposes a new neural machine translation-based approach for automatic conversion between programming languages.
  
  2. The researchers used a large-scale monolingual source code dataset from GitHub to train the model and implemented high-quality function translation between three popular programming languages (C++, Java and Python).
  
  3. In contrast to traditional rule-based approaches, this approach does not require any expert knowledge or manually written rules, and thus can be easily extended to other programming languages.
  
  4. The study also provides validation and test datasets as well as unit tests to evaluate the correctness of the generated translations.

### 2. Innovative points
  1. The study uses a large-scale dataset of monolingual source code to train the model, which enables automatic translation between programming languages without any parallel data.
  
  2. The study presents a simple yet effective neural machine translation model that can perform highly accurate function translation between three different programming languages.
  
  3. The study demonstrates the effectiveness of this unsupervised learning approach and compares it with commercial systems, showing that it outperforms traditional rule-based approaches.

### 3. Future Works
  1. This research provides a promising approach for future programming language conversions that can significantly reduce programmer workload and cost.
  
  2. The results of this study may help to facilitate collaboration across teams and open source projects, thereby increasing the efficiency of software development.
 
  3. The study also needs to further explore how to deal with issues such as more complex program structures and library calls to achieve a higher level of programming language conversion. 
