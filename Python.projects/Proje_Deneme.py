from kütüphane import *
#kütüphane.py dosyasını import ettik o dosyada Kütüphane ve kitap classsını ve fonksiyonlarını kullanabiliriz
print(""""**************************************

Kütüphane programına hoşgeldiniz
işlemler
1.kitapları göster
2.kitap sorgula
3.kitap ekle
4.kitap sil
5.baskı yükselt
çıkmak için q ya bas

*****************************************





""")


kütüphane=Kutuphane()
while(True):
    işlem=input("yapacağınız işlemin numarasını girin")
    if (işlem=="q"):
        print("programdan çıkıldı")
        break
    elif(işlem=="1"):
        kütüphane.kitapları_goster()

    elif (işlem == "2"):
        isim=input("sorgulamak istediğiniz kitap")
        print("kitabınız sorgulanıyor")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
    elif (işlem == "3"):
        isim=input("kitabın ismini girin ")
        yazar = input("kitabın yazarını girin ")
        yayınevi = input("kitabın yayınevini girin ")
        tur = input("kitabın turunu girin ")
        baski = int(input("kitabın baskı adedini girin "))
        print("kitap ekleniyor")
        time.sleep(2)
        kitap=Kitap(isim,yazar,yayınevi,tur,baski)
        kütüphane.kitap_ekle(kitap)
        print("kitap eklendi")

    elif (işlem == "4"):
        isim =input("hangi kitabı silmek istiyorsunuz")
        emin_misin=input("emin misin E/H e evet H hayır")
        if (emin_misin=="E"):
            print("kitabınız siliniyor")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("kitap silindi")
    elif (işlem == "5"):
        isim=input("baskısını arttırmak istedğiniz kitabın adı : ")
        print("baskı yükseltiliyor")
        time.sleep(2)
        kütüphane.baski_yukselt(isim)
        print("baski yükseltildi")


    else:
        print("geçersiz işlem")

























