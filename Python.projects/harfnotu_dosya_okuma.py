

def nothesapla(satır):
    satır=satır[:-1]
    liste=satır.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2=int(liste[2])
    not3=int(liste[3])
    final=(not1*0.3)+(not2*0.3)+(not3*0.4)
    if(final>=90):
        harf="AA"
    elif(final>=85):
        harf="BA"
    elif (final >= 80):
        harf = "BB"
    elif (final >=75):
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
        harf="FF"
    return isim+"------------------------->"+ harf + "\n"

with open("dosya.txt","r",encoding="utf-8") as file:
    eklenecekler=[]
    for i in file:
        eklenecekler.append(nothesapla(i))
    print(eklenecekler)
with open("notlar.txt","w",encoding="utf-8") as file2:
    file2.writelines(eklenecekler)


with open("notlar.txt","r",encoding="utf-8")as file3:
    kalanlar=list()
    gecenler=list()
    for i in file3:
        i=i
        liste=i.split(">")
        if(liste[1]=="FF" or liste[1]=="FD"):

            kalanlar.append(liste[0])
        else:
            gecenler.append(liste[0])

with open("kalanlar.txt","w",encoding="utf-8") as file4:
    file4.writelines(kalanlar)
with open("gecenler.txt", "w", encoding="utf-8") as file4:
    file4.writelines(gecenler)










