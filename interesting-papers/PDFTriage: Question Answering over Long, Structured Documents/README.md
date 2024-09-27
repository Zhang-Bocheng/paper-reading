# PDFTriage: Question Answering over Long, Structured Documents
[paper link](https://arxiv.org/pdf/2309.08872) 
| Year | Introduction                                                         | Research Field                 |
| ---- | ------------------------------------------------------------ | -------------------- |
| 2023 |  This paper explores the problems of large language models when dealing with long structured documents and proposes a new approach called PDFTriage to solve this problem.          | Large Language Models         |

## Methodology

### 1. Abstract
Most existing work answers questions by retrieving relevant context and representing it as plain text, but this approach does not deal well with naturally structured document types such as PDFs, web pages and presentations. Therefore, the authors developed a new approach that can retrieve context based on the structure or content of a document to better answer questions. Experimental results show that this approach is more effective than existing retrieval-enhanced language models, and the authors provide a Q&A dataset containing multiple categories to facilitate further research.

### 2. Method Description 
This paper proposes a document retrieval and Q&A system called PDFTriage, which uses a pre-trained language model (e.g., GPT-3) in combination with structured document metadata to answer user questions about PDF documents. The system is divided into three steps: first, PDF documents are converted to HTML tree structures and structural elements are extracted from them; then the documents are queried using the pre-trained language model to select the desired content; and finally, the answers are generated based on the questions and the retrieved content.

![image](https://github.com/user-attachments/assets/735fbe14-a73a-42db-b43d-e8f60a37200c)

### 3. Methodological improvements
Compared to traditional text retrieval techniques, PDFTriage uses more advanced structured document metadata and pre-trained language models, which enables it to better process various information in PDF documents, including headings, paragraphs, tables, charts, and so on. In addition, PDFTriage also provides a series of functions for different types of document problems, such as table extrapolation, cross-page tasks, etc., which can meet the needs of more practical application scenarios.

### 4. Issues addressed 
PDFTriage solves the problem that traditional text retrieval can not effectively deal with a variety of information in PDF documents, but also to deal with more complex types of document problems. This makes PDFTriage in the actual application of a wide range of applicability and practicality.

## Experiments
This paper focuses on the use of the GPT-3 model for PDF document quizzing and conducts comparative experiments with two other methods. Specifically, the authors use the following three methods:

![image](https://github.com/user-attachments/assets/cb41505e-c1e7-415e-b549-d83041ce9cdb)

**PDFTriage**: this method exploits the structure of PDF documents and the ability of the GPT-3 model to extract answers more accurately. In their experiments, the authors tested a variety of question types and found that PDFTriage outperformed the other two methods.

**Page Retrieval**: this method retrieves the pages that are most similar to the query vector by embedding the PDF page text into the vector space and using a cosine similarity calculation. The text of each page is then fed into the GPT-3 model as context to answer the question. However, this method performs poorly on certain tasks such as classification and text questions.

**Chunk Retrieval**: this method divides the text of the entire PDF file into 100 word chunks and embeds them into a vector space. Then, a cosine similarity calculation is used to retrieve the chunks that are most similar to the query vector. Finally, the text of each block is fed into the GPT-3 model as context to answer the question. However, this approach performs poorly on certain tasks such as classification and text questions. 

![image](https://github.com/user-attachments/assets/7bf6797c-a00b-4864-ae57-8cce9fc23eeb)

## Conclusion

### 1. Advantages of the Thesis
  1. Compared to existing techniques such as page retrieval and block retrieval, PDFTriage performs better in terms of performance and is able to effectively deal with a variety of document lengths and contextual environments.
  
  2. In addition, the paper builds a dataset of approximately 900 human-written questions representing 10 different categories of question types that users may ask, including ‘document structure questions,’ ‘table reasoning questions,’ and ‘Skill questions’ and many other categories.

### 2. Innovative points
  1. The methodological innovation of this thesis is to allow the model to retrieve relevant contexts based on document structure or content, thus solving some of the problems in current document QA approaches based on prefetching strategies.
  
  2. Specifically, the method allows the model to reliably answer some questions that cannot be answered by ordinary/current document QA methods by providing the model with metadata about the document structure and a set of callable retrieval functions.

### 3. Future Works
Directions for future work include the development of multimodal approaches, the incorporation of tabular and graphical information into the GPT-4 question-answering system, and the consideration of question types to be incorporated into the PDFTriage approach to improve its efficiency and effectiveness.   
