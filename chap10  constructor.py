class Employee:
    company = "Google"
    def __int__(self, name, salary, subunit):
        salf.name = name
        self.salary = salary
        salf.subunit = subunit
        print("Employee is created!")
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The name of the employee is {self.salary}")
        print(f"The name of the employee is {self.subunit}")

    def getsalary(self, signeture):
     print(f"Salary for this employee working in {self.company} is {self.salary} per month/n {signeture}")

    @staticmethod
    def greet():
        print("Good morning, sir")
        viraaj = Employee("viraaj", 500000, "youtube")
        viraaj.getDetails()