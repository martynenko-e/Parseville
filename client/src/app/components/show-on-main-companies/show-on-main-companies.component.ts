import { Component, OnInit } from '@angular/core';

import { Company } from '../../classes/company';
import { ShowOnMainCompanyService } from '../../services/show-on-main-company.service';

@Component({
  selector: 'app-show-on-main-companies',
  templateUrl: './show-on-main-companies.component.html',
  styleUrls: ['./show-on-main-companies.component.css']
})
export class ShowOnMainCompaniesComponent implements OnInit {

  companies: Company[];
  errorMessage: string;

  constructor(private _showOnMainCompanyService: ShowOnMainCompanyService) { }

  getShowOnMainCompanies(): void {
    this._showOnMainCompanyService.getShowOnMainCompanies()
      .subscribe(
      companies => this.companies = companies,
      error => this.errorMessage = <any>error,
      () => console.log('showOnMainCompanies --> subscription is done')
      )
  }

  ngOnInit() {
    this.getShowOnMainCompanies();
  }

}
