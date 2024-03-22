class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")
    def  fareInfo(self):
        print(f"The price of the train ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket hass been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in some other...")

intercity = Train("Intercity Express: 34905", 50, 300)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.fareInfo()