import sqlite3

def dataset_py():
    words=[]                             #parse edilen kelimeleri tutacak dizi
    con=sqlite3.connect("data_set.db")      #veri tabanına bağlanır.
    cursor=con.cursor()   
    cursor.execute("SELECT *FROM words")#tüm datayı çeker.
    datadb=cursor.fetchall()
    con.close() 

    #veri tabanından gelen kelimeleri parse ederek kelime dizisine çeviren metot
    for i in datadb:
        words.append(str(i[0].strip()).lower())
    
    return words