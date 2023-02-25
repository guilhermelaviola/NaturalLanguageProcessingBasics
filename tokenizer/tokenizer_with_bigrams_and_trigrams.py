# Basic example of Tokenizer with bigrams and trigrams
from nltk import ngrams
from nltk.tokenize import WordPunctTokenizer
from collections import Counter

# Text example
text = "Là in mezzo al campo c'è un nuovo campione. È un tiro che parte"\
       + "da questa canzone. Forza non mollare mai!!! AMALA!!! Amala Pazza"\
       +"Inter amala! È una gioia infinita, che dura una vita. Pazza Inter Amala!!!"

# Tokenizing a text
tokens = WordPunctTokenizer().tokenize(text)
print(tokens)

# Splitting the text into characters and displaying the most common characters in the text
char_tokens = [c for c in text]
print(Counter(char_tokens).most_common(10))

# Creating and displaying bigrams
bigrams = [w for w in ngrams(tokens, n=2)]
print(bigrams)

# Creating and displaying trigrams
trigrams = ['_'.join(w) for w in ngrams(tokens, n=3)]
print(trigrams)

# Creating and displaying bigrams with underline
bi_tokens = ['_'.join(w) for w in bigrams]
print(bi_tokens)