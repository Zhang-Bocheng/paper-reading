# SciEval: A Multi-Level Large Language Model Evaluation Benchmark for Scientific Research
[paper link](https://arxiv.org/pdf/2308.13149) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | Most current assessment benchmarks are based on pre-collected objective questions, which suffers from data leakage and lacks assessment of subjective question-answer ability.          |  LLMs        |

## Methodology

### 1. Abstract
To address these issues, this paper proposes SciEval, a comprehensive and multidisciplinary assessment benchmark designed to systematically assess scientific research capacity. SciEval is based on Bloom's taxonomy and covers four dimensions, including dynamic subsets designed to prevent potential data leakage. At the same time, SciEval includes both objective and subjective questions, features that make it a more effective benchmark for assessing LLM scientific research capacity. Comprehensive experiments on state-of-the-art LLMs have shown that while GPT-4 achieves state-of-the-art performance compared to other LLMs, there is still significant room for improvement, especially for dynamic problems. 

![image](https://github.com/user-attachments/assets/6d9eb044-af9c-4c59-b302-ea4a55e5dfda)

### 2. Method Description 
This paper describes different benchmark tests for assessing the performance of language models and proposes specific benchmark tests for particular downstream tasks. SciEval is a multi-dimensional and flexible scientific proficiency assessment system with a dynamic data subset design, which aims to assess the scientific proficiency and intellectual reasoning of language models in several aspects.

![image](https://github.com/user-attachments/assets/82bae5b1-621d-4945-ad18-c5a4e92d7355)
  
### 3. Methodological improvements
SciEval uses a community Q&A data source, which makes the data more diverse and flexible than existing Q&A datasets in the scientific domain. In addition, SciEval was designed with a dynamic data subset to minimize the risk of data leakage.

### 4. Issues addressed 
By introducing SciEval, a new scientific competence assessment system, researchers can more comprehensively assess the scientific competence and intellectual reasoning ability of language models in different domains, and thus better understand the effectiveness of their practical application. At the same time, the flexibility and versatility of this assessment system can also help to improve researchers' knowledge and understanding of the performance of language models.

## Experiments
This paper describes the experimental design and result analysis of SciEval. First, the authors introduce the experimental data sources and categorization, and design three different data types: static data, dynamic data, and experimental data. Then, the authors conducted three comparison experiments:

![image](https://github.com/user-attachments/assets/c1d13e70-3e8a-479a-8ec1-80ef600a0332)

**On the static data**, the authors evaluated the accuracy of 15 highly expressive large-scale language models (LLMs) in answering questions. The results show that only GPT-4, GPT-3.5-turbo, and Claude-v1.3 achieve an average accuracy of over 60%, while the other models perform relatively poorly.

**On the dynamic data**, the authors used basic information and attributes from the chemistry and physics domains to generate the data and categorized it into two subsets: **knowledge application and scientific computation**. The results show that in the field of chemistry, most models with billions of parameters perform poorly, indicating that they have limited knowledge of molecular structure. Whereas in the field of physics, where the accuracy of the models should be at least 25% since all problems are four-choice problems, these models did not achieve satisfactory results.

**On the experimental data**, the authors evaluated multiple open-ended problems in each experiment. The results showed that the GPT-series and Claude-series models performed well, while the other two models performed poorly. In addition, although some models performed well in terms of experimental design, they did not perform satisfactorily when analyzing the experimental results.

![image](https://github.com/user-attachments/assets/48128b81-494a-4dd2-8f90-82993d313472)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper proposes a scientific competence assessment benchmark called SciEval, which aims to assess the advanced competence of large language models in scientific domains. The benchmark covers three basic scientific domains, chemistry, physics, and biology, and measures the scientific capabilities of large language models in these domains through a multilevel comprehensive assessment.
 
  2. In addition, the benchmark employs a combination of objective and subjective questions, as well as dynamic data generation techniques to avoid potential data leakage problems. The experimental results show that most large language models perform poorly on SciEval, but the GPT series and Claude series models perform better.

### 2. Innovative points
  1. multilevel and comprehensive assessment of the competence of large language models in scientific domains, 
  2. combination of objective and subjective questions, and 
  3. use of dynamic data generation techniques to avoid potential data leakage problems. 
  
  These features make SciEval a more comprehensive and unbiased tool for assessing scientific competence. 
### 3. Future Works
  1. Future research can further explore how SciEval can be used to assess the performance of large language models in different scientific domains, and can extend SciEval by adding more subtopics and experimental designs.
  
  2. In addition, it could be investigated how to incorporate other types of problems, such as reasoning problems and natural language generation problems, to more comprehensively assess the capabilities of large language models.  
