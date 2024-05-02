def analize(_data,total):
      _data=_data.strip() 
      if(len(_data)==2):  #girdi kelimesine uygun olan dizi belirlenir
          w=total[0]
          z=total[9]
      elif(len(_data)==3):
        w=total[1] 
        z=total[10]
      elif(len(_data)==4):
        w=total[2]
        z=total[11] 
      elif(len(_data)==5):
        w=total[3] 
        z=total[12]
      elif(len(_data)==6):
        w=total[4] 
        z=total[13]
      elif(len(_data)==7):
        w=total[5] 
        z=total[14]
      elif(len(_data)==8):
        w=total[6] 
        z=total[15]
      elif(len(_data)==9):
        w=total[7]
        z=total[16]
      elif(len(_data)>9):
        w=total[8] 
        z=total[17]  

      return w,z           