from Person       import Person  #imports class Person from file Person.py
from Student      import Student #imports class Student from file Student.py
from Cat          import Cat #imports class Cat from file Cat.py
from JapaneseCat  import JapaneseCat #imports class JapaneseCat from file JapaneseCat.py
from BrazilianCat import BrazilianCat #imports class BrazilianCat from file BrazilianCat.py

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