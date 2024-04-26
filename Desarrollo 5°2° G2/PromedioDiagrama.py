a=int(input("Ingrese la primera nota: "))
b=int(input("ingrese la segunda nota: "))
c=int(input("ingrese la tercera nota: "))
d= a+b+c
e=d/3
if e>=7:
    print("Promocionaste con: ", e)
else:
    if e>=4:
        print("Regular con: ", e)
    else:
        print("Reprobaste con: ", e)