# TrustLLM: Trustworthiness in Large Language Models
[paper link](https://arxiv.org/pdf/2401.05561) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper presents a trust assessment methodology and result analysis for Large Language Models (LLMs).         |   Large Language Models (LLMs)       |

## Methodology

### 1. Abstract
An eight-dimensional system of principles is first proposed and benchmark tests across six dimensions, including authenticity, security, fairness, robustness, privacy and machine ethics, are established. By testing 16 mainstream LLMs, trust was found to be positively correlated with functional effectiveness. In addition, a number of key insights were found, such as the challenges faced by LLMs in providing truthful answers and the high level of trust exhibited by some open source LLMs. Finally, the importance of transparency is emphasised and a call is made for the creation of an AI consortium to advance trust in LLMs.

![image](https://github.com/user-attachments/assets/b1a7b543-9ff5-4a3a-9dd3-f66fda1c4471)

### 2. Method Description 
This article describes the design, training, and application of Large Language Models (LLMs), a language model based on the Transformer architecture that learns world knowledge and basic linguistic competence through large-scale pre-training and further improves performance in task fine-tuning. The article highlights three main designs in LLMs: the encoder-decoder architecture, the causal decoder architecture, and the prefix decoder architecture. Of these, the most widely used is the causal decoder architecture, which uses an attention mask to ensure that each input token focuses only on previous tokens and on itself.

The training of LLMs typically consists of three phases: pre-training, instruction fine-tuning, and alignment tuning. Pre-training is to equip the model with world knowledge and basic language skills; instruction fine-tuning is to enhance the model's ability to generalise tasks; and alignment tuning is to align the model with human values and avoid producing harmful content.

### 3. Methodological improvements
This paper proposes two alignment training methods: supervised fine-tuning (SFT) and reinforcement learning from human feedback (RLHF).SFT is a method for instructing the model to understand cues and generate meaningful responses by calculating the loss of cross-entropy to assess whether the model-generated response matches the human-written response. However, SFT provides only a human-written response and fails to capture the diversity of human responses. To address this problem, RLHF has been proposed to provide fine-grained human feedback and is trained using pairwise comparison labelling. 

A typical RLHF consists of three main steps: 1) SFT using a high-quality instruction set; 2) collecting manually ranked pairs of comparison responses and training a quality-assessed reward model; and 3) optimising the SFT model using the PPO reinforcement learning framework while adding a KL scatter regularisation term to prevent overfitting. 

However, the PPO algorithm is unstable during the training process, so the Reward Ranking Fine-tuning (RAFT) method, which learns directly on highly ranked samples, is proposed as an alternative to PPO training. In addition, offline algorithms such as rank-based methods and language-based methods are proposed to eliminate the risk of overfitting and improve training stability.

### 4. Issues addressed 
The LLMs approach proposed in this paper addresses many natural language processing tasks such as sample less tasks, instruction following, context learning and stepwise reasoning. In addition, the alignment training methods aim to align models with human values and avoid producing harmful content. These methods can be applied to various NLP application scenarios such as chatbots, question and answer systems, etc.

## Experiments
This article focuses on research related to the evaluation and trustworthiness of Large Language Models (LLMs). The article first provides an overview of LLM and lists its applications in several domains. Then, the article describes the criteria for assessing trust in LLMs under various dimensions and related research, including:

**Authenticity:** this dimension focuses on whether the information generated by LLM is authentic and accurate. The assessment indicators include accuracy, human evaluation, etc. Experimental results show that while LLM performs well on some tasks, it may have problems with misleading information on other tasks.

**Security:** this dimension focuses on whether LLM has security issues, such as whether it generates harmful content or is exploited by attackers. The evaluation metrics include security tests, misuse tests, etc. The experimental results show that LLM has certain security risks and needs to strengthen security measures.

**Fairness:** This dimension focuses on whether LLM can treat different groups fairly and avoid discrimination and prejudice. The assessment indicators include fairness test, diversity test, etc. Experimental results show that LLM may be discriminatory in some cases, and further optimisation of the algorithm is needed to improve fairness.

**Robustness:** this dimension focuses on the ability of LLM to perform in the face of abnormal situations. The evaluation metrics include robustness test, anomaly detection, etc. The experimental results show that LLM may have wrong output when facing some abnormal situations, and further optimisation of the algorithm is needed to improve robustness.

**Privacy Protection:** this dimension focuses on how LLM protects users' privacy. The evaluation metrics include privacy leakage test, data encryption, etc. The experimental results show that LLM may have the risk of privacy leakage when processing user data, and needs to take appropriate privacy protection measures.

**Ethics:** This dimension focuses on whether LLM meets ethical and moral standards. The assessment indicators include ethical and moral tests, ethical decision-making, etc. The experimental results show that LLM may not be able to make correct ethical decisions in some cases, and further optimisation of the algorithm is needed to improve the level of ethics and morality.

![image](https://github.com/user-attachments/assets/72022091-3e4a-4447-a22b-3ffc4a049444)

In summary, this paper presents research related to the evaluation and trustworthiness of large-scale language models (LLMs), which is analysed and discussed in detail in six dimensions: authenticity, security, fairness, robustness, privacy protection and ethics. These research results have important guiding significance for the further development and application of large-scale language models. 

## Conclusion

### 1. Advantages of the Thesis
  1. The paper systematically explores the application of large-scale pre-trained language models (LLMs) in the field of natural language processing and the challenges they face.
 
  2. The thesis raises two important issues, transparency and accountability, with respect to the characteristics of LLMs, and elaborates on the methods and techniques to address these issues.

  3. The paper proves the effectiveness and feasibility of these methods through experiments, which provides important reference value for the application of LLMs.

### 2. Innovative points
  1. The thesis proposes an interpretability-based technique to enhance the transparency of LLMs, which is an innovative point in the current research on LLMs.

  2. The thesis also explores how to enhance the accountability of LLMs, e.g., by means of authentication and regulation to ensure their correctness and security.

  3. In addition, the paper proposes some new research directions, such as knowledge updating and editing, cross-linguistic capabilities and cross-modal capabilities, which provide new ideas and possibilities for the development of LLMs.


### 3. Future Works
  1. As LLMs continue to develop and become more popular, they will be used in more domains, and thus the demand for their transparency and accountability will increase.

  2. Future research can further explore how technologies such as machine learning and artificial intelligence can be utilised to address the various challenges faced by LLMs, leading to more reliable and efficient language processing.

  3. At the same time, there is a need to strengthen the norms and constraints in terms of law and ethics to ensure the safety and fairness of LLMs. 