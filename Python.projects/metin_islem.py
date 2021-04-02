class Dosya:
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:

            dosya_icerigi=file.read()
            print(dosya_icerigi)
            kelimeler=dosya_icerigi.split()
            print (kelimeler)
            self.sadece_kelimeler=list()
            for i in kelimeler:
                i.split("\n")
                i.split()
                i.split(".")
                i.split(",")
                self.sadece_kelimeler.append(i)
            for i in self.sadece_kelimeler:
                print(i)
    def tum_kelimeler(self):
        kelimeler_kumesi=set()#aynı kelimeyi birden fazla göstermek istemedğim için küme oluşturdum ve tüm kelimeleri kümeye atttım
        for i in self.sadece_kelimeler:
            kelimeler_kumesi.add(i)
        print("Tüm kelimeler................")
        for i in kelimeler_kumesi:
            print(i)
            print("***************************")
    def kelime_frekansı(self):
        kelime_sözlük=dict()
        for i in self.sadece_kelimeler:
            if (i in kelime_sözlük):
                kelime_sözlük[i]+=1
            else:
                kelime_sözlük[i]=1
        print(kelime_sözlük.items())
        for kelime,sayı in kelime_sözlük.items():
            print("{} kelimesi {} defa geçiyor.".format(kelime,sayı))



dosya=Dosya()
dosya.tum_kelimeler()
dosya.kelime_frekansı()