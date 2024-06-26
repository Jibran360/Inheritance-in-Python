# Single Inheritance

class Employee:              # Base class / Parent class
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):  # Inherted class / Child class
    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is an Programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
# print(p.company)
