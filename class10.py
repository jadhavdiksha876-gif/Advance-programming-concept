class Vehicle:
    def __init__(self, number, model, rate):
        self.number = number
        self.model = model
        self.rate = rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle Rented")
        else:
            print("Vehicle Not Available")

    def return_vehicle(self, days):
        self.available = True
        charge = self.rate * days
        print("Vehicle Returned")
        print("Rental Charge:", charge)

v = Vehicle("MH12AB1234", "Swift", 1000)

v.rent()
v.return_vehicle(3)