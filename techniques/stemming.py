# Stemming example
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import PorterStemmer
#from nltk.corpus import stopwords
import numpy as np
import requests
import stopwords

# This function returns the raw text of a Wikipedia page given its page title
def wikipedia_page_stemming(title):

    params = {
        'action': 'query',
        'format': 'json',  # request json formatted content
        'titles': title,  # title of the Wikipedia page
        'prop': 'extracts',
        'explaintext': True
    }

    # Sending a request to the Wikipedia API
    response = requests.get('https://en.wikipedia.org/w/api.php', params=params).json()

    # Parsing the result
    page = next(iter(response['query']['pages'].values()))

    # Returning the page content
    if 'extract' in page.keys():
        return page['extract']
    else:
        return "Page not found"

text = wikipedia_page_stemming('Inter Milan').lower()

# Tokenizing and removing the stopwords from the Wikipedia article
tokens = WordPunctTokenizer().tokenize(text)
tokens = [tk for tk in tokens if tk not in stopwords.words('english')]

# Instantiating a PorterStemmeer
ps = PorterStemmer()

# Stemming
stem = [ps.stem(tk) for tk in tokens]

np.random.choice(stem, size=10)