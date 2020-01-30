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
        Student student1 = new Student("Marília", 29, "IFBA");
        Student student2 = new Student("Neto", 23, "UNIFACS");

        //cannot access attribute 3 from any instance, since it's private
        //[ERROR] System.out.println("Student 1 studies at " + student1.institution + ", Student 2 studies at " + student2.institution + "."); [ERROR]

        //calling method 1 from both instances
        student1.greet();
        student2.greet();

        //calling method 3 from both instances (only way to see the private attribute 3)
        student1.studentAt();
        student2.studentAt();
    }
}