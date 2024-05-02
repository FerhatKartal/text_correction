import sqlite3

def data_gram2_py():
    text=[]
    con=sqlite3.connect("data_gram2.db") #veri tabanına bağlanır.
    cursor=con.cursor()   
    cursor.execute("SELECT *FROM words")#tüm datayı çeker.
    datadb=cursor.fetchall()
    con.close() 
    for i in datadb:
        text.append(str(i[0].strip()).lower())
    
    return text