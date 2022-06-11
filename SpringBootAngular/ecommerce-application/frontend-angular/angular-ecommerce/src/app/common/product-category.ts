import { ICategory } from "./iproduct";

export class ProductCategory implements ICategory {
   id: number;
    public getId(): number {
        return this.id;
    }
    
    categoryName: string;
    public getCategoryName(): string {
       
        return this.categoryName;
    }
    
    constructor(id: number,categoryName: string) {
        this.id= id;
        this.categoryName=categoryName;

    }
       

}