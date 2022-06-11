package mySamplejava8.typeInterface;

public class Example02 {
	public static void main(String[] args) {  
        GenericClass<String> genericClass = new GenericClass<String>();  
        genericClass.setName("Peter");  
        System.out.println(genericClass.getName());  
          
        GenericClass<String> genericClass2 = new GenericClass<>();  
        genericClass2.setName("peter");  
        System.out.println(genericClass2.getName());  
      
        // New improved type inference  
        System.out.println(genericClass2.genericMethod(new GenericClass<>()));  
    }  
}
