a=int(input("Ingrese primer nota: "))
b=int(input("Ingrese segunda nota: "))
c=int(input("Ingrese tercera nota: "))
d=a+b+c
e=d/3
if e>=7:
    print("Has aprobado, tu nota es: ", e)
else:
    print("Has desaprobado, tu nota es: ", e)