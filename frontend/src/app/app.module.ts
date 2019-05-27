import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { SlimLoadingBarModule } from 'ng2-slim-loading-bar';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { StudentService } from './student.service';
import { StudentAddComponent } from './student-add/student-add.component';
import { StudentGetComponent } from './student-get/student-get.component';
import { StudentUpdateComponent } from './student-update/student-update.component';

@NgModule({
  declarations: [
    AppComponent,
    StudentAddComponent,
    StudentGetComponent,
    StudentUpdateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SlimLoadingBarModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [StudentService],
  bootstrap: [AppComponent]
})
export class AppModule { }
