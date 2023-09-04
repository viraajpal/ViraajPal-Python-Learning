class Employee:
    company = "camel"
    Salary = 100
    Location = "Delhi"

    def changeSalary(self, sal):
        self.__class__.salary = sal

    @classmethod
    def changesalary(cls, sal):
        cls.salary = sal
e = Employee()
# print(e.salary)
print(Employee.Salary)
e.changeSalary(433)
print(e.salary)
