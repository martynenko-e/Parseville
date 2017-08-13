import { Component, OnInit } from '@angular/core';

import { Company } from '../../classes/company';
import { CompanyListService } from '../../services/company-list.service';

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})

export class CompanyListComponent implements OnInit {

  companies: Company[];
  counter: number = 1;
  errorMessage: string;
  selectedCompany: Company;
  someTest:number;

  constructor(private _companyListService: CompanyListService) { }

  selectCompany(id: number): void {
    this.companies.forEach(i => {
      if (i.id === id) {
        console.log(`selected company ${i} id is ${i.id} <-------`);
        this.selectedCompany = i;
      }
    });
  }

  getCompanies(): void {
    this._companyListService.getCompanies()
      .subscribe(
      companies => this.companies = companies,
      error => this.errorMessage = <any>error,
      () => console.log(`getting initial amount of companies is done`)
      )
  }

  showMoreCompanies(): void {
    this._companyListService.getMoreCompanies(this.counter)
      .subscribe(
      companies => {
        companies.forEach(i => {
          this.companies.push(i);
        })
        this.counter++;
      },
      error => this.errorMessage = <any>error,
      () => console.log(`getting companies by ${this.counter} is done`)
      )
  }

  ngOnInit() {
    this.getCompanies();
  }

}
