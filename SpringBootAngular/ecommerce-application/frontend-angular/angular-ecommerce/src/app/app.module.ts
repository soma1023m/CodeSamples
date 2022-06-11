import { Component, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProductListComponent } from './components/product-list/product-list.component';
import { HttpClientModule } from '@angular/common/http';
import { ProductService } from './services/product.service';
import { NgLetModule } from 'ng-let';
import {Routes,RouterModule} from '@angular/router';
const routes : Routes=[
  {path:'category/id', component:ProductListComponent},
  {path:'category', component:ProductListComponent},
  {path:'products', component:ProductListComponent},
  {path:'', redirectTo:"", pathMatch:"full"},
  {path:'**', redirectTo:"", pathMatch:"full"}
];
@NgModule({
  declarations: [
    AppComponent,
    ProductListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule.forRoot(routes)
  ],
  providers: [ProductService],
  bootstrap: [AppComponent]
})
export class AppModule { }
