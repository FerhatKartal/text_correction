from newspaper import fulltext,Article

from bs4 import BeautifulSoup
import requests

#veri setinin çekileceği url'ler belirlenerek bir dizide tutulur.
def fetchdata():
    urls=[
        "https://tr.wikipedia.org/wiki/YouTube",
        "https://tr.wikipedia.org/wiki/T%C3%BCrkiye",	
        "https://tr.wikipedia.org/wiki/2022_FIFA_D%C3%BCnya_Kupas%C4%B1",	
        "https://tr.wikipedia.org/wiki/FIFA_D%C3%BCnya_Kupas%C4%B1",
        "https://tr.wikipedia.org/wiki/2023_UEFA_%C3%BClkeler_s%C4%B1ralamas%C4%B1",	
        "https://tr.wikipedia.org/wiki/Bergen_(%C5%9Fark%C4%B1c%C4%B1)",	
        "https://tr.wikipedia.org/wiki/N%C3%BCfuslar%C4%B1na_g%C3%B6re_%C3%BClkeler_listesi",	
        "https://tr.wikipedia.org/wiki/Mustafa_Kemal_Atat%C3%BCrk",	
        "https://tr.wikipedia.org/wiki/%C3%9Cmit_%C3%96zda%C4%9F",
        "https://tr.wikipedia.org/wiki/II._Elizabeth",
        "https://tr.wikipedia.org/wiki/NATO_%C3%BCyesi_%C3%BClkeler",	
        "https://tr.wikipedia.org/wiki/Instagram",	
        "https://tr.wikipedia.org/wiki/Osmanl%C4%B1_%C4%B0mparatorlu%C4%9Fu",
        "https://tr.wikipedia.org/wiki/Osmanl%C4%B1_padi%C5%9Fahlar%C4%B1_listesi",	
        "https://tr.wikipedia.org/wiki/%C4%B0stanbul",	
        "https://tr.wikipedia.org/wiki/Cristiano_Ronaldo",	
        "https://tr.wikipedia.org/wiki/Montr%C3%B6_Bo%C4%9Fazlar_S%C3%B6zle%C5%9Fmesi",	
        "https://tr.wikipedia.org/wiki/Ukrayna",
        "https://tr.wikipedia.org/wiki/II._Abd%C3%BClhamid",
        "https://tr.wikipedia.org/wiki/Jeffrey_Dahmer",	
        "https://tr.wikipedia.org/wiki/Amerika_Birle%C5%9Fik_Devletleri",	
        "https://tr.wikipedia.org/wiki/Lozan_Antla%C5%9Fmas%C4%B1",
        "https://tr.wikipedia.org/wiki/S%C3%BCper_Lig_%C5%9Fampiyonlar%C4%B1_listesi",	
        "https://tr.wikipedia.org/wiki/UEFA_%C5%9Eampiyonlar_Ligi",	
        "https://tr.wikipedia.org/wiki/D%C3%BCnya",	
        "https://tr.wikipedia.org/wiki/I._S%C3%BCleyman",	
        "https://tr.wikipedia.org/wiki/II._Mehmed",
        "https://tr.wikipedia.org/wiki/II._D%C3%BCnya_Sava%C5%9F%C4%B1",
        "https://tr.wikipedia.org/wiki/Google",	
        "https://tr.wikipedia.org/wiki/Netflix",	
        "https://tr.wikipedia.org/wiki/WhatsApp",
        "https://tr.wikipedia.org/wiki/I._D%C3%BCnya_Sava%C5%9F%C4%B1",	
        "https://tr.wikipedia.org/wiki/Elon_Musk",	
        "https://tr.wikipedia.org/wiki/Lionel_Messi",	
        "https://tr.wikipedia.org/wiki/Rusya",	
        "https://tr.wikipedia.org/wiki/YouTube_eri%C5%9Fiminin_engellenmesi",
        "https://tr.wikipedia.org/wiki/E-Devlet_(T%C3%BCrkiye)",
        "https://tr.wikipedia.org/wiki/Osman_Gazi",	
        "https://tr.wikipedia.org/wiki/S%C3%BCper_Lig",	
        "https://tr.wikipedia.org/wiki/Fenerbah%C3%A7e_(futbol_tak%C4%B1m%C4%B1)",
        "https://tr.wikipedia.org/wiki/Vladimir_Putin",	
        "https://tr.wikipedia.org/wiki/2022_UEFA_%C3%BClkeler_s%C4%B1ralamas%C4%B1",	
        "https://tr.wikipedia.org/wiki/Y%C3%BCz%C3%B6l%C3%A7%C3%BCmlerine_g%C3%B6re_%C3%BClkeler_listesi"
    ]
    
        
#çekilen veriler birleştirilerek düz metin şekline dönüştürülerek işlenmeye hazır hale getirilir.
    text=""
    count=0
    for i in urls:
        count+=1
        a=Article(i)
        a.download()
        a.parse()
        text+=a.text

    return text#düz metin haline getirilen veri toplamını main'e döner.

