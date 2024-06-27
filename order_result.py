import numpy as np

def order_result(results,oneriler):     #ngram datalarını uygun cümleye çeviren metot
  
    results=results.split(",")
    boyut=len(oneriler)

    matris1=[]
    for i in range(boyut):
            satir = []     
            matris1.append(satir)

    matris2=[]
    for i in range(boyut):
            satir = []     
            matris2.append(satir)

    for i in results:
        if(i!=results[-1]):
            t=i.split("-")
            matris1[int(t[1])].append(t[0]) 

    for i in range(boyut):
         matris2[i]=oneriler[i][0]

    lastmatris=[]
    for i in range(boyut):
          if(len(matris1[i])>1):
            for j in matris1[i]:
                t=j.split(" ")
                matris2[i]=t[0]
                matris2[i+1]=t[1]
                if(lastmatris.count(matris2)==0):
                    lastmatris.append(matris2.copy())

    return lastmatris,matris2
    

    
    

  
