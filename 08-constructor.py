class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):                  # Constructor
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")
    
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

ahad = Employee("ahad", 1000, "YouTube")
# ahad = Employee() --> This thorws an error (missing 3 required positional arguments:)

ahad.getDetails()
# ahad.getSalary("thanks!")
# ahad.greet()