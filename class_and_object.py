#Encapsulation
class Room:
    name = ""
    mat = 1
    window = 2
    door = 2

    def has(self):
        print("This", self.name, "has",self.door,"door")


kitchen = Room()
kitchen.name = "kitchen"
kitchen.has()

drawing_room = Room()
drawing_room.name = "drawing room"
drawing_room.has()

#Constructor

class Room:   
    def __init__(self,name,mat,window,door):
        self.name = name
        self.mat = mat
        self.window = window
        self.door = door

    def has(self):
        print("This", self.name, "has",self.door,"door")


kitchen = Room("kintchen","koo","4","8")
kitchen.has()


drawing_room = Room("Drawing room","foo","1","3")
drawing_room.has()

#Inheritance

class Car:
    def __init__(self,name):
        self.wheels = 4
        self.name = name

    def breake(self):
        print(self.name,"has stopped")

    def accelerate(self):
        print(self.name," is acclerating")

class MiniCar(Car):

    def __init__(self,name):
        super().__init__(name)
        pass

mini = MiniCar("nano")
print(mini.wheels)
mini.breake()

#Polymorphism

class Car:
    def __init__(self,name):
        self.wheels = 4
        self.name = name

    def brake(self):
        print(self.name,"has stopped")

    def accelerate(self):
        print(self.name," is acclerating big car")

class MiniCar(Car):

    def __init__(self,name):
        super().__init__(name)
        pass

    def accelerate(self):
        print(self.name," is acclerating mini car")


def use_brakes(car):
    car.brake()

big_car = Car("Audi")

mini_car = MiniCar("coupe")

use_brakes(mini_car)

#Abstraction







