import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormGroup,  FormBuilder,  Validators } from '@angular/forms';
import { StudentService } from '../student.service';

@Component({
  selector: 'app-student-update',
  templateUrl: './student-update.component.html',
  styleUrls: ['./student-update.component.css']
})
export class StudentUpdateComponent implements OnInit {

  student: any = {};
  angForm: FormGroup;
  constructor(private route: ActivatedRoute,
    private router: Router,
    private bs: StudentService,
    private fb: FormBuilder) {
      this.createForm();
  }

  createForm() {
   this.angForm = this.fb.group({
    id: ['', Validators.required ],
    roll: ['', Validators.required ],
    name: ['', Validators.required ],
    student_class: ['', Validators.required ],
    date_of_birth: ['', Validators.required ],
    address: ['', Validators.required ],
    email_address: ['', Validators.required ],
    phone_number: ['', Validators.required ],
    });
  }

  updateStudent(roll, name, student_class, date_of_birth, address, phone_number, email_address) {
    this.route.params.subscribe(params => {
       this.bs.updateStudent(params['id'],roll, name, student_class, date_of_birth, address, phone_number, email_address );
       this.router.navigate(['student']);
 });
}
  ngOnInit() {
    this.route.params.subscribe(params => {
      this.bs.editStudent(params['id']).subscribe(res => {
        this.student = res;
    });
  });
  }

}
