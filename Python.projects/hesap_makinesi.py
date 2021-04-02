print("hesap makinesi programı")
print("Toplama işlemi için +\n"
      "çıkarma işlemi için -\n"
      "çarpma işlemi için *\n"
      "bölme işlemi için / 'e basın                      "
      )
sayi1=int(input("bir sayi gir"))
sayi2=int(input("bir sayi gir"))
işlem=input("işlemi girin")

if(işlem=="+"):
    print("{} + {} = {} ".format(sayi1,sayi2,sayi1+sayi2))
elif(işlem=="-"):
    print("{} - {} = {} ".format(sayi1, sayi2, sayi1 - sayi2))
elif(işlem=="*"):
    print("{} x {} = {} ".format(sayi1, sayi2, sayi1 * sayi2))
elif(işlem=="/"):
    print("{} / {} = {} ".format(sayi1, sayi2, sayi1 / sayi2))
else:
    print("gecersiz işlem")

