# Class attributes
class Employee:
    company = "google"
    salary = int(700000)
Viraaj = Employee()
Sukriti = Employee()
print(Viraaj.company)
print(Viraaj.salary)
print(Sukriti.company)
print(Sukriti.salary)

# Instance attributes
Viraaj.salary = int(85000)
Sukriti.salary = int(95000)
Viraaj.company = "NASA"
Sukriti.company = "NASA"
print(Viraaj.company)
print(Viraaj.salary)
print(Sukriti.company)
print(Sukriti.salary)