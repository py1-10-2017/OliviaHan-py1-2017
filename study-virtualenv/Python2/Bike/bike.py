class Bike(object):
    def __init__ (self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles

    def ride(self):
        print 'Riding'
        self.miles = self.miles + 10
        print self.miles

    def reverse(self):
        print 'Reversing'
        self.miles = self.miles - 5
        if self.miles < 0 :
            self.miles = 0
        print self.miles

bike1 = Bike(200,'25mph')

print bike1.ride()
print bike1.ride()
print bike1.ride()
print bike1.reverse()
print bike1.displayInfo()


bike2 = Bike(300,'30mph')

print bike2.ride()
print bike2.ride()
print bike2.reverse()
print bike2.reverse()
print bike2.displayInfo()

bike3 = Bike(400,'40mph')

print bike3.reverse()
print bike3.reverse()
print bike3.reverse()
print bike3.displayInfo()
