class Person:        
    country = "Pakistan"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"salary of a programmer is {self.salary}")

p = Person()
p.takeBreath()
# print(p.company)   # Throws error

e = Employee()
e.takeBreath()

pr = Programmer()
# pr.takeBreath()      # Uses function of Employee class
pr.salary = 50000
pr.getSalary()