package mySamplejava8.defaultmethods;

public class Example01 implements Sayable{
	public void sayMore(String msg){        // implementing abstract method   
        System.out.println(msg);  
    }  
    public static void main(String[] args) {  
    	Example01 dm = new Example01();  
        dm.say();   // calling default method  
        dm.sayMore("Work is worship");  // calling abstract method  
  
    }  
}
