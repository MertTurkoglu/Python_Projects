from ply.yacc import yacc

print("ATM programı\n"
      "bakiye sorgulamak icin 1\n"
      "para cekmek icin 2\n"
      "para yatırmak icin 3\n"
      "cıkmak icin q ya basın"
      )
bakiye=1000
while(True):
    islem=input("işlemi girin")
    if(islem=="1"):
        print("bakiyeniz = ",bakiye)
    elif(islem=="2"):
        cekilen_para = int(input("cekmek istediğiniz tutar"))
        if(cekilen_para>bakiye):
            print("cekmek istediğiniz tutar bakiyeden büyük olmamalı (bakiyeniz = ",bakiye)
        else:
            bakiye = bakiye-cekilen_para
            print("yeni bakiyeniz = ",bakiye)
    elif(islem=="3"):
        yatirilan_tutar=int(input("yatırmak istediğiniz tutar"))
        bakiye = bakiye + yatirilan_tutar
        print("yeni bakiyeniz: ",bakiye)
    elif(islem=="q"):
        print("programdan cıkıldı")
        break
    else:
        print("yanlış islem")
