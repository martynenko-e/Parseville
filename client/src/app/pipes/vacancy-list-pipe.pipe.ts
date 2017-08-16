import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'vacancyListPipe'
})
export class VacancyListPipePipe implements PipeTransform {

  transform(value: any, args?: any): any {
    return null;
  }

}
