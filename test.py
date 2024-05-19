import sqlite3
from _zemberek import zbrk,zbrky


def yuklem_bulan(onlylastmatris,lastmatris):
    yuklem=""
    dif=[]
    _temp=[]
    correct_result=[]
    return_result=[]

    for i in onlylastmatris:
        for j in i:
            if("Verb" in zbrky(j)):
                yuklem=j
                print(yuklem)

    for i in lastmatris:
        for j in i:
            _temp.append(j)
    for i in _temp:
        if(_temp.count(i)==1):
            dif.append(i)
            print(dif)


    textAll=[]
    con=sqlite3.connect("dataPure.db") #veri tabanına bağlanır.
    cursor=con.cursor()   
    cursor.execute("SELECT *FROM postags")#tüm datayı çeker.
    datadb=cursor.fetchall()
    con.close() 
    for i in datadb:
        textAll.append(str(i[0].strip()).lower())
    
    datas=textAll
    dogrular=[]
    son_yuklem=zbrk(yuklem)
    uzunluk=len(son_yuklem)
    print(son_yuklem)
    for i in datas:
        i=i.split(" ")
        k=i[-1]
        if(k[0:uzunluk]==son_yuklem):
            dogrular.append(i)

    for d in dif:
        for i in dogrular:
            for j in i:
                if(d in j):
                    correct_result.append(d)

    for i in lastmatris:
        for c in correct_result:
            if((c in i) and (i not in return_result)):
                return_result.append(i)
    print(return_result)
    return return_result
