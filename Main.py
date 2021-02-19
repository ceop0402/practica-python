from calculadora import calculadora
from persona import Persona
calculadora()

name = (input("Ingrese su nombre: "))
lastname = (input("Ingrese su apellido: "))
day =(input("ingrese día de nacimiento: "))
month=(input("ingrese mes de nacimiento: "))
year=(input("ingrese año de nacimiento: "))
p=Persona()
print (p.calcular_edad(year))
p.datos_persona(name, lastname, day, month, year)
print("Tu nombre es: " + (p.name + " " + p.lastname))
print("Tu fecha de nacimiento es: " + p.day + "/" + p.month + "/" + p.year) 

Numbers = int(input("Ingrese un numero: "))
Calculo=((Numbers+p.calcular_edad(year)))
print((Calculo))
if Calculo%2==0:
    print (Calculo, "Tu edad es par!!")
elif Calculo!=0:
    print(Calculo, "Tu edad es impar!!")