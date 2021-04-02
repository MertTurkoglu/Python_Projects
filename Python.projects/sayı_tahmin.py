import random
import time
print("""***************************************



sayı tahmin oyunu 1 ile 40 arasında bir sayı tutun




**************************************
""")

sayim=random.randint(1,40)
tahmin_hakki=7
while(True):
    if (tahmin_hakki == 0):
        print("tahmin hakkınız kalmadığı için programdan çıkıldı")
        break

    tahmin = int(input("tuttuğunuz sayıyı girin"))

    if(tahmin<sayim):

        tahmin_hakki -= 1
        print("yanlış tahmin")
        print("tahmininiz tuttuğum sayıdan kucuk")
        print("kalan tahmin hakkınız = ",tahmin_hakki)

    elif(tahmin>sayim):
        print("yanlış tahmin")
        tahmin_hakki -= 1
        print("tahmininiz tuttuğum sayıdan buyuk")
        print("kalan tahmin hakkınız = ", tahmin_hakki)

    elif(tahmin==sayim):
        print("tebrikler doğru tahmin ettiniz")
        break



