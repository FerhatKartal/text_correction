from kelimeler import sozluk
from analiz import ozne_yuklem_analiz


"""
gelen cumlede birbirine bağlı birden çok nesne varsa
bunları tek bir nesneye ve fiile indirgeyerek
yuklemle uyumunu kontrol eder

"""
def nesne_nesne_analiz(cumle):
    liste1=[]
    liste2=[]
    
    

    for i in range(len(cumle)):
        
        if ((cumle[i].find('in')<0) and
                (cumle[i].find('ın')<0) and
                (cumle[i].find('un')<0) and
                (cumle[i].find('ün')<0) and
                (cumle[i].find('nin')<0) and
                (cumle[i].find('nın')<0) and
                (cumle[i].find('nün')<0) and
                (cumle[i].find('nun')<0)):
            for j in range(len(sozluk)):
                boyut=len(sozluk[j][0])
                if(cumle[i][:boyut]==sozluk[j][0] and sozluk[j][1]=="nesne"):
                    liste1.append(sozluk[j][1:])
                    
                elif(cumle[i][:boyut]==sozluk[j][0] and sozluk[j][1]=="fiil"):
                    liste2.append(sozluk[j][1:])
            
    if(len(liste1)>1 and len(liste2)>1): 
                   
        return ozne_yuklem_analiz(liste1,liste2)
        
    else:
        return 1