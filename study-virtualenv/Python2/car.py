class car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            tax = 0.15
        else:
            tax = 0.12
        self.tax = tax


    def display_all(self):
        print "Price:" + " " + str(self.price)
        print "Speed:" + " " + str(self.speed)
        print "Fuel:" + " " + str(self.fuel)
        print "Mileage:" + " " + str(self.mileage)
        print "Tax:" + " " + str(self.tax)


car1 = car(2000, "35mph", "Full", "15mpg")

car2 = car(2000, "5mph", "Not Full", "105mpg")

car3 = car(2000, "15mph", "Kind of Full", "95mpg")

car4 = car(2000, "45mph", "Empty", "25mpg")

car5= car(20000, "55mph", "Not Full", "35mpg")

car6 = car(105000, "5mph", "Ful", "105mpg")

car6.display_all()
