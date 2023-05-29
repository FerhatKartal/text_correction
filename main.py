from deneme import deneme
from sayac import sayac
from duzelten import duzelten
soru='E'
while soru=='E':

    cumle=""
    duzeltilenCumle=[]
    
    #kullanıcıdan cümle alır
    cumle=input("bir cumle giriniz:")
    
    kontrolcu=sayac(cumle)

    if(kontrolcu==0):
        deneme(cumle)
    else:
        duzeltilenCumle=duzelten(cumle)
        print("sozlukte bulunmayan kelimeler mevcut")
        duzeltilenCumle=duzeltilenCumle.split("]")
                
        for i in range(len(duzeltilenCumle)):
            print(duzeltilenCumle[i])

    soru=input("devam etmek istiyor musunuz?'E' - 'H':").upper()


