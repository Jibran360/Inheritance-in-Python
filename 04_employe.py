class Employe:
    company = "Google"    # Class attirbute
    salary = 1000

saad = Employe()       # Instance attribute of Employe class
ahad = Employe()
print(saad.company)
print(ahad.company)
saad.salary = 400
ahad.salary = 500

Employe.company = "Youtube"
print(saad.company)
print(ahad.company)
print(saad.salary)
print(ahad.salary)

# Employe.company = "Tesla"
# print(saad.company)
# print(ahad.company)
# saad.salary = 1000
# ahad.salary = 2000
# print(saad.salary)
# print(ahad.salary)
