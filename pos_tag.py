#cümlemizdeki özel isimleri, sıfatları vb. bulur

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from text import text

kelimeler = word_tokenize(text)

tagged = nltk.pos_tag(kelimeler)
print(tagged)