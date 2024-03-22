class Employe:
    company = "Google"    # Class attirbute
    salary = 1000
    

saad = Employe()       # Instance attribute of Employe class
ahad = Employe()

# Creating instance attribute for both objects
# saad.salary = 400     # Refers instance attribute firstly if not then check in class attribute
# ahad.salary = 500

print(saad.salary)
print(ahad.salary)

# Throws an error as address is not present in instance/class
# print(ahad.address)