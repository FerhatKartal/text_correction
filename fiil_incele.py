from fiil_ekleri import fiil_ekleri
from fiiller import fiiller

kelime="belirlenilecekmişlerdir"
total=[]
sayac=0

for i in fiiller:
    start=0
    stop=len(i)
    if(kelime.find(i,start,stop)==0):
        total.append(i)
        kelime=kelime[stop::]
        while(len(kelime)>0):
            for j in fiil_ekleri:
                start=0
                stop=len(j[0])
                if(kelime.find(j[0],start,stop)==0):
                    total.append(j[0])
                    kelime=kelime[stop::]
                    break
                else:
                    sayac=sayac+1
                    if(sayac==10000):
                        kelime=""
    
print(total)
