from classes.Person       import Person #import class Person from file /classes/Person.py
from classes.Student      import Student #import class Student from file /classes/Student.py
from classes.Cat          import Cat #import class Cat from file /classes/Cat.py
from classes.JapaneseCat  import JapaneseCat #import class JapaneseCat from file /classes/JapaneseCat.py
from classes.BrazilianCat import BrazilianCat #import class BrazilianCat from file /classes/BrazilianCat.py

#making every class visible from the same folder
__all__ = ["Person", "Student", "Cat", "JapaneseCat", "BrazilianCat"]