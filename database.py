import sqlite3


#data.db dosyasında "words" adında boş bir database tablosu oluşturur.
database=sqlite3.connect("data.db")
cursor=database.cursor()
def createDatabase():
    database=sqlite3.connect("data.db")
    cursor=database.cursor()

    def createTable():
        cursor.execute("CREATE TABLE IF NOT EXISTS words(sampleData TEXT)")
   
    createTable()

# "words" tablosunu main'den gelen etiketlenmiş metin ile ,her satırda bir cümle olacak şekilde,doldurur.
def saveDatabase(liste):
    for sent in liste:
        wordSample =""
        for words in sent:
            wordSample+="---"
            for word in words:
                wordSample+=word[0]+" "
            wordSample+="["+word[1]+"]"
    

         
        cursor.execute("INSERT INTO words (sampleData) VALUES(?)",(wordSample,))

    database.commit()     
    database.close()