import re
from deneme import deneme
from sayac import sayac
from duzelten import duzelten

cumle=""
duzeltilenCumle=[]

#kullanıcıdan cümle alır
cumle=input("bir cumle giriniz:")
    
cumle =re.sub(r'[^\w\s]',' ', cumle)#cümledeki noktalama işaretlerini ayıklar.


kontrolcu=sayac(cumle)#cümlede eksik yada yanlış olan kelimelerin sayısının tutar.

if(kontrolcu==0):
    deneme(cumle)
else:
    duzeltilenCumle=duzelten(cumle)
    print("sozlukte bulunmayan kelimeler mevcut")
    duzeltilenCumle=duzeltilenCumle.split("]")

    duzeltilenCumle=list(set(duzeltilenCumle))#dönen sonuçların tekrar etmemesi için veriler set'e çevrilir.

    for i in range(len(duzeltilenCumle)):
        print(duzeltilenCumle[i])

    


