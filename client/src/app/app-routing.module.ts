import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { VacancyListComponent } from './components/vacancy-list/vacancy-list.component';
import { CompanyListComponent } from './components/company-list/company-list.component';
import { ShowOnMainVacanciesComponent } from './components/show-on-main-vacancies/show-on-main-vacancies.component';
import { ShowOnMainCompaniesComponent } from './components/show-on-main-companies/show-on-main-companies.component';
import { PageNotFoundComponent } from './components/page-not-found/page-not-found.component';
import { MainComponent } from './components/main/main.component';

const routes: Routes = [
    { path: '', component: MainComponent },
    { path: 'vacancies', component: VacancyListComponent },
    { path: 'companies', component: CompanyListComponent },
    { path: '**', component: PageNotFoundComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }