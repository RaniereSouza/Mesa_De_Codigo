from classes import * #import all classes from directory /classes

#creating instances of Person
person1 = Person("Raniere", 28)
person2 = Person("Truppel", 32)

#accessing attribute 1 from both instances
print("Person 1 is called {}, Person 2 is called {}.".format(person1.name, person2.name))

#trying to access attribute 2 from both instances will throw an error, as an advise to not access private attributes
#[ERROR] print(person1.__age, person2.__age) [ERROR]

#calling method 1 from both instances
person1.greet()
person2.greet()

#calling method 2 from both instances (legal way to show attribute 2)
person1.howOld()
person2.howOld()

#creating instances of Student
student1 = Student("Marília", 29, "IFBA")
student2 = Student("Neto", 23, "UNIFACS")

#trying to access attribute 3 from both instances will throw an error, as an advise to not access private attributes
#[ERROR] print(student1.__institution, student2.__institution) [ERROR]

#calling method 1 from both instances
student1.greet()
student2.greet()

#calling method 3 from both instances (legal way to show attribute 3)
student1.studentAt()
student2.studentAt()

#let's save this instance so we can recover it later:
storePerson1 = person1

#Python is a dinamically typed language, so a variable will change it's type depending on the value that is passed to it
#knowing that, this is a legal operation: we're passing the Student instance that is in the variable student1 to the variable person1 (previously of the type Person)
person1 = student1

#it calls the method 1 normally (as if it was student1)...
person1.greet()

#... and also method 3 (from what previously was in student1)
person1.studentAt()

#recovering the instance to it's original variable:
person1 = storePerson1

#it can be dangerous to keep class attributes as public! it means that it can be overwritten by anyone!
#for example, you can do things like this:
person2.name = "Rodrigo"

#Person 2 now has "Rodrigo" as it's name!
person2.greet()

#from now on, we will follow the rule of encapsulation, and all the classes we use will have private attributes

#let's instantiate some Cats!
cat1 = Cat("Tom") #instance from superclass of JapaneseCat and BrazilianCat
cat2 = JapaneseCat("Yoruichi") #instance of a subclass of Cat
cat3 = BrazilianCat("Satanas") #instance of a subclass of Cat

#we will now observe some polymorphism in action: using the same method name, and having different behaviours

#this is the original talk method in the Cat superclass:
cat1.talk()

#those are different versions of the talk method, overriden by each of the subclasses
cat2.talk()
cat3.talk()

#this method was also overloaded in the BrazilianCat class, which means it was written with a different behaviour if it receives different arguments
cat3.talk("outro gato!")