class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Address: {self.address}"
    
    def __repr__(self):
        return self.name

csaba = Person("Csaba", 22, "Pécs")
kriszta = Person("Kriszta", 25, "Bodapest")
balazs = Person("Balázs", 20, "Debrecen")

my_friends = [csaba, kriszta, balazs]
print(my_friends)