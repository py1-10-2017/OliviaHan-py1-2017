class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def display_health(self):
        print "animal health is: " + str(self.health)
        return self

animal1 = Animal('animal_name', 50)

# animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog1 = Dog('dog1_name', 40)
# animal1.walk().walk().walk().run().run().display_health()

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name,health)
        self.health = 170
        super(Dragon, self).display_health()
        print "I am a dragon"

    def fly(self):
        self.health -= 10
        return self
dragon1 = Dragon('dragon1_name', 90)

dragon1.walk().walk().walk().run().run().fly().display_health()
animal1.walk().walk().walk().run().run().display_health()
