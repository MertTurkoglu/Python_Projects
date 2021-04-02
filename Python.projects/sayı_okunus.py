print("2 basamaklı sayıyı okuma programı\n***********************")
birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
def okunus(sayi):
    birler_basamagı=sayi%10
    onlar_basamagı=sayi//10
    return onlar[onlar_basamagı]+" "+birler[birler_basamagı]
while(True):
    sayi = int(input("2 basamaklı sayıyı gir(cıkmak icin -1 e bas)"))
    if(sayi==-1):
        print("programdan cıkıldı...")
        break
    print(okunus(sayi))

