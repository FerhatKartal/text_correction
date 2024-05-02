def arrayAndIndexes(total):
    
    iki=[]         #veri aramasını hızlandırmak için datalar kelime uzunluğuna göre gruplara ayrılır
    uc=[]
    dort=[]
    bes=[]
    alti=[]
    yedi=[]
    sekiz=[]
    dokuz=[]
    on=[]
    iki_index=[]         #veri aramasını hızlandırmak için datalar kelimelerdeki harflerin değerlerinin toplamına göre gruplara ayrılır
    uc_index=[]
    dort_index=[]
    bes_index=[]
    alti_index=[]
    yedi_index=[]
    sekiz_index=[]
    dokuz_index=[]
    on_index=[]

    total_index=[]
    for k in total:
        x=k.lstrip()
        c=0
        for i in x:
            c+=(ord(i))
        
        total_index.append(c)
        
        

    for i in range(len(total)):
        s=i
        i=str(total[i])
        if(len(i)==1 or len(i)==2 or len(i)==3):
            iki.append(i)
            iki_index.append(total_index[s])
        if(len(i)==2 or len(i)==3 or len(i)==4):
            uc.append(i)
            uc_index.append(total_index[s])
        if(len(i)==3 or len(i)==4 or len(i)==5):
            dort.append(i)
            dort_index.append(total_index[s])
        if(len(i)==4 or len(i)==5 or len(i)==6):
            bes.append(i)
            bes_index.append(total_index[s])
        if(len(i)==5 or len(i)==6 or len(i)==7):
            alti.append(i)
            alti_index.append(total_index[s])
        if(len(i)==6 or len(i)==7 or len(i)==8):
            yedi.append(i)
            yedi_index.append(total_index[s])
        if(len(i)==7 or len(i)==8 or len(i)==9):
            sekiz.append(i)
            sekiz_index.append(total_index[s])
        if(len(i)==8 or len(i)==9 or len(i)==10):
            dokuz.append(i)
            dokuz_index.append(total_index[s])
        if(len(i)==9 or len(i)>=10):
            on.append(i)
            on_index.append(total_index[s])

    return iki,uc,dort,bes,alti,yedi,sekiz,dokuz,on,iki_index,uc_index,dort_index,bes_index,alti_index,yedi_index,sekiz_index,dokuz_index,on_index