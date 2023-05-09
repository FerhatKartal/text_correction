from sadelestir import sadelestir
from ayikla import ayikla
from kelimeler import sozluk

#örnek cümle1="tavsanlar buharlasabilirler"
#örnek cümle2="arabamiz carpmaz"
#örnek cümle3="kayalar akıyordu"
#örnek cümle4="hizli ucaklar konacaklardi"
#örnek cümle5="dallar hizlica uzayacaktir"
#örnek cümle6="ates serttir eriyebilir"
cumle="ates serttir eriyebilir"

"""
cümlenin kelimelerini ,sözlukte karsılığı olan,en yalın hallerine cevirir
"""
cumle=sadelestir(cumle)


"""cumleyi ayikla fonksiyonuna gönderir ve sonucu yazdırır.
sonuc, cümlenin mantıklı olup olmadığını gösterir
"""
print(ayikla(cumle))



