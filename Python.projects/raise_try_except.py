'''
Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın.
Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün.
Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın.
Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın
ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.
'''
def cıftler(sayı):
    if(sayı%2==0):
        return sayı
    else:
        raise ValueError("bu sayı tek")
liste=[1,2,3,4,5,6,7,8,9,10]
for i in liste:
    try:
        print(cıftler(i))
    except ValueError:
        pass # pass komutu bir bloğa bişey yazmak istemediğimde kullanabilirim bu şekilde hata almam


