from wordControl import wordController
from sentControl import sentController
from createList import createList
from otoset import otoController

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


 #eksik ya da yanlış girilen kelimelere uygun öneriler döndürür
def show_correct():
     _oneri_arr=[]
     _oneri_text=""
     _oneri.delete(1.0,'end')
     _data=_entry.get()
     _data=_data.split(" ")
     _data=_data[-1]
     _data=_data.strip()
     _oneri_arr=otoController(_data)
     _oneri_arr=set(_oneri_arr)

     limit=0
     for i in _oneri_arr:
         if(limit<4):
             _oneri_text=_oneri_text+i+"\n"
             limit=limit+1
             

     if(_data!=None):
        _oneri.insert('end',_oneri_text)

     _window.after(1000,show_correct)




#bir sonraki kelime tahmini yapar
def changing():
    _label.delete(1.0, 'end')
    _data=_entry.get()

    #kullanıcıdan cümle alır
    _sent=_data
    _sent=_sent.lower()#tüm harfleri küçük harf yapar.
                    
    _sent =re.sub(r'[^\w\s]',' ', _sent)#cümledeki noktalama işaretlerini ayıklar.

    allData=""
    say=0
    allDatax=""
    suggest=wordController(_sent)
    if(_data.strip()==""):
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
    _data=_entry.get()
                
                

    #kullanıcıdan cümle alır
    arr=[]
    _sent=_data
    _sent=_sent.lower()#tüm harfleri küçük harf yapar.
                    
    _sent =re.sub(r'[^\w\s]',' ', _sent)#cümledeki noktalama işaretlerini ayıklar.

    _sent=_sent.split(" ")
    for s in _sent:
        s.strip()
        if(s==" " or s==""):
            continue
        else:
            arr.append(s)

    suggest=sentController(arr)

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

_lbl=tk.Label(_window,text='bunu mu demek istediniz?')
_lbl.pack()

_oneri=tk.Text(_window,height=5,width=60)
_oneri.pack()

_button1=tk.Button(_window,text='bir sonraki kelimeyi tahmin et',command=changing)
_button1.pack()

_button3=tk.Button(_window,text='cümle öner',command=suggesting)
_button3.pack()

_label = tk.Text(_window,height=20,width=120)
_label.config(state='normal')
sb = tk.Scrollbar(_window)
sb.pack(side="right", fill="both")
_label.config(yscrollcommand=sb.set)
sb.config(command=_label.yview)
_label.pack()

_button2=tk.Button(_window,text='temizle',command=cleaning)
_button2.pack()

show_correct()

_window.mainloop()     
