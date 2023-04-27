# Imports relevant modules
import re

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords

from functions import return_labels, clean_text
from sklearn.model_selection import train_test_split

file = 'CSAT-vus-labelled.xlsx'
row_start = 'A'
row_end = 'F'
row_string = row_start + ':' + row_end
column_names = ['Comments', 'Service', 'Able', 'Solution',
                'Cat', 'Notes']

"""Reads a file using custom columns and names them with a 
given set of names in the form of a list"""
data = pd.read_excel(file, usecols=row_string,
                     names=column_names)

data = data.iloc[:433]
data['Cat'] = data['Cat'].replace(np.nan, 'N')

"""The function label data returns data associated with a particular category
T = technology
J = Journey
I = Information
A = Amount
C = Communication

Returns a data frame that has a list of boolean values indicating if it belongs to the category."""
data['journey'] = return_labels(data, 'J')
data['tech'] = return_labels(data, 'T')
data['info'] = return_labels(data, 'I')
data['amount'] = return_labels(data, 'A')
data['comm'] = return_labels(data, 'C')

data.drop(columns=['Cat', 'Able', 'Solution', 'Notes'], inplace=True)

data['Comments'] = data['Comments'].apply(clean_text)

X = data.Comments
y = data.journey

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
               ])
nb.fit(X_train, y_train)

from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay

y_pred = nb.predict(X_test)

print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred, target_names=['Journey Comment', 'Not Journey Comments']))
ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred)).plot()
plt.show()

# with pd.ExcelWriter('CSAT_with_labels.xlsx', engine='openpyxl') as writer:
#     data.to_excel(writer, sheet_name='data')
