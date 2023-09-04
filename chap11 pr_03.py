# SalaryAfterIncrement =self.salary*self.increment

class Employee:
    Salary = 10000
    increment = 1.5

    @property
    def  SalaryAfterIncrement(self):
        return self.Salary*self.increment

    @ SalaryAfterIncrement.setter
    def  SalaryAfterIncrement(self, sai):
        self.increment = sai/self.Salary


        e = Employee()
        print(e.SalaryAfterIncrement)
        e.SalaryAfterIncrement = 2000
        print(e.increment)
