a=int(input("denklemin  a sı: "))
b=int (input("denklemin b si :" ))
c = int (input("denklemin c si : "))
delta= float(b**-(4*a*c))
birinci_kök= (-b - delta**0.5)/2*a
ikinci_kök=(-b + delta**0.5)/2*a
print("denklemin 1.kökü : {}\n  denklemin2.kökü = {} ".format(birinci_kök,ikinci_kök))
