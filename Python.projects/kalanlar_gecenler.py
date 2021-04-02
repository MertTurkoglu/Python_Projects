'''Kodlama egzersizimizde bir sınıfın harf notlarını hesapladığımız programı geliştirerek
kalanları "kalanlar.txt" dosyasında ve geçenleri "geçenler.txt" dosyasına yazmaya çalışın.'''
def nothesapla(satır):
    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    final = (not1 * 0.3) + (not2 * 0.3) + (not3 * 0.4)
    if (final >= 90):
        harf = "AA"
    elif (final >= 85):
        harf = "BA"
    elif (final >= 80):
        harf = "BB"
    elif (final >= 75):
        harf = "CB"
    elif (final >= 70):
        harf = "CC"
    elif (final >= 65):
        harf = "DC"
    elif (final >= 60):
        harf = "DD"
    elif (final >= 55):
        harf = "FD"
    else:
        harf = "FF"
    return isim + "------------------------->" + harf + "\n"




with open("dosya.txt","r",encoding="utf-8") as file:

    for i in file:
        print(i)
with open("notlar.txt","w",encoding="utf-8") as file2:
    pass
    #file2.writelines(eklenecekler)