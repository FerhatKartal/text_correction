import sqlite3
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


#mainden gelen kelime eksik ya da yanlış ise düzelterek gösterir
def otoController(param):

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
        for t in text:
             if((fuzz.ratio(t, param))>70):
                 guestText.append(t)
                 
    con.close()           
    return guestText
      
