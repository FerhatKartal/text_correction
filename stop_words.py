#metinde herhangi bir önemi olmayan kelimeleri çıkarma

from nltk.corpus import stopwords
etkisiz_kelimeler = list(stopwords.words('turkish'))
print(etkisiz_kelimeler)