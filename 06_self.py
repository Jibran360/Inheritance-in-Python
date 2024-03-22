class Employee:
    company = "Google"
    
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")
saad = Employee()
saad.salary = 100000
saad.getSalary()
# print(saad.getsalary)
# Employe.getsalary(saad)