import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'vacancyListPipe'
})
export class VacancyListPipePipe implements PipeTransform {

  transform(vacancies: any, term: any): any {
    // check if search is undefined
    if (term === undefined) return vacancies;

    return vacancies.filter(vacancy => {
      return vacancy.name.toLowerCase().includes(term.toLowerCase());
    });
  }

}
