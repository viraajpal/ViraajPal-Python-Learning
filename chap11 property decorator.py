# beauty of python oops

class Employee:
    company = "Bharat Gas"
    salary = 4000
    salarybonous = 300
    # totalSalary =6000

    @property
    def totalSalary(self):
        return self.salary + self.salarybonous

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonous = val -self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 7000
print(e.salary)
print(e.salarybonous)