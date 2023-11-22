# ham metni küçük parçalara ayırma uygulaması olarak bilinen tokenize etme işlemi

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from text import text

def sentTokenize(text):
    return sent_tokenize(text)

def wordTokenize(text):
    return word_tokenize(text)
