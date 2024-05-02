def results(_total_arr,n2grams):
     deneme=[]
     hepsi=""
     for i in range(len(_total_arr)):#benzer kelimeleri ngram analizini yapar.     
         if(i<len(_total_arr)-1):
            for k in _total_arr[i]:
                for j in _total_arr[i+1]:
                    if(n2grams.__contains__(k+" "+j)):
                        deneme.append(k+" "+j+"-"+str(i))
                    
     for l in deneme:           #ngram sonuçlarını main'e gönderir.
         if(len(l)>0):
                hepsi+=str(l)+","

     return hepsi