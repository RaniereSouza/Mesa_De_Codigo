from . import Person #imports class Person from file Person.py (needed for inheritance)

#class definition: Student --> inherits from (is a subclass of) Person
class Student (Person) :

    #costructor function
    def __init__ (self, name, age, institution) :
        super().__init__(name, age)      #attributes 1 and 2 declared and instantiated with parent class (superclass) constructor
        self.__institution = institution #attribute 3 (declaration + instantiation)
    
    #methods 1 and 2 defined at parent class (superclass)

    #method 3
    def studentAt (self) :
        print("{} is a student at {}.".format(self.name, self.__institution))