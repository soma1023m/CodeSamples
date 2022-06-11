package mySamplejava8.base64.forEach;

import java.util.ArrayList;
import java.util.List;

public class Example01 {
	public static void main(String[] args) {  
        List<String> gamesList = new ArrayList<String>();  
        gamesList.add("Football");  
        gamesList.add("Cricket");  
        gamesList.add("Chess");  
        gamesList.add("Hocky");  
        System.out.println("------------Iterating by passing lambda expression--------------");  
        gamesList.forEach(games -> System.out.println(games));  
        gamesList.forEach(System.out::println);  
        gamesList.stream().forEachOrdered(System.out::println);  
          
    }  
}
