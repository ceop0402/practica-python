from Calculadora import Calculadora
from Persona import Persona
 ## def __init__(self, name, lastname, day , month, year):
   # self.name = name
    #self.lastname = lastname
    #self.day= day
    #self.month=month
    #self.year=year

nombre = (input("Ingrese su nombre: "))
apellido = (input("Ingrese su apellido: "))
dia=(input("ingrese día de nacimiento: "))
mes=(input("ingrese mes de nacimiento: "))
ano=(input("ingrese año de nacimiento: "))
numero=(input("Ingrese un numero: "))

p1 = Person(nombre,apellido,dia,mes,ano)

print(p1.name)
print(p1.lastname)
print(p1.day, "/" + p1.month, "/" +p1.year) 

year=int(ano)
edad=2021-year
print(edad)
def my_function():
   
   print(edad + "años") 
   print(edad+numero)
