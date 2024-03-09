import sqlite3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


#mainden gelen kelime eksik ya da yanlış ise düzelterek dönderir
def otoController(param,data):
    
    guestText=[]                #toplam sonucu tutacak dizi
    
    for i in data:
        if(len(guestText)<4):          #en fazla 4 adet sonuç getirir.
            text=[]
            eachDataWord=i[0].split("---")
            for k in eachDataWord:
                pureDataWord=k.split(" [")
                pureDataWord=pureDataWord[0].split(" ")
                for p in pureDataWord:
                    text.append(p.lower())
              
            for t in text:          #fuzzy_wuzzy algoritmasının seçilen benzerlik oranına göre dönülecek kelimeleri belirler.
                if(t.strip()!=""):
                    # if((fuzz.ratio(t, param))>(90 if len(param)*10>90 else len(param)*10) and 
                    #    guestText.count(t.strip().lower())==0 and 
                    #    (len(param)<len(t)+3 or len(param)>len(t)-3)):
                        
                    # if((fuzz.ratio(t, param))>80 and guestText.count(t.strip().lower())==0 and (len(param)<len(t)+2 or len(param)>len(t)-2)):

                    # if((fuzz.ratio(t, param))>30 and guestText.count(t.strip().lower())==0):
                    # if((fuzz.ratio(t, param))>40 and guestText.count(t.strip().lower())==0):
                    # if((fuzz.ratio(t, param))>50 and guestText.count(t.strip().lower())==0):
                    # if((fuzz.ratio(t, param))>60 and guestText.count(t.strip().lower())==0):
                    # if((fuzz.ratio(t, param))>70 and guestText.count(t.strip().lower())==0):
                    if((fuzz.ratio(t, param))>80 and guestText.count(t.strip().lower())==0):
                    # if((fuzz.ratio(t, param))>90 and guestText.count(t.strip().lower())==0):
                    
                        guestText.append(t.lower())

    for i in data:
        if(len(guestText)<4):
            text=[]
            eachDataWord=i[0].split("---")
            for k in eachDataWord:
                pureDataWord=k.split(" [")
                pureDataWord=pureDataWord[0].split(" ")
                for p in pureDataWord:
                    text.append(p.lower())
              
            for t in text:
                if(t.strip()!=""):
                    # if((fuzz.ratio(t, param))>(90 if len(param)*10>90 else len(param)*10) and 
                    #    guestText.count(t.strip().lower())==0 and 
                    #    (len(param)<len(t)+3 or len(param)>len(t)-3)):
                        
                    # if((fuzz.ratio(t, param))>80 and guestText.count(t.strip().lower())==0 and (len(param)<len(t)+2 or len(param)>len(t)-2)):

                    # if((fuzz.ratio(t, param))>30 and guestText.count(t.strip().lower())==0):
                    # if((fuzz.ratio(t, param))>40 and guestText.count(t.strip().lower())==0):
                    # if((fuzz.ratio(t, param))>50 and guestText.count(t.strip().lower())==0):
                    # if((fuzz.ratio(t, param))>60 and guestText.count(t.strip().lower())==0):
                    # if((fuzz.ratio(t, param))>70 and guestText.count(t.strip().lower())==0):
                    if((fuzz.ratio(t, param))>60 and guestText.count(t.strip().lower())==0):
                    # if((fuzz.ratio(t, param))>90 and guestText.count(t.strip().lower())==0):
                    
                        guestText.append(t.lower())
                                           
    return guestText
      
