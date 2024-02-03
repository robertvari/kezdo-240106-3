class Person:
    # class attribut
    nationality = "Hungary"

    def __init__(self, name):
        # instance attribute
        self.name = name


tamas = Person("Tamas")
kriszta = Person("Kriszta")
balazs = Person("Balázs")

print(tamas.name, tamas.nationality)
print(kriszta.name, kriszta.nationality)
print(balazs.name, balazs.nationality)

Person.nationality = "Germany"

print(tamas.name, tamas.nationality)
print(kriszta.name, kriszta.nationality)
print(balazs.name, balazs.nationality)