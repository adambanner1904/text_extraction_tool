# Imports relevant modules
import pandas as pd
from functions import label_data

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

"""The function now returns data associated with a particular category
T = technology
J = Journey
I = Information
A = Amount
C = Communication

Returns a data frame that has a list of boolean values indicating if it belongs to the category."""
technical_data = label_data(data, 'T')
technical_data.drop(columns=['index', 'Notes', 'Solution', 'Able', 'Cat'], inplace=True)
print(technical_data.columns, technical_data.shape)


# with pd.ExcelWriter('journey_comments.xlsx', engine='openpyxl') as writer:
#     journey_data.to_excel(writer, sheet_name='Journey')
