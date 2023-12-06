from tokenization import sentTokenize
from pos_tag import posTag
from stop_words import stopWords

# main'den gelen düz metni etiketler.
def createList(text):

    #metin cümlelere ayrıldıktan sonra ,cümle içindeki ogeler tespit edilir
    #art arda gelen aynı ogeler tek bir blok oge olarak ele alınır
    liste=[]    #metnin cümlelerinin ogelere ayrılmış olan durumunu tutar
    arr=sentTokenize(text) #metni cümlelere ayıran fonksiyon 


    for sents in arr:   #her bir cümle üzerinde gezinilir

        sentToWords=posTag(sents)#cümleleri kelimelere böler

        sublist=[]  #cümlelerin ogelere ayrılmış olan durumunu tutar
        insublist=[] #art arda gelen aynı ogeleri tutar
        count=0  
        for word in sentToWords:   #cümle içindeki her bir kelime  üzerinde gezinir
            stopControl=stopWords(word[0]) #cümle anlam önemi olmayan kelimelerden tamizlenir
            if(stopControl and len(word[0])>1): #kelime anlamsız değilse ve ".,><" gibi bir karakter değilse işleme alınır
                if(insublist==[]):#kelime ogelerinin tekrarlı olanları bulmak için geçici listelere atılır(liste işlemin başında boştur)
                    insublist.append(word)
                    sublist.append(insublist)
                elif( word[1].__eq__(insublist[-1][1])):#kelime ogesi bir önceki ile aynıysa aynı gruba alınır
                    insublist.append(word)
                    count+=1
                else: #kelime ögesi bir öncekiyle aynı değilse ayrı liste elemanı olarak işleme devam eder
                    if(count==0):
                        sublist.pop()
                    sublist.append(insublist)
                    insublist=[word]
                    count+=1
        sublist.append(insublist)
        liste.append(sublist)#ögeleri belirlenerek,gruplandırılan cümle metne aktarılır
    return liste#etiketlenen metin main'e döndürülür.