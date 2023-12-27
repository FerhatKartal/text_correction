import sqlite3
import re


#mainden gelen cümleyi database ile taratarak anahtar girdilere uygun cümle kalıplarını döner
def sentController(param):

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
            pureDataWord=pureDataWord[0].split(" ")
            for p in pureDataWord:
                text.append(p.lower())
       
        text.pop(0)
        count=1
        for p in param:
            if(text.__contains__(p.lower())):
                count=count*1
            else:
                count=count*0
        if(count==1):
            guestText.append(text)
    con.close()           
    return guestText
      
