print("Bir sayının bölenlerini bulma programı")

def bolen(sayi):
    liste = list()
    i=1
    while(i<=sayi):
        if(sayi%i==0):
            liste.append(i)
        i=i+1
    return liste

while(True):
    sayi=int(input("bir sayı girin cıkmak icin -1"))
    if(sayi==-1):
        print("programdan cıkıldı")
        break
    else:
        print("sayının bölenleri")
        print(bolen(sayi))


