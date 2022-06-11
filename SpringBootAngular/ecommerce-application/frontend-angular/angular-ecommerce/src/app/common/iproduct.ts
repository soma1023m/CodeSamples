
export interface ICategory {
    id: number;
    categoryName: string;
}

export interface IProduct {
    id: number;
    category: ICategory;
    sku: string;
    name: string;
    description: string;
    unitPrice: number;
    imageUrl: string;
    active: boolean;
    unitsInStock: number;
    dateCreated: Date;
    lastUpdated?: Date;
}




