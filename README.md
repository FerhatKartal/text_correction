***PROGRAMIN İŞLEVİ***

Metin düzeltme programı , matrisleri kullanarak ,kelimelere gerçek dünyadaki özelliklerini temsil edecekleri değerler verir.

Cümle bazında analiz yaparak cümleyi önce öğelerine ayırır.

Kelimelere atanan ve kelimelerin özelliklerini rakamsal ifadelerle tutan matrisleri kullanarak,önce kelimelerin uyumunu,sonra öğelerinin  mantıksal yönden birbirleriyle uyumluluklarını, metotlarla kontrol eder.

Sonuçta cümlenin mantıklı olup olmadığı bilgisini döner.

***PROGRAMDAKİ METOTLAR***

**main metot** ile programa bir cümle girdisi verilir.

**main metot**'a girilen cümle önce **deneme.py** ye gönderilir.Bu metot cümlenin mantıklı olup olmadığı sonucunu döner.Cümlede eksik yada yanlış kelime varsa harf istatistiklerine göre en yakın olan kelimelerin listesi döner.

**düzelten**,girdide bulunan hatalı kelimeleri tespit eder.

**kelimeler.py**,programın sözlüğüdür.Bu sözlükte kelimelerin matrislerle tutulan halleri bulunur.

**sayac.py**,sözlükte bulunmayan kelimelerin sayısını belirler.

**deneme.py**,main metottan gelen cümleyi analiz eder.

**olumlumu.py**,girdi olarak verilen cümlenin olumlu yada olumsuz olduğunu tespit eder.

**sadelestir.py**,cümledeki kelimeleri eklerinden ayırarak sözlükteki en yalın ,matrislerle temsil edilebilen haline indirger.

**ayıkla.py**,girdi olarak verilen cümleyi öğelerine ayırır.

**on_analiz.py**,nesnelerin birbirleriyle uyumunu kontrol eder.Birbirlerine bağlı nesneler varsa bunları tek bir nesneye indirger.

**analiz.py**,özne-yüklem ve sıfat-nesne uyumunu kontrol eder.

**tekil**,aynı kökten türeyen kelimelerin birbirine karışmasını engeller ve string sonuç döndürür.

**tekil2**,aynı kökten türeyen kelimelerin birbirine karışmasını engeller ve dizi şeklinde sonuç döndürür.

***PROGRAMIN ÇALIŞTIRILMASI***
**"main"** den "run" butonu ile program çalıştırılır.
* Ekranda beliren "Tkinter" arayüzündeki text alanına cumle girilir.
* "Kontrol Et" butonuna basılarak çalıştırılır.
* Program cümlenin analizini yaparak yanlış yada eksik yazılan kelimeler varsa doğrularını önerir,kelimeler doğru girilmişse cümlenin mantıklı olup olmadığı sonucunu döner.

