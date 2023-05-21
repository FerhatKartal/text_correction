from sadelestir import sadelestir
from ayikla import ayikla
from kelimeler import sozluk
from olumlumu import olumlumu,dogruluk_kontrolu
from on_analiz import nesne_nesne_analiz
from duzelten import duzelten

def deneme(cumle):
    cumle=cumle.lower()#girilen cümledeki tüm harfleri küçük harfe dönüştürür

        #yanlış yazılan kelimeleri düzeltir,en yakın kelime listesini gösterir.
    duzeltilenCumle=duzelten(cumle)


    try:
        #cümlenin nesnelerini analiz eder
        sonuc1=nesne_nesne_analiz(cumle)

        #cümlenin olumlu-olumsuz durumunu belirler
        sonuc2=olumlumu(cumle)

        #cümlenin kelimelerini yalın hale getirir
        cumle=sadelestir(cumle)

        #cumlenin ögelerinin uyumunu kontrol eder
        sonuc3=ayikla(cumle)

        #cümlenin kurallara uygun olup olmadığını yazdırır
        print(dogruluk_kontrolu(sonuc1,sonuc2,sonuc3))
            
    except:
            
        print("sozlukte bulunmayan kelimeler mevcut")

        duzeltilenCumle=duzeltilenCumle.split("]")
            
        for i in range(len(duzeltilenCumle)):
            print(duzeltilenCumle[i])
            