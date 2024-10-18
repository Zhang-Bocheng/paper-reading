# The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits
[paper link](https://arxiv.org/pdf/2402.17764) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper discusses the era of 1-bit bit large language models (LLMs) and proposes a new approach to compress all LLMs to less than 1.58 bits.         | Large Language Models (LLMs)         |

## Methodology

The authors point out that with the current limited computational resources, it is becoming increasingly difficult to develop efficient language processing applications with high quality. Therefore, they propose a model compression method based on low bit-rate encoding, which can compress large language models to only 1.58 bits or less, thus significantly reducing storage and computational costs. Experimental results show that their method significantly improves the efficiency and scalability of the model while maintaining high accuracy. This work provides important guidance for future natural language processing applications.

## Experiments
This paper introduces BitNet b1.58, a new 1-bit LLM, and conducts several comparative experiments on it. 

First, the authors compare the difference in zero-sample performance between BitNet b1.58 and full-precision LLMs and find that BitNet b1.58 can achieve similar performance to full-precision LLMs for the same model size. 
![image](https://github.com/user-attachments/assets/cfec45b7-a404-4cb5-9b65-557691cd280d)

Second, the authors also compare the differences between BitNet b1.58 and full-precision LLM in terms of GPU memory usage, latency, and energy consumption, and find that BitNet b1.58 has significant advantages in all of these areas. In addition, the authors test the performance of BitNet b1.58 with larger training data and find that BitNet b1.58 is still able to maintain a high level of performance. 
![image](https://github.com/user-attachments/assets/1cc8eb52-65d5-42f7-a2aa-84a42f723b64)

Finally, the authors analyse the relationship between the computational cost and performance of BitNet b1.58 and propose a new computational law and optimisation scheme. Overall, this paper demonstrates the potential and advantages of BitNet b1.58 as a new and efficient LLM.
![image](https://github.com/user-attachments/assets/e8f1300d-b97b-4a8c-b7a2-369158dae059)
 
## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new quantisation scheme, BitNet b1.58, which significantly reduces memory consumption by reducing the activations to 1.58 bits and enables long sequence processing without overflow.

  2. BitNet b1.58 also has low energy consumption and high scalability, which makes it widely used in edge and mobile devices.
     
  3. The paper also explores how BitNet b1.58 can be further optimised, e.g. by designing a large-scale language model hardware system specifically for 1-bit quantisation.

### 2. Innovative points
  1. BitNet b1.58 employs a new quantisation approach, i.e., reducing activations to 1.58 bits, achieving more efficient memory usage and higher computational speed.

  2. BitNet b1.58 can also be applied to long sequence processing, solving the problem that traditional quantisation methods cannot handle long sequences.

  3. The paper also suggests design recommendations for specific hardware, which provide directions for future research.

### 3. Future Works
  1. The quantisation scheme of BitNet b1.58 can be applied to large-scale language models and other deep learning tasks, which is expected to improve computational efficiency and energy utilisation.
  
  2. Further research can be done to design more efficient hardware systems to support large-scale language models with 1-bit quantisation.

  3. Other types of quantisation schemes, such as binary quantisation, can also be explored to improve the performance and efficiency of the models.
 
