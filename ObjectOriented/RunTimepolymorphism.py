class Animal():
    def __init__(self,name):
        self.name = name

    def moving(self):
        print("Animal with name {} is walking ".format(self.name))

class Vehicle:
    def __init__(self,name):
        self.name = name

    def moving(self):
        print("{} Vehicle is moving".format(self.name))

if __name__ == '__main__':
    a = Animal("Dog")
    v = Vehicle("Swift")
    for obj in (a,v):
        obj.moving()