# Question Answering system for "Trạng Nguyên" in VietNam
  System pineline: Question classification, Information Retrieval and Answer extraction
![pineline](image/pineline.png)
## Question classification:
  Navie Bayes from scikit-learn with ~300 questions to train.
  Accuracy: ~83.3%
  
![confusion_matrix](image/confusion_matrix.jpg)
## Information Retrieval:
  From question, with Lucene libary to caculate distance score between the document from data and the question.  
## Answer Extraction:
  Regular Expression with basic keywords to extract the answer from the document.    .
