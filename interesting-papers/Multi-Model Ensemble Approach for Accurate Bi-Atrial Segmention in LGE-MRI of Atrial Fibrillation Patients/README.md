# Multi-Model Ensemble Approach for Accurate Bi-Atrial Segmention in LGE-MRI of Atrial Fibrillation Patients
[paper link](https://arxiv.org/pdf/2409.16083) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a multi-model integration approach for accurate segmentation of the left and right atria and their wall structures in cardiac magnetic resonance imaging (LGE-MRI) data from patients with atrial fibrillation.           | Object Segmention         |

## Methodology

### 1. Abstract
The method utilises multiple machine learning models, including Unet, ResNet, EfficientNet and VGG, and achieves high Dice similarity coefficients and low Hausdorff distances on an internal test set. This approach helps to improve the understanding of AF and supports the development of more accurate and effective ablation strategies.

### 2. Method Description 
The study used four different convolutional neural network (CNN) architectures; U-Net, ResNet, EfficientNet and VGG, and trained on each. Each of these models accepts a single-channel 2D LGE-MRI slice as input and outputs a four-channel image, where each output channel represents the probability that a pixel belongs to a specific class. All models used data enhancement techniques to improve generalisation.

### 3. Methodological improvements
  1. **Dataset segmentation:** dividing the original dataset into training, validation and test sets to evaluate model performance.
  2. **Data enhancement:** increasing the number of training samples by randomly applying transformations such as flipping and rotating to improve the generalisation ability of the model.
  3. **Model fusion:** weighted average of the prediction results from multiple models to get the final prediction results, which further improves the accuracy of the model.

### 4. Issues addressed 
This study aims to address the problem of left ventricular wall segmentation identification in cardiac magnetic resonance imaging. By using deep learning techniques and multiple CNN architectures, the study was able to effectively identify different tissue types in cardiac MRI images, providing strong support for clinical diagnosis.

## Experiments
In this paper, comparative experiments of several models are conducted to evaluate their performance in the task of segmenting the left and right ventricles in cardiac MRI data. Specifically, the authors compare the performance of four submodels, UNet, EfficientNet, ResNet, and VGG, and compare them to an Ensemble model.

First, the authors used two evaluation metrics, Dice coefficient and HD95 distance, to measure the performance of each model on three categories (wall, right atrium, and left heart). The results showed that UNet performed the worst on this task, with the lowest Dice score and the largest HD95 distance. In contrast, EfficientNet and ResNet performed better because they have deeper architectures that capture the data distribution more accurately. And surprisingly, VGG performed the best in this task, probably because it has a higher complexity than ResNet and is more easily adapted to multi-class segmentation problems.

Finally, the authors also compared the performance of an Ensemble model with four other sub-models. The results show that the Ensemble model performed the best, achieving the highest Dice score and the smallest HD95 distance on each category. This reflects the strength of the Ensemble model, which is able to combine the advantages of multiple individual models to obtain better results. Meanwhile, Figure 1 demonstrates the output of each model on three MRI scans and their true labels, showing that there are some small errors in each model, such as atrial walls being too thick or incorrectly shaped edges, which the Ensemble model is able to mitigate through its collective power. 

![image](https://github.com/user-attachments/assets/69b95293-1000-4bc2-acea-7e6bd7310222)

![image](https://github.com/user-attachments/assets/cdb42181-3c9e-4fb4-8408-5561f9a22885)

## Conclusion

### 1. Advantages of the Thesis
  1. The study used multiple deep learning models for multi-class biventricular segmentation and improved performance by fusing these models.
  2. The researchers achieved the best results in the challenge, proving the validity and reliability of their approach.
  3. The study shows that model diversity helps reduce errors and improve generalisation, reflecting the power of integrated learning.

### 2. Innovative points
  1. The study presents an integrated learning-based approach that combines multiple deep learning models for better multi-class biventricular segmentation.
  2. The researchers used different deep learning architectures, including UNet, ResNet, EfficientNet, and VGG, to obtain more comprehensive results.
  3. The researchers also explored the relationship between model complexity and capturing complex features in LGE-MRI data. 

### 3. Future Works
  1. Further optimisation of model parameters or integration of other architectures can be done in the future to improve segmentation accuracy.
  2. It could be explored how the method could be applied to other areas of medical image analysis, such as liver segmentation.
  3. Further research could also focus on how to extend the method to more biomedical image analysis tasks.    
