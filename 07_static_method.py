class Employee:
    company = "Google"
    
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

ahad = Employee()
ahad.salary = 100000
ahad.getSalary("Thanks!") # Employee.getSalary(ahad)
ahad.greet() # Employee.greet()