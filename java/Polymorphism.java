class Human{
    String name;
    int age;
    public void display_name(String name,int age){
        this.name = name;
        this.age = age;
        System.out.println(name+" "+age);
    }
}

public class Polymorphism {
    public static void main(String args[]) {
        Human human = new Human();
        human.display_name("harshith", 20);
          
        // Creating an Animal object
   System.out.println("heloo worlld");
    }
}
