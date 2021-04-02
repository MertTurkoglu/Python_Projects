boy=float(input("boyunu gir"))
kilo=int(input("kilonu gir"))
bki=(kilo/(boy*boy))
if(bki<18.5):
    print("Zayıf")
elif(bki<25):
    print("Normal")
elif(bki<30):
    print("fazla kilolu")
else:
    print("Obez")