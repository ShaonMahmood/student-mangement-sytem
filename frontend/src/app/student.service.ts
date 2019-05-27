import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class StudentService {
  uri = 'https://steel-league-241504.appspot.com/api/v1/students';
  constructor(private http: HttpClient) { }

  addStudent(student_id, roll, name, student_class, date_of_birth, address, phone_number, email_address) {
    const obj = {
      student_id: student_id,
      roll: roll,
      name: name,
      phone_number: phone_number,
      student_class: student_class,
      date_of_birth: date_of_birth,
      address: address,
      email_address: email_address
    };
    console.log(obj);
    this.http.post(`${this.uri}`, obj)
        .subscribe(res => console.log('Done'));
  }

  getStudents() {
    return this
           .http
           .get(`${this.uri}`);
  }

  editStudent(id) {
    return this
            .http
            .get(`${this.uri}/${id}`);
    }

    updateStudent(student_id,roll, name, student_class, date_of_birth, address, phone_number, email_address,) {

      const obj = {
        student_id: student_id,
        roll: roll,
        name: name,
        phone_number: phone_number,
        student_class: student_class,
        date_of_birth: date_of_birth,
        address: address,
        email_address: email_address
        };
      this
        .http
        .put(`${this.uri}/${student_id}`, obj)
        .subscribe(res => console.log('Done'));
    }

    deleteStudent(student_id) {
      return this
                .http
                .delete(`${this.uri}/${student_id}`);
    }

}


