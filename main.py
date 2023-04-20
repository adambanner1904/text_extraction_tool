# Imports relevant modules
import pandas as pd

file = 'CSAT-vus-labelled.xlsx'
row_start = 'A'
row_end = 'F'
row_string = row_start + ':' + row_end
column_names = ['Comments', 'Service', 'Able', 'Solution',
                'Cat', 'Notes']

def find_cat_from
    """Reads a file using custom columns and names them with a 
    given set of names in the form of a list"""
    data = pd.read_excel(file, usecols=row_string,
                         names=column_names)

    """I have to select a specific range of these 
    ones because I havent done all of the labelling 
    and I switched conventions at index 125. This is 
    specific to this file and to make
    it reproducible the format must be standardised.
    
    It then resets the index to help the iteration"""
    data = data.iloc[125:433].dropna(subset='Cat').reset_index()
    """Creates a series out of the label columns"""
    series = data['Cat']

    """Creates an empty list for the truth values of 
    whether it contains a particular letter"""
    labels = []

    """A loop to go through every row in the series and 
    append the truth value of whether it contains the letter"""

    """For each row in the series"""
    for i in series:

        """Append the value of whether letter is in that row
        (string etc 'JTCIA')"""
        labels.append(('J' in i))

    """The new data frame with only those where the """
    reversed_labels = [not label for label in labels]

    false_data = data[reversed_labels]
    truth_data = data[labels]














# with pd.ExcelWriter('journey_comments.xlsx', engine='openpyxl') as writer:
#     journey_data.to_excel(writer, sheet_name='Journey')