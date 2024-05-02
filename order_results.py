import numpy as np

def order_result(results,data):     #ngram datalarını uygun cümleye çeviren metot

    data_splited=data.split(" ")
    data_len=len(data_splited)
    matris = []
    matris2=[]
    number_arr=[]
    max_num=0
    for i in range(data_len):
        satir = []     
        matris.append(satir)

    results_arr=results.split(",")
    for k in results_arr:
        splited_k=k.split("-")
        if(len(splited_k)==2):
            num=int(splited_k[1])
            number_arr.append(num)
            if(num>max_num):
                max_num=num
            text=splited_k[0]
            matris[num].append(text)
    
    for i in range(len(data_splited)):
        if(number_arr.count(i)==0):
            matris[i]=[data_splited[i]]

    
    v=0
    for i in matris:
        if(v==0):
            matris2.append(i[0])
        else:
            for j in i:
                k=matris2[-1].split(" ")
                if(k[-2]==j[0]):
                    matris2.append(j)
                    break

    sceen=""
    z=0
    for i in matris2:
        if(z==0):
            sceen+=i+" "
        else:
            f=i.split(" ")
            if(len(f)==2):
                sceen+=f[1]+" "
        z+=1
    return sceen
   

  