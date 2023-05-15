***PROGRAMIN İŞLEVİ***

metin düzeltme programı , matrisleri kullanarak ,kelimelere gerçek dünyadaki özelliklerini temsil edecekleri değerler verir.
cümle bazında analiz yaparak cümleyi önce öğelerine ayırır.
kelimelere atanan ve kelimelerin özelliklerini rakamsal ifadelerle tutan matrisleri kullanarak,önce kelimelerin uyumunu,sonra öğelerinin   mantıksal yönden birbirleriyle uyumluluklarını, metotlarla kontrol eder.
sonuçta cümlenin mantıklı olup olmadığı bilgisini döner.

***PROGRAMDAKİ METOTLAR***

**main metot** ile programa bir cümle girdisi verilir.
cümle önce **duzelten.py** ye gönderilir.Burada cümlede eksik yada yanlış kelime varsa harf istatistiklerine göre en yakın olan kelimelerin listesi döner.
**kelimeler.py**,programın sözlüğüdür.Bu sözlükte kelimelerin matrislerle tutulan halleri bulunur.
**olumlumu.py**,girdi olarak verilen cümlenin olumlu yada olumsuz olduğunu tespit eder.
**sadelestir.py**,cümledeki kelimeleri eklerinden ayırarak sözlükteki en yalın ,matrislerle temsil edilebilen haline indirger.
**ayıkla.py**,girdi olarak verilen cümleyi öğelerine ayırır.
**on_analiz.py**,nesnelerin birbirleriyle uyumunu kontrol eder.Zincirleme nesneler varsa bunları tek bir nesneye indirger.
**analiz.py**,özne-yüklemin ve sıfat-nesne uyumunu kontrol eder.
