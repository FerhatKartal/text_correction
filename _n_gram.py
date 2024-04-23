import nltk 
from nltk import word_tokenize
from nltk.util import ngrams


def nGrams(sample,data,n):
    n_return=[]
    token = word_tokenize(sample)
    n_sample = list(ngrams(token, n))

    for i in data:
        token2 = word_tokenize(i)
        n_data = list(ngrams(token2, n))
        for k in n_sample:
            for s in n_data:
                if(s==k and n_return.__contains__(s)==False):
                    n_return.append(s)

    return n_return

