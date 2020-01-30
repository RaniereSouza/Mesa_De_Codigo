package br.com.remember.oop; //all classes in the same package to be mutually visible

//class definition: Student --> inherits from (is a subclass of) Person
public class Student extends Person {

    //attributes 1 and 2 declared at parent class (superclass)
    private String institution; //declaring attribute 3

    //constructor function
    public Student (String name, int age, String institution) {
        super(name, age);               //attributes 1 and 2 instantiated with parent class (superclass) constructor
        this.institution = institution; //instantiating attribute 3
    }

    //methods 1 and 2 defined at parent class (superclass)

    //method 3
    public void studentAt () {
        System.out.println(this.name + " is a student at " + this.institution + ".");
    }
}