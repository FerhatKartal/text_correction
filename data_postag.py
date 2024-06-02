from _zemberek import zbrkc

#sonuçların herbirinin veri tabanında bulunması durumunun istatistiğini çıkarır

def postag_analize(words_arr,postag_data):
    words_arr_core=[]
    
    for i in words_arr:
         words_core=[]
         for j in i:
              words_core.append(zbrkc(j).lower())
         words_arr_core.append(words_core)

    count=0
    for word in words_arr_core:
        s=[]
        for i in range(len(word)-1):
             s.append(0)

        for postag in postag_data:                
                for w in range(len(word)-1):
                    if(postag.__contains__(word[w]) and postag.__contains__(word[-1])):
                        s[w]+=1
        words_arr[count].append(str(s))
        count+=1
    return words_arr
