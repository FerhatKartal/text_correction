***PROGRAMIN İŞLEVİ***

Text Correction, Türkçe Otomatik Metin Düzeltme programıdır.Girdi olarak verilen bir cümledeki kelimelerin birbirleriyle anlamsal bağlamları kurulmaya çalışılmaktadır.

Program girdi olarak aldığı kelimelerden eksik ya da hatalı olanlarını doğru olanıyla değiştirir ve girilen cümleyi anlamsal bağlamda düzelterek kullanıcıya döndürür.


***PROGRAMDAKİ METOTLAR***

**main.py:** Programı yöneten ana metottur.Arayüz sağlar.

**arrays_and_indexes.py:** veri tabanlarından çekilen verileri kelime uzunluğuna ve toplam harf değerlerine göre gruplandırır.

**otoset.py:** Eksik ya da yanlış girilen kelimelere alternatif kelimeleri bulan metottur.

**correctwords.db:** Türkçe sözlük olarak kullanılan dosyadır.75,775 adet kelime bulunmaktadır.

**correctwords.py:** correctwords.db datalarını çeker.

**data_analize.py:** Girdiye uygun data gruplarını belirler.

**dataPure.db:** Cümle bazında analiz yapmak için bu dosyadaki veriler kullanılmaktadır.47,959 adet cümle bulunmaktadır.

**data_set.db:** Ekli halleri bulunan kelimeleri tutar.

**data_set.py:** data_set.db datalarını çeker.

**data_gram2.db:** data.db ve correctwords.txt datalarının bigram versiyonlarını tutar.675,953 adet bigram datası bulunur.

**data_gram2.py:** data_gram2.db verilerini çeker.

**data_postag.db:** verilerin etiketlenmiş halini içerir.

**fetch_data_postag.py:** data_postag.db'den verileri çeker.

**data_postag.py:** çıktıların kelime analizlerini yapar.

**order_result.py:** n_gram datalarını normal cümleye çevirir.

**result.py:** düzeltilen girdi datalarını n_gram datalarıyla karşılaştırır.

**stop_words:** Metinden bir öznitelik çıkarımı yaparken herhangi bir önem taşımayan kelimelerden kurtulunur.Nltk kütüphanesine aittir.

**text_cleaning:** Metni noktalama işaretlerinden ve özel karakterlerden arındırır.Nltk kütüphanesine aittir.

**_zemberek.py:** Zemberek kütüphanesi aracılığıyla kelime analizi yapılmaktadır.

***PROGRAMIN ÇALIŞTIRILMASI***

Programı VsCode ile çalıştırmak için:

1)cmd açılır.

2)python -m venv <myenv vs. gibi bir dosya adı verilir>

3)"myenv/Scripts/activate" komutu ile dosyaya girilir.

4)"pip install numpy==1.26.4" komutu ile numpy kütüphanesi kurulur.

5)"pip install nltk==3.8.1" komutu ile nltk kütüphanesi kurulur.

6)"pip install zemberek-python==0.2.3" komutu ile zemberek kütüphanesi kurulur.

7)"pip install textdistance==4.6.2" komutu ile kelime karşılaştırma algoritmalarını içeren kütüphane indirilmelidir.

8)"setuptools==69.5.1" versiyonunda olmalıdır.

9)her bir .py uzantılı dosya "python <dosya adı>.py" gibi komutlarla çalıştırılır.

örneğin; "python wordnet.py"

***PROGRAM ARAYÜZÜ***

**mesaj girin:** Kullanıcının cümle girdisi yapacağı alandır.

**öneriler:** Girdideki eksik ya da yanlış yazılan kelimeleri düzelterek uygun cümle sonuçlarının döndürüldüğü alandır.Sonuç için uygun n-gram sonuçları ve veri tabanı istatistik sonuçları döndürülür.

**düzelt butonu:** öneriler bölümünün çalışmasını sağlar.

**temizle butonu:** Arayüzü temizler.
