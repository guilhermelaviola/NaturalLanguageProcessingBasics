# Generating text based on Wikipedia article and Project Gutenberg website
# and creating a WordCloud ot of it
import requests
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

# This function returns the raw text of a Wikipedia page given its page title
def wikipedia_page(title):

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

# Setting lower to avoid having to deal with uppercase words
text = wikipedia_page('Inter Milan').lower()
print(text)

# Getting the book link and displaying its content
result = requests.get('https://www.gutenberg.org/cache/epub/164/pg164.txt')
print(result.text)

wordcloud = WordCloud(
    random_state = 8,
    normalize_plurals = False,
    width = 600,
    height = 300,
    max_words = 300,
    stopwords = [])

wordcloud.generate(text)
# Transforming the text into a list of words
words_list = text.split(' ')

# Defining the stopwords manually
stopwords = ['the', 'of', 'and', 'is', 'to', 'in', 'a', 'from', 'by', 'that', 'with', 'this', 'as', 'an', 'are', 'its', 'at', 'for']

words_without_stopwords = ['the', 'of', 'and', 'is', 'to', 'in', 'a', 'from', 'by', 'that', 'with', 'this', 'as', 'an', 'are', 'its', 'at', 'for']

# Transforming the text into a list of words
# by splitting over the space character ' '
word_list = text.split(' ')

# Counting the words
word_count = Counter(word_list)

# Counting the 20 most used words in the text
Counter(words_without_stopwords).most_common(20)

# Instantiating a new WordCloud
wordcloud = WordCloud(
    random_state = 8,
    normalize_plurals = False,
    width = 600,
    height = 300,
    max_words = 300,
    stopwords = [])

# Transforming the list of words into a String
text_without_stopwords = ' '.join(words_without_stopwords)

# Applying the wordcloud to the Wikipedia text
wordcloud.generate(text)

# Plotting the WordCloud
fig, ax = plt.subplots(1,1, figsize=(9,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# Displaying the WordCloud
plt.show()