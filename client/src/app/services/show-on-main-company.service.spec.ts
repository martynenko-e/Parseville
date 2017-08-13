/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { ShowOnMainCompanyService } from './show-on-main-company.service';

describe('ShowOnMainCompanyService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ShowOnMainCompanyService]
    });
  });

  it('should ...', inject([ShowOnMainCompanyService], (service: ShowOnMainCompanyService) => {
    expect(service).toBeTruthy();
  }));
});
