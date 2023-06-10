from kelimeler import sozluk
"""
aynı kökten türeyen kelimelerden doğru olanı seçer.Dizi olarak tutar.
"""
def tekil2(cumle):
    cumle=cumle.split()
    tekiller=[]
    sayac=0
    
    for i in range(len(cumle)):
        sayac=0
        for j in range(len(sozluk)):
           
            boyut=len(sozluk[j][0])
            if(sayac==0 and cumle[i][:boyut]==sozluk[j][0]):
                tekiller.append(sozluk[j][0])
                sayac=1
    
    return tekiller

