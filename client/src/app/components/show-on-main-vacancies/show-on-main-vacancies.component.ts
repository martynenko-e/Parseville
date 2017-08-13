import { Component, OnInit } from '@angular/core';

import { Vacancy } from '../../classes/vacancy';
import { ShowOnMainVacancyService } from '../../services/show-on-main-vacancy.service';

@Component({
  selector: 'app-show-on-main-vacancies',
  templateUrl: './show-on-main-vacancies.component.html',
  styleUrls: ['./show-on-main-vacancies.component.css']
})
export class ShowOnMainVacanciesComponent implements OnInit {

  vacancies: Vacancy[];
  errorMessage: string;

  constructor(private _showOnMainVacancyService: ShowOnMainVacancyService) { }


  getShowOnMainVacancies(): void {
    this._showOnMainVacancyService.getShowOnMainVacancies()
      .subscribe(
      vacancies => this.vacancies = vacancies,
      error => this.errorMessage = <any>error,
      () => console.log('done')
      )
  }

  ngOnInit() {
    this.getShowOnMainVacancies();
  }

}
