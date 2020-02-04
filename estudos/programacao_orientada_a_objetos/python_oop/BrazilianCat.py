from Cat import Cat #imports class Cat from file Cat.py (needed for inheritance)

#class definition: BrazilianCat --> inherits from (is a subclass of) Cat
class BrazilianCat (Cat) :

    #doesn't need to declare any new attributes, inherits everything from the superclass
    
    #constructor function
    def __init__ (self, name) :
        super().__init__(name) #executes everything from the superclass constructor
    
    #this method exists in the superclass and is now being overwritten by the subclass 
    def talk (self, message=None) :

        #the attribute __name is private to the Cat class, which means that not even its subclasses can access it freely... that's why we need to use the getName method here
        name = self.getName()

        #the behavior changes depending on the arguments passed when the method is called
        #behavior 1: when no argument is passed 
        if message is None :
            print("{} says: miau!".format(name))
        #behavior 2: when something is passed as argument
        else :
            print("{} says: {}".format(name, message))
        