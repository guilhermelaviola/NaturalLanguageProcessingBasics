# Generating text from the book Twenty Thousand Leagues under the Sea by Jules Verne
# from Project Gutenberg website
import requests

# Getting the book link and displaying its content
result = requests.get('https://www.gutenberg.org/cache/epub/164/pg164.txt')
print(result.text)