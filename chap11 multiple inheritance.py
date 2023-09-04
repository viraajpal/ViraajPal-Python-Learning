class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradelevel(self):
          self.level = self.level + 1

class Employee:
     company = "visa"


class Programmer(Employee, Freelancer):
    name = "Viraaj"

p = Programmer()
p.upgradelevel()
print(p.company)



