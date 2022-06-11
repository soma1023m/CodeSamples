package mySamplejava8.methodreferences;

public class Example01 {
	public static void saySomething(){  
        System.out.println("Hello, this is static method.");  
    }  
    public static void main(String[] args) {  
        // Referring static method  
        Sayable sayable = Example01::saySomething;  
        // Calling interface method  
        sayable.say();  
    }  
}
