class Flightform():
    formtype = "Flightform"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Flight is {self.aeroplane}")
viraajsapplication = Flightform()
viraajsapplication.name = "Viraaj"
viraajsapplication.aeroplane = "Air India"
viraajsapplication.printData()

