class Employee:
    company = "Gas Station"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6000

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter         # Setter method
    def totalSalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 5900
print(e.salary)
print(e.salarybonus)