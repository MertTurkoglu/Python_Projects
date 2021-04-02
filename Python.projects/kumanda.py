import random
import time
class Kumanda():
    def __init__(self,tv_durumu="Kapalı",tv_ses=0,kanal_listesi=["Trt"],mevcut_kanal="Trt"):
        self.tv_durumu=tv_durumu
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.mevcut_kanal=mevcut_kanal

    def tv_ac(self):
        if(self.tv_durumu == "Açık"):
            print("tv zaten acık")
        else:
            print("televizyonunuz açıldı")
            self.tv_durumu="Açık"
    def tv_kapa(self):
        if(self.tv_durumu=="Kapalı"):
            print("tvniz zaten kapalı")
        else:
            self.tv_durumu="Kapalı"
    def ses_ayarları(self):
        while(True):
            işlem=input("ses arttırmak için >\n azaltmak için <\nçıkmak için q ya bas")
            if(işlem==">"):

                if( self.tv_ses!=100):
                    self.tv_ses = self.tv_ses + 1
                    print("tv sesi = ", self.tv_ses)

                else:
                    print("ses seviyesi 100 zaten daha da artamaz")

            elif(işlem=="<"):
                if (self.tv_ses != 0):
                    self.tv_ses = self.tv_ses - 1
                    print("tv sesi = ", self.tv_ses)
                else:
                    print("ses seviyesi 0 zaten daha da azalamaz")



            elif(işlem=="q"):
                print("ses güncellendi")
                print("tv sesi = ", self.tv_ses)
                break
            else:
                print("geçersiz işlem girdiniz")

    def kanal_ekle(self,yeni_kanal):
        print("kanal ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(yeni_kanal)
        print("kanal eklendi")
    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi))
        self.mevcut_kanal=self.kanal_listesi[rastgele]
        print("mevcut kanal = " ,self.mevcut_kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "tv_durumu={}\ntv sesi = {}\nkanal listesi ={}\nmevcut kanal={}".format(self.tv_durumu,self.tv_ses,self.kanal_listesi,self.mevcut_kanal)


kumanda1=Kumanda()

print("""
*****************************************************

uzaktan tv kumandası programı

1.Tv aç
2.Tv kapa
3.sesi ayarla
4.kanal ekle
5.rastgele kanala geçme
6.kanal sayısını öğrenme
7.tv bilgileri öğrenme için başındaki numaraları girin
çıkmak için q ya bas


*******************************************************




""")
while(True):

    islem=input("işlemi girin")
    if(islem=="q"):
        print("programdan çıkıldı")
        break
    elif(islem=="1"):
        kumanda1.tv_ac()
    elif(islem=="2"):
        kumanda1.tv_kapa()
    elif(islem=="3"):
        kumanda1.ses_ayarları()
    elif(islem=="4"):
        kanal_adı=input("eklencek kanallarının adı ',' ile ayırarak girin")
        kanal_listesi=kanal_adı.split(",")
        for eklenecek_kanallar in kanal_listesi:
            kumanda1.kanal_ekle(eklenecek_kanallar)
    elif(islem=="5"):
        kumanda1.rastgele_kanal()
    elif(islem=="6"):
        print("kanal sayısı = ",len(kumanda1))
    elif(islem=="7"):
        print(kumanda1)
    else:
        print("geçersiz işlem")







