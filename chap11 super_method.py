class Person:
    country = "India"

    def __int__(self):
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __int__(self):
        super.__init__()
        print("Initializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.Salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):

        print("No Salary for Programmers...")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Programmer so I am breathing++..")

 p = Person()
p.takeBreath()
# print(p.country)
# print(p.company)# throws error

e = Employee()
e.takeBreath()
# print(e.company)

pr = Programmer()
pr.takeBreath()
# print(p.country)
# print(pr.company)
