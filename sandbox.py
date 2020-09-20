class Dog(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def walk(self):
        print("* walk fabulously *")

    def bark(self):
        print("Woof woof!")

    def get_name(self):
        print("My name is " + self.name)

    def set_name(self, name):
        self.name = name

    def get_type(self):
        print("I'm a " + self.type + " dog")


heli = Dog("Heli", "Puddle")
heli.walk()
heli.bark()
heli.get_name()
heli.get_type()
heli.set_name("Hola")
heli.get_name()