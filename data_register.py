from createList import createList
from database import createDatabase
from text import fetchdata
from database import saveDatabase


# Aşağıdaki satırlar kaynaktan çekilen verileri etiketleyerek database kayıt eder.
def register():
    createDatabase() #boş bir database tablosu olusturur

    text=fetchdata() #kaynaktan dataları çeker

    liste=createList(text) #metini cümlelere ve kelimelere böler,kelimeleri ögelerine göre etiketler.

    saveDatabase(liste) #etiketlenen metni database kaydeder.


