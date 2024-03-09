from otoset import otoController
from data_register import register
import tkinter as tk
import sqlite3

# Aşağıdaki satır kaynaktan çekilen verileri etiketleyerek database kayıt eder.
#Bir kere çalıştırıldığı için program her çalıştığında tekrar çalıştırılmasına gerek yoktur.

# register()
#------------------------------------------------------------------------------------------------------   

con=sqlite3.connect("data.db")      #veri tabanına bağlanır.
cursor=con.cursor()
    
cursor.execute("SELECT *FROM words")#tüm datayı çeker.
allData=cursor.fetchall()
con.close()   

#arayüzü temizler       
def cleaning():
    _oneri.delete(1.0, 'end') #öneri bölümünü temizler
    _entry.delete(0,tk.END)   #girdi bölümünü temizler
    
 #eksik ya da yanlış girilen kelimelere uygun öneriler döndürür
def show_correct():
     _oneri.config(state= "normal") #öneri bölümünü "yazılabilir" yapar.
     _oneri_arr=[]                  #gelen önerileri tutmak için boş bir öneri dizisi oluşturur.
     _oneri_text=""                 #gelen her bir öneriyi tutmak için boş bir öneri stringi oluşturur.
     _oneri.delete(1.0,'end')       #öneri bölümünü temizler.
     _data=_entry.get()             #girdi olarak verilen datayı alır.
     _data=_data.split(" ")         #girdiyi boşluklara göre split eder.
     _data=_data[-1]                #split edilen diziden son girdiyi alır.
     _data=_data.strip()            #son girdiyi noktalama işaretlerinden ayıklar.
     _oneri_arr=otoController(_data,allData)#girdi ve toplam datayı göndererek girdiye uygun sonuçları getirir.
     _oneri_arr=set(_oneri_arr)     #sonuçları tekrarsız diziye çevirir.

     
     for i in _oneri_arr:               #sonucu text'e çevirir.
        _oneri_text=_oneri_text+i+"\n"
        
     if(_data!=None):                   #başka bir girdi yoksa sonuçları yazdırır.
        _oneri.insert('end',_oneri_text)

     _oneri.config(state= "disabled")   #öneri bölümünü "yazılamaz" yapar.
     _window.after(1000,show_correct)   #her saniye girdi bölümünü denetler ve öneri fonksiyonunu çalıştırır


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

_oneri=tk.Text(_window,height=5,width=30) #önerilen kelimeler kutusu
_oneri.pack()

_button2=tk.Button(_window,text='temizle',command=cleaning) #girdi ve önerileri temizleyen buton
_button2.pack()

show_correct()

_window.mainloop()     
