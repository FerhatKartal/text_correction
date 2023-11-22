#metinde herhangi bir önemi olmayan kelimeleri çıkarma

from nltk.corpus import stopwords
stop_words = list(stopwords.words('turkish'))

def stopWords(word):
    if(stop_words.__contains__(word)):
        return False
    else:
        return True