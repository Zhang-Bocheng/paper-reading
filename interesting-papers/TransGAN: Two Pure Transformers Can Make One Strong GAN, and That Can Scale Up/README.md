# TransGAN: Two Pure Transformers Can Make One Strong GAN, and That Can Scale Up
[paper link](https://arxiv.org/pdf/2102.07074) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2021 | This paper explores the possibility of building Generative Adversarial Networks (GANs) using a pure transformer architecture and proposes a new model called TransGAN.         |  Transformer         |

## Methodology

### 1. Abstract
The model includes a transformer-based memory-friendly generator and a multi-scale discriminator for capturing semantic context and low-level textures. To further alleviate memory bottlenecks and improve high-resolution generation, the authors also introduce a new mesh self-attention module. In addition, the authors develop a unique training methodology that includes a series of techniques such as data augmentation, modified normalisation and relative position coding to mitigate the training instability problem of TransGAN. Experimental results show that TransGAN achieves performance comparable to or better than the current best results on datasets such as STL-10, CIFAR-10, and CelebA, and especially excels in high-resolution generation tasks.

### 2. Method Description 
The GAN model proposed in this paper uses a memory-friendly generator and a multi-scale discriminator, and employs the Grid Self-Attention technique to improve the efficiency and performance of the model in high-resolution image generation tasks.

The generator is designed using a Transformer-based basic block, which contains a self-attention module and a fully-connected layer, to achieve high-resolution image generation by iteratively increasing the feature map resolution and decreasing the embedding dimension. Meanwhile, a pyramid structure and a modified upsampling layer are introduced to alleviate the memory and computational explosion problem.

The discriminator, on the other hand, employs a multi-scale design where the input image is partitioned into regions of different sizes and processed separately to extract semantic structure and texture details. Relative positional coding techniques are also employed to enhance the expressiveness of the model.

Grid Self-Attention, on the other hand, is an efficient self-attention mechanism for high-resolution image generation tasks, which improves the efficiency and performance of the model by dividing the full-size feature map into multiple non-overlapping grids, and calculating only the interactions within each grid.

![image](https://github.com/user-attachments/assets/bece93fa-cff6-472b-86a5-ffb60fea6e34)

### 3. Methodological improvements
  1. **Data enhancement**: by using data enhancement techniques such as translation, cropping and colour perturbation, the training of the model can be significantly improved.
  
  2. **Relative position coding**: Compared to traditional absolute position coding, relative position coding can better capture the relationship between local content, thus improving the model's expressiveness.
  
  3. **Modified normalisation**: By replacing the default used layer normalisation with token-wise deflation layer, the training process of the model can be effectively stabilised.
     
### 4. Issues addressed 
&emsp;**Design of Memory-Friendly Generator and Multiscale Discriminator**: by improving the generator and discriminator, the model can have better performance and efficiency in high-resolution image generation tasks.
<br>&emsp;**Application of Grid Self-Attention technique**: by introducing the Grid Self-Attention technique, the efficiency and performance of the model in high-resolution image generation tasks can be effectively improved.

## Experiments
This paper focuses on the performance of the authors' generative adversarial network (TransGAN) using the Transformer architecture on an image generation task and compares it with other CNN-based models 

![image](https://github.com/user-attachments/assets/f65f9701-b749-4496-acb5-52bf30619230)
![image](https://github.com/user-attachments/assets/487bb29e-553f-4ede-8950-29e2af17c901)
![image](https://github.com/user-attachments/assets/7f298a42-4759-40df-b8ec-b5c388a9edc8)

## Conclusion

### 1. Advantages of the Thesis
  1. **Systematic research**: The article first explores the reasons why traditional GAN needs to use CNN as backbone, and proposes the idea of using pure transformer instead of CNN.
  
  2. **Innovative architectural design**: The article proposes a series of innovative designs to address the challenges of applying pure transformer to image generation, including the use of a discriminator with multi-scale structure, grid self-attention mechanism, etc. The article also proposes a series of innovative designs to address the challenges of applying pure transformer to image generation.
  
  3. **Comprehensive experimental validation**: The article conducts a large number of experimental validations comparing TransGAN and other state-of-the-art methods, and achieves good results on multiple datasets.

### 2. Innovative points
  1. **Use of pure transformer structure**: traditional GANs use CNNs as the backbone, while this article completely abandons CNNs and adopts a pure transformer structure.
  
  2. **Discriminator with multi-scale structure**: in order to solve the problem that the pure transformer structure cannot capture global information, the article proposes a discriminator with multi-scale structure, which can capture both global and local information.
  
  3. **Grid self-attention mechanism**: In order to solve the problem that pure transformer structure is difficult to deal with high-resolution images, a grid self-attention mechanism is proposed in the article, which can effectively improve the performance of the model.

### 3. Future Works
  1. In terms of high-resolution image generation, TransGAN's performance is not as good as that of other methods;
  
  2. in addition, due to the large computational volume of the transformer structure, how to further optimise the model to improve the efficiency is also a direction worth exploring.
  
  3. In conclusion, this paper proposes a novel GAN architecture, which provides new ideas and directions for research in the field of image generation. 
