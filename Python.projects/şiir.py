'''
Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun
ve bu string'i ekrana yazdırın.
'''
with open("şiir.txt","r",encoding="utf-8")as file:
    basharfler=""
    for i in file:
        basharfler+=i[0]


print(basharfler)
