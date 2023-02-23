# Generating text based on Wikipedia articles
import requests

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