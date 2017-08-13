/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { VacancyModalComponent } from './vacancy-modal.component';

describe('VacancyModalComponent', () => {
  let component: VacancyModalComponent;
  let fixture: ComponentFixture<VacancyModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VacancyModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VacancyModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
