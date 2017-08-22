import { Component, OnInit } from '@angular/core';

import { News } from '../../classes/news';
import { NewsService } from '../../services/news.service';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {

  news: News[];
  errorMessage: string;

  constructor(private _newsService: NewsService) { }

  getNews(): void {
    this._newsService.getNews()
      .subscribe(
      news => this.news = news,
      error => this.errorMessage = <any>error,
      () => console.log('done < -- news')
      )
  }

  ngOnInit() {
    this.getNews();
  }

}
