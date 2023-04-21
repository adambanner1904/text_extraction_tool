

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
