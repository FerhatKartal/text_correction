import sqlite3
import re


#mainden gelen kelimeleri database taraması yaparak bir sonraki kelimeyi ve öge kalıplarını tahmin eder
def wordController(param):

    con=sqlite3.connect("data.db")
    cursor=con.cursor()

    
    cursor.execute("SELECT *FROM words")
    data=cursor.fetchall()
    guestText=[]
    for i in data:
        text=[]
        eachDataWord=i[0].split("---")
        for k in eachDataWord:
            pureDataWord=k.split(" [")
            text.append(pureDataWord[0])

        for m in text:
            if(re.search("^{}".format(param), m.lower())):
                guestText.append(m)
    guestText=set(guestText)
    con.close()           
    return guestText
      
