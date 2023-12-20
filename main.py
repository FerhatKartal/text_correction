from wordControl import wordController
from sentControl import sentController
from createList import createList

import tkinter as tk
import re

#Aşağıda yorum satırına alınmış olan ilk 4 satır kaynaktan çekilen verilerin etiketlenerek database kayıt edilmesi amacıyla yazılmıştır.Bir kere çalıştırıldığı için program her çalıştığında tekrar çalıştırılmasına gerek yoktur.

# createDatabase() #boş bir database tablosu olusturur

# text=fetchdata()

# liste=createList(text) #metini cümlelere ve kelimelere böler,kelimeleri ögelerine göre etiketler.

# saveDatabase(liste) #etiketlenen metni database kaydeder.

#------------------------------------------------------------------------------------------------------   

#arayüzü temizler       
def cleaning():
    _label.config(text="")
    _entry.delete(0,tk.END)
    _text.config(text="kontrol et")


#bir sonraki kelime tahmini yapar
def changing():
    _text.config(text="kontrol edildi")
    _data=_entry.get()
                
                

    #kullanıcıdan cümle alır
    _sent=_data
    _sent=_sent.lower()#tüm harfleri küçük harf yapar.
                    
    _sent =re.sub(r'[^\w\s]',' ', _sent)#cümledeki noktalama işaretlerini ayıklar.

    allData=""
    suggest=wordController(_sent)
    for i in suggest:
        allData=allData+i+"\n"

    if(len(allData)>0):
        _label.config(text=allData)

    else:
        _sentx=_data.split(" ")
        suggestx=wordController(_sentx[-1])
        allDatax=""
        for i in suggestx:
            allDatax=allDatax+i+"\n"

        _label.config(text=allDatax)



#kalıp olarak verilen cümleyi tamamlar
def suggesting():
    showLabel=""
    _text.config(text="tahmin edildi")
    _data=_entry.get()
                
                

    #kullanıcıdan cümle alır
    _sent=_data
    _sent=_sent.lower()#tüm harfleri küçük harf yapar.
                    
    _sent =re.sub(r'[^\w\s]',' ', _sent)#cümledeki noktalama işaretlerini ayıklar.

    suggest=sentController(_sent.split(" "))

    for eachSuggest in suggest:
        for s in eachSuggest:
            showLabel=showLabel+s+" "
        showLabel=showLabel+"\n"

    _label.config(text=showLabel)


#arayüz kodları
_window=tk.Tk()
_window.geometry('800x400+50+50')
_window.title("TEXT CORRECTION")
_window.resizable(False,False)

_entry=tk.Entry(width=100)
_entry.pack()

_text=tk.Label(_window,text='mesaj girin')
_text.pack()

_button1=tk.Button(_window,text='kontrol et',command=changing)
_button1.pack()

_button3=tk.Button(_window,text='tahmin et',command=suggesting)
_button3.pack()

_label=tk.Label(text="sonuç")
_label.pack()

_button2=tk.Button(_window,text='temizle',command=cleaning)
_button2.pack()

_window.mainloop()     
