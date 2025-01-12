# -*- coding: utf-8 -*-
"""NLP_Basics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C4GhlvPGwwKHEBDGQc2vmsgxcE7f1k7a
"""

! pip install nltk

paragraph = " Narendra Damodardas Modi (Gujarati:; born 17 September 1950)[a] is an Indian politician who is the 14th and current Prime Minister of India since 26 May 2014. Modi was the chief minister of Gujarat from 2001 to 2014 and is the Member of Parliament (MP) for Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right wing Hindu nationalist paramilitary volunteer organisation. He is the longest-serving prime minister outside the Indian National Congress.[3]Modi was born and raised in Vadnagar in northeastern Gujarat, where he completed his secondary education. He was introduced to the RSS at the age of eight. At the age of 18, he was married to Jashodaben Modi, whom he abandoned soon after, only publicly acknowledging her four decades later when legally required to do so. Modi became a full-time worker for the RSS in Gujarat in 1971. The RSS assigned him to the BJP in 1985 and he rose through the party hierarchy, becoming general secretary in 1998.[b] In 2001, Modi was appointed Chief Minister of Gujarat and elected to the legislative assembly soon after. His administration is considered complicit in the 2002 Gujarat riots,[c] and has been criticised for its management of the crisis. According to official records, a little over 1,000 people were killed, three-quarters of whom were Muslim; independent sources estimated 2,000 deaths, mostly Muslim.[12] A Special Investigation Team appointed by the Supreme Court of India in 2012 found no evidence to initiate prosecution proceedings against him.[d] While his policies as chief minister were credited for encouraging economic growth, his administration was criticised for failing to significantly improve health, poverty and education indices in the state."

paragraph

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

##Tokenization: Convert paragraph-sentences-words
nltk.download('punkt')
sentences = nltk.sent_tokenize(paragraph)

sentences

type(sentences)

stemmer = PorterStemmer()

stemmer.stem('history')

from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

import nltk

# Downloading the necessary resources
nltk.download('wordnet')
nltk.download('omw-1.4')

# Now you can use wordnet without issues
from nltk.corpus import wordnet as wn

# # Example usage
# syns = wn.synsets("program")
# print(syns)

lemmatizer.lemmatize('history')

len(sentences)

import re

corpus = []
for i in range(len(sentences)):
  text = re.sub('[^a-zA-Z]',' ',sentences[i])
  text = text.lower()
  corpus.append(text)

corpus

nltk.download('stopwords')

stopwords.words('english')

## Stemming:
for i in corpus:
  words=nltk.word_tokenize(i)
  for word in words:
    if word not in set(stopwords.words('english')):
      print(stemmer.stem(word))

for i in corpus:
  words=nltk.word_tokenize(i)
  for word in words:
    if word not in set(stopwords.words('english')):
      print(lemmatizer.lemmatize(word))

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()

X = cv.fit_transform(corpus)

cv.vocabulary_

corpus[0]

X[0].toarray()

# Applying Stopwords and Lemmatize:
import re
corpus= []
for i in range(len(sentences)):
  text = re.sub('[^a-zA-Z]',' ',sentences[i])
  text = text.lower()
  text = text.split()
  text = [lemmatizer.lemmatize(word) for word in text if not word in set(stopwords.words('english'))]
  text = ' '.join(text)
  corpus.append(text)

corpus

