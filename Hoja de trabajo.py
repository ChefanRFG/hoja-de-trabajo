N1=0
N2=0
operacion=" "
Respuesta=0
N1=float(input("Ingrese un numero: "))
N2=float(input("Ingrese otro numero: "))

operacion=input("que operacion desea realizar?: ")
if operacion=="+":
    print(N1+N2)
if operacion=="-":
    print(N1-N2)
if operacion=="*":
    print(N1*N2)
if operacion=="/":
    print(N1/N2)