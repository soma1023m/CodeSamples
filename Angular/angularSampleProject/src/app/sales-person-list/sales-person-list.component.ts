import { Component, OnInit } from '@angular/core';
import { SalesPerson } from './sales-person';

@Component({
  selector: 'app-sales-person-list',
  templateUrl: './sales-person-list-bootstrap.component.html',
  styleUrls: ['./sales-person-list.component.css']
})
export class SalesPersonListComponent implements OnInit {
  salesPersonList :SalesPerson[]=[
    new SalesPerson(1,"tom","Hill","tomhil@gmail.com",1000),
    new SalesPerson(2,"tom2","Hill2","tomhil2@gmail.com",50000),
    new SalesPerson(3,"tom3","Hill3","tomhil3@gmail.com",60000),
    new SalesPerson(4,"tom4","Hill4","tomhil4@gmail.com",1000),
    new SalesPerson(5,"tom5","Hill5","tomhil5@gmail.com",30000)
    ]
  constructor() { }

  ngOnInit(): void {
  }
  


}
