import os
from path import path
 
KAYNAK = 'C:/Users/DCBidab/Desktop/hedef/a'  # Müziklerin bulunduğu dizin
HEDEF = 'C:/Users/DCBidab/Desktop/kaynak/a_copy'  # Müziklerin Kopyalanacağı Dizin
 
k = Path(KAYNAK)  #KAYNAK Adlı değişken string bir ifadedir . Bu ifadeyi Path tipine dönüştürüyoruz .
h = Path(HEDEF) #HEDEF Adlı değişken string bir ifadedir . Bu ifadeyi Path tipine dönüştürüyoruz .
 
print("\n\nKAYNAK adlı değişkenin tipi : %s" % type(KAYNAK))
print("k adlı değişkenin tipi : %s " % type(k))
 
print("\n\nHEDEF adlı değişkenin tipi",type(HEDEF))
print("h adlı değişkenin tipi",type(h))
 
def transfer():
    print ("\n\nDosyalar %s adresinden %s adresine kopyalanıyor !!\n" % (k, h))
    dosya_sayisi = 0
    for i in k.walk(): #dizinin içindek dosyaları gez
        if i.isfile() and i.endswith("mp3"): #eğer mevcut indiste bir mp3 uzantılı dosya var ise
 
            dosya_sayisi += 1 #dosya sayısını artır
            print("Kopyalanıyor %s" % i)
            i.copy(h) #hedefe mevcut indisteki mp3 uzantılı dosyayı kopyala
 
 
    if (dosya_sayisi == 0):
        print("Mevcut dizinde .mp3 uzantılı dosya bulunamadı ! ")
    else:
        print("\n%s adet dosya başarılı şekilde kopyalandı" % dosya_sayisi)
 
 
 
if __name__ == "__main__":
    if(os.path.exists(KAYNAK)):
        transfer()
    else:
        print("\n\nDosya Yolu Bulunamadı")
