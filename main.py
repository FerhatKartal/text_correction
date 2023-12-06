from text import text
from database import createDatabase,saveDatabase
from createList import createList



createDatabase() #boş bir database tablosu olusturur

liste=createList(text) #metini cümlelere ve kelimelere böler,kelimeleri ögelerine göre etiketler.

saveDatabase(liste) #etiketlenen metni database kaydeder.

            
      


