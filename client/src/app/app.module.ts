import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { VacancyListComponent } from './components/vacancy-list/vacancy-list.component';
import { CompanyListComponent } from './components/company-list/company-list.component';
import { CompanyModalComponent } from './components/company-modal/company-modal.component';
import { VacancyModalComponent } from './components/vacancy-modal/vacancy-modal.component';
import { PageNotFoundComponent } from './components/page-not-found/page-not-found.component';
import { ShowOnMainVacanciesComponent } from './components/show-on-main-vacancies/show-on-main-vacancies.component';
import { ShowOnMainCompaniesComponent } from './components/show-on-main-companies/show-on-main-companies.component';
import { NavComponent } from './components/nav/nav.component';
import { FooterComponent } from './components/footer/footer.component';
import { MainComponent } from './components/main/main.component';
import { NewsComponent } from './components/news/news.component';
import { EventsComponent } from './components/events/events.component';

import { VacancyListService } from './services/vacancy-list.service';
import { CompanyListService } from './services/company-list.service';
import { ShowOnMainVacancyService } from './services/show-on-main-vacancy.service';
import { ShowOnMainCompanyService } from './services/show-on-main-company.service';
import { VacancyListPipePipe } from './pipes/vacancy-list-pipe.pipe';


@NgModule({
  declarations: [
    AppComponent,
    CompanyModalComponent,
    VacancyModalComponent,
    VacancyListComponent,
    CompanyListComponent,
    ShowOnMainVacanciesComponent,
    ShowOnMainCompaniesComponent,
    PageNotFoundComponent,
    NavComponent,
    FooterComponent,
    MainComponent,
    NewsComponent,
    EventsComponent,
    VacancyListPipePipe
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule
  ],
  providers: [
    VacancyListService,
    ShowOnMainVacancyService,
    CompanyListService,
    ShowOnMainCompanyService],
  bootstrap: [AppComponent]
})
export class AppModule { }
