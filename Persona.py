class Persona:
    def calcular_edad(self, year):
        self.year=int(year)
        self.age=2021-self.year
        return self.age

    def datos_persona(self, name, lastname, day, month, year):
        self.name = name
        self.lastname = lastname
        self.day= day
        self.month=month
        self.year=year