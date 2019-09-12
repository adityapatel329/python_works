class Car:

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"


    def drive(self):
        print('driving maxspeed : ' + str(self.__maxspeed))

redcar = Car()
redcar.drive()

redcar.__maxspeed = 30
redcar.drive()
