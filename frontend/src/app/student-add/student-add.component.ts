import { Component, OnInit } from '@angular/core';
import { FormGroup,  FormBuilder,  Validators } from '@angular/forms';
import { StudentService } from '../student.service';

@Component({
  selector: 'app-student-add',
  templateUrl: './student-add.component.html',
  styleUrls: ['./student-add.component.css']
})
export class StudentAddComponent implements OnInit {

  angForm: FormGroup;
  constructor(private fb: FormBuilder, private bs: StudentService) {
    this.createForm();
  }

  createForm() {
    this.angForm = this.fb.group({
      student_id: ['', Validators.required ],
      roll: ['', Validators.required ],
      name: ['', Validators.required ],
      student_class: ['', Validators.required ],
      date_of_birth: ['', Validators.required ],
      address: ['', Validators.required ],
      email_address: ['', Validators.required ],
      phone_number: ['', Validators.required ],
      
    });
  }

  addStudent(student_id, roll, name, student_class, date_of_birth, address, phone_number, email_address) {
    this.bs.addStudent(student_id, roll, name, student_class, date_of_birth, address, phone_number, email_address);
  }

  ngOnInit() {
  }

}
