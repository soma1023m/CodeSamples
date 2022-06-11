package mySamplejava8.StringJoiner;

import java.util.StringJoiner;

public class Example01 {
	 public static void main(String[] args) {  
	        StringJoiner joinNames = new StringJoiner(","); // passing comma(,) as delimiter   
	          
	        // Adding values to StringJoiner  
	        joinNames.add("Rahul");  
	        joinNames.add("Raju");  
	        joinNames.add("Peter");  
	        joinNames.add("Raheem");  
	                  
	        System.out.println(joinNames);  
	        
	        StringJoiner joinNames2 = new StringJoiner(":", "[", "]");   // passing comma(,) and square-brackets as delimiter   
	          
	        // Adding values to StringJoiner  
	        joinNames2.add("Rahul");  
	        joinNames2.add("Raju");  
	        joinNames2.add("Peter");  
	        joinNames2.add("Raheem");  
	                  
	        System.out.println(joinNames2); 
	        StringJoiner merge = joinNames.merge(joinNames2);   
	        System.out.println(merge);  
	    }  
}
