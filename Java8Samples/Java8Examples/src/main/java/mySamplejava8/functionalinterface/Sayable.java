package mySamplejava8.functionalinterface;

@FunctionalInterface
public interface Sayable {
	void say(String msg);  
	// It can contain any number of Object class methods.  
    int hashCode();  
    String toString();  
    boolean equals(Object obj);  
}
