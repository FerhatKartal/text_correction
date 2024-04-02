from otoset import otoController
# from data_register import register
import tkinter as tk
import sqlite3

# Aşağıdaki satır kaynaktan çekilen verileri etiketleyerek database kayıt eder.
#Bir kere çalıştırıldığı için program her çalıştığında tekrar çalıştırılmasına gerek yoktur.

# register()
#------------------------------------------------------------------------------------------------------   

#DATADB'DEN ÇEKİLEN VERİLER
text=[]                             #parse edilen kelimeleri tutacak dizi
con=sqlite3.connect("data.db")      #veri tabanına bağlanır.
cursor=con.cursor()   
cursor.execute("SELECT *FROM words")#tüm datayı çeker.
datadb=cursor.fetchall()
con.close() 

#veri tabanından gelen kelimeleri parse ederek kelime dizisine çeviren metot
for i in datadb:
    eachDataWord=i[0].split("---")
    for k in eachDataWord:
        pureDataWord=k.split(" [")
        pureDataWord=pureDataWord[0].split(" ")
        for p in pureDataWord:
            text.append(p.lower())


#CORRECTWORDS'DEN ÇEKİLEN VERİLER           
words=[]                         #parse edilen kelimeleri tutacak dizi
dosya = open("correctwords.txt","r",encoding="utf-8")
words = dosya.readlines()
dosya.close()

total=words+text #total dizisi iki veri tabanından gelen verileri birleştirir
 



#arayüzü temizler       
def cleaning():
    _oneri.delete(1.0, 'end') #öneri bölümünü temizler
    _entry.delete(0,tk.END)   #girdi bölümünü temizler
    
 #eksik ya da yanlış girilen kelimelere uygun öneriler döndürür
def show_correct():
     _oneri.config(state= "normal") #öneri bölümünü "yazılabilir" yapar.
     _total_arr=[]                  #cümledeki tüm önerilen kelimeleri tutar.
     _oneri_arr=[]                  #gelen önerileri tutmak için boş bir öneri dizisi oluşturur.
     _oneri_text=""                 #gelen her bir öneriyi tutmak için boş bir öneri stringi oluşturur.
     _oneri.delete(1.0,'end')       #öneri bölümünü temizler.
     _data=_entry.get()             #girdi olarak verilen datayı alır.
     _data=_data.split(" ")         #girdiyi boşluklara göre split eder.
    
     for i in _data:
      _data=i.strip()                  #girdiyi noktalama işaretlerinden ayıklar.
      _oneri_arr=otoController(i,total)#girdi ve toplam datayı göndererek girdiye uygun sonuçları getirir.
      _total_arr.append(_oneri_arr)    #tüm kelimelerin benzerlerini tutan dizi
     
    
     

     s=0
     while(s<10):                       #en fazla 10 adet öneri dönülmesini garanti eder.
      for i in range(len(_total_arr)): #sonucların arayüze yazılması için sıraya koyar.
            if(len(_total_arr[i])>s and len(_total_arr[i])>0):     
               _oneri_text=_oneri_text+_total_arr[i][s]+"--"
            else:
               _oneri_text=_oneri_text+"bulunamadı"+"--"  #sonuç yoksa uyarı yazar.
        
      s+=1
      _oneri_text=_oneri_text+"\n"
    
     _oneri.insert('end',_oneri_text)

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
