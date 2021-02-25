import datetime


class Persona:
    def calcular_edad(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)
        x = datetime.datetime.now()
        age = x.year - self.year
        if self.month < x.month:
            age -= 1
        if self.month == x.month and self.day > x.day:
            age -= 1
        self.age = age
        return self.age

    def datos_persona(self, name, lastname, day, month, year):
        self.name = name
        self.lastname = lastname
        self.day = day
        self.month = month
        self.year = year
