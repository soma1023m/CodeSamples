import { HttpClient, JsonpClientBackend } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from '../common/product';
import { map } from 'rxjs'; 
@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private baseUrl="http://localhost:8080/api/products?size=5";
  jsonResponse:any;
  jsonResponseList=[];

  constructor(private httpClient: HttpClient) { }

  getProductList(): Observable<any>{
      console.log("Output here---------------------");
      //return this.httpClient.get<GetResponse>(this.baseUrl).pipe(
      //map(Response=>Response._embedded.products)
      this.jsonResponse=this.httpClient.get(this.baseUrl);
      console.log("jsonResponse---------------------",this.jsonResponse);
      return this.jsonResponse;
    }
    
 
}

