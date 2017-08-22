import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';

import { Observable } from 'rxjs/Observable';
import { News } from '../classes/news';
import 'rxjs/add/operator/map';

@Injectable()
export class NewsService {

  private url: string = 'https://parse-it.in.ua/api/article/';

  constructor(private _http: Http) { }

  getNews(): Observable<News[]> {
    return this._http.get(this.url)
      .map((response: Response) => {
        console.log(`----------> News Service === response from getNews -> ${response.json().news}`);
        return response.json().news;
      })
  }

  /* todo question if we need more news to be shown on main page */
}
