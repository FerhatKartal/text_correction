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
    _label.delete(1.0, 'end')
    _entry.delete(0,tk.END)
    _text.config(text="kontrol et")
    
#bir sonraki kelime tahmini yapar
def changing():
    _label.delete(1.0, 'end')
    _text.config(text="işlem gerçekleşti")
    _data=_entry.get()

    #kullanıcıdan cümle alır
    _sent=_data
    _sent=_sent.lower()#tüm harfleri küçük harf yapar.
                    
    _sent =re.sub(r'[^\w\s]',' ', _sent)#cümledeki noktalama işaretlerini ayıklar.

    allData=""
    say=0
    allDatax=""
    suggest=wordController(_sent)
    if(_data==""):
        _label.insert('end', "herhangi bir sonuç bulunamadı")
    else:
        for i in suggest:
            say+=1
            if(say<5):
                allData=allData+i+"\n"

        if(len(allData)>0):
            _label.insert('end', allData)

        else:
            _sentx=_data.split(" ")
            suggestx=wordController(_sentx[-1])
            say=0
            for i in suggestx:
                say+=1
                if(say<5):
                    allDatax=allDatax+i+"\n"

            _label.insert('end', allDatax)

    


#alınan girdileri kullanarak cümle önerisi yapar
def suggesting():
    _label.delete(1.0, 'end')
    showLabel=""
    _text.config(text="işlem gerçekleşti")
    _data=_entry.get()
                
                

    #kullanıcıdan cümle alır
    _sent=_data
    _sent=_sent.lower()#tüm harfleri küçük harf yapar.
                    
    _sent =re.sub(r'[^\w\s]',' ', _sent)#cümledeki noktalama işaretlerini ayıklar.

    suggest=sentController(_sent.split(" "))

    sayan=0
    
    for eachSuggest in suggest:  
        if(sayan<4):      
            for s in eachSuggest:
                showLabel=showLabel+s+" "           
            showLabel=showLabel+"\n"+"---------------------------------------------------------"+"\n"
            sayan+=1

    if(showLabel==""):
        _label.insert('end',"herhangi bir sonuç bulunamadı")
    else:
        _label.insert('end', showLabel)


#arayüz kodları
_window=tk.Tk()
_window.geometry('1000x600+50+50')
_window.title("TEXT CORRECTION")
_window.resizable(False,False)


_entry=tk.Entry(width=100)
_entry.pack()

_text=tk.Label(_window,text='mesaj girin')
_text.pack()

_button1=tk.Button(_window,text='bir sonraki kelimeyi tahmin et',command=changing)
_button1.pack()

_button3=tk.Button(_window,text='cümle öner',command=suggesting)
_button3.pack()

_label = tk.Text(_window,height=30,width=120)
_label.config(state='normal')
sb = tk.Scrollbar(_window)
sb.pack(side="right", fill="both")
_label.config(yscrollcommand=sb.set)
sb.config(command=_label.yview)
_label.pack()

_button2=tk.Button(_window,text='temizle',command=cleaning)
_button2.pack()

_window.mainloop()     
