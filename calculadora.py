def calculadora (edad,number):
    y= int(edad)
    operacion = input("¿Qué operación quieres hacer? SUMAR=s - Restar=r - Multiplicar=m - Dividir=d ")
    select = {'s' : number+y, 'r' : y-number, 'm' : number*y, 'd' : y/number}
    if operacion in select:
        print (select[operacion]) 
        return select[operacion]
    print("opción no valida")
    return 0
