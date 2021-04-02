print("faktöriyel bulma programı")
while(True):
    sayi = int(input("faktöriyeli öğrenmek istediğiniz sayi(cıkmak icin-1 e bas"))
    if(sayi==0 or sayi == 1):
        print("{}! = {}".format(sayi, 1))
        continue
    elif(sayi==-1):
        print("programdan cıkıldı")
        break
    i = 1
    carpim = 1
    while (i <= sayi):
        carpim = carpim * i
        i = i + 1
    print("{}! = {}".format(sayi, carpim))






