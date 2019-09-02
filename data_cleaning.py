# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:52:25 2019

@author: User
"""

filename = "metamorphosis_clean.txt"
file = open(filename, 'rt')
text = file.read()
file.close()
#data cleaning manualyy
#tokenization
# split into words by white space
words = text.split()
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
#capitalization

stripped = [w.lower() for w in stripped]
#changings words to lower case
print(stripped[:100])


#text data cleaning using nltk
# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print(tokens[:100])

#remove punctuation
# remove all tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]
print(words[:100])

#removing stopwords stemming
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)


