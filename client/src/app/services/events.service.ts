import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';

import { Observable } from 'rxjs/Observable';
import { Event } from '../classes/event';
import 'rxjs/add/operator/map';

@Injectable()
export class EventsService {

  private url: string = 'https://parse-it.in.ua/api/event/';

  constructor(private _http: Http) { }

  getEvents(): Observable<Event[]> {
    return this._http.get(this.url)
      .map((response: Response) => {
        console.log(`----------> Events Service === response from getEvents -> ${response.json().events}`);
        return response.json().events;
      })
  }

  /* todo question if we need more events to be shown on main page */
}
