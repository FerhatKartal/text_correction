from kelimeler import sozluk

"""
cümlenin fiilinde mez,maz eki varsa cümlenin olumsuz olduğunu döner
"""
def olumlumu(cumle):
    
    a=cumle[-1].find('maz')
    a*=cumle[-1].find('mez')
    if a<0:
        return False
    else:
        return True
    

#sonucları test ederek main fonksiyona doner
def dogruluk_kontrolu(sonuc1,sonuc2,sonuc3):
    
    
    if sonuc2==True:
        if(sonuc1==1 and sonuc3==1):
            sonuc="cumle kurallara uygun"
        else:
            sonuc="cumle uygun degil"
    else:
        if(sonuc1==1 and sonuc3==1):
            sonuc="cumle kurallara uygun"
        else:
            sonuc="cumle uygun degil"
    return sonuc
