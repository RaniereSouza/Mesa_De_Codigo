from Person  import Person  #imports class Person from file Person.py
from Student import Student #imports class Student from file Student.py

#creating instances of Person
person1 = Person("Raniere", 28)
person2 = Person("Truppel", 32)

message = "Person 1 is called {}, Person 2 is called {}."

#accessing attribute #1 from both instances
print(message.format(person1.name, person2.name))

#calling method 1 from both instances
person1.greet()
person2.greet()

#calling method 2 from both instances
person1.howOld()
person2.howOld()

#creating instances of Student
student1 = Student("Marília", 29, "IFBA")
student2 = Student("Neto", 23, "UNIFACS")

#calling method 1 from both instances
student1.greet()
student2.greet()

#calling method 3 from both instances
student1.studentAt()
student2.studentAt()