from kelimeler import sozluk
"""
sözlükte olmayan kelimeleri tespit ederek,sayac ile sayılarını tutar.
"""
def sayac(cumle):
    cumle=cumle.split()
    sayac=0
    for i in range(len(cumle)):
        sayac2=0
        for j in range(len(sozluk)):
            boyut=len(sozluk[j][0])
            if sayac2==0 and cumle[i][:boyut]==sozluk[j][0]:
                sayac+=1
                sayac2+=1
    sayac=len(cumle)-sayac
    return sayac
        