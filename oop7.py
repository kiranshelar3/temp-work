print("***********ticket booking system*************")

class train:
    def __init__(self, name, fare, seats, n):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.n=n

    def getStatus(self):
        print(f"name of the train is {self.name}")
        print(f"seats avilable in the train is {self.seats}")
        print("*******************************")

    def fareInfo(self):
        print(f"price of the ticket is Rs.{self.fare}")

    def bookTicket(self):
        if self.seats > self.n:
            print("Your ticket has been booked")
            self.seats = self.seats-self.n
            print(f"now avilable seats are {self.seats}")
        else:
            print("ticket is not available kindly try next time")

raji =train("Rajdhani", 250, 100, 2)
raji.getStatus()
raji.fareInfo()
raji.bookTicket()
raji.bookTicket()
