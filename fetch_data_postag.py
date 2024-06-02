import sqlite3

def postag_py():          
    words=[]                         #parse edilen kelimeleri tutacak dizi
    con3=sqlite3.connect("data_postag.db")      #veri tabanına bağlanır.
    cursor3=con3.cursor()   
    cursor3.execute("SELECT *FROM words")#tüm datayı çeker.
    datadb3=cursor3.fetchall()
    con3.close()
   
    for i in datadb3:
        s=[]
        i=i[0].split("--")
        for k in i:
            k=k.split(":")
            k=k[0]
            s.append(str(k).lower())
        words.append(s)
    return words



def plain_text(lastmatris,matris2): #çıktıyı düz metne çevirir

    sceen=""
    for i in lastmatris:
         for k in i:
              sceen+=k+" "
         sceen+="\n"

    if(sceen=="" and lastmatris.count(matris2)==0):
        for i in matris2:
         sceen+=i+" "
        sceen+="\n"

    return sceen