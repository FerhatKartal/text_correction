import tkinter as tk
import re
from deneme import deneme
from sayac import sayac
from duzelten import duzelten


def temizle():
    etiket.config(text="")
    giris.delete(0,tk.END)
    yazi.config(text="kontrol et")

def degistir():
    yazi.config(text="kontrol edildi")
    veri=giris.get()
                
                
    duzeltilenCumle=[]

    #kullanıcıdan cümle alır
    cumle=veri
    cumle=cumle.lower()#tüm harfleri küçük harf yapar.
                    
    cumle =re.sub(r'[^\w\s]',' ', cumle)#cümledeki noktalama işaretlerini ayıklar.


    kontrolcu=sayac(cumle)#cümlede eksik yada yanlış olan kelimelerin sayısının tutar.

    if(kontrolcu<=0):
        gorsel=deneme(cumle)
        etiket.config(text=gorsel)
    else:
        duzeltilenCumle=duzelten(cumle)
        
        duzeltilenCumle=duzeltilenCumle.split("]")

        duzeltilenCumle=list(set(duzeltilenCumle))#dönen sonuçların tekrar etmemesi için veriler set'e çevrilir.
        str=""
        str+="sozlukte bulunmayan kelimeler mevcut:"
        str+="\n"
        for i in range(len(duzeltilenCumle)):
            if(duzeltilenCumle[i].__contains__("!")):
                str+=duzeltilenCumle[i]
                str+="\n"
            etiket.config(text=str)

pencere=tk.Tk()
pencere.geometry('800x400+50+50')
pencere.title("TEXT CORRECTION")
pencere.resizable(False,False)

giris=tk.Entry(width=100)
giris.pack()

yazi=tk.Label(pencere,text='mesaj girin')
yazi.pack()

dugme1=tk.Button(pencere,text='kontrol et',command=degistir)
dugme1.pack()

etiket=tk.Label(text="sonuç")
etiket.pack()

dugme2=tk.Button(pencere,text='temizle',command=temizle)
dugme2.pack()

pencere.mainloop()