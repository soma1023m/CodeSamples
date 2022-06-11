import { nullSafeIsEquivalent } from "@angular/compiler/src/output/output_ast";
import { IProduct } from "./iproduct";
import { ProductCategory } from "./product-category";

export class Product implements IProduct {
    id: number;
    category: ProductCategory;
    sku: string;
    name: string;
    description: string;
    unitPrice: number;
    imageUrl: string;
    active: boolean;
    unitsInStock: number;
    dateCreated: Date;
    lastUpdated: Date;



    constructor(id: number, category: ProductCategory, sku: string, name: string, description: string,
        unitPrice: number, imageUrl: string, active: boolean, unitsInStock: number, dateCreated: Date, lastUpdated: Date) {
        this.id = id;
        //this.category = new ProductCategory(category.id,category.categoryName);
        this.category = category;
        this.sku = sku;
        this.name = name;
        this.description = description;
        this.unitPrice = unitPrice;
        this.imageUrl = imageUrl;
        this.active = active;
        this.unitsInStock = unitsInStock;
        this.dateCreated = dateCreated;
        this.lastUpdated = lastUpdated;       

    }
    

}


