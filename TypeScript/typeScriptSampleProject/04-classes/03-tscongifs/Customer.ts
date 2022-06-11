class Customer{
    //Usage of tsc --target ES5 --noEmitOnError Customer.ts
    private _firstName: string;
    public get firstName(): string {
        return this._firstName;
    }
    public set firstName(value: string) {
        this._firstName = value;
    }
    private _lastName: string;
    public get lastName(): string {
        return this._lastName;
    }
    public set lastName(value: string) {
        this._lastName = value;
    }
    
    constructor(theFirst:string,theLast:string){
        this._firstName=theFirst;
        this._lastName=theLast;
    }
   
}
let myCustomer =new Customer("Tommy","Hilfiger");

console.log(myCustomer.firstName);
console.log(myCustomer.lastName);