# Multimodal Pathway: Improve Transformers with Irrelevant Data from Other Modalities
[paper link](https://arxiv.org/pdf/2401.14405) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 | This paper presents a method called ‘multimodal paths’, which aims to improve a modal-specific transformer model by using data from other modes.          |      Transformer    |

## Methodology

### 1. Abstract
Unlike other methods that use paired or alternating data from different modes, this method emphasises that the data samples from the target modes are independent of the other modes. The authors propose a method called ‘multimodal paths’, where given a target mode and a transformer model designed for it, they use an auxiliary transformer from another mode and construct paths connecting the two model components so that data from the target mode can be processed by both models. This approach takes advantage of the generic sequence-to-sequence modelling capability of the transformer obtained in both modalities. The authors observed significant and consistent performance improvements in image, point cloud, video, and audio recognition tasks, demonstrating the effectiveness of the approach.

### 2. Method Description 
The Multi-Modal Pre-training Transformer (M2PT) model proposed in this paper is a neural network model for multi-modal pre-training. The model employs an adaptive architectural design and cross-modal parameterisation techniques to achieve effective representation learning and transfer learning on multimodal data.

Specifically, the M2PT model consists of three modules: a modality-specific disambiguator, a transformer block without modal properties, and a modality-specific head. For different modal data (e.g., image, video, point cloud, audio, etc.), corresponding disambiguators are designed to transform the input data into D-dimensional vector representations. Meanwhile, the M2PT model adopts a structural design similar to Vision Transformer (ViT), i.e., each transformer block consists of a self-attention block and a feed-forward network block with the same hyperparameter settings.

![image](https://github.com/user-attachments/assets/0526e2f2-a8c8-4a5f-bfe7-11690729ab30)

### 3. Methodological improvements
In contrast to traditional unimodal pre-trained models, the M2PT model introduces a cross-modal parameterisation technique that allows model weights to be shared and migrated between different modalities. Specifically, in each transformer block, in addition to the original weight matrix, an additional trainable weight matrix is added and initialised to the corresponding weight matrix in another transformer block trained on the auxiliary modality. In this way, the M2PT model is able to utilise the data information from the other modality to improve its own learning.

In addition, the M2PT model adopts an adaptive architectural design, i.e., it dynamically adjusts the design of the disambiguator and the head according to the different needs of the target modality. This adaptive design enables the M2PT model to better adapt to diverse application scenarios.

### 4. Issues addressed 
  1. Inefficient learning: since only single-modal data is considered, it is difficult for the model to make full use of the information from multimodal data.
  2. Limited migration capability: since the model is trained only for a single modality, its performance on other modalities may be poor.

## Experiments
This paper focuses on the performance of a multimodal pre-trained based model (M2PT) on the tasks of image recognition, point cloud understanding, audio recognition and video understanding, and several comparative experiments are conducted to verify its effectiveness.

Firstly, on the image recognition task, the authors used three representative datasets (ImageNet-1K, MSCOCO and ADE-20K) and used two different initialisations to compare the performance of M2PT. The results show that M2PT improves its performance on all datasets with relative improvements of 0.7%, 5.7%, and 3.9%, respectively, when compared to the model pre-trained using only ImageNet.

![image](https://github.com/user-attachments/assets/6ff66720-4f70-473d-abe1-14c57568941f)

Second, on the point cloud understanding task, the authors applied M2PT to the ShapeNetPart and PartNet datasets and compared it with other point cloud pre-training methods such as Point-BERT and Point-MAE. The results show that M2PT improves both class mIoU and instance mIoU on both datasets, with relative improvements of 1.4% and 1.6%, respectively.

![image](https://github.com/user-attachments/assets/bce71c40-c539-487d-8cf5-bbcee9c02da4)

Again, on the audio recognition task, the authors applied M2PT to the AudioSet-2k dataset and compared it with other competing methods (e.g., SSAST, AST, and AudioMAE). The results show that M2PT outperforms the other methods by 0.8% in top-1 accuracy on balanced splitting, with a relative improvement of 0.8%.

![image](https://github.com/user-attachments/assets/46a9c622-0044-4a2c-bce5-bfbded998573)

Finally, on the video comprehension task, the authors applied M2PT to the Kinetics-400 dataset and compared it with other methods (e.g. SlowFast, MViTv2, TimeSFormer, and Video-MAE). The results show that M2PT's top-1 accuracy on this dataset is at least 0.8% higher than the other methods, with a relative improvement of 0.8%. 

![image](https://github.com/user-attachments/assets/9e2caf61-327c-41a5-8cfc-9a8975eeec02)

## Conclusion

### 1. Advantages of the Thesis
  1. A method to improve the performance of a specific modality using irrelevant data is proposed, which has some theoretical significance.
  2. In the experiments, significant performance improvement is achieved by using data from multiple modalities to train the model and using only data from the target modality during testing.
  3. The experimental results show that the method can effectively improve the performance of the model on multiple modalities, providing a new idea for multimodal learning.

### 2. Innovative points
  1. Cross-modal knowledge transfer is utilised, which improves the generalisation ability of the model by linking knowledge between different modalities.
  2. The M2PT framework was employed to achieve cross-modal knowledge transfer by sharing parameters across modalities without increasing computational effort.

### 3. Future Works
  1. The method still needs more experiments to prove its effectiveness, especially on larger datasets.
  2. Further exploration can be done on how to select the optimal auxiliary modality and how to adjust the parameters to optimise the model performance.
  3. The method can be considered to be applied to other fields, such as natural language processing.    
