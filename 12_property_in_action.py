class Student:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__scores = []
    
    def __str__(self) -> str:
        return self.full_name
    
    def add_score(self, score):
        self.__scores.append(score)
    
    @property
    def average(self):
        return sum(self.__scores) / len(self.__scores)
    
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    
csaba = Student("Kiss", "Csaba")
kriszta = Student("Kovács", "Krisztina")

csaba.add_score(3)
csaba.add_score(4)
csaba.add_score(2)

kriszta.add_score(5)
kriszta.add_score(5)
kriszta.add_score(4)

print(f"{csaba.full_name} average: {csaba.average}")
print(f"{kriszta.full_name} average: {kriszta.average}")