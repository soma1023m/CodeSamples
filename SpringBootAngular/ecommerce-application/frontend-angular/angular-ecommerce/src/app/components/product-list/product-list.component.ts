import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

import { ProductService } from 'src/app/services/product.service';
import { map } from 'rxjs';

import { plainToClass, plainToInstance } from 'class-transformer';
import { Product } from 'src/app/common/product';
import { ProductCategory } from 'src/app/common/product-category';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-product-list',
  templateUrl: './product-list-grid.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  products: Product[] = [];
  currentCategoryId: number = 1;

  constructor(private productService: ProductService, private route: ActivatedRoute) {

  }
  ngOnInit() {
    this.route.paramMap.subscribe(() => {
      this.listProducts();
    });
  }
  listProducts() {
    const hasCategoryId: boolean = this.route.snapshot.paramMap.has("id");
    if (hasCategoryId) {
      this.currentCategoryId = 1;//
      //this.route.snapshot.paramMap.get("id");
    } else {
      this.currentCategoryId = 1;
    }
    this.productService.getProductList().subscribe(
      data => {
        console.log("data---------------------", data);
        //Write code to move json objectarray to product object array
        //npm install class-transformer --save to install class-transformer
        //npm install reflect-metadata --save
        //npm install es6-shim --save
        //https://www.npmjs.com/package/class-transformer
        this.products = plainToInstance(Product, data); // to convert user plain object a single user. also supports arrays

        console.log("products---------------------", this.products);
      }
    );




  }

}
