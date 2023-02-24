# Tokenizing a Wikipedia article text and displaying the 30 most common words in it
from nltk.tokenize import WordPunctTokenizer
import requests
from collections import Counter

# This function returns the raw text of a Wikipedia page given its page title
def wikipedia_page_tokenizer(title):

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

text = wikipedia_page_tokenizer('Inter Milan')
tokens = WordPunctTokenizer().tokenize(text)
print(Counter(tokens).most_common(30))