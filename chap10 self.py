class Employee:
    company = "Google"
    def getsalary(self, signeture):
     print(f"Salary for this employee working in {self.company} is {self.salary} per month/n {signeture}")

    @staticmethod
    def greet():
     print("Good morning, sir")
Viraaj = Employee()
Viraaj.salary = 95000
Viraaj.getsalary("thanks!")
# Employee.getsalary(Viraaj)
Viraaj.greet()
