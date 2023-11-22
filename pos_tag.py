#cümlemizdeki özel isimleri, sıfatları vb. bulur

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from text import text

def posTag(text):
    words = word_tokenize(text)
    tagged = nltk.pos_tag(words)
    return tagged