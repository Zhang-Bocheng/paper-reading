# Stack-and-Delay_ a new codebook pattern for music generation
[paper link](https://arxiv.org/pdf/2309.08804) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 | This paper introduces a new approach to music generation, the stack-and-delay decoding strategy (STACK-AND-DELAY).          |  Transformer        |

## Methodology

### 1. Abstract
Traditional music generation models use a flat codebook representation to generate waveform sequences, but this decoding method is slow. The stack-and-delay decoding strategy proposed by the authors improves the decoding speed by a factor of four while guaranteeing the same quality, and allows for faster inference on the GPU in small batches. Experimental results show that the method performs better than the traditional delay mode and is almost comparable to the flat mode for the same inference efficiency budget. In addition, subjective evaluations also show that samples generated using the new model are selected more often than competitor models.

### 2. Method Description 
The paper focuses on an encoder-decoder model and its corresponding codebook model for music generation tasks. Specifically, by converting text descriptions into sequential text embeddings and feeding them as conditional signals into an autoregressive Transformer decoder, the model generates an audio waveform consisting of a stack of EnCodec tokens. In this case, EnCodec is a hierarchical token system used to represent the audio signal, which is obtained by a CNN autoencoder that computes its embedding vectors and quantises them. In addition, the paper proposes three different codebook modes: **delayed mode, stacked mode and stacked delayed mode** to optimise the performance and inference time of the model.

![image](https://github.com/user-attachments/assets/e4e3b83e-2679-49e0-9a56-fc4c57ccb3d8)

### 3. Methodological improvements
Unlike the traditional method of representing audio based on individual tokens, this paper uses a hierarchical token system to represent the audio signal, which enables the model to better capture the hierarchical structure information in the audio signal. In addition, the paper proposes three different codebook patterns that can improve the performance and inference efficiency of the model by adjusting the decoding order and number of steps.

### 4. Issues addressed 
The main goal of the thesis is to develop an efficient and accurate music generation model to meet the modern demand for high quality music. To this end, this paper proposes an encoder-decoder model based on a hierarchical token system and designs three different codebook patterns to optimise the performance and inference time of the model. Through experimental verification, the model proposed in this paper performs well in terms of both sound quality and inference speed, and has good application prospects.

## Experiments
This paper presents an experimental study of the MusicGen model, including the experimental setup, generation method, dataset, and evaluation metrics, and verifies the effectiveness of different models through several comparative experiments.

Firstly, the authors used the EnCodec model as a Tokenizer to encode 32 kHz mono audio into a set of four tokens, each corresponding to 20 ms (50 Hz frame rate) of audio information.The Transformer decoder was implemented by a customised version of audiocraft, using Pytorch 2.02 Flash Attention for training and generation to optimise memory footprint and speed up the training process. The model was trained for 200 epochs (400k steps) on a randomly cropped full repertoire using the AdamW optimiser with β1 = 0.9, β2 = 0.95, a cosine learning rate schedule with an initial learning rate of 0.0001 and a final learning rate of 0.00001, a batch size of 192, a weighting decay is 0.1, and the gradient is not truncated. The training process uses fp16 mixed precision and distributed data parallelism techniques and runs on 24 A100 GPUs.

Second, the authors explored the generation method in a variety of ways. At each decoding step, the Transformer decoder outputs a probability distribution that is used to select the time step and level to decode according to the decoding plan.Token is obtained based on distribution sampling, which uses a top-k core sampling method with k = 250 and a temperature of 1.0.In addition, a free guide for classification in the no-text condition is applied, using a guide guidance scalar with a scale of 3.0.

![image](https://github.com/user-attachments/assets/ad0fbe4a-9ba0-47e4-bbd2-396aa3c87e82)

Next, the authors compare three different codebook modes: flat, stack, and stack-delay. of these, the flat mode produces the highest quality audio but requires more computational resources, while the delay mode is a better compromise for real-time streaming with an RTF close to 1. The stack mode is a novel alternative to the scheme with comparable quality to flat mode and even outperforms flat mode in terms of FAD scores. stack-delay mode further improves the efficiency of stacking mode while maintaining similar RTF values, which can unlock better real-time streaming scenarios.

![image](https://github.com/user-attachments/assets/d10c3bfc-cce7-4e9b-a58d-e7f2db42bda4)

Finally, the authors also tried four different decoding time-step scheduling schemes, and the results show that as the number of time-step separations between neighbouring locations increases, the FAD scores are lower, and the KLD and CLAP scores fluctuate within a similar range. This demonstrates the benefit of aligning the time steps. If there is no alignment and only the same time-step order as for DELAY is followed, the STACK-DELAY model achieves only minor improvements. In addition, the authors attempted to apply the permuted time-step scheduling scheme to the DELAY mode, but the performance was only at the benchmark level, implying that the combination of the proposed stacking mode and the permuted decoding time-step scheduling scheme is crucial to obtain better performance.

## Conclusion

### 1. Advantages of the Thesis
  1. This paper presents a new codebook model that stacks music tokens and delays/offsets subsequent levels of decoding, and decodes them in a decoding scheme arranged in time steps. This combination outperforms the delayed baseline quality aspect with the same inference efficiency budget and a 45% reduction in in-domain FAD, as parallel decoding compensates for the increased sequence length.
  
  2. Furthermore, this paper shows that stacked tokens should be preferred to flattened tokens when highest quality is the priority.
  
  3. Finally, the disambiguation study shows that time-step alignment is critical for achieving optimal performance, suggesting that decoding neighbouring positions with only partial knowledge of the previous time-step may affect the performance of delayed patterns.

### 2. Innovative points
  1. The stacked-delay pattern proposed in this paper is able to generate music at the same rate as the original delay pattern, but with significantly higher quality. By inheriting the quality of the flat mode, the mode is able to reduce the past key/value streaming cache footprint during inference, resulting in faster and more memory-efficient performance.
  
  2. In addition, this paper proposes a new decoding scheme involving interleaved decoding of locations that prevents the model from decoding neighbouring locations before they have sufficient context.

### 3. Future Works
In the future, the model still needs further research and improvement, such as how to better handle the decoding order and how to optimise the training process of the model. Meanwhile, the results in this paper can also be applied to other fields, such as natural language processing and computer vision.    
