class Employee3:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee3):
      language = "Python"

      def getlanguage(self):
        print("This language is {self.language")

      def showDetails(self):
        print("This is a Programmer")

e = Employee3()
e.showDetails()
# e.showDetails()
p = Programmer()
# p = Programmer()
p.showDetails()
# p.showDetails()
print(p.company)
