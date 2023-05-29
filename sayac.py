from kelimeler import sozluk

def sayac(cumle):
    cumle=cumle.split()
    sayac=0
    for i in range(len(cumle)):
        for j in range(len(sozluk)):
            boyut=min(len(cumle[i]),len(sozluk[j][0]))
            if cumle[i][:boyut]==sozluk[j][0][:boyut]:
                sayac+=1
    sayac=len(cumle)-sayac
    return sayac
        