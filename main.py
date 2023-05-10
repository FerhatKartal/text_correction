from sadelestir import sadelestir
from ayikla import ayikla
from kelimeler import sozluk
from olumlumu import olumlumu,dogruluk_kontrolu
from on_analiz import nesne_nesne_analiz
#örnek cümle1="tavsanlar buharlasabilirler"
#örnek cümle2="arabamiz carpmaz"
#örnek cümle3="kayalar akıyordu"
#örnek cümle4="hizli ucaklar konacaklardi"
#örnek cümle5="dallar hizlica uzayacaktir"
#örnek cümle6="ates serttir eriyebilir"
cumle="hizli ucaklar konamazlar"
#cumle="ucaklar konamaz"


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






