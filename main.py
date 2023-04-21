# Imports relevant modules
import pandas as pd

file = 'CSAT-vus-labelled.xlsx'
row_start = 'A'
row_end = 'F'
row_string = row_start + ':' + row_end
column_names = ['Comments', 'Service', 'Able', 'Solution',
                'Cat', 'Notes']


"""I feel like this is going to come in more useful down the line. 
This could split them up by category based upon the current naming
scheme and we can send the relevant people the comments related to their departments. 
Developers get techincal problems. Designers get journey problems. HMRC get amount issues"""
def label_data(data, letter):
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
        labels.append((letter in i))

    """The new data frame with only those where the """
    data['labels'] = labels

    """Return the data with an added column that is true if that row is in the category
    and 0 if it is not. """
    return data


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
