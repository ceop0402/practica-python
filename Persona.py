def Persona ():
    class Person:
     def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality= nationality

    nombre = (input("Dime tu nombre y apellido: "))
    y = int(input("¿En qué año naciste?: "))
    edad=2021-y
    nacionalidad=(input("Dime tu nacionalidad: "))

    p1 = Person(nombre, edad,nacionalidad)

    print(p1.name)
    print(p1.age)
    print(p1.nationality)