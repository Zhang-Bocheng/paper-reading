# Text2Scene: Text-driven Indoor Scene Stylization with Part-aware Details
[paper link](https://arxiv.org/pdf/2308.16880) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper describes a new method called Text2Scene that automatically creates realistic textures for multiple objects in a virtual scene.          | computer vision         |

## Methodology

### 1. Abstract
The method uses reference images and textual descriptions as a guide to make the generated colours respect semantic segments or hierarchies composed of similar materials by adding detailed textures to labelled 3D geometry in a room. Unlike traditional single-step smoothing stylisation, the method first obtains weak semantic cues from the geometric segmentation and further clarifies the results produced by assigning initial colours to the segmented parts. Then, texture details are added to each object such that their projections on the image space have feature embeddings that match the input embeddings. 

This approach is scalable and can complete the entire process with modest computational resources and memory. Since the framework utilises existing resources for image and text embeddings, there is no need to use datasets with high quality textures, which have been designed by skilled artists. So far, this is the first practical and scalable approach to create detailed and realistic textures that have the desired style and maintain structural context for scenes containing multiple objects.

![image](https://github.com/user-attachments/assets/61067375-c7b6-44a2-b098-0033c54f0388)

### 2. Method Description 
The paper presents a CLIP-based image style transformation method for applying a given target image to objects in a 3D interior scene. The method is divided into two parts for processing: **structural elements (walls, ceilings and floors) and objects (3D models)**. For the structural elements, the colour distribution of the target image is matched using textures already available in the MATch material library, while for the objects, the processing is carried out through the steps of segmentation, colour assignment and detail optimisation.

![image](https://github.com/user-attachments/assets/8c128019-e083-4212-947b-f4afc7d46850)
  
### 3. Methodological improvements
Compared to traditional 3D modelling or texturing techniques, the method employs a simpler and faster technique for image style conversion. In the object part, local texture consistency and overall visual realism are achieved by decomposing into multiple parts and merging them based on similar material properties. In addition, a neural style field (LNSF) is introduced to further refine the local texture and geometric deformation is utilised to produce more realistic results.

### 4. Issues addressed 
The method solves the problem of how to apply a given target image to a 3D indoor scene, enabling the objects in the scene to exhibit a style similar to the target image. It also ensures that the whole scene is stylistically consistent by incorporating the CLIP model. This approach provides a new solution for real-time and efficient 3D scene style transformation.

## Experiments
This paper focuses on Text2Scene, a text-driven 3D scene stylisation method, and evaluates and compares it through several experiments. Specifically, the authors first conduct experiments on individual objects, using multiple types of object models, and demonstrate that the method can generate high-quality textures and discover different part information by testing it on objects of different sizes and classes. The authors then also show the effect of using this method in a room-level scene and provide user evaluation results to further validate its quality.

In the first experiment, the authors compare their method with Text2Mesh, another text-driven 3D stylisation method. They found that since Text2Mesh uses a deformation field to enhance detail changes, it may introduce unwanted noise and does not estimate the boundaries between different parts of an object well. 

In contrast, the authors' method makes use of the obtained partial information and a stylisation scheme of coarse and fine differentiation, which allows for the creation of more realistic textures and the clear assignment of boundaries to the various parts of each object. Additionally, the authors provide a version that does not use two-step stylisation and point out that their partial discovery module and coarse and fine differentiation stylisation scheme are crucial for producing textures with high fidelity and realism.

![image](https://github.com/user-attachments/assets/d8e607ff-7054-4c63-b920-e91f580b2da9)

In the second experiment, the authors demonstrate how Text2Scene can be used to quickly generate textures with a sense of realism to fill a room with multiple objects. They constructed two bedrooms and two living rooms using the same set of objects, and provided a target image It and text describing the desired style to guide the generation process. The results show that the generated textures respect the semantic labels of the various furnishings and contain locally diverse details. 

In contrast to many previous stylisation methods, which distribute subtle variations evenly throughout the scene, the textures generated by Text2Scene are more realistic. In addition, the authors provide results for other input configurations and point out that styles can be easily changed by editing object positions in the 3D scene.

![image](https://github.com/user-attachments/assets/4079aa78-ea67-4968-93dc-724b49c66e95)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a new framework called Text2Scene for generating textures for 3D scenes. The framework is able to handle highly detailed textures for various types of objects, including books or paintings.
  
  2. By exploiting the representation capabilities of pre-trained CLIP models, the framework does not require any 3D dataset with textures or partial annotations.
  
  3. Given a 3D mesh model and class labels or text descriptions for objects, the framework can easily produce stylised results by selecting target images and simple text descriptions. 

### 2. Innovative points
  1. The methodological innovation of this paper is the use of a CLIP-based representation learning technique, which enables fast generation of high-quality visual renderings without a large number of 3D scenes with textures or large memory overheads. Specifically, the method employs a staged strategy, where the input polygons are first split into segments and they are divided according to low-level geometric cues.
  
  2. Then, the solution to the simplification problem, i.e., assigning a colour to each segment, is initiated. Furthermore, the authors propose an additional perturbation term to increase the detailed texture of individual objects and impose constraints on the projected image features, thus enhancing the high-frequency neural fields of the base colour.
     
### 3. Future Works
Future research directions may include: further improving the speed and efficiency of the algorithm; exploring more detailed texture generation methods; expanding to larger-scale scenes and objects; and combining with other deep learning techniques, such as GAN, to achieve higher-level texture synthesis.  
