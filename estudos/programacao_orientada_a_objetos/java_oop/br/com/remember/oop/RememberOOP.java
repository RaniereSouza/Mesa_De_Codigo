package br.com.remember.oop; //all classes in the same package to be mutually visible

//class definition: RememberOOP (class used only to define and run the main program)
public class RememberOOP {

    public static void main (String[] args) {

        //creating instances of Person
        Person person1 = new Person("Raniere", 28);
        Person person2 = new Person("Truppel", 32);

        //accessing attribute 1 from both instances, since it's public
        System.out.println("Person 1 is called " + person1.name + ", Person 2 is called " + person2.name + ".");
        
        //cannot access attribute 2 from any instance, since it's private
        //[ERROR] System.out.println("Person 1 is " + person1.age + " years old, Person 2 is " + person2.age + " years old."); [ERROR]

        //calling method 1 from both instances
        person1.greet();
        person2.greet();

        //calling method 2 from both instances (only way to see the private attribute 2)
        person1.howOld();
        person2.howOld();

        //creating instances of Student
        Student student1 = new Student("Marilia", 29, "IFBA");
        Student student2 = new Student("Neto", 23, "UNIFACS");

        //cannot access attribute 3 from any instance, since it's private
        //[ERROR] System.out.println("Student 1 studies at " + student1.institution + ", Student 2 studies at " + student2.institution + "."); [ERROR]

        //calling method 1 from both instances
        student1.greet();
        student2.greet();

        //calling method 3 from both instances (only way to see the private attribute 3)
        student1.studentAt();
        student2.studentAt();

        //this is a legal operation: since Student inherits from Person, the code considers that a Student is also a Person
        Person person3 = new Student("Ramon", 26, "UFBA");

        //it calls the method 1 normally...
        person3.greet();

        //...but, as the instance person3 is of the type Person, and not of the type Student, it cannot access the method 3
        //[ERROR] person3.studentAt(); [ERROR]

        //this is an illegal operation since a Student is a Person, but the other way around is not necessarily true
        //[ERROR] Student student3 = new Person("Morgana", 28); [ERROR]

        //it can be dangerous to keep class attributes as public! it means that it can be overwritten by anyone!
        //for example, you can do things like this:
        person2.name = "Rodrigo";

        //Person 2 now has "Rodrigo" as it's name!
        person2.greet();

        //from now on, we will follow the rule of encapsulation, and all the classes we use will have private attributes

        //let's instantiate some Cats!
        Cat          cat1 = new Cat("Tom"); //instance from superclass of JapaneseCat and BrazilianCat
        JapaneseCat  cat2 = new JapaneseCat("Yoruichi"); //instance of a subclass of Cat
        BrazilianCat cat3 = new BrazilianCat("Satanas"); //instance of a subclass of Cat

        //we will now observe some polymorphism in action: using the same method name, and having different behaviours

        //this is the original talk method in the Cat superclass:
        cat1.talk();

        //those are different versions of the talk method, overriden by each of the subclasses
        cat2.talk();
        cat3.talk();

        //this method was also overloaded in the BrazilianCat class, which means it was written with a different behaviour if it receives different arguments
        cat3.talk("outro gato!");
    }
}