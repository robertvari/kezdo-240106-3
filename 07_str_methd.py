class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

csaba = Person("Csaba")
kriszta = Person("Kriszta")
balazs = Person("Balázs")

print(csaba)
print(kriszta)
print(balazs)