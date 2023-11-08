# ham metni küçük parçalara ayırma uygulaması olarak bilinen tokenize etme işlemi

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from text import text

print(word_tokenize(text))
print(sent_tokenize(text))
