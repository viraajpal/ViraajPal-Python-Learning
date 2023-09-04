class Train:
    def __int__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the  train is {self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print("your seat has been booked! your seat number is {self.seat")
            self.seats = self.seats - 1
        else:
            print("sorry the train is full kindely try in tatkal")

    def cancelTicket(self):


intercity = ("Intercity Express: 12344, 90, 2")
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket() # this will tell train is full
intercity.getStatus()