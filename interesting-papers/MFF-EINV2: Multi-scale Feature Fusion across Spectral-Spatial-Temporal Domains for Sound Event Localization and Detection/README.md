# MFF-EINV2: Multi-scale Feature Fusion across Spectral-Spatial-Temporal Domains for Sound Event Localization and Detection
[paper link](https://arxiv.org/pdf/2406.08771) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2024 |  This paper describes a network architecture called Multi-scale Feature Fusion (MFF) for extracting multi-scale features in the acoustic, spatial, and temporal domains to solve the sound event localisation and detection (SELD) problem.         | Feature Extraction         |

## Methodology

### 1. Abstract
The method utilises a parallel sub-network architecture to generate multi-scale spectral and spatial features and a TF convolution module to provide multi-scale time domain features. Combining MFF with Event-Independent Network V2 (EINV2), referred to as MFF-EINV2, experimentally proved its effectiveness, achieving state-of-the-art performance on the DCASE Challenge Task 3 dataset in 2022 and 2023.

### 2. Method Description 
This thesis presents a multi-scale feature extraction network structure called MFF-EINV2 for sound source localisation and sound event detection tasks. The network structure consists of two branches: the sound event detection (SED) branch and the direction angle (DoA) branch. At the input layer, log-mel spectrograms and basis vector maps are spliced along the channel dimensions and converted into feature maps with [C, T, F] dimensions by means of a double convolutional layer. The MFF module is then introduced to fully extract multiscale features from the spectral, spatial and temporal domains. 

Next, the network is divided into two branches: the SED branch and the DoA branch, each containing three double convolutional layers. After each double convolutional layer, a pooling layer of size (2,2) is applied to align with the time domain resolution of the target labels. In order to avoid the MFF module from losing original information or extracting irrelevant features, a residual join is established to connect the output of the MFF module to the output of the first double convolutional layer. 

Finally, the Conformer block is used as a decoder to extract both local and global temporal context information using a multi-head self-attention mechanism. The fully-connected layer outputs three tracks that can handle up to three overlapping sound events.

![image](https://github.com/user-attachments/assets/9406f74d-5e95-45ec-a63f-9f80de6241d9)

### 3. Methodological improvements
The method employs a parallel multiresolution subnetwork to generate multi-scale spectral and spatial features. The input feature mapping is transformed into multiple sub-networks by a frequency down-sampling operation, maintaining high resolution in the time dimension. This allows different types of audio source information to be captured at different scales. And, a TF-convolution module is introduced to extract multi-scale temporal features, as well as a repetitive multi-scale fusion process to enhance the information exchange capability of each sub-network.

### 4. Issues addressed 
The method mainly addresses problems in sound source localisation and sound event detection, such as accurately identifying different types of sound source locations and sound events. By introducing a multiscale feature extraction network structure, it is able to better capture multiscale features in the spectral, spatial and temporal domains, thus improving the performance of the model.

## Experiments
This paper focuses on the performance of the MFF-EINV2 model on the STARSS22 and STARSS23 datasets and compares it with several other models. Specifically, the paper first introduces the datasets, hyperparameters and evaluation metrics used in the experiments, and then demonstrates the performance advantages of the MFF-EINV2 model through three comparison experiments.

The first comparison experiment compares the MFF-EINV2 model with several other models on the STARSS22 dataset. This experiment uses five evaluation metrics (ER20◦, F20◦, LECD, LRCD, and SELDscore) to assess the performance of the models. The results show that the MFF-EINV2 model outperforms the 2022 Baseline and ResNet-Conformer models on all evaluation metrics and has a slight improvement over the CST-former model. In addition, the MFF-EINV2 model is able to better extract spatial information and therefore performs better on the LECD and LRCD metrics.

![image](https://github.com/user-attachments/assets/e2c7f984-197d-488a-91f2-d78b99ec87bc)

The second comparison experiment compares the different models on the STARSS23 dataset. This experiment also used five evaluation metrics to assess the performance of the models. The results show that the MFF-EINV2 model outperforms the 2023 Baseline and DST attention models on all the evaluation metrics and performs better relative to the CST-former model. In addition, the MFF-EINV2 model is able to better understand the overall structure of the soundscape and therefore performs better on the ER20◦ and LRCD metrics.

![image](https://github.com/user-attachments/assets/a28fe06f-f350-4b51-b7c0-75f5fe01a43b)

The third comparative experiment investigates the effect of the number of parallel sub-networks in the MFF-EINV2 model. The experimental results show that the best SELD performance can be achieved using three parallel sub-networks.

The fourth comparison experiment is a study of the effect of the number of convolutional blocks in the TFCM. The experimental results show that using six convolutional blocks can effectively capture multi-scale temporal information.

## Conclusion

### 1. Advantages of the Thesis
  1. A new multi-scale feature fusion (MFF) module is proposed for improving performance in acoustic event localisation and detection (SELD) tasks.
  2. The MFF module employs a parallel sub-network structure and uses a time-frequency convolution module (TFCM) to extract multi-scale features across the spectral, spatial and time domains.
  3. Through repeated multiscale fusion, each subnetwork can continuously receive information from other parallel representations, thus improving the representation capability.
  4. Experimental results show that MFF-EINV2 significantly reduces the number of parameters (by 68.5%) while improving the SELD score (by 18.2%) compared to EINV2, and outperforms other published methods to reach the state-of-the-art performance level without data enhancement.

### 2. Innovative points
  1. The MFF module is a novel multi-scale feature fusion module that extracts multi-scale features across three domains, spectral, spatial and time domains, to enhance the learning capability and performance of the model.
  2. Through the parallel sub-network structure and TFCM, the MFF module is able to effectively utilise the information interaction between multiple sub-networks to further enhance the feature extraction capability.
  3. The design ideas of the MFF module provide reference and borrowing value for future multi-scale feature fusion techniques. 

### 3. Future Works
  1. The MFF module proposed in this study achieved excellent performance in the SELD task, but there are still some challenges to overcome, such as how to better handle multi-scale features from different domains and how to further optimise the performance of the model.
  2. Future research directions include, but are not limited to: exploring more multi-scale feature fusion strategies; combining research results from other fields, such as speech recognition, audio signal processing, etc., to further improve the performance of the SELD task; and developing more efficient deep learning algorithms to achieve faster and more accurate SELD tasks.  
