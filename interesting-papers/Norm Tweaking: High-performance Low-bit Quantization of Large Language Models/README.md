# Norm Tweaking: High-performance Low-bit Quantization of Large Language Models
[paper link](https://arxiv.org/pdf/2309.02784) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a technique called ‘paradigm tuning’ that can be used in current model compression methods to achieve high-accuracy and low-cost quantisation.          | Large Language Models (LLMs)         |

## Methodology

### 1. Abstract
The method restores the accuracy of large language models (LLMs) by recalibrating the quantisation activation distributions to match their floating-point counterparts. The authors devise a strategy incorporating calibration data generation and channel distance constraints for updating the weights of the normalisation layer to improve generalisation. Experimental results show that the method achieves significant improvements between both quantised-only and jointly quantised weights and activations and outperforms existing model compression methods when tested extensively on multiple publicly available LLMs.

![image](https://github.com/user-attachments/assets/911120f3-69e3-4b45-8233-2beec8474880)

### 2. Method Description 
The quantisation technique proposed in this paper is a fast optimisation method for large language models (LLMs). The core idea of the method is to adjust the activation distribution of the quantised model by fine-tuning the LayerNorm to make it closer to the original floating-point model. Since LLMs typically use LayerNorm or similar normalisation operations, this method can be widely used in a variety of large language models.

Specifically, the method first generates a set of textual data as a calibration dataset using the pre-trained LLM, and then processes each Transformer layer one by one to quantise and update its weights. During the iteration process, the loss function at the channel level is computed to guide the direction of parameter updates, and the learning rate and step size scheduler are adjusted as needed. Finally, after multiple iterations, a high-performance quantised LLM is obtained.

![image](https://github.com/user-attachments/assets/d2b3be9d-aab0-470f-b0bd-dddceb70d877)
  
### 3. Methodological improvements
Compared to traditional fine-tuning methods based on gradient descent, the method in this paper does not need to directly tune all parameters of the model, but only fine-tunes the weights of the LayerNorm. This makes the algorithm more efficient and easy to implement. In addition, the method introduces channel-level constraints and a relaxed alignment strategy to further improve the performance and generalisation of the model.

### 4. Issues addressed 
The method proposed in this paper addresses the problem that existing quantisation techniques cannot quickly adapt to large language models. By fine-tuning the LayerNorm, the accuracy of the model can be quickly restored without compromising the performance of the model. In addition, the method improves the generalisation ability and robustness of the model by reasonably selecting the calibration dataset, designing the corresponding loss function, and employing different learning rates and step schedulers. 

## Experiments
This paper focuses on Norm-Tweaking, a quantitative method for Language Models (LLMs), and demonstrates its superior performance through several comparison experiments. The following are the details of each comparison experiment:

**Comparison Experiment 1:** Norm-Tweaking vs. GPTQ This experiment was conducted on the LAMBADA dataset and tested using LLMs of different sizes such as GLM, OPT, LLaMa and BLOOM. The results show that Norm-Tweaking is able to better maintain model accuracy with 2-bit weight quantisation compared to GPTQ, and even outperforms GPTQ by almost 10% on the GLM-130B and OPT-66B models.

![image](https://github.com/user-attachments/assets/fffe3fa3-83af-4c46-9981-563b6d57c402)

**Comparison Experiment 2:** Norm-Tweaking vs. other post-quantisation methods This experiment integrates Norm-Tweaking into two commonly used post-quantisation methods, namely RTN and SmoothQuant, and tests them in different quantisation modes. The results show that Norm-Tweaking can provide stable performance improvement in both weight quantisation and activation quantisation and is highly versatile.

![image](https://github.com/user-attachments/assets/dde76920-e3ec-4115-be10-66a2876d5f03)

**Comparison Experiment 3:** Subjective Evaluation of Norm-Tweaking vs. GPTQ This experiment evaluates the performance of Norm-Tweaking and GPTQ by generating results on human evaluations. The results show that quantification using Norm-Tweaking avoids problems such as obvious grammatical errors, logical errors, and factual errors, which are present in the low-bit quantified GPTQ model.

![image](https://github.com/user-attachments/assets/bb7032ea-bb2b-4856-8856-0915300a2047)

**Comparison Experiment 4:** The Impact of the Number of Iterations and Calibration Data Selection in Norm-Tweaking This experiment investigates the impact of the number of iterations and calibration data selection in Norm-Tweaking on model performance. The results show that too many iterations impair the accuracy of the model, while using the generated data as calibration data improves the performance of the quantitative model. 

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a new quantisation compression method that significantly improves the performance of large language models (LLMs) and is superior to the best existing methods such as GPTQ and SmoothQuant.
  2. The method is characterised by generating generic calibration data and adjusting the channel distribution loss in the normalisation layer, which enables fast and highly accurate model quantisation at low cost.
  3. In addition, the authors explored methods for compressing LLM models in the 2-bit range to achieve optimal performance. This approach offers promising solutions for reducing the computational and storage costs of LLMs while maintaining their high performance.

### 2. Innovative points
  1. This approach is applicable to a wide range of quantisation methods and has a very low additional computational cost. The authors conducted an extensive experimental evaluation of the method and showed that Norm-Tweaking consistently improves the performance of GPTQ and SmoothQuant on different large language models.
  2. In addition, in subjective evaluations, Norm-Tweaking performs well on very low bitrate models and is able to better preserve general semantic capabilities.
 
### 3. Future Works
 Future research can further explore how to apply the method to other types of neural network models and try to combine it with other quantisation techniques to obtain better results. And, it can also be investigated how to automatically adjust the Norm-Tweaking parameters during the training process to further improve the performance of the model.    
