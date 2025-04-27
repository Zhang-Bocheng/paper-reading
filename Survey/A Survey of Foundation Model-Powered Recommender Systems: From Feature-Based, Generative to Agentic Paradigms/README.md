# A Survey of Foundation Model-Powered Recommender Systems: From Feature-Based, Generative to Agentic Paradigms
[paper link](https://arxiv.org/pdf/2504.16420) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2025 | This paper is a review of research on applying foundational models in recommender systems.          |  Recommender Systems        |

## Methodology

### 1. Abstract
Traditional recommender systems have relied heavily on task-specific models of user-item interactions and content features. However, the paradigm of recommender systems is changing with the development of Foundation Models (FMs), such as models trained on large-scale data like GPT, LLAMA and CLIP. This paper provides a comprehensive overview of FM4RecSys, including their integration in three paradigms: **feature-based representation enhancement, generative recommendation methods, and agent-based interaction systems**. The article first reviews the data base of RS, from traditional explicit or implicit feedback to multimodal content sources. It then describes FM and its capabilities for representation learning, natural language understanding, and multimodal reasoning in the context of RS. The core section discusses how RS can be enhanced by feature-based paradigms (improved feature representation), generative paradigms (direct generation of recommendations or relevant content), and agent-based paradigms (implementation of autonomous recommendation agents and simulators.) Subsequently, the authors explore the application of FM to a variety of recommendation tasks, e.g., Top-N recommendation, sequential recommendation, zero/few samples scenarios, conversational recommendation, and novel content generation. 

By analyzing recent research, the authors highlight some of the key opportunities that have been realized (e.g., improved generalization, better interpretability, and inference), while also pointing out some of the challenges encountered (e.g., cross-domain generality, interpretability, fairness, and multimodal integration). Finally, the authors outline open research directions and technical challenges for the next generation of FM4RecSys, such as multimodal recommender agents, retrieval enhancement frameworks, lifelong learning to deal with long sequential users, efficiency and cost issues. This paper not only reviews the current state-of-the-art approaches, but also critically analyzes the trade-offs among the three paradigms of feature-based, generative, and agent-based approaches, and identifies key unresolved issues and future research directions.

![image](https://github.com/user-attachments/assets/f7428cd9-22b3-418c-a767-f2b5c0825839)

### 2. Method Description 
The FM4RECSYS proposed in this paper is an integration method based on three paradigms: **feature, generation and agent**. Among them, the feature paradigm focuses on the matching relationship between user needs and system functions; the generation paradigm focuses on automatically generating content that meets user needs; and the agent paradigm realizes the satisfaction of user needs through an agent mechanism. These paradigms can be realized by different technical means, such as rule engines, template filling, natural language processing, etc.

![image](https://github.com/user-attachments/assets/708cd8ee-b3bf-4a5c-9381-4731e5e01dc5)

### 3. Methodological improvements
Compared with the traditional single-paradigm approach, FM4RECSYS adopts a combination of multiple paradigms, which can better satisfy the diversified needs of users and can be adapted to applications in different scenarios. In addition, the method is scalable and flexible, and can be adjusted and optimized according to specific application scenarios.

### 4. Issues addressed 
The traditional single-paradigm approach has limitations when facing complex user requirements, making it difficult to provide comprehensive services. FM4RECSYS, on the other hand, is able to understand user needs more accurately and provide personalized services by integrating the three paradigms of features, generation and agents. This approach has a wide range of application areas, including recommender systems, intelligent customer service, smart homes, and other fields.

## Experiments
This paper focuses on three different approaches to recommender systems using base models: **feature-based recommender systems, generative recommender systems, and agent-based recommender systems**, and provides a detailed discussion and comparative analysis of each approach.

**In feature-based recommender systems**, the base model is used as a high-quality feature extractor for generating embedding vectors for users and items. This approach takes advantage of pre-trained knowledge to improve representation quality and facilitate task performance. However, this approach lacks dynamic adaptability and interaction capabilities, limiting its application in complex environments.
![image](https://github.com/user-attachments/assets/0cd4860b-c578-4d54-82d7-32cef7373888)

**Generative recommender systems** redefine the recommendation problem as an end-to-end natural language generation problem. This approach exploits the intrinsic generative power of the underlying model and can handle personalized recommendations in zero- or few-sample situations. However, the approach suffers from challenges such as output control and consistency with user intent, which need to be addressed to ensure its utility.

![image](https://github.com/user-attachments/assets/a60f6814-ba08-403d-8667-2e9e9edd0e36)

**Agent-based recommender systems** view the recommender system as an autonomous intelligence with the ability to reason, reflect, and use tools. This approach can enhance the real-time responsiveness and user experience of recommender systems through multiple rounds of dialog, feedback, and external tools. However, the complexity of the approach poses challenges in terms of scalability and real-time performance. 
![image](https://github.com/user-attachments/assets/3f136b0f-a463-443c-9c4c-07069ee28a40)

## Conclusion

### 1. Advantages of the Thesis
  1. The authors describe in detail different types of recommendation tasks and their applicable base models, and illustrate the advantages of these models in enhancing recommendation system capabilities.
  2. In addition, the article explores the challenges and opportunities of the underlying models in terms of online deployment, enhanced recommender system capabilities, technical scalability and efficiency, and methodological improvements.

### 2. Innovative points
  1. The main contribution of this article is to systematically summarize the research progress of FM4RecSys, while pointing out the challenges and future research directions in the field. By deeply analyzing different types of recommendation tasks and their applicable underlying models, the article reveals the advantages of these models in enhancing the capabilities of recommendation systems.
  2. And, the article explores the challenges and opportunities of the underlying models in terms of online deployment, enhancement of recommender system capabilities, technical scalability and efficiency, and methodological improvements. 

### 3. Future Works
In the future, it can expect that more research will be based on base models to improve the performance and effectiveness of recommender systems. 
  1. In online deployment, more efficient technical solutions can be explored to reduce latency and cost; in enhancing the capability of recommender systems, techniques such as multimodal data and reinforcement learning can be combined to further improve the personalization and diversity of recommender systems; 
  2. In terms of technical scalability and efficiency, more efficient training and inference algorithms can be developed to adapt to the needs of large-scale data and complex scenarios; 
  3. And in terms of methodology improvement, interpretive and inference algorithms can be further explored. improvement, issues such as interpretability and trust can be further explored to improve users' trust and acceptance of recommendation results.
