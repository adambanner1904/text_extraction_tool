# Imports relevant modules
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from functions import return_labels, clean_text, add_columns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay

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

# Selecting all the labelled data
data = data.iloc[:433]

# Replacing the ones that fit no category with U for undefined/useless
# This can be used to get rid of irrelevant comments
data['Cat'] = data['Cat'].replace(np.nan, 'U')

"""The function label data returns data associated with a particular category
T = technology
J = Journey
I = Information
A = Amount
C = Communication

Returns a data frame that has a list of boolean values indicating if it belongs to the category."""
data = add_columns(data)

data.drop(columns=['Cat', 'Solution', 'Notes'], inplace=True)

data['Comments'] = data['Comments'].apply(clean_text)


# Input is the comment and output is the
# label of whether it belongs to that category or not.
X = data.Comments
y = data.c

# Splitting the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)


# model = SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=2, max_iter=5, tol=None)
model = RandomForestClassifier(n_estimators=200, random_state=42)

sgd = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', model),
               ])

# Fit the model
sgd.fit(X_train, y_train)

# Test the model
y_pred = sgd.predict(X_test)


print(classification_report(y_test, y_pred, target_names=['Positive', 'Negative']))
ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred)).plot()
plt.show()

# with pd.ExcelWriter('CSAT_with_labels.xlsx', engine='openpyxl') as writer:
#     data.to_excel(writer, sheet_name='data')
