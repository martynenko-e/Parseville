/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { ShowOnMainVacancyService } from './show-on-main-vacancy.service';

describe('ShowOnMainVacancyService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ShowOnMainVacancyService]
    });
  });

  it('should ...', inject([ShowOnMainVacancyService], (service: ShowOnMainVacancyService) => {
    expect(service).toBeTruthy();
  }));
});
