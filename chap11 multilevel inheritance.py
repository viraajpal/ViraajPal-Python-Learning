class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.Salary}")

    def takeBreath(self):
        print("I am an Employee so I am breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print("No Salary for Programmers...")

    def takeBreath(self):
        print("I am an Programmer so I am breathing++..")

p = Person()
p.takeBreath()
print(p.country)
# print(p.company)# throws error
e = Employee()
e.takeBreath()
print(e.company)
pr = Programmer()
pr.takeBreath()
print(p.country)
print(pr.company)
pr.takeBreath()
print(p.country)
print(pr.company)