/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { CompanyListService } from './company-list.service';

describe('CompanyListService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CompanyListService]
    });
  });

  it('should ...', inject([CompanyListService], (service: CompanyListService) => {
    expect(service).toBeTruthy();
  }));
});
