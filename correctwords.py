import sqlite3

def correctwords_py():          
    words=[]                         #parse edilen kelimeleri tutacak dizi
    con3=sqlite3.connect("correctwords.db")      #veri tabanına bağlanır.
    cursor3=con3.cursor()   
    cursor3.execute("SELECT *FROM words")#tüm datayı çeker.
    datadb3=cursor3.fetchall()
    con3.close()
    for i in datadb3:
        words.append(str(i[0].strip()).lower())

    return words