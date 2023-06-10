from kelimeler import sozluk
from tekil2 import tekil2

yeni_cumle=[]#yalınlastırılan cumleyi tutar
def sadelestir(cumle):#gelen cumleyi sozlukteki kelimelere indirger
    for i in range(len(cumle)):
        for j in range(len(sozluk)):
            boyut=min(len(sozluk[j][0]),len(cumle[i]))#sozlukteki kelimenin boyutunu tutar
            if(cumle[i][:boyut]==sozluk[j][0]):#cümledeki yalınlasan kelime ile sozlukteki kelimeyi karşılastırır
                yeni_cumle.append(sozluk[j][0])#yalın kelimelerden oluşan yeni cumle elde edilir 
          
    return yeni_cumle         
        
                