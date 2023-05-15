from kelimeler import sozluk


duzelenCumle=[]#düzeltilen kelimelerin listesini içerir.

"""
eksik yada yanlış yazılan kelimeyi tespit ederek sözlükteki en yakın kelimelerin listesini döner.
"""
def duzelten(cumle): 
    donenCumle=""
    cumle=cumle.split()
   
    for i in range(len(cumle)):
        sayac=0
        for j in range(len(sozluk)):
            boyut=len(cumle[i])
            if cumle[i]==sozluk[j][0][:boyut]:
                duzelenCumle.append(cumle[i])
                sayac+=1
        
        if sayac==0:
            istatistik(cumle[i])
    for m in range(len(duzelenCumle)):
        donenCumle+=duzelenCumle[m]+" "
    return donenCumle

def istatistik(kelime):#eksik yada yanlış kelimeye en yakın olan kelimeleri bulur.
    sayac=[]
    
    count=0
    
    
    for i in range(len(kelime)):
        sayac+=kelime[i]
    
    for j in range(len(sozluk)):
        for k in range(min(len(sozluk[j][0]),len(sayac))):
            if sayac[k]==sozluk[j][0][k]:
                count+=1
                
        count=(count/min(len(sozluk[j][0]),len(sayac)))*100#benzerlik oranı için yüzdelik durumu belirler.
        
        if count>30:#harflerin frekans benzerliğine göre %30 oranında benzer olanları seçer. 
            
            duzelenCumle.append(sozluk[j][0])
            
        count=0
        
        