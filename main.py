from ayikla import ayikla
from kelimeler import sozluk

#örnek cümle1="tavsan buharlas"(***tavsan buharlasamaz)
#örnek cümle2="araba carp"(***araba carpabilir)
#örnek cümle3="kaya ak"(***kaya akamaz)
#örnek cümle4="hizli ucak kon"(***hızlı bir ucak konabilir)
#örnek cümle5="dal hizli uza"(***dal hızlı uzayabilir)
#örnek cümle6="ate sert eri"(***ates sert değildir ve erimez)
cumle="ates sert eri"


"""cumleyi ayikla fonksiyonuna gönderir ve sonucu yazdırır.
sonuc, cümlenin mantıklı olup olmadığını gösterir
"""
print(ayikla(cumle))



