package br.com.remember.oop; //all classes in the same package to be mutually visible

//class definition: Person
public class Person {

    public  String name; //declaring attribute 1
    private int    age;  //declaring attribute 2

    //constructor function
    public Person (String name, int age) {
        this.name = name; //instantiating attribute 1
        this.age = age;   //instantiating attribute 2
    }

    //method 1
    public void greet () {
        System.out.println("Hello, " + this.name + "!");
    }

    //method 2
    public void howOld () {
        System.out.println(this.name + " is " + this.age + " years old.");
    }
}