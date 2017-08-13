/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { VacancyListService } from './vacancy-list.service';

describe('VacancyListService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [VacancyListService]
    });
  });

  it('should ...', inject([VacancyListService], (service: VacancyListService) => {
    expect(service).toBeTruthy();
  }));
});
