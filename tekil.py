from kelimeler import sozluk

"""
aynı kökten türeyen kelimelerden doğru olanı seçer.String olarak tutar.
"""

def tekil(cumle):

    tekiller=""
    sayac=0
    cumle=cumle.split()
    
    for i in range(len(cumle)):
        sayac=0
        for j in range(len(sozluk)):
           
            boyut=len(sozluk[j][0])
            if(sayac==0 and cumle[i][:boyut]==sozluk[j][0]):
                tekiller=tekiller+" "+sozluk[j][0]
                sayac=1
    return tekiller

