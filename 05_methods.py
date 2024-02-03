class Person:
    # constructor
    def __init__(self, name, age, email, address):
        self.name = name
        self.age = age
        self.email = email
        self.address = address

    # method
    def introduce(self):
        print(f"Hello my name is {self.name}. I'm {self.age} old. My email is {self.email}. I live in {self.address}")

    def say_hello(self):
        print(f"Hello I'm {self.name}")

    def go_to_sleep(self):
        print(f"{self.name} says: I'm tired... I go to sleep...")


csaba = Person("Csaba", 18, "csaba@gmail.com", "Budapest")
kriszta = Person("Kriszta", 22, "kriszta@gmail.com", "Debrecen")
balazs = Person("Balázs", 33, "balazs@gmail.com", "Pécs")

csaba.go_to_sleep()
kriszta.go_to_sleep()
balazs.go_to_sleep()