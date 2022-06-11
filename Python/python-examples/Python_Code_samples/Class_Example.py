#To inherit from another class
#class derivedClassName (BaseClass1Name,BaseClass2Name):
class Customer:
    #mutable structure is common to all instances
    phones=[]
    def __init__ (self,id,name,address,phone):
        self.id=id
        self.name=name
        self.address=address
        self.phone=phone
        self.phones.append(phone)
    
    def display(self):
        print("id={0}, name={1} , address={2} , phone= {3}".format(self.id,self.name,self.address,self.phone))
        print("phones={0}".format(self.phones))
  

cust1= Customer(10,"Soma","123hjt","12312-3123")
cust1.display()
cust2= Customer(20,"Soma2","123hjt2","9999-9999")
cust2.display()
#mutable properties show same data
cust1.display()
    

