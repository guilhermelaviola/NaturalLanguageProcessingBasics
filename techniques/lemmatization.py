# Tokenization and Lemmatization example with SpaCy
import spacy

nlp = spacy.load('en_core_web_sm')

# Text example
doc = nlp('The quick brown fox \t jumps over the lazy dog.')

# Displaying the tokens and whether they are spaces,
# punctuations, uppercase, digit or stopwords or not
for token in doc:
    print(token, token.is_space, token.is_punct, token.is_upper, token.is_digit, token.is_stop)

# Manipulating the Lemmatization
for token in doc:
    print(f'(token.text) \t (token.lemma_)')

# Part-of-the-speech tagging. In other words, it checks whether each of
# the tokenized words are verbs, nouns, adverbs, adjectives, etc...
for token in doc:
    print(f'(token.text) \t (token.pos_)')