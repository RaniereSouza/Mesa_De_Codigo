from Cat import Cat #imports class Cat from file Cat.py (needed for inheritance)

#class definition: JapaneseCat --> inherits from (is a subclass of) Cat
class JapaneseCat (Cat) :

    #doesn't need to declare any new attributes, inherits everything from the superclass

    #constructor function
    def __init__ (self, name) :
        super().__init__(name) #executes everything from the superclass constructor
    
    #this method exists in the superclass and is now being overwritten by the subclass
    def talk (self) :
        #the attribute __name is private to the Cat class, which means that not even its subclasses can access it freely... that's why we need to use the getName method here
        print("{} says: nyan! =^.^=".format(self.getName()))
    