'''Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.

liste = ["345","sadas","324a","14","kemal"]

Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın.
'''

liste = ["345","sadas","324a","14","kemal"]

sayılar=list()
for i in liste:
    try:
        rakam = int(i)
        sayılar.append(i)
    except ValueError:
        pass
print("listedeki sayılar")
print(sayılar)