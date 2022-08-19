class Animal:
    def __init__(self,name):
        self.name = name

    def print(self):
        print("My name is {}".format(self.name))

    def speak(self):
        print("Animal is eating")


class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)

    def speak(self):
        print("Dog making woo woo sound")


a = Animal("Praani")
a.speak()

b = Dog("Kariya")
#calling overrided method in the class Dog
b.speak()
b.print()