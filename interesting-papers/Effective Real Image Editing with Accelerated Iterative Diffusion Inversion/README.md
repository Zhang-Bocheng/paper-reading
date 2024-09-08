# Effective Real Image Editing with Accelerated Iterative Diffusion Inversion
[paper link](https://arxiv.org/pdf/2309.04907) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper explores how to effectively edit and manipulate natural images and presents a new method called AIDI.          |  Diffusion Model        |

## Methodology

### 1. Abstract
The method uses a novel hybrid bootstrapping technique that enables high-quality reconstruction results without the need for free bootstrapping with a large number of classifiers. In addition, AIDI exhibits higher robustness in fast image editing compared to other diffusion inversion based work. The method significantly improves the reconstruction accuracy by accelerating the iterative diffusion inversion process with little additional overhead in terms of space and time complexity.

### 2. Method Description 
This paper proposes a diffusion model based image generation method called AIDI (Accelerated Iterative Diffusion Inversion). The method uses a pre-trained text-to-image diffusion model with an acceleration technique to improve reconstruction accuracy and stability during the iteration process. In addition, to achieve better editing results, a hybrid guidance method is introduced, in which pixels in the editing region use a larger guidance scale, while other regions remain unchanged.

![image](https://github.com/user-attachments/assets/d21a71e2-30f7-4e87-b811-078f9da3594c)

### 3. Methodological improvements
Compared with the traditional DDIM sampling process, the AIDI method proposed in this paper employs a more efficient iterative solution to better control the editing effect and improve the editing quality. Meanwhile, by introducing the hybrid guidance method, more delicate editing operations can be achieved, which further improves the quality of image editing.

### 4. Issues addressed 
The AIDI method proposed in this paper solves some problems in traditional image editing methods, such as unstable reconstruction results and difficult to control editing effects. By using the hybrid guidance method, more precise editing operations can also be achieved, thus satisfying the users' needs for high-quality image editing.

## Experiments
This paper focuses on the application of the Stable Diffusion model to image editing and conducts several comparative experiments to verify its performance and effectiveness.

Firstly, the authors conducted a reconstruction test using 5000 images from the COCO test set to evaluate the performance of AIDI by comparing the reconstruction accuracy with different textual cues. The results show that AIDI can significantly improve reconstruction accuracy compared to simple backpropagation, and that AIDI is capable of approximate backpropagation when there is no classifier free guidance. In addition, the authors compare other related techniques, including PTP, NTI and EDICT, and show that AIDI outperforms these methods.

Secondly, the authors performed a quantitative evaluation by conducting a set of experiments using the AFHQ dataset, converting dogs to cats as the target task. The authors used metrics such as LPIPS and FID to assess editing quality and consistency and compared them with other methods. The results show that AIDI performs best in this task, maintaining high quality output even with only 10 editing steps.

![image](https://github.com/user-attachments/assets/d928bf7e-7bc1-496d-8214-f7df26198df9)

In addition, the authors explore the robustness of AIDI with a small number of editing steps and compare it with other methods. The results show that AIDI maintains high quality with fewer editing steps, while the other methods show significant degradation.

Finally, the authors also discuss how random editing can be used to improve editing results. They find that in some cases, random editing can improve the quality of editing results, especially in the case of failure. The authors also provide results of quantitative analyses that demonstrate the effectiveness of random editing. 

![image](https://github.com/user-attachments/assets/64f1515a-643b-46b3-9ba1-0542ff96ebf0)

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents an Accelerated Iterative Diffusion Inversion Algorithm (AIDI) for improving image reconstruction and editing accuracy, and significantly improves the balance between computational efficiency and quality.
  
  2. AIDI makes image editing more accurate and efficient by using trans-attentional mappings to guide the editing regions and editable content.
  
  3. In addition, AIDI provides detailed information about edit controls for better control of editable regions. Although the method relies on auxiliary masks or hints to specify editable regions and content, its logically setup hints have little effect on the results and thus remain promising for application.
 
### 2. Future Works
  1. Future research directions include further improving the AIDI algorithm to increase its stability and accuracy, as well as applying it to a wider range of image processing tasks. It is also possible to explore how AIDI can be combined with other deep learning techniques to achieve higher levels of image processing functionality.
  
  2. Attention also needs to be paid to potential problems that AIDI algorithms may have, such as potential biases and errors, and how these can be addressed. In conclusion, the AIDI algorithm provides a new idea and tool in the field of image processing, which is expected to play an important role in future research and practice.  
