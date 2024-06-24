# A Neural Algorithm of Artistic Style
[paper link](https://arxiv.org/pdf/1508.06576) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2015 |   This paper presents an artistic style conversion method based on deep neural networks       |    Deep Neural Networks       |

## Methodology

### 1. Abstract
  This paper presents an artistic style conversion method based on deep neural networks. The method realizes the artistic conversion of input images by extracting the content and style information of the images using a convolutional neural network and separating them for independent processing. Experimental results show that the method can effectively apply the styles of different artworks to arbitrary input images, producing new images with novel visual effects.

### 2. Method Description 
  This paper involves generating images that combine the content representation of one image with the style representation of another. This is achieved by using a Convolutional Neural Network (CNN) to separately manipulate the content and style representations. Specifically, the content representation of a photograph is matched with the style representations of various well-known artworks. The synthesis process involves finding an image that simultaneously aligns with the content representation of the photograph and the style representation of the artwork. 

### 3. Methodological improvements
  1. Separation of Content and Style Representations: Previous work on separating content from style was often limited to simpler sensory inputs, such as characters in different handwriting or images of faces in various poses. This paper demonstrates the ability to separate content and style in more complex.
     
  2. Use of Deep Neural Networks: Earlier methods for artistic style transfer, such as texture transfer techniques, primarily relied on non-parametric techniques that directly manipulated pixel representations. This paper leverages high-performing Deep Neural Networks (DNNs) trained on object recognition tasks to manipulate feature spaces that explicitly represent high-level content and style. 

  3. Hierarchical Processing: This paper highlights the hierarchical nature of Convolutional Neural Networks (CNNs), where each layer captures increasingly complex features of the input image. By manipulating features from different layers, the method can control the granularity of style transfer, from fine textures to more global structures.

  4. Perceptual Quality: The synthesized images in this paper maintain the global arrangement of the original photograph while adopting the colors and local structures of the artwork, resulting in images that perceptually resemble the style of the artwork while retaining the content of the photograph.
  
## Experiments
  This paper describes a new approach to image synthesis that allows for the mixing of content and style from different sources for the study of visual perception and the characterization of neural representations. The method uses CNN to extract features of an image and compute independent representations of its content and style. By optimizing the loss function, new images with specific content and style can be generated. This method has great potential for applications in experimental studies of visual perception, functional imaging and neural recording. Also, the method provides an algorithmic understanding that neural representations of the nervous system can independently capture the appearance and presentation of an image.

## Conclusion
  This paper lists many research papers and experimental results related to deep learning, including research results in image classification, face recognition, neural network structure, and so on. These research results not only promote the development of artificial intelligence technology, but also provide an important reference for us to better understand the human visual system. Meanwhile, this paper also introduces some algorithms and techniques for image processing, such as texture synthesis, style migration, etc., which are also widely used in the field of digital art creation.

  

