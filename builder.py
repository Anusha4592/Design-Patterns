from abc import ABCMeta, abstractmethod

class Director(object):

    def __init__(self, builder):
        self.builder = builder

    def build_car(self):
        self.builder.new_car()
        self.builder.build_size()
        self.builder.build_doors()
        self.builder.build_seats()

class Car(object):
    def __init__(self):
        self.size = None
        self.doors = None
        self.seats = None 
        self.headlights = None

    def __repr__(self):
        return "Car Specs: \n Size :%s\n Doors:%s\n Seats:%s" %(self.size, self.doors, self.seats)

#Abstarct Car Builder
class CarBuilder(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.car = None

    @abstractmethod
    def build_size(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def build_seats(self):
        pass

    def build_headlights(self):
        self.car.headlights = 2

    def new_car(self):
        self.car = Car()

class SedanCarBuilder(CarBuilder):

    def build_size(self):
        self.car.size = "Medium" 
        print "Building Size of the car as %s..." %self.car.size

    def build_doors(self):
        self.car.doors = 4
        print "Building %s doors for the car..." %self.car.doors

    def build_seats(self):
        self.car.seats = 5
        print "Building %s seats for the car..." %self.car.seats

    def get_car(self):
        return self.car

class CoupeBuilder(CarBuilder):

    def build_size(self):
        self.car.size = "Small"
        print "Building Size of the car as %s..." %self.car.size

    def build_doors(self):
        self.car.doors = 2
        print "Building %s doors for the car..." %self.car.doors

    def build_seats(self):
        self.car.seats = 5
        print "Building %s seats for the car..." %self.car.seats

    def get_car(self):
        return self.car

if __name__ == '__main__':
    #builder = SedanCarBuilder()
    builder = CoupeBuilder()
    director = Director(builder)
    director.build_car()
    #print builder.car
    print builder.get_car()
