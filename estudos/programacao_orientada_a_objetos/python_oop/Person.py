#class definition: Person
class Person :

    #constructor function
    def __init__ (self, name, age) :
        self.name = name #attribute 1 (declaration + instantiation)
        self.__age = age #attribute 2 (declaration + instantiation)

    #method 1 
    def greet (self) :
        greeting = "Hello, {}!"
        print(greeting.format(self.name))
    
    #method 2
    def howOld (self) :
        tellAge = "{} is {} years old."
        print(tellAge.format(self.name, self.__age))