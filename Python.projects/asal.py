print("asal sayı mı değil mi programı")
def asal(sayi):
    if(sayi==1):
        return False

    if(sayi==2):
        return True

    else:
        for i in range(2,sayi):
            if(sayi%i==0):
                return False
        return True

while(True):

    sayi = int(input("bir sayı girin cıkmak icin -1 e bas"))
    if (asal(sayi) == False):
        print("sayi:", sayi, " asal bir sayı değil")
    elif(sayi==-1):
        print("programdan cıkıldı")
        break
    else:
        print("sayi:", sayi, " asal bir sayı ")










