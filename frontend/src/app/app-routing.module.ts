import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { StudentAddComponent } from './student-add/student-add.component';
import { StudentUpdateComponent } from './student-update/student-update.component';
import { StudentGetComponent } from './student-get/student-get.component';

const routes: Routes = [
  {
    path: 'students/create',
    component: StudentAddComponent
  },
  {
    path: 'students/edit/:id',
    component: StudentUpdateComponent
  },
  {
    path: 'students',
    component: StudentGetComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
