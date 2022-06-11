class Customer{
    //Usage of tsc --target ES5 --noEmitOnError Customer.ts
  
    public get firstName(): string {
        return this._firstName;
    }
    public set firstName(value: string) {
        this._firstName = value;
    }
   
    public get lastName(): string {
        return this._lastName;
    }
    public set lastName(value: string) {
        this._lastName = value;
    }
    
    constructor(private _firstName: string,private _lastName: string){
        
    }
   
}
let myCustomer =new Customer("Tommy","Hilfiger");

console.log(myCustomer.firstName);
console.log(myCustomer.lastName);