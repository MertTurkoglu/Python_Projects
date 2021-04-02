print("armstrong Number programı")
basamak_sayisi=0
sayi=input("sayiyi girin")
basamak_sayisi=len(sayi)
sayi=int(sayi)
basamak = 0
toplam = 0
gecici_sayi = sayi
while(gecici_sayi>0):
    basamak=gecici_sayi%10
    toplam = toplam+basamak**basamak_sayisi
    gecici_sayi=gecici_sayi // 10
if(toplam==sayi):
    print(sayi,"bir armstrong sayisi")
else:
    print(sayi,"bir armstrong sayısı değildir")
