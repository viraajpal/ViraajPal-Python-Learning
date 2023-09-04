class programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getinfo(self):
        print(f"The name of the programmer is {self.name} and the product is {self.product}")

aashi = programmer("aashi", "skype")
viren = programmer("viren", "github")
aashi.getinfo()
viren.getinfo()