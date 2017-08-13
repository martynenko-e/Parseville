/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { ShowOnMainVacanciesComponent } from './show-on-main-vacancies.component';

describe('ShowOnMainVacanciesComponent', () => {
  let component: ShowOnMainVacanciesComponent;
  let fixture: ComponentFixture<ShowOnMainVacanciesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ShowOnMainVacanciesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ShowOnMainVacanciesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
