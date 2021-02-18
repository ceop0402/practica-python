def Calculadora ():
    x = int(input("Dime un numero: "))
    y = int(input("Dime otro numero: "))
    operacion = input("¿Qué operación quieres hacer? SUMAR=s - Restar=r - Multiplicar=m - Dividir=d ")

    if operacion == 's':
        print((x+y))
    elif operacion == 'r':
        print((x-y))
    elif operacion == 'm': 
        print((x*y))
    elif operacion == 'd':
        print((x/y))
    else:
        print("opción no valida")