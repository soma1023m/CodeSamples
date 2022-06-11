package mySamplejava8.jdbc;

import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverAction;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class Example01 implements DriverAction{
	// implementing deregister method of DriverAction interface  
    public void deregister() {  
        System.out.println("Driver deregistered");  
    }  
    public static void main(String args[]){  
        try{  
            // Creating driver instance  
            Driver driver = new com.mysql.jdbc.Driver();  
            // Creating Action Driver  
            DriverAction da = new Example01();  
            // Registering driver by passing driver and driverAction  
            DriverManager.registerDriver(driver, da);  
            // Creating connection  
            Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/full-stack-ecommerce?useSSL=false&useUnicode=yes&characterEncoding=UTF-8&allowPublicKeyRetrieval=true&serverTimezone=UTC","ecommerceapp","ecommerceapp");  
            //Here student is database name, root is username and password is mysql  
            Statement stmt=con.createStatement();   
            // Executing SQL query  
            ResultSet rs=stmt.executeQuery("select * from product");    
            while(rs.next()){    
                System.out.println(rs.getInt(1)+""+rs.getString(2)+""+rs.getString(3));    
            }  
            // Closing connection  
            con.close();    
            // Calling deregisterDriver method  
            DriverManager.deregisterDriver(driver);  
        }catch(Exception e){ System.out.println(e);}    
    }    
}
