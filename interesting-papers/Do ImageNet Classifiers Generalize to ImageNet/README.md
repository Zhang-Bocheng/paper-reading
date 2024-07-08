# Do ImageNet Classifiers Generalize to ImageNet?
[paper link](https://arxiv.org/abs/1902.10811)
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2019 | This paper aims to test whether current image classification models are well adapted to new datasets.         |  Machine Learning         |

## Methodology

### 1. Abstract
  The authors constructed new test sets to examine the performance of these models on the new data. They performed extensive evaluations on both the CIFAR-10 and ImageNet datasets and found that the accuracy of these models decreased by 3% to 15% on the new test set, whereas the increased accuracy on the original test set resulted in a much larger improvement. The results suggest that these drops in accuracy are not due to the models' lack of adaptive capability, but rather to their inability to handle slightly "harder" images that are different from those in the original test set.
  
### 2. Method Description 
  The study aims to explore the reasons why models outperform training sets on test sets and suggests ways to distinguish between adaptation and distribution gaps. The researchers used multiple models to measure their accuracy to see how the two gaps evolve over time. They hypothesized that the later models experienced more adaptive overfitting because they were obtained by incrementally tuning the hyperparameters on the same test set. Therefore, the higher accuracy scores of these models should come from the increased adaptive gap, reflecting progress only on specific examples in the test set, rather than on the actual distribution D. However, the researchers found that the later models did not see a diminishing returns effect, but rather a greater advantage relative to the earlier models, suggesting that the decline in accuracy stems primarily from the larger distributional gap.
  
### 3. Methodological improvements
  The researchers provided a more nuanced understanding by measuring the accuracy of multiple models. This approach can help determine how the fitness and distribution gaps change over time. Additionally, the researchers explored the relationship between adaptation and distribution gaps and concluded that adaptation gaps are not the primary cause of models outperforming the training set on the test set.
  
### 4. Issues addressed 
  The study addresses the question of why models outperform the training set on the test set and suggests ways to distinguish between adaptation and distributional gaps. The researchers' findings can inform related research in the field of machine learning and help people better understand how models perform on different datasets.
  
## Experiments
  This paper focuses on the experiments conducted by the authors on the reproducibility of image classification models and analyzes the results. Specifically, the authors chose two widely used benchmark datasets for image classification, CIFAR-10 and ImageNet, and explored new test set creation methods for them. The authors first selected some data similar to the original datasets as the source of the new test set and manually filtered these data to ensure correctness. Then, the authors used a variety of DL models to evaluate them on the new test set and compared the differences in their performance on the old and new test sets. The experimental results showed that all models were less accurate on the new test set than on the original test set, but this decrease was not particularly significant. In addition, the authors found that the rankings of the different models on the old and new test sets did not change much, suggesting that the accuracy of the models is closely related to their original accuracies. Finally, the authors further explored the causes of the decrease in accuracy through a series of follow-up experiments, and concluded that it may be due to human error in the data cleaning process.
  
## Conclusion

### 1. Advantages of the Thesis
  1. The paper experimentally investigates the performance of machine learning models on new data and suggests two possible causes: adaptive overfitting and distribution gaps.
  
  2. The experimental results show that there is a large performance degradation of current machine learning models for new test sets, but there is no adaptive overfitting.
  
  3. The researchers also propose a simple data model to explain this phenomenon and explore how to better assess the reliability of machine learning models.
     
### 2. Innovative points
   1. By re-labeling an existing dataset and creating a new test set, the researchers validated the performance of the machine learning model on the new data.

  2. The researchers propose a simple method to model the phenomenon of adaptive overfitting and provide suggestions for future research directions.
     
### 3. Future Works
  1. This study provides some ideas and methods for assessing the reliability of ML models, but more empirical studies are needed to further validate these findings.
  
  2. Future research could explore the influence of more factors on machine learning models, such as the quantity and quality of training data.
  
  3. Attempts can be made to use more complex models or algorithms to improve the generalization ability of machine learning models, thus reducing the performance degradation on new data.
     
