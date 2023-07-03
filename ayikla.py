from analiz import ozne_yuklem_analiz
from analiz import sifat_nesne_analiz
from kelimeler import sozluk



"""
ayıkla fonksiyonu cumleyi kelimelere ayırır
"""
def ayikla(dizi):

    #nesneleri,sıfatları ve fiilleri tutan listeler
    nesneListesi=[]
    sifatListesi=[]
    fiilListesi=[]

    #son fonksiyondan dönene değerleri tutan liste
    onayListesi=[]

    #kelimeleri sınıflandıran döngü
    for i in range(len(dizi)):
        sira=0
        for j in range(len(sozluk)): 
            if (dizi[i]==sozluk[j][0]):
                if (sozluk[j][1]=="nesne"):
                    sira+=1
                    sozluk[j][11][0]+=sira
                    nesneListesi.append(sozluk[j][1:])
                elif (sozluk[j][1]=="sifat"):
                    sira+=1
                    sozluk[j][4]+=sira
                    sifatListesi.append(sozluk[j][1:])
                elif (sozluk[j][1]=="fiil"):
                    sira+=1
                    sozluk[j][4]+=sira
                    fiilListesi.append(sozluk[j][1:])

    #listeler boş değilse ozne ve yuklem uyumluluğunu kontrol eden metoda gönderilir              
    
    if(len(nesneListesi)>0 and len(fiilListesi)>0):
        onay1=ozne_yuklem_analiz(nesneListesi,fiilListesi)
        onayListesi.append(onay1)
    else:
        onay1=1  
        onayListesi.append(onay1)

    #listeler boş değilse sıfat ve nesne uyumluluğunu kontrol eden metoda gönderilir
    if(len(sifatListesi)>0 and len(nesneListesi)>0):
        onay2=sifat_nesne_analiz(sifatListesi,nesneListesi)
        onayListesi.append(onay2)
        
    else:
        onay2=1
        onayListesi.append(onay2)
        
    #sonuclar kontrol edilir.3 onaydan da olumlu sonuc alınırsa True,alınmazsa False doner.   
    if(onayListesi[0]==1 and onayListesi[1]==1):
        return 1
    else:
        return -1
        