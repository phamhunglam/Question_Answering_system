# importing necessary libraries 
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# loading the iris dataset
# iris = datasets.load_iris()
df = pd.read_csv('QA.csv')
# X -> features, y -> label
X = df['QA']
y = df["labels"]


# dividing X, y into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.3)

# training a Naive Bayes classifier
from sklearn.naive_bayes import MultinomialNB

vect = CountVectorizer().fit(X_train)
X_train_vectorized = vect.transform(X_train)
# print(X_train_vectorized)
clfrNB = MultinomialNB(alpha = 0.1)
clfrNB.fit(X_train_vectorized, y_train)
preds = clfrNB.predict(vect.transform(X_test))
# accuracy on X_test
accuracy = clfrNB.score(vect.transform(X_test), y_test)
# print("accuracy: "+ str(accuracy))
#
# # creating a confusion matrix
# cm = confusion_matrix(y_test, preds)
# print(cm)
# test = clfrNB.predict(vect.transform(X_test[0]))
# print(test)
qestion = 'Lưu Danh Công đỗ năm nào?'
# result = clfrNB.predict(vect.transform([qestion]))
result = clfrNB.predict_proba(vect.transform([qestion]))
# result = result*100
# result = pd.DataFrame(result)

# print(qestion)
# print('pred_label: '+ result[0])
print(result)