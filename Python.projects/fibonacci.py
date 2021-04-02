#22 tane sayının bulunudğu fibonacci serisi
'''fib0=1
fib1=1
count=1
while(count<=20):
    print(fib0,fib1)
    i = fib0 + fib1
    fib0 = fib1
    fib1 = i
    count=count+1
'''
fib0=1
fib1=1
list=[fib0,fib1]
for i in range(20):

    fib2=fib0+fib1
    fib0=fib1
    fib1=fib2

    list.append(fib2)
print(list)



