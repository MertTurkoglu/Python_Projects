print("1 ile 1000 arasındaki mükemmel sayıları ekrana basan program")

def mukemmel_sayi(sayi):
    i=1
    sum=0
    while(i<sayi):

        if(sayi%i==0):
            sum = sum+i
        i=i+1

    if(sum==sayi):
        return True
    else:
        return False


liste=list()
for i in range(1,1000):

    if (mukemmel_sayi(i) == True):
        liste.append(i)

print("1 ila 1000 arasındaki mükemmel sayılar")
print(liste)
print(mukemmel_sayi(6))







