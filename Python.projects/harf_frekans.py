'''
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
'''
string="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
kelime_ve_sayısı=dict()
for i in string:
    if(i in kelime_ve_sayısı):
        kelime_ve_sayısı[i]+=1
    else:
        kelime_ve_sayısı[i]=1

print(kelime_ve_sayısı)
print(kelime_ve_sayısı.items())
for i,j in kelime_ve_sayısı.items():
    print("{} metinde {} defa geçiyor".format(i,j))