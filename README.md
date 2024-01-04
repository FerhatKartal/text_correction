***PROGRAMIN İŞLEVİ***

Program, Türkçe Metin Düzenleme için yapay zeka ve makine öğrenmesi kullanmaktadır. NLP kütüphanesi kullanılarak,veri analizi yapılmaktadır.Veriler cümlelere ve kelimelere ayrılarak ,öğeler tespit edilecek,kelimelerin birbirleriyle mantıksal bağlamları kurulacak ve program girdi olarak verilen cümlelerin mantıksal yönünü denetleyecektir.

Program geliştirilme aşamasında olduğu için amaca yönelik metot eklemeleri devam edecektir.

***PROGRAMDAKİ METOTLAR***

**main.py:** Programı yöneten ana metottur.

**createList.py:** Veri setini etiketleyen metottur.

**otoset.py:** Eksik ya da yanlış girilen kelimeler için veri tabanındaki yakın kelimeleri bulur.

**database.py:** Database tablosu oluşturan ve etiketlenen veriyi tabloya kaydeden metottur.

**data.db:** Program tarafından oluşturulan database dosyasıdır.Bu dosyayı açmak için ,işletim sistemine uygun olan "sqlLite veri tabanı motoru" indirilmelidir.

**text.py:** Veri setini tutar.

**pos_tag:** Bu fonksiyon sayesinde, cümlemizdeki özel isimleri, sıfatları vb. bulabiliriz.

**stop_words:** Metinden bir öznitelik çıkarımı yaparken herhangi bir önem taşımayan kelimelerden kurtulunur.

**text_cleaning:** Metni noktalama işaretlerinden ve özel karakterlerden arındırmak. 

**tokenization:** Ham metni cümle ve kelimelere ayırır.

**wordnet:** İki kelimenin birbirine olan benzerlik oranını hesaplar.

**sentControl:** Arayüzden girilen cümleyi cümleyi database ile taratarak benzer cümle kalıplarını döner.

**wordControl:** Arayüzden girilen kelimeleri database taraması yaparak bir sonraki kelimeyi ve öge kalıplarını tahmin eder.

***PROGRAMIN ÇALIŞTIRILMASI***

Programı VsCode ile çalıştırmak için:

1)cmd açılır.

2)python -m venv <myenv vs. gibi bir dosya adı verilir>

3)"myenv/Scripts/activate" komutu ile dosyaya girilir.

4)"pip install numpy" komutu ile numpy kütüphanesi kurulur.

5)"pip install nltk" komutu ile nltk kütüphanesi kurulur.

6)her bir .py uzantılı dosya "python <dosya adı>.py" gibi komutlarla çalıştırılır.

örneğin; "python wordnet.py"

7)"pip install fuzzywuzzy"
  "pip install python-Levenshtein" komutları ile fuzzywuzzy kütüphanesi indirilmelidir.Bu kütüphane iki kelimeyi karşılaştırarak benzerlik oranını hesaplar.

***PROGRAM ARAYÜZÜ***

**bunu mu demek istediniz?:** Eksik yada yanlış girilen kelimeler için anlık olarak uygun kelimeler önerir.

**sonraki_kelimeleri_tahmin_et butonu:** Girilen kelimeye uygun kalıp ögeleri döner ve bir sonraki kelime tahminleri yapar.

**cümle_öner butonu:** Girilen anahtar kelimeleri kullanarak uygun bir cümle önerisi yapar.

**temizle butonu:** Arayüzü temizler.
