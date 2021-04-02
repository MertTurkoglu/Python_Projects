liste = list(range(1,101))
liste2=[]
print(liste)
for i in liste:
    if(i%2==0):
        liste2.append(i)
print(liste2)
liste3=[i for i in liste if i%2==0]
print(liste3)
