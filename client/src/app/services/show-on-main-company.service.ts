import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';

import { Observable } from 'rxjs/Observable';
import { Company } from '../classes/company';
import 'rxjs/add/operator/map';

@Injectable()
export class ShowOnMainCompanyService {

  private url: string = 'https://parse-it.in.ua/api/company/';

  constructor(private _http: Http) { }

  getShowOnMainCompanies(): Observable<Company[]> {
    return this._http.get(this.url)
      .map((response: Response) => {
        console.log(`-------------> response from ShowOnMainCompanies Service`);
        console.log(`${response.json().companies}`);
        return response.json().companies;
      });
  }
}
