# Underspecification Presents Challenges for Credibility in Modern Machine Learning
[paper link](https://arxiv.org/pdf/2011.03395) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2020 | This paper explores one of the reasons for the poor behaviour of machine learning models in practice - ‘under-specification’. Under-normality refers to when a machine learning pipeline can return multiple predictors that all perform quite strongly in the training domain.         | Machine Learning          |

## Methodology

### 1. Abstract
The kind of underspecification is common in modern machine learning pipelines, such as those based on deep learning. The authors note that these predictors may exhibit very different behaviours in the deployment domain, which can lead to instability and affect model performance. In addition, underspecification may lead to bias and fairness issues. Using examples from a variety of domains, including computer vision, medical imaging, natural language processing, and clinical risk prediction, this paper demonstrates that underspecification is a pervasive problem and suggests that underspecification needs to be taken into account in real-world applications.

### 2. Method Description 
The aim of this study was to investigate the generalisation ability of genomics prediction models in different populations and to analyse the relationship between their sensitivity and the selected genetic variants. The study used a random feature model (RFM) to simulate the behaviour of neural networks and was experimentally validated by a prediction task for intraocular pressure (IOP).

Specifically, the researchers first performed genome-wide association analysis (GWAS) on the UK Biobank dataset, identifying 4,054 genetic variant loci associated with IOP and grouping them into 129 clusters. The researchers then constructed collections of 1,000 genetic features containing the best representatives from each cluster and used these collections to train linear regression models to predict IOP. Finally, they assessed the performance of these models in both UK and non-UK populations and compared the results using different sets of genetic features.

![image](https://github.com/user-attachments/assets/256782be-94e1-4e51-bb7e-e20e9202496b)

### 3. Methodological improvements
The study used stochastic feature models to simulate the behaviour of neural networks, a commonly used tool to understand how neural networks learn and explain their behaviour. In addition, the study improved the generalisation performance of the model by determining the strength of the L2 regularisation through cross-validation.

### 4. Issues addressed 
  1. The ability of genomics prediction models to generalise across different populations: the researchers found that in non-UK populations, models based on genetic traits had higher sensitivity relative to models using only demographic information, suggesting that the performance of genomics prediction models may vary considerably across different populations.
 
  2. Relationship between sensitivity and selected genetic variants: the researchers observed that models using representatives of clusters selected in the training set as genetic traits performed better in the UK population but poorly in the non-UK population, suggesting that selected genetic variants may not always be optimal in different populations.

## Experiments
This paper presents experimental studies in three areas, including medical genomics, computer vision, and natural language processing. In each domain, the authors use similar experimental approaches to explore model uncertainty and find some important insights.

First, in the field of **medical genomics**, the authors used a simple prediction task to construct different feature sets and then demonstrated model instability by comparing the performance of these feature sets. The results show that different feature sets lead to different generalisation abilities even on the same training data.

Second, in the area of **computer vision**, the authors used two pre-trained models (ResNet-50 and BiT) for an image classification task and subjected them to a variety of stress tests. The results show that both models suffer from some degree of instability, especially in the face of distributional changes. This suggests that different random seeds or other initialisations may lead to different performances even on the same training data.

![image](https://github.com/user-attachments/assets/6665c1ad-12ec-4c4c-ac9f-54b1466d52c4)

Finally, in the field of **natural language processing**, the authors use a neural network-based language generation model and explore its instability by comparing model outputs under different initial states. The results show that even small changes may lead to very different outputs, implying that such models may not be well adapted to new scenarios.  

## Conclusion

### 1. Advantages of the Thesis
  1. The paper investigates the reasons for the existence of underspecification in deep learning models and its impact on model performance through a series of experiments.
  2. The authors use a variety of cases to illustrate the existence of underspecification and propose corresponding solutions. Also, the paper provides multiple open source tools and codes for readers' reference and use.
  
### 2. Innovative points
The main contribution of the paper is that it proposes a new approach to evaluate the phenomenon of underspecification and provides some practical tools and codes to help researchers better understand and solve this problem. And, the paper presents some existing solutions, which are compared and analysed. 

### 3. Future Works
  1. In future research, it is possible to consider combining underspecification with other problems in deep learning, such as combating attacks and interpretability.
  2. Also, attempts can be made to develop more efficient and accurate methods to detect and mitigate the phenomenon of underspecification.
