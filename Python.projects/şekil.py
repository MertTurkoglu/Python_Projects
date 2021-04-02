print("geometrik şekil hesaplama programı")
print("üçgen için 1 e\n"
      "dikdörtgen için 2 ye bas")
işlem=(input("işlemi girin"))
if(işlem=="2"):
    a=int(input("1.kenarı gir"))
    b = int(input("2.kenarı gir"))
    c = int(input("3.kenarı gir"))
    d= int(input("4.kenarı gir"))
    if(a==c and b==d):
        print("girdiğiniz kenarlara göre bu bi dikdörtgen")
    elif(a==b==c==d):
        print("bu bi kare")
    else:
        print("bu bi sıradan dörtgen")
if(işlem=="1"):
    a = int(input("1.kenarı gir"))
    b = int(input("2.kenarı gir"))
    c = int(input("3.kenarı gir"))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")


