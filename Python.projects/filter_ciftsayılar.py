'''
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

'''
from functools import reduce
liste=[1,2,3,4,5,6,7,8,9,10]
ciftler=list(filter(lambda x:x%2==0,liste))
print(ciftler)
cift_toplam=reduce(lambda x,y:x+y,ciftler)
print(cift_toplam)
def cift(liste):
    listem=list()
    for i in liste:
        if(i%2==0):
            listem.append(True)
        else:
            listem.append(False)
    return listem

print(cift(liste))

