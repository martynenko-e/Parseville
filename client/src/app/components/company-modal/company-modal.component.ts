import { Component, OnInit, Input } from '@angular/core';

import { Company } from '../../classes/company';

@Component({
  selector: 'app-company-modal',
  templateUrl: './company-modal.component.html',
  styleUrls: ['./company-modal.component.css']
})
export class CompanyModalComponent implements OnInit {

  @Input()
  selectedCompany: Company;

  constructor() { }

  ngOnInit() {
  }

}
