# Image-to-Image Translation with Conditional Adversarial Networks
[paper link](https://arxiv.org/pdf/1611.07004) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2018 | This paper introduces a generalized solution, conditional adversarial networks (conditional GAN), for the image-to-image transformation problem.         |  GANs        |

## Methodology

### 1. Abstract
   The method learns not only the mapping relation between the input image to the output image, but also the loss function that trains this mapping relation. This allows the same generalized method to be applied to problems that traditionally require different loss functions. The authors demonstrated the effectiveness of this method for compositing photographs, reconstructing objects, and coloring, and since the release of the pix2pix software associated with the paper, many Internet users, have experimented with their systems, further demonstrating its broad applicability and ease of adoption without the need to tweak parameters. 

   ![image](https://github.com/user-attachments/assets/41c5f8fa-422b-4d9f-a729-88915513ca90)

### 2. Method Description 
  The paper proposes a conditional generative adversarial network (conditional GAN) to solve the image translation problem. While traditional GAN learn a model that maps random noise vectors to output images, conditional GAN learn a model that maps observed images and random noise vectors to output images. The method uses a U-Net shaped generator and adds skip connections between multiple layers to avoid information bottlenecks. In addition, they design a discriminator for PatchGAN to focus only on structures in localized image blocks and enforce low-frequency correctness through L1 distance.

  ![image](https://github.com/user-attachments/assets/de06ba2b-3485-4238-b79a-29f75e57da4a)

### 3. Methodological improvements
  The paper proposes a number of improvements to increase the effectiveness of conditional GAN. 
  
  1. First, the authors mix the traditional GAN loss function with L2 or L1 distances to encourage the generation of outputs that are closer to the real image.
  
  2. Second, they found that providing Gaussian noise inputs was not effective for generating highly randomized outputs, so they used dropout noise as an alternative.
  
  3.  Finally, they used the discriminator of PatchGAN to focus only on the structure in the localized image chunks, which reduces the number of parameters and increases the speed.
     
### 4. Issues addressed 
  The authors attempted to convert color images to grayscale images, line drawings to photographs, etc. These problems require GANs that are able to capture structural similarities between inputs and outputs and are able to change color or texture while maintaining detail. By using conditional GAN and some improvements.
  
## Experiments
  This paper describes the experiments and results of Pix2Pix. The method can convert one type of image to another type of image, such as converting a black and white line drawing to a color photo. The experiments include several tasks and datasets, such as from maps to aerial photographs, from sketches to real photographs, etc., and different loss functions are used to compare the results. Among them, FCN-score is a commonly used evaluation metric, which is assessed by testing whether the generated images can be correctly recognized as target labels by the classifier. The experimental results show that Pix2Pix achieves better results on a wide range of tasks, and the quality of the generated images can be further improved using conditional GANs.

  ![image](https://github.com/user-attachments/assets/6fa308bf-c8f5-4971-b809-6b7b6fa581ad)

  ![image](https://github.com/user-attachments/assets/ccc39766-bb82-4cd4-8225-7afbd58e2f1f)

## Conclusion

### 1. Advantages of the Thesis
  1. The framework learns loss functions adapted to specific tasks and data, and thus is applicable to many different settings.
  
  2. The authors also analyze important architectural choices in the framework for subsequent research.

### 2. Innovative points
  1. The main contribution of this paper is to present the Pix2Pix framework, which uses conditional GAN for image-to-image translation tasks.
 
  2. Compared to traditional special-purpose machines, Pix2Pix can adaptively learn loss functions suitable for different tasks and data without designing a specific loss function.
  
  3. In addition, the framework can be applied to many types of output structures, including highly structured graphical output.

### 3. Future Works
  1. In the future, can expect more improvements and extensions to further improve the performance and applicability of Pix2Pix. 
  
  2. the performance of the model can be improved by introducing more complex model structures or increasing training data.
  
  3. combining Pix2Pix with other techniques, such as RL or migration learning, can also be considered to solve more complex problems.

