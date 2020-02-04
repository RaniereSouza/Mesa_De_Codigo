#class definition: Cat
class Cat :

    __species    = "Felis catus" #declaring and assigning a value to attribute __species
    __catCounter = 0 #this attribute will be used as static, which means it will be shared by all objects of the Cat class

    #constructor function
    def __init__ (self, name) :

        plural = ""

        self.__name = name #attribute __name (declaration + instantiation)
        Cat.__catCounter += 1 #incrementing static attribute

        if Cat.__catCounter > 1 : plural = "s"

        print("The world has been blessed with {} cat{}. welcome!".format(Cat.__catCounter, plural))

    #getter method for attribute __species
    def getSpecies (self) :
        return self.__species

    #setter method for attribute __species; a cat will always be a cat, so we keep this setter away
    """
    def setSpecies (self, newSpecies) :
        self.__species = newSpecies
    """

    #getter method for attribute __name
    def getName (self) :
        return self.__name
    
    #setter method for attribute __name; we don't want the name to be changed by anyone, so we keep this setter away
    """
    def setName (self, newName) :
        self.__name = newName
    """

    #original talk method in the superclass
    def talk (self) :
        print("{} says: meow!".format(self.__name))