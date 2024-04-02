from text_cleaning import cleaning
import textdistance as td

#mainden gelen kelime eksik ya da yanlış ise düzelterek dönderir
def otoController(param,total):   
    guestText=[]                #toplam sonucu tutacak dizi
    guestScore=[]               #benzerlik oranını tutacak dizi
    box=10                      #her kelime için kaç öneri dönüleceğini belirleyen değişken

    for t in total:  
                
     if(t.strip()!=""):       #her kelimeyi noktalama işaretlerinden temizler.
        t=cleaning(t.strip()) 
        param=cleaning(param.strip())

    

                #DÜZENLEME TABANLI
#------------------------------------------------------------------------------------------------------------------------
        #LEVENSTEIN
        rangeoflike=(td.levenshtein.normalized_similarity(param,t))*100
       

#------------------------------------------------------------------------------------------------------------------------
        


    #en benzer kelimeleri belirleyen metot
        if((rangeoflike>=60)
           and (abs(len(param)-len(t))<2)
           and guestText.count(t.strip().lower())==0):         
                 
            if(len(guestText)<box):
                guestText.append(t.lower())
                guestScore.append(rangeoflike)
            elif(len(guestText)==box):
                for i in range(len(guestScore)):
                    if((guestScore[i]<rangeoflike) and (guestText.count(t)==0)):
                        guestScore[i]=rangeoflike
                        guestText[i]=t
                            
    
    return guestText


