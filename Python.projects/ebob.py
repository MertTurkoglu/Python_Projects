def ebob(a,b):

    i=1


    while(i<=a and i<=b ):
        if(a%i==0 and b%i==0):
            ebob = i
        i=i+1

    return ebob



print(ebob(18,24))

while(True):
    sayi1=int(input("1.sayıyı gir cıkmak icin -1 e bas"))
    sayi2 = int(input("2.sayıyı gir cıkmak icin yeniden -1 e bas"))
    if (sayi1 == -1):
        print("programdan cıkıldı")
        break


    else:
        print(sayi1,"ve", sayi2,"nin ebobu", ebob(sayi1,sayi2))
        


