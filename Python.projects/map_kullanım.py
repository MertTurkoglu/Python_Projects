'''
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve
bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]

'''
def func(liste):
    return liste[0]*liste[1]

liste=[(3,4),(10,3),(5,6),(1,9)]
print()

sonuc=list(map(func,liste))
print(sonuc)




