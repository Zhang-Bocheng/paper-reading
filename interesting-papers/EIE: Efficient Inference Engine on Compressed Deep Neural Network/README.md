# EIE: Efficient Inference Engine on Compressed Deep Neural Network
[paper link](https://arxiv.org/pdf/1602.01528) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2016 | This paper presents an energy efficient deep learning inference engine called EIE (Efficient Inference Engine).          | Compressed Algorithm         |

## Methodology

### 1. Abstract
  The paper presents a compression method to compress large deep neural networks (DNNs) into on-chip SRAM by pruning redundant connections and sharing weights.EIE is able to perform efficient inference on such compressed models and accelerate the computation using sparse matrix-vector multiplication. Experimental results show that EIE is 189x and 13x faster on nine DL benchmarks compared to uncompressed CPU and GPU implementations, respectively. In addition, EIE is more energy efficient than CPUs and GPUs, capable of processing 18,800,000 frames per second while processing AlexNet's fully-connected layer with a power consumption of only 600 milliwatts.

  ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/7027fb44-1e1c-49b9-bc0c-ea99f3f13203)

### 2. Method Description 
  The method is mainly implemented through the following steps:

  1. The NN is compressed using deep compression techniques to reduce the size of the weight matrix.
  
  2. The sparse weight matrix is stored in a data structure called interleaved compressed sparse column (ICSC) to utilize dynamic activation sparsity and static weight sparsity.
  
  3. The input vectors are loaded element by element into each processing element (PE) and the output vectors are computed using sparse matrix multiplication inside the PE.
  
  4. Only non-zero elements are considered during the computation and the first non-zero element is selected using distributed leader zero detection logic to further improve computational efficiency.
     
### 3. Methodological improvements
 1. Dynamic activation sparsity and static weight sparsity are utilized to improve computational efficiency.
 
 2. Distributed leader zero detection logic is used, which enables more accurate selection of the first non-zero element and reduces unnecessary computation.

 3. An alternating compressed column data structure is used, allowing sparse matrices to be stored and accessed more efficiently.

### 4. Issues addressed 
  1. The problem of NN running slowly in resource-constrained environments such as mobile devices.
  
  2. The problem of compressing NN to facilitate efficient operation on resource-constrained devices.
  
  3. The problem of how to utilize sparsity to improve computational efficiency.

    ![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/939d4793-ed00-43ce-bd7b-420a3d14c140)

## Experiments
  This paper presents an experimental study designed by the authors for a deep learning gas pedal and compared with three different types of computing devices, including CPUs, GPUs, and mobile GPUs.The experimental results show that the gas pedal excels in both performance and energy efficiency, being several times or even tens of times faster than the other computing devices, and is able to significantly reduce energy consumption. 

**Experimental purpose**: To verify whether the design of the deep learning gas pedal can outperform traditional computing devices in terms of performance and energy efficiency.

**Experimental methodology**: Hardware modules were modeled using a custom C++ simulator with 93% accuracy, and then each hardware module was abstracted into an object and tested in two dimensions: time and energy. In addition, the structure and performance of the gas pedal is analyzed through layout (after place-and-route) and power/area decomposition.

**Comparison experiments**: The deep learning gas pedal was compared with three different computing devices, including Intel Core i-7 5930k CPU, NVIDIA GeForce GTX Titan X GPU, and NVIDIA Tegra K1 mobile GPU. specific experiments are as follows:

  a. **Performance Comparison**: the performance of the compressed network was compared with the performance of the uncompressed network in nine benchmarks. The experimental results show that the deep learning gas pedal is on average 189 times faster than the CPU, 13 times faster than the GPU, and 307 times faster than the mobile GPU in all tests.

  b. **Energy Efficiency Comparison**: Again, the energy efficiency of the compressed network was compared to the energy efficiency of the uncompressed network in nine benchmark tests. The results show that the Deep Learning Accelerator saves an average of 24,000x energy over the CPU, 3,400x energy over the GPU, and 2,700x energy over the mobile GPU in all tests.

**CONCLUSION**: Deep Learning Accelerators excel in both performance and energy efficiency, being several or even tens of times faster than traditional computing devices, and significantly reducing energy consumption. This makes deep learning gas pedals ideal for processing real-time data.

![image](https://github.com/Zhang-Bocheng/paper-reading/assets/160409071/d249170c-04aa-45ff-a4d5-be65dfc4e7b1)

## Conclusion

### 1. Advantages of the Thesis
 1. This paper proposes a high-performance gas pedal, EIE, for Dnns and experimentally verify its superiority in terms of performance and energy consumption.
 
 2. The gas pedal employs compression techniques and storage optimization strategies, which can significantly reduce the memory bandwidth requirement and energy consumption overhead, while improving the computational efficiency.
 
 3. In addition, the paper proposes three different matrix chunking schemes and provides a detailed comparison and evaluation of them for practical applications.

### 2. Innovative points
  1. The main contribution of this paper is to propose a high-performance gas pedal based on compression technique and combining several optimization strategies to improve computational efficiency and reduce energy overhead.
  
  2. The compression technique  can reduce the model size to less than one-tenth of the original size by processing the weights and activation values such as quantization and sharing, thus reducing the memory bandwidth requirement and energy consumption overhead.
  
  3. In addition, the paper proposes three different matrix chunking schemes and provides a detailed comparison and evaluation of them for practical applications.

### 3. Future Works
  Future research directions can be carried out in the following aspects: 
  1. continue to explore more efficient compression techniques, such as using fewer bits or more sparsity;
  
  2. second, study smarter matrix chunking strategies to adapt to the needs of different scenarios;
  
  3. and third, combine the optimization at the hardware and software levels to achieve more comprehensive performance improvement.
