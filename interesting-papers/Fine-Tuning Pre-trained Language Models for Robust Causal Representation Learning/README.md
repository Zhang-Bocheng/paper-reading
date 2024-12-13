# Fine-Tuning Pre-trained Language Models for Robust Causal Representation Learning
[paper link](https://arxiv.org/pdf/2410.14375) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper explores how pre-trained language models (PLMs) can be used for fine-tuning to improve the robustness of causal representation learning.          | pre-trained language models (PLMs)         |

## Methodology

### 1. Abstract
Existing approaches typically rely on non-causal representations that are difficult to generalise over out-of-domain data. The authors propose a method based on causal front-door tuning and decomposition assumptions that uses the fine-tuned representation as a source of data augmentation, resulting in a more robust representation. Experimental results show that the method has better generalisation performance than existing methods. This work provides new ideas for solving the domain generalisation problem and links fine-tuning to causal mechanisms, further advancing the research on representation learning.

### 2. Method Description 
  1. Learning the feature representation R1 using a standard supervised fine-tuning estimation algorithm.
  2. Learning invariant causal features C by optimising the objective function.
  3. Extracting local signals in the text using a local feature construction algorithm.
  4. Based on the results of the above three steps, the CTA algorithm is used for training and prediction.

![image](https://github.com/user-attachments/assets/3c718b70-82d9-4e7d-ae43-bde72ef8322c)

### 3. Methodological improvements
  1. Data augmentation using PLM to identify causal features.
  2. Learning a representation for dealing with local features to achieve the so-called causal front-door adjustment.

### 4. Issues addressed 
The aim of this paper is to address the unstable performance of supervised fine-tuning estimation algorithms in OOV scenarios. By analysing the standard supervised fine-tuning estimation algorithms, this paper concludes that they are unable to effectively deal with OOV features associated with the original features. Therefore, this paper proposes a new approach that uses PLM for data augmentation and learns a representation that can handle local features, which improves the robustness and OOV generalisation of the model.

## Experiments
This paper focuses on the authors' semi-synthetic and real-world experiments on two NLU benchmark datasets and compares the effectiveness of their approach with some baseline methods. Specifically, they conducted the following four comparison experiments:

![image](https://github.com/user-attachments/assets/2d693432-7916-4468-8d7d-7e31b64bdf17)

**Comparing SFT0 and SFT methods** (SFT0 is a simple classifier based on a pre-trained model, while SFT is a common transfer learning strategy).

**Comparing the WSA and WISE methods** (WSA is averaging multiple points to obtain a more robust classifier, and WISE is a method that interpolates pre-trained and fine-tuned models to improve generalisation).

![image](https://github.com/user-attachments/assets/df36c854-c031-47ee-a7c2-a488d01a4f70)

![image](https://github.com/user-attachments/assets/1e9f189d-2a9c-4479-81d1-3f681d556c99)

Experiments were conducted using three different versions to further **investigate the impact of the different representations on the prediction performance:** the CTL-N does not apply a tuning formula and only uses Φ and C to estimate the label Y; the CTL-C uses the estimated causal variable C to predict the label Y; and the Causal-Φ uses the local misrepresentation feature Φ to predict Y.

In a real-world case, the authors conduct experiments using a dataset constructed from Amazon and Yelp reviews and compare it to other single-domain generalisability baselines.
In these experiments, the authors used accuracy as an assessment metric and repeated each experiment five times to ensure the reliability of the results. The experimental results show that their method performs better in dealing with misleading information, especially when dealing with domain shifts.  
![image](https://github.com/user-attachments/assets/62c1693a-a790-42c2-be2e-349a58287be6)

## Conclusion

### 1. Advantages of the Thesis
  1. The paper proposes a new method for constructing robust causal representations using pre-trained language models, and verifies its superior performance in OOV scenarios through a series of semi-synthetic and real-world experiments.
  2. The method improves the generalisation ability of the model by decomposing the input text, separating non-causal features from causal features, and using pre-trained language models to extract stable causal features.
  3. In addition, the method explores how to identify and control potential sources of bias, providing new ideas for solving bias problems in practical applications.

### 2. Innovative points
The paper proposes a method based on structural causal graphs to distinguish causal and non-causal features, and extracts stable causal features using pre-trained language models. Meanwhile, the method also considers the impact of data distribution changes on the model and proposes a corresponding solution. These innovations make the method highly practical and scalable. 

### 3. Future Works
The method needs more empirical studies to demonstrate its effectiveness on different tasks and datasets. Therefore, future research could focus on these issues to further improve the effectiveness and usefulness of the method.   
