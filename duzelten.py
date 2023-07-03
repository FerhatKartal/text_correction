from kelimeler import sozluk




"""
eksik yada yanlış yazılan kelimeyi tespit ederek sözlükteki en yakın kelimelerin listesini döner.
"""


def duzelten(cumle): 
    duzelenCumle=[]#düzeltilen kelimelerin listesini içerir.
    donenCumle=""
    cumle=cumle.split()
    
    for i in range(len(cumle)):
        
        tek=0
        sayac=0
        for j in range(len(sozluk)):
            
            if(tek==0):
                for k in range(len(cumle[i])):
                    if(k==0 and cumle[i]==sozluk[j][0]):
                        duzelenCumle.append(cumle[i])
                        tek=1
                        sayac=sayac+1    
                    elif cumle[i][:-k]==sozluk[j][0]:
                        duzelenCumle.append(cumle[i])
                        tek=1
                        sayac=sayac+1
        if sayac==0:
            donen=istatistik(cumle[i])
            duzelenCumle.append(donen)

    
    for i in range(len(duzelenCumle)):
        for j in range(len(duzelenCumle[i])):
            donenCumle+=duzelenCumle[i][j]+" "
    return donenCumle


def istatistik(kelime):#eksik yada yanlış kelimeye en yakın olan kelimeleri bulur.
    sayac=[]
    duzelenler=[]#duzeltilen cumleleri tutar.
    count=0
    icerik=[]
    
    
    
    for i in range(len(kelime)):
        sayac+=kelime[i]
    
    for j in range(len(sozluk)):
        for k in range(min(len(sozluk[j][0]),len(sayac))):
            for t in range(min(len(sozluk[j][0]),len(sayac))):
                if t==k :
                    if sayac[t]==sozluk[j][0][k]:
                        count+=1
                
                
        count=(count/min(len(sozluk[j][0]),len(sayac)))*100#benzerlik oranı için yüzdelik durumu belirler.
        
        if (count>40 and len(sozluk[j][0])>=len(kelime)):#harflerin frekans benzerliğine göre %40 oranında benzer olanları seçer. 
            if (count<100):
                
                duzelenler.append(sozluk[j][0])
        count=0
    icerik.append("]")    
    icerik.append("!*")
    icerik.append(kelime)
    icerik.append("için onerilenler;")
    for i in range(len(duzelenler)):
        icerik.append(duzelenler[i])
        icerik.append("-")
    icerik.append("]")
    
    return icerik
        