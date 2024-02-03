# class definition
class Person:
    name = None
    age = 0


# instancing
csaba = Person()
csaba.name = "csaba"
csaba.age = 18

kriszta = Person()
kriszta.name = "kriszta"
kriszta.age = 22

tamas = Person()
tamas.name = "tamas"
tamas.age = 16

balazs = Person()
balazs.name = "balazs"
balazs.age = 24

print(f"Name: {csaba.name} Age: {csaba.age}")
print(f"Name: {kriszta.name} Age: {kriszta.age}")
print(f"Name: {tamas.name} Age: {tamas.age}")
print(f"Name: {balazs.name} Age: {balazs.age}")