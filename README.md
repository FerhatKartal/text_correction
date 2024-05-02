***PROGRAMIN İŞLEVİ***

Text Correction, Türkçe Otomatik Metin Düzeltme programıdır.Girdi olarak verilen bir cümledeki kelimelerin birbirleriyle mantıksal bağlamları kurulmaya çalışılmaktadır.

Program girdi olarak aldığı kelimelerden eksik ya da hatalı olanlarını doğru olanıyla değiştirir ve girilen cümleyi mantıksal bağlamda düzelterek kullanıcıya döndürür.

Program geliştirilmekte olduğu için bu aşamada sadece kelimeleri düzeltmektedir. Cümle bazında düzeltmeler için metot eklemeleri devam edecektir.

***PROGRAMDAKİ METOTLAR***

**main.py:** Programı yöneten ana metottur.Arayüz sağlar.

**arrays_and_indexes.py:** veri tabanlarından çekilen verileri kelime uzunluğuna ve toplam harf değerlerine göre gruplandırır.

**otoset.py:** Eksik ya da yanlış girilen kelimelere alternatif kelimeleri bulan metottur.

**correctwords.db:** Türkçe sözlük olarak kullanılan dosyadır.75,775 adet kelime bulunmaktadır.

**data.db:** Cümle bazında analiz yapmak için bu dosyadaki veriler kullanılmaktadır.47,959 adet cümle bulunmaktadır.Bu dosyayı görüntülemek için ,işletim sistemine uygun olan "sqlLite veri tabanı motoru" indirilebilir.

**data_gram2.db:** data.db ve correctwords.txt datalarının bigram versiyonlarını tutar.675,953 adet bigram datası bulunur.

**stop_words:** Metinden bir öznitelik çıkarımı yaparken herhangi bir önem taşımayan kelimelerden kurtulunur.Nltk kütüphanesine aittir.

**text_cleaning:** Metni noktalama işaretlerinden ve özel karakterlerden arındırır.Nltk kütüphanesine aittir.

***PROGRAMIN ÇALIŞTIRILMASI***

Programı VsCode ile çalıştırmak için:

1)cmd açılır.

2)python -m venv <myenv vs. gibi bir dosya adı verilir>

3)"myenv/Scripts/activate" komutu ile dosyaya girilir.

4)"pip install numpy" komutu ile numpy kütüphanesi kurulur.

5)"pip install nltk" komutu ile nltk kütüphanesi kurulur.

6)"pip install textdistance" komutu ile kelime karşılaştırma algoritmalarını içeren kütüphane indirilmelidir.

7)her bir .py uzantılı dosya "python <dosya adı>.py" gibi komutlarla çalıştırılır.

örneğin; "python wordnet.py"

***PROGRAM ARAYÜZÜ***

**mesaj girin:** Kullanıcının cümle girdisi yapacağı alandır.

**öneriler:** Girdi olarak eksik ya da yanlış yazılan kelimelere uygun sonuçların döndürüldüğü alandır.Her kelime için uygun n-gram sonuçlarından döndürülür.

**düzelt butonu:** öneriler bölümünün çalışmasını sağlar.

**temizle butonu:** Arayüzü temizler.
