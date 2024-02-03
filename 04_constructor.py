class Person:
    # constructor
    def __init__(self, name, age, email, address):
        self.name = name
        self.age = age
        self.email = email
        self.address = address


csaba = Person("csaba", 18, "csaba@gmail.com", "Budapest")
kriszta = Person("kriszta", 22, "kriszta@gmail.com", "Debrecen")
balazs = Person("balázs", 33, "balazs@gmail.com", "Pécs")

print(csaba.name, csaba.age, csaba.email, csaba.address)
print(kriszta.name, kriszta.age, kriszta.email, kriszta.address)
print(balazs.name, balazs.age, balazs.email, balazs.address)