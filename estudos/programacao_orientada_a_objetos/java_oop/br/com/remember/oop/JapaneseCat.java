package br.com.remember.oop; //all classes in the same package to be mutually visible

//class definition: JapaneseCat --> inherits from (is a subclass of) Cat
public class JapaneseCat extends Cat {

    //doesn't need to declare any new attributes, inherits everything from the superclass

    //constructor function
    public JapaneseCat (String name) {
        super(name); //executes everything from the superclass constructor
    }

    @Override //this annotation indicates that this method exists in the superclass and is now being overwritten by the subclass
    public void talk () {
        //the attribute name is private to the Cat class, which means that not even its subclasses can access it freely... that's why we need to use the getName method here
        System.out.println(this.getName() + " says: nyan! =^.^=");
    }
}