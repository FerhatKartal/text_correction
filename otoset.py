from text_cleaning import cleaning
import textdistance as td

#mainden gelen kelime eksik ya da yanlış ise düzelterek dönderir
def otoController(param,total,indexx): 

    z_index=0
    
    x=param.lstrip()   #param rakamsal değeri hesaplanır
    z_index=0
    for i in x:
        z_index+=(ord(i))
        
     

    guestText=[]                #toplam sonucu tutacak dizi
    guestScore=[]               #benzerlik oranını tutacak dizi
    box=10                      #her kelime için kaç öneri dönüleceğini belirleyen değişken

    counter=-1
    for t in total: 
     counter+=1 
     m=indexx[counter]        
     if(t.strip()!="" and abs(m-z_index)<120):  #her kelimenin karşılaştırılacağı kelimeleri kısıtlar.
        t=cleaning(t.strip()) 
        param=cleaning(param.strip())

    

                #DÜZENLEME TABANLI
#------------------------------------------------------------------------------------------------------------------------
        #LEVENSTEIN
        rangeoflike=(td.levenshtein.normalized_similarity(param,t))*100
       

#------------------------------------------------------------------------------------------------------------------------
        


    #en benzer kelimeleri belirleyen metot
        if((rangeoflike>=60)
           and guestText.count(t.strip().lower())==0):         
                 
            if(len(guestText)<box):
                guestText.append(t.lower())
                guestScore.append(rangeoflike)
            elif(len(guestText)==box):
                for i in range(len(guestScore)):
                    if((guestScore[i]<rangeoflike) and (guestText.count(t)==0)):
                        guestScore[i]=rangeoflike
                        guestText[i]=t

           
            for i in range(len(guestScore)-2):
                if(guestScore[i]<guestScore[i+1]):
                    tmp_score=guestScore[i]
                    guestScore[i]=guestScore[i+1] 
                    guestScore[i+1]=tmp_score

                    tmp_text=guestText[i]  
                    guestText[i]=guestText[i+1]
                    guestText[i+1]=tmp_text 
    return guestText


