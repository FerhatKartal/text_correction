from otoset import otoController
# from data_register import register
import tkinter as tk
import sqlite3

# Aşağıdaki satır kaynaktan çekilen verileri etiketleyerek database kayıt eder.
#Bir kere çalıştırıldığı için program her çalıştığında tekrar çalıştırılmasına gerek yoktur.

# register()
#------------------------------------------------------------------------------------------------------   


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

iki=[]         #veri aramasını hızlandırmak için datalar kelime uzunluğuna göre gruplara ayrılır
uc=[]
dort=[]
bes=[]
alti=[]
yedi=[]
sekiz=[]
dokuz=[]
on=[]
iki_index=[]         #veri aramasını hızlandırmak için datalar kelimelerdeki harflerin değerlerinin toplamına göre gruplara ayrılır
uc_index=[]
dort_index=[]
bes_index=[]
alti_index=[]
yedi_index=[]
sekiz_index=[]
dokuz_index=[]
on_index=[]

total2=[]
for k in total:
    x=k.lstrip()
    c=0
    for i in x:
        c+=(ord(i))
    
    total2.append(c)
    
    

for i in range(len(total)):
    s=i
    i=str(total[i])
    if(len(i)==1 or len(i)==2 or len(i)==3):
        iki.append(i)
        iki_index.append(total2[s])
    if(len(i)==2 or len(i)==3 or len(i)==4):
        uc.append(i)
        uc_index.append(total2[s])
    if(len(i)==3 or len(i)==4 or len(i)==5):
        dort.append(i)
        dort_index.append(total2[s])
    if(len(i)==4 or len(i)==5 or len(i)==6):
        bes.append(i)
        bes_index.append(total2[s])
    if(len(i)==5 or len(i)==6 or len(i)==7):
        alti.append(i)
        alti_index.append(total2[s])
    if(len(i)==6 or len(i)==7 or len(i)==8):
        yedi.append(i)
        yedi_index.append(total2[s])
    if(len(i)==7 or len(i)==8 or len(i)==9):
        sekiz.append(i)
        sekiz_index.append(total2[s])
    if(len(i)==8 or len(i)==9 or len(i)==10):
        dokuz.append(i)
        dokuz_index.append(total2[s])
    if(len(i)==9 or len(i)>=10):
        on.append(i)
        on_index.append(total2[s])


ikilemeler=[]
for i in words:
    k=i.split(" ")
    if(len(k)==2):
        ikilemeler.append(str((k[0].strip())+" "+(k[1].strip()))) 
        
 
text2=[]
con2=sqlite3.connect("data_gram2.db") #veri tabanına bağlanır.
cursor2=con2.cursor()   
cursor2.execute("SELECT *FROM words")#tüm datayı çeker.
datadb2=cursor2.fetchall()
con2.close() 
for i in datadb2:
    text2.append(str(i[0].strip()).lower())

text2+=ikilemeler

#arayüzü temizler       
def cleaning():
    _oneri.delete(1.0, 'end') #öneri bölümünü temizler
    _entry.delete(0,tk.END)   #girdi bölümünü temizler
    
 #eksik ya da yanlış girilen kelimelere uygun öneriler döndürür
def show_correct():
     _oneri.config(state= "normal") #öneri bölümünü "yazılabilir" yapar.
     _total_arr=[]                  #cümledeki tüm önerilen kelimeleri tutar.
     _oneri_arr=[]                  #gelen önerileri tutmak için boş bir öneri dizisi oluşturur.
     _oneri.delete(1.0,'end')       #öneri bölümünü temizler.
     _data=_entry.get()             #girdi olarak verilen datayı alır.
     _data=_data.split(" ")         #girdiyi boşluklara göre split eder.
    
     for i in _data: #girdiyi noktalama işaretlerinden ayıklar.
      _data=i.strip() 
      if(len(_data)==2):  #girdi kelimesine uygun olan dizi belirlenir
          w=iki
          z=iki_index
      elif(len(_data)==3):
        w=uc 
        z=uc_index
      elif(len(_data)==4):
        w=dort
        z=dort_index 
      elif(len(_data)==5):
        w=bes 
        z=bes_index
      elif(len(_data)==6):
        w=alti 
        z=alti_index
      elif(len(_data)==7):
        w=yedi 
        z=yedi_index
      elif(len(_data)==8):
        w=sekiz 
        z=sekiz_index
      elif(len(_data)==9):
        w=dokuz
        z=dokuz_index
      elif(len(_data)>9):
        w=on 
        z=on_index                
      _oneri_arr=otoController(i,w,z)#girdi,sözlük datasını,kelimelerin rakamsal değerleri göndererek girdiye uygun sonuçları getirir.
      _total_arr.append(_oneri_arr)    #tüm kelimelerin benzerlerini tutan dizi
     
    #  print(_total_arr)
     deneme=[]
     hepsi=""
     for i in range(len(_total_arr)):       #benzer kelimeleri ngram analizine verir
         if(i<len(_total_arr)-1):
            for k in _total_arr[i]:
                for j in _total_arr[i+1]:
                    if(text2.__contains__(k+" "+j)):
                        deneme.append(k+" "+j)

     for l in deneme:           #ngram sonuçlarını ekrana yazar
         if(len(l)>0):
                # print(l)
                hepsi+=str(l)+"---" +"\n"         
     _oneri.insert('end',hepsi)

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
