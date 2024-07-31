# Neural Architecture Search without Training
[paper link](https://arxiv.org/pdf/2006.04647) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper explores a problem in deep neural network design: manual design takes a lot of time and effort, while automated design algorithms are often slow and expensive.        | Deep Neural Networks          |

## Methodology

To address problem, the researchers propose a new approach - predicting the training performance of a network by analyzing the overlap of activations between data points in an untrained network, and applying this metric to a simple search algorithm that can find robust network structures in seconds, without any training.

![image](https://github.com/user-attachments/assets/81f5f8c5-92d5-47a9-b5e0-da6742f61831)

## Conclusion

### 1. Advantages of the Thesis
  1. This research presents a method for quickly searching NN architectures that avoids the significant training time and resource costs associated with traditional NN architecture search (NAS).

  2. The researchers used benchmark datasets such as NAS-Bench-201 and devised a new evaluation metric by observing the similarity between activation patterns in untrained networks.

  3. They also developed a simple search algorithm based on this evaluation metric that can find highly accurate NN architectures in a short period of time.

  4. Finally, the researchers show how their approach can be combined with existing NAS technology to further improve search efficiency.

  ![image](https://github.com/user-attachments/assets/d1fb6ac2-0475-425d-8f39-bd62e8954a2c)

### 2. Innovative points
  1. The evaluation metric proposed in this study is a novel approach that utilizes information from untrained networks to predict their final performance, thus avoiding significant training time.

  2. The search algorithm developed by the researchers is so simple that it requires only one GPU to complete the search task in a few seconds.

  3. The study also explores how their approach can be used in conjunction with other NAS technologies to further improve search efficiency.

### 3. Future Works
  1. This research provides a new method for quickly searching NN architectures that can significantly reduce training time and resource costs.

  2. This work could also shed light on automated search problems in other areas, such as automated machine learning and adaptive systems.

  3. Future research could explore more complex search spaces and attempt to extend this approach to problems in other domains.
