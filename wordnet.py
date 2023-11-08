#İki kelimenin birbirine olan benzerlik oranını hesaplar

from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
kelime_1 = wordnet.synset("Travel.v.01") 
kelime_2 = wordnet.synset("Walk.v.01")
print('Benzerlik: ' + str(kelime_1.wup_similarity(kelime_2)))