# bu dosyayı modül olarak kullancaz

import sqlite3
import time# program daha gerçekçi olsun diye
class Kitap():

    def __init__(self,isim,yazar,yayınevi,tur,baski):
        self.isim=isim
        self.yazar=yazar
        self.yayınevi=yayınevi
        self.tur=tur
        self.baski=baski
    def __str__(self):

        return "Kitap ismi : {}\n Kitabın Yazarı: {}\n Yayınevi :{}\n tur : {}\n baski : {}\n ".format(self.isim,self.yazar,self.yayınevi,self.tur,self.baski)


# asıl işi kütüphane classında yapıcaz
class Kutuphane():
    def __init__(self):
        self.baglantı_olustur()


    def baglantı_olustur(self):
        self.baglanti=sqlite3.connect("Kutuphane.db")# self.baglanti değişkeninini artık veritabanı için yapılan işlemlerde kullancaz(veritabanı kapatma ...)
        self.cursor=self.baglanti.cursor()#self.cursor değişkeni imleç görevi görüyo veritabanına yapılan işlemlerde (select delete update insert gibi işlemlerde kullancaz)
        sorgu=" create table if not exists Kitaplar(İsim TEXT,Yazar TEXT,Yayınevi TEXT,Tur TEXT,Baski INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def kitapları_goster(self):

        sorgu="select * from Kitaplar"
        self.cursor.execute(sorgu)
        liste=self.cursor.fetchall()
        if (len(liste)==0):
            print("kütüphanede hiçbir kitap yok")
        else:
            for i in liste:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)




    def kitap_sorgula(self,isim):
        sorgu="select * from Kitaplar where İsim =?"
        self.cursor.execute(sorgu,(isim,))
        liste=self.cursor.fetchall()
        if(len(liste)==0):
            print("bu isimde bir kitap yok")
        else:
            kitap = Kitap(liste[0][0],liste[0][1],liste[0][2],liste[0][3],liste[0][4])
            print(kitap)
    def kitap_ekle(self,kitap_objesi):
        sorgu ="insert into Kitaplar values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap_objesi.isim,kitap_objesi.yazar,kitap_objesi.yayınevi,kitap_objesi.tur,kitap_objesi.baski))
        self.baglanti.commit()
    def kitap_sil(self,isim):
        sorgu="delete from kitaplar where İsim =?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()
    def baski_yukselt(self,isim):
        sorgu = "select * from Kitaplar where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        liste=self.cursor.fetchall()
        if (len(liste)==0):
            print(isim,"adlı bir kitap yok")
        else:
            baski=liste[0][4]
            sorgu2 = "update Kitaplar set Baski=? where İsim= ?"
            self.cursor.execute(sorgu2,(baski+1,isim))
            self.baglanti.commit()




