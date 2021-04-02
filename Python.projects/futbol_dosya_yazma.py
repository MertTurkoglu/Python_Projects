with open("futbolcu.txt","r",encoding="utf-8")as file:
    fb=list()
    gs=list()
    bjk=list()
    for i in file:
        i=i[:-1]
        liste=i.split(",")
        if(liste[1]=="Fenerbahçe"):
            fb.append(liste[0]+"\n")
        elif(liste[1]=="Galatasaray"):
            gs.append(liste[0]+"\n")
        elif (liste[1] == "Beşiktaş"):
            bjk.append(liste[0]+"\n")

print(fb)
print(bjk)
with open("fb.txt","w",encoding="utf-8")as file:
    file.writelines(fb)

with open("gs.txt", "w", encoding="utf-8")as file:

    file.writelines(gs)
with open("bjk.txt","w",encoding="utf-8")as file:
    file.writelines(bjk)
