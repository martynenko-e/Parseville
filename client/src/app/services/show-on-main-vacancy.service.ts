import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';

import { Observable } from 'rxjs/Observable';
import { Vacancy } from '../classes/vacancy';
import 'rxjs/add/operator/map';

@Injectable()
export class ShowOnMainVacancyService {

  private url: string = 'https://parse-it.in.ua/api/vacancy/';

  constructor(private _http: Http) { }

  getShowOnMainVacancies(): Observable<Vacancy[]> {
    return this._http.get(this.url)
      .map((response: Response) => {
        console.log('============>  response for Shwo on Main ---');
        console.log(response.json().vacancies);
        return response.json().vacancies;
      });
  }

}
