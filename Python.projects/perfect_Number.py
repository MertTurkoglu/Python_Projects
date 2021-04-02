print("perfect number programı")
while(True):
    number=int(input("sayıyı girin (cıkmak icin -1 e bas)"))
    if(number==-1):
        print("programdan cıkıldı")
        break
    i=1
    sum = 0
    while(i<number):
        if(number%i==0):
            sum=sum+i
        i=i+1
    if(sum==number):
        print("this Number = ", number, "is a perfect number")
    else:
        print("this Number = ", number, "is not a perfect number")



