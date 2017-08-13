import { Component, OnInit, Input } from '@angular/core';

import { Vacancy } from '../../classes/vacancy';


@Component({
  selector: 'app-vacancy-modal',
  templateUrl: './vacancy-modal.component.html',
  styleUrls: ['./vacancy-modal.component.css']
})
export class VacancyModalComponent implements OnInit {

  @Input()
  selectedVacancy: Vacancy;

  constructor() { }

  ngOnInit() {
  }

}
