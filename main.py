from calculadora import calculadora
from persona import Persona

name = (input("Ingrese su nombre: "))
lastname = (input("Ingrese su apellido: "))
day = (input("ingrese día de nacimiento: "))
month= (input("ingrese mes de nacimiento: "))
year= (input("ingrese año de nacimiento: "))
p=Persona()
p.datos_persona(name, lastname, day, month, year)
print ("Tu nombre es: " + (p.name + " " + p.lastname))
print ("Tu fecha de nacimiento es: " + p.day + "/" + p.month + "/" + p.year) 
edad= p.calcular_edad(day, month, year)
print ("Tu edad es:", edad)

number = int(input("Ingrese un numero: "))
Calculo= calculadora(edad,number)

print((Calculo))
if Calculo%2==0:
    print (Calculo, "Tu edad es par!!")
elif Calculo!=0:
    print(Calculo, "Tu edad es impar!!")