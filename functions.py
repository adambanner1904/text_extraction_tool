

"""I feel like this is going to come in more useful down the line.
This could split them up by category based upon the current naming
scheme and we can send the relevant people the comments related to their departments.
Developers get techincal problems. Designers get journey problems. HMRC get amount issues"""
import re

from nltk.corpus import stopwords


def return_labels(data, letter):
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

    """Return a list of whether those comments are related to the topic or not."""
    return labels


def clean_text(text):
    """
        text: a string

        return: modified initial string
    """
    REPLACE_BY_SPACE_RE = re.compile('[/(){}@,;]')
    BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
    STOPWORDS = set(stopwords.words('english'))
    text = str(text)

    text = text.lower()  # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text)  # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text)  # delete symbols which are in BAD_SYMBOLS_RE from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)  # delete stopwors from text
    return text