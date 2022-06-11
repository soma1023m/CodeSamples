package mySamplejava8.nashorn;

import java.util.Scanner;
import java.util.StringJoiner;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.SimpleScriptContext;

public class Example01 {
	public static void main(String[] args) throws Exception{  
        // Creating script engine  
		ScriptEngine engine = new ScriptEngineManager().getEngineByName("nashorn");
		SimpleScriptContext context = new SimpleScriptContext();
		// Reading Nashorn file  
        StringJoiner joinNames = new StringJoiner("");
        try (Scanner scanner = new Scanner(Example01.class.getResourceAsStream("/js/hello.js"))) {
        	  while (scanner.hasNextLine()) {        		
        	    //System.out.println(scanner.nextLine());
        	   joinNames.add(scanner.nextLine().toString());
        	  }     	  
        	  
        	}
        //engine.eval("print('Hello Nashorn');",context);  
        System.out.println("joinNames"+joinNames);
       // Invocable invocable = (Invocable)engine;  
        //engine.eval(joinNames.toString());
        // calling a function  
        //invocable.invokeFunction("functionDemo1");  
        // calling a function and passing variable as well.  
        //invocable.invokeFunction("functionDemo2","Nashorn");    
        
    }  
}
