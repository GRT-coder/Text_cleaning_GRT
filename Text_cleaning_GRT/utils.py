import re
import os
import sys
import json

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import unicodedata
from textblob import TextBlob

import nltk
from nltk.stem.wordnet import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer

path = os.path.dirname(os.path.abspath(__file__))
stopwords_path = os.path.join((path, 'data','stopwords.txt'))

def _get_word_counts(x):
    word_counts = len(str(x).split())
    return word_counts

def _get_avg_wordlength(x):
	count = _get_charcounts(x)/_get_wordcounts(x)
	return count

def _get_stopwords_counts(x):
	l = len([t for t in x.split() if t in stopwords])
	return l

def _get_char_counts(x):
    s = x.split()
    x = ''.join(s)
    return len(x)

def _get_urls(x):
	urls = re.findall(r"(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?", x)
	counts = len(urls)
	return counts, urls

def _remove_urls(x):
    return re.sub(r"(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?", '', x)


def _remove_special_chars(x):
    x = re.sub(r"[^\w ]+", " ", x)
    x = ' '.join(x.split())
    return str(x)


def _remove_html_tags(x):
    return BeautifulSoup(x, 'lxml').get_text().strip()


def _remove_accented_chars(x):
    x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')


def _remove_stopwords(x):
    stopwords = pd.read_csv(stopwords_path, header=None)
    stopwords = set(stopwords[0])
    return ' '.join([t for t in x.split() if t not in stopwords])


def _remove_digits(x):
    x = re.sub(r"\b\d+\b", " ", x)
    x = ' '.join(x.split())
    return str(x)


def _remove_short_long_words(x):
    x = re.sub(r"(/b[a-z]{1,2}/b)|(/b[a-z]{20,}/b)", " ", x)
    x = ' '.join(x.split())
    return str(x)


def _lemmatize(x):
    lem = WordNetLemmatizer()
    review_words = x.split()
    review_norm = [lem.lemmatize(word) for word in review_words]
    review_norm = " ".join(review_norm)
    return str(review_norm)

def _preprocess_data(x):
    x = x.lower()
    x = _remove_html_tags(x)
    x = _remove_special_chars(x)
    x = _remove_stopwords(x)
    x = _lemmatize(x)
    x = _remove_digits(x)
    x = _remove_short_long_words(x)
    return x