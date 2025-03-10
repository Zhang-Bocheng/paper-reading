# Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text
[paper link](https://arxiv.org/pdf/2401.12070) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper introduces a method called ‘Binoculars’ for detecting machine-generated text.          |   Large Language Models       |

## Methodology

### 1. Abstract
While traditional detection methods require training data and model-specific modifications, Binoculars uses only two pre-trained language models to perform simple computations to achieve highly accurate detection results without requiring any training data. The method was thoroughly evaluated across a wide range of document types and contexts, and was able to accurately detect samples generated by modern language models such as ChatGPT in more than 90% of cases, while keeping false positives below 0.01%.

### 2. Method Description 
In this paper, we propose a detection method called ‘Binoculars’ for recognising machine-generated text. The method solves the problem that traditional perplexity-based detection methods cannot accurately determine whether a text is human-written or not when handwritten prompts are present.The Binoculars method measures the degree of surprise of a text by comparing the expected perplexity of the observed text with that of the model on the same text, and normalises it to a normalised score, which allows for an effective distinction between machine-generated and human-written texts.

Specifically, the Binoculars method uses two similar language models, M1 and M2, and calculates their perplexity for a given text. These two perplexities are then divided to obtain a normalised score, called the Binoculars score. This score reflects the degree of surprise of the text with respect to the two models, and if the score is below a certain threshold, the text is considered to have been written by a human, otherwise it is considered to have been generated by a machine.

![image](https://github.com/user-attachments/assets/1dc9958e-055c-4f1a-a856-b142a32d2278)

### 3. Methodological improvements
  1. Traditional perplexity-based detection methods only consider the perplexity of a single model on a given text and do not take into account other possible factors.The Binoculars method removes this limitation by comparing the perplexity of two similar language models and is better adapted to different cues and text types.

  2. In addition, the Binoculars method provides a standardised evaluation metric that allows different researchers to compare their results more easily. This is important for promoting further development in the field.

### 4. Issues addressed 
Traditional perplexity-based detection methods do not work well with texts with handwritten prompts that affect the perplexity of the text.The Binoculars method removes this effect by introducing an alternative language model and provides a standardised evaluation metric that allows researchers to more accurately assess the effectiveness of the algorithms they use. This helps to improve the quality of machine-generated text and reduces the likelihood of misclassification.

## Experiments
This paper focuses on the performance of using Binoculars to detect generated text, and conducts several sets of comparative experiments to verify its effectiveness. Specifically, this paper examines the following four areas of experimentation:

**Comparison with existing generative model detectors:** comparisons using existing models such as Ghostbuster and GPTZero show that Binoculars performs better in most cases.

![image](https://github.com/user-attachments/assets/356c33ef-fa72-4099-a69f-398401d4b297)

**Testing of detection ability for different languages:** by using multiple language samples from the M4 dataset, the results show that Binoculars has better cross-language generality.

**Test of detection ability for non-native English speakers' writing:** by testing on articles written by non-native English speakers on the EssayForum website, the results show that Binoculars is able to accurately recognise machine-generated articles.

![image](https://github.com/user-attachments/assets/993fd514-6d0b-4c9c-8e61-6d8d53aad5d6)

**Ability test for detecting modified prompting strategies:** by testing the data generated from LLAMA-2-13B chat, the results show that Binoculars also has high accuracy for modified prompting strategies.

![image](https://github.com/user-attachments/assets/a3c522c3-8cba-4ae2-8019-7e27ade0f831)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new zero-sample method for detecting language models that can accurately detect many different language models without using any training data.  
  2. Through comparative experiments, the researcher finds that the method exhibits high accuracy in a variety of textual domains and is able to effectively deal with adversarial attacks.  
  3. The paper also provides an in-depth discussion on the limitations and application prospects of the method, which provides a valuable reference for subsequent research.

### 2. Innovative points
  1. The method utilises two different language models to compute the cross perplexity of the input text, thus enabling the detection of multiple different language models.
  2. Compared with traditional methods based on statistical features or training data, the method is more flexible and adaptable to a wider range of scenarios.
  3. The method is also validated by testing on several publicly available datasets and compared with other existing methods to demonstrate its superiority.

### 3. Future Works
  1. The method can be further extended to other types of model detection, such as deep learning models in areas such as image recognition.
  2. The method can be considered for more application scenarios, such as machine-generated content detection on social media platforms, advertisement fraud detection, and other fields.
  3. Research on aspects such as interpretation and visualisation of detection results is also a direction worth exploring.    
