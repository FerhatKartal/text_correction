from otoset import otoController
from data_gram2 import data_gram2_py
from data_set import dataset_py
from correctwords import correctwords_py
from arrays_and_indexes import arrayAndIndexes
from data_analize import analize
from result import results
from order_results import order_result
import tkinter as tk
import sqlite3

#data_gram.db'den verileri çeker.
n2grams=data_gram2_py()

#dataset.db'den verileri çeker
words1=dataset_py()

#correctwords.db'den verileri çeker.
words2=correctwords_py()

#databaseleri karakter uzunluğuna göre ve karakter değerlerine parçalara ayırır.
#Dönüş dizisinde 10 adet kelime datası dizisi ve 10 adet index datası dizisi vardır.
total=arrayAndIndexes(words1+words2)
 

#arayüzü temizler       
def cleaning():
    _oneri.config(state= "normal")#öneri bölümünü "yazılabilir" yapar.
    _oneri.delete(1.0, 'end') #öneri bölümünü temizler
    _oneri.config(state= "disabled")#öneri bölümünü "yazılamaz" yapar.
    _entry.delete(0,tk.END)   #girdi bölümünü temizler
    
 #eksik ya da yanlış girilen kelimelere uygun öneriler döndürür
def show_correct():
     _oneri.config(state= "normal") #öneri bölümünü "yazılabilir" yapar.
     _total_arr=[]                  #cümledeki tüm önerilen kelimeleri tutar.
     _oneri_arr=[]                  #gelen önerileri tutmak için boş bir öneri dizisi oluşturur.
     _oneri.delete(1.0,'end')       #öneri bölümünü temizler.
     _data_pure=_entry.get()             #girdi olarak verilen datayı alır.
     _data=_data_pure.split(" ")         #girdiyi boşluklara göre split eder.
    
     for i in _data: 
      data_index=analize(i,total)#girdi analizi için data dizisi belirler.
      i=i.strip()   
      _oneri_arr=otoController(i,data_index[0],data_index[1])#girdi,sözlük datasını,kelimelerin rakamsal değerleri göndererek girdiye uygun sonuçları getirir.
      _total_arr.append(_oneri_arr)    #tüm kelimelerin benzerlerini tutan dizi
     datas_results=results(_total_arr,n2grams)    #dataları ngram analizine verir.
     ordered_results=order_result(datas_results,_data_pure.strip())#datayı doğru dizilimli cümlelere çevirir.
    
     _oneri.insert('end',ordered_results)    #sonucu öneri bölümüne yazar.

     _oneri.config(state= "disabled")   #öneri bölümünü "yazılamaz" yapar.             
        

#arayüz kodları
_window=tk.Tk()                     #pencere genel ayarları
_window.geometry('600x600+50+50')
_window.title("TEXT CORRECTION")
_window.resizable(False,False)


_entry=tk.Entry(width=100)         #girdi kutusu
_entry.pack()

_text=tk.Label(_window,text='mesaj girin') #girdi kutusunun ismi
_text.pack()

_lbl=tk.Label(_window,text='öneriler')  #önerilen kelimeler kutusunun adı
_lbl.pack()

_oneri=tk.Text(_window,height=15,width=70) #önerilen kelimeler kutusu
_oneri.pack()

_button2=tk.Button(_window,text='temizle',command=cleaning) #girdi ve önerileri temizleyen buton
_button2.pack()

_button3=tk.Button(_window,text='düzelt',command=show_correct) #önerileri gösteren buton
_button3.pack()

_window.mainloop()     
