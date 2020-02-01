package br.com.remember.oop; //all classes in the same package to be mutually visible

//class definition: Cat
public class Cat {

    private        String species    = "Felis catus"; //declaring and assigning a value to attribute species
    private static int    catCounter = 0; //this attribute is static, which means it is shared by all objects of the Cat class
    private        String name; //declaring attribute name

    //constructor function
    public Cat (String name) {

        String plural = "";

        this.name = name; //assigning a value to attribute name
        Cat.catCounter++; //incrementing static attribute

        if (Cat.catCounter > 1) plural = "s";

        System.out.println("the world has been blessed with " + Cat.catCounter + " cat" + plural + ". welcome!");
    }

    //getter method for attribute name
    public String getName () {
        return this.name;
    }

    //setter method for attribute name; we don't want the name to be changed by anyone, so we keep this setter away
    /* public void setName (String newName) {
        this.name = newName;
    } */

    //original talk method in the superclass
    public void talk () {
        System.out.println(this.name + " says: meow!");
    }
}