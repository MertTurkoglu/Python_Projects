hak=3
nickname="merdo"
password="merdo123"
while(hak!=0):
    girilen_isim=input("kullanıcı adını gir")
    girilen_sifre=input("şifreni gir")
    if(girilen_isim!=nickname and girilen_sifre==password):
        hak=hak-1
        print("kullanıcı adı yanlıs(kalan hakkınız {} )".format(hak))
    elif(girilen_isim==nickname and girilen_sifre!=password):
        hak= hak-1
        print("sifre yanlıs(kalan hakkınız {} )".format(hak))
    elif(girilen_isim!=nickname and girilen_sifre!=password):
        hak = hak-1
        print("hem kullanıcı adı hem sıfre yanlıs(kalan hakkınız {} )".format(hak))
    else:
        print("giris yapildi")
        break

