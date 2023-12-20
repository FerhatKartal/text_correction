import sqlite3
import re


#mainden gelen cümleyi database ile taratarak benzer cümle kalıplarını döner
def sentController(param):

    con=sqlite3.connect("data.db")
    cursor=con.cursor()

    
    cursor.execute("SELECT *FROM words")
    data=cursor.fetchall()
    guestText=[]

    for i in data:
        count=0
        text=[]
        eachDataWord=i[0].split("---")
        for k in eachDataWord:
            pureDataWord=k.split(" [")
            text.append(pureDataWord[0])
       
        if(text[1].lower()==(param[0].lower())):
            for t in text:
                for p in param:
                    print(t.lower())
                    print(p.lower())
                    if((t.lower()).__contains__(p.lower())):
                        count+=1
                               
        if(count>(len(param)*2)-3):
            guestText.append(text)
      

    print(guestText)  
    con.close()           
    return guestText
      
