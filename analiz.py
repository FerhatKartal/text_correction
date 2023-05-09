
#ozne ve yuklemin uyumluluğunu kontrol eder
def ozne_yuklem_analiz(ozne,fiil):
    hedef=fiil[-1][-3]
    if ozne[0][hedef][0]==1:
        return 1
    else:
        return 0

#sıfat ve nesnenin uyumluluğunu kontrol eder
def sifat_nesne_analiz(sifat_listesi,nesne_listesi):
    for i in range(len(sifat_listesi)):
        for j in range(len(nesne_listesi)):
            if (sifat_listesi[i][-1]==nesne_listesi[j][-1][0]):
                hedef=sifat_listesi[i][1]
                if (nesne_listesi[j][hedef][0]==1):
                    return 1
                else:
                    return 0

"""
bu fonksiyon henüz tamamlanmadı,simdilik True dönüyor
nesne ve ara fiil uyumunu kontrol eder
"""
def nesne_yuklem_analiz(nesneListesi,fiilListesi):
    return 1