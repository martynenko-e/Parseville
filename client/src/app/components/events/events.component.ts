import { Component, OnInit } from '@angular/core';

import { Event } from '../../classes/event';
import { EventsService } from '../../services/events.service';


@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent implements OnInit {

  events: Event[];
  errorMessage: string;

  constructor(private _eventsService: EventsService) { }

  getEvents(): void {
    this._eventsService.getEvents()
      .subscribe(
      events => this.events = events,
      error => this.errorMessage = <any>error,
      () => console.log('done <-- events')
      )
  }

  ngOnInit() {
    this.getEvents();
  }

}
