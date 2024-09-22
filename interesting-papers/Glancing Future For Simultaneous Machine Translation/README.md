# Glancing Future For Simultaneous Machine Translation
[paper link](https://arxiv.org/pdf/2309.06179) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This article mainly explores the problem of simultaneous machine translation (SiMT) and proposes a novel method to improve its translation ability.          | Machine Learning         |

## Methodology

### 1. Abstract
The existing SiMT methods use prefix to prefix training, but this approach reduces the model's ability to capture global information and introduces forced prediction due to the lack of necessary source information. Therefore, in order to enhance the translation capability of the SiMT model, it is necessary to establish a bridge between prefix 2 training and sequence to sequence (seq2seq) training. The new method proposed by the author is to browse the future in course learning, gradually reducing the available source information, and transitioning from the entire sentence to prefixes corresponding to the delay. The experimental results show that this method outperforms powerful baselines.

### 2. Method Description 
This paper proposes a translation method based on the sequence-to-sequence (seq2seq) model, which aims to improve the quality of machine translation. The method compensates for the shortcomings of ‘prefix2prefix’ training by introducing ‘glancing future’ training, and optimises it by combining the existing ‘wait-k’ and ‘HMT’ strategies. The method is optimised by introducing ‘glancing future’ training to compensate for ‘prefix2prefix’ training, and combining it with the existing ‘wait-k’ and ‘HMT’ strategies.

![image](https://github.com/user-attachments/assets/a1e82da5-30ae-47ea-92ce-e8620e868b30)

### 3. Methodological improvements
While traditional ‘prefix2prefix’ training may cause the model to lose the ability to capture global information, ‘glancing future’ training compensates for this problem by exposing unsourced information to the SiMT model. This problem is compensated by ‘glancing future’ training, which exposes unsourced information to the SiMT model. However, ‘glancing future’ training also has some challenges, such as too much future information may affect the model's ability to adapt to different delay scenarios. To address this issue, the paper introduces ‘curriculum learning’, which gradually reduces the amount of available source information during the training process so that the model can better adapt to incomplete input scenarios.

### 4. Issues addressed 
The main purpose of this method is to improve the quality of machine translation, by introducing ‘glancing future’ training and ‘curriculum learning’, the model can be enhanced to adapt to the unknown source information while guaranteeing the translation quality. By introducing ‘glancing future’ training and ‘curriculum learning’, the model's ability to adapt to unknown source information can be enhanced while ensuring the quality of translation, further improving the effect of machine translation. At the same time, this method can also be combined with the existing ‘wait-k’ and ‘HMT’ strategies to achieve a more flexible and efficient translation process.

## Experiments
This paper focuses on Glance Future Training, a new training method in the Transformer-based end-to-end machine translation model (SiMT), and evaluates and analyses it through several comparative experiments.

Firstly, for the experimental setup, the authors chose two datasets, IWSLT15 English to Vietnamese (En→Vi) and WMT15 German to English (De→En), and used TED tst2012 and TED tst2013 as the development set and test set. Also, for the De→En task, BPE coding was used to process the text.

Then, the authors compared Glance Future Training with some previous SiMT methods, including Whole Sentence Translation Model, Wait-k Strategy, MoE Wait-k Strategy, Adaptive-Wait-k Strategy, MMA Strategy, LEAPT Strategy, and HMT Strategy. Among them, Glance-Wait-k is the result of applying Glance Future Training to Wait-k strategy, while Glance-HMT is the result of applying it to HMT strategy.

![image](https://github.com/user-attachments/assets/a21105a4-933d-4914-a2ff-b7717e899433)

In terms of experimental results, the authors found that Glance Future Training achieved better performance performance relative to all other SiMT methods. Specifically, under the fixed strategy, Glance-Wait-k is close to the performance of MoE Wait-k, which is currently the best fixed strategy, and Glance Future Training brings significant improvements relative to the traditional Wait-k strategy, especially at low latencies. And with the adapted strategy, Glance-HMT shows a large improvement relative to the HMT strategy at low latency and is able to achieve a comparable level of performance to the HMT strategy at high latency.

In addition, the authors conducted an Ablation Study to investigate the effects of different parameter settings on Glance Future Training. The results show that Curriculum Learning can significantly improve the effectiveness of Glance Future Training as it allows each target token to interact with a different length of the source prefix, thus enhancing the translation capability of the SiMT model. In addition, the adjustment of αmin can also improve the effect of Glance Future Training, which indicates the importance of providing appropriate future information to the SiMT model.

![image](https://github.com/user-attachments/assets/3f4f0d9d-da3c-4f4b-a21d-84d550a5e95a)

Finally, the authors also analysed the method of selecting future information for Glance Future Training and found that it works better when selecting adjacent future information. In addition, the authors explored the problem of hallucination that may occur during the training process of the SiMT model and proposed the metric Hallucination Rate (HR) to quantify the hallucination phenomenon. The experimental results show that Glance Future Training can effectively reduce the hallucination phenomenon of the SiMT model during the translation process, thus improving its translation ability.
 
## Conclusion

### 1. Advantages of the Thesis
This paper proposes a novel method, glancing future training (GFT), to achieve the transition from seq2seq training to prefix2prefix training by introducing future source information in Curriculum Learning. Experimental results show that the method outperforms strong baselines.
 
### 2. Innovative points
Unlike traditional SiMT methods, this paper proposes GFT, which gradually approximates prefix2prefix training by progressively reducing the amount of future information that the model can access, and each target marker can access source markers beyond its delay range. This approach enhances the ability of SiMT models to utilise global information and reduces the phantom phenomenon in translation.

### 3. Future Works
Future research could further explore how to better utilise future source information and how to apply GFT to other types of machine translation tasks.
