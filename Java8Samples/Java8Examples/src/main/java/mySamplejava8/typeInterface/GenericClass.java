package mySamplejava8.typeInterface;

class GenericClass<X> {  
    X name;  
  public void setName(X name){  
      this.name = name;  
    }  
  public X getName(){  
      return name;  
    }  
  public String genericMethod(GenericClass<String> x){  
      x.setName("John");  
      return x.name;  
    }  
}  
