#class definition: Person
class Person :

    #constructor function
    def __init__ (self, name, age) :
        self.name = name #attribute 1 (declaration + instantiation)
        self.__age = age #attribute 2 (declaration + instantiation)

    #method 1 
    def greet (self) :
        print("Hello, {}!".format(self.name))
    
    #method 2
    def howOld (self) :
        print("{} is {} years old.".format(self.name, self.__age))