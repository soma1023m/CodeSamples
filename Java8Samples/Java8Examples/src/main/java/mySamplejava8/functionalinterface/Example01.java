package mySamplejava8.functionalinterface;

public class Example01 implements Sayable{
	public void say(String msg){  
        System.out.println(msg);  
    }  
    public static void main(String[] args) {  
    	Example01 fie = new Example01();  
        fie.say("Hello there");  
    }  

}
