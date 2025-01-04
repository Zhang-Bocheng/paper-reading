# Learning the Geodesic Embedding with Graph Neural Networks
[paper link](https://arxiv.org/pdf/2309.05613) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper presents a graph neural network-based learning method for computing the approximate geodesic distance between any two points on a discrete polyhedral surface.          | Graph Neural Network (GNN)        |

## Methodology

### 1. Abstract
The method features constant time complexity and fast preprocessing compared to previous related methods, and can learn the embedding vectors of the input mesh in a high-dimensional embedding space to compute the geodesic distance between two points using a lightweight decoding function. The authors propose novel graph convolution and graph pooling modules to fuse local geodesic information and demonstrate that they are more efficient than previous designs. Experimental results show that the method is several orders of magnitude faster than existing methods on ShapeNet while achieving comparable or better accuracy.

![image](https://github.com/user-attachments/assets/06f4880b-e736-4674-99cd-c3b2374efc3d)

### 2. Method Description 
This thesis presents an efficient and accurate method for computing geometric distances based on GNN. The method consists of two main parts: precomputation and geometric distance query (GDQ). In the pre-computation phase, for a given input mesh, a graph neural network is used to extract high-dimensional feature vectors for each vertex and store them for subsequent queries. In the geometric distance query phase, the geometric distance between two vertices is predicted by passing the power difference between them to a fixed-size multilayer perceptron. This process has a constant time complexity and thus can handle a large number of geometric distance query requests in a very short time.

![image](https://github.com/user-attachments/assets/8f069e12-051d-4612-8f03-dce50e62abba)

### 3. Methodological improvements
The main improvement of the method over the previously proposed graphical convolution-based method for computing geometric distances is the introduction of a new graphical pooling module, GeoPool, which is able to efficiently take into account the relationship between Euclidean and curvature distances, thus improving the accuracy of geometric distances. In addition, the method employs the learning of decoding functions, which makes the prediction results more accurate and reliable.

### 4. Issues addressed 
The method solves the problem of efficiency and accuracy in calculating geometric distances. While traditional methods for calculating geometric distances usually take a lot of time and computational resources, the method is able to handle a large number of geometric distance query requests in a short period of time and provide more accurate results. This has important application value for large-scale 3D model processing, computer vision and other fields.

## Experiments
This paper focuses on the application of GEGNN in computing geometric distance queries and verifies its performance and advantages through a series of comparative experiments. Specifically, the authors conducted experiments in the following four areas:

The efficiency and accuracy of GEGNN in computing geometric distance queries are verified. The authors used a subset of the ShapeNet dataset to train the model and tested it. They compared the results with classical geometric distance algorithms, including methods such as MMP, HM, DGG, EEM, and FPGDC. The results show that GEGNN is faster and more accurate than other methods.

![image](https://github.com/user-attachments/assets/610a5eb5-7ff4-4021-bb06-00ae98808f0d)

The effects of different design modules were compared. The authors compared the designs of graph convolution, graph pooling and decoding functions to verify their effectiveness. The results show that the graph convolution module of GEGNN is more effective than other graph convolution methods.

![image](https://github.com/user-attachments/assets/af14c80e-5806-41e0-ba36-1589287202f8)

The effectiveness of GEGNN in practical applications is demonstrated. The authors demonstrate the application of GEGNN in texture mapping, shape matching and computing geometric paths. These applications demonstrate the feasibility and effectiveness of GEGNN in practical applications.

## Conclusion

### 1. Advantages of the Thesis
  1. Shortest path queries with constant time complexity are implemented, making the method applicable to large-scale polygonal meshes.
  2. A novel graph convolution module and graph pooling module are proposed to enhance the learned geometric embedding.
  3. A learnable distance function is used to map embedded features to shortest path distances, resulting in a significant improvement in approximation accuracy.

### 2. Innovative points
  1. The introduction of local distance features and an adaptive graph pooling module to better capture local geometric structures in polygonal meshes.
  2. Improved approximation accuracy by using a lightweight multilayer perceptron as a learnable distance function that maps embedded features to shortest path distances. 

### 3. Future Works
  1. Exploring the learning of other geometric distances, such as the bi-harmonic distance, and training a single generic model for all geometric distance computations.
  2. Apply graph neural networks to solve other geometric optimisation problems such as shape deformation, resampling and parameterisation.
  3. Apply transformer on polygonal meshes to replace graph neural networks and improve performance.    
