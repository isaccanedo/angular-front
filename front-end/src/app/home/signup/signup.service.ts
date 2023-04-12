import { Signup } from './signup.model';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SignupService {

  constructor(private httpClient: HttpClient) { }

  createUser(signup: Signup): Observable<any> {
    return this.httpClient.post(`${environment.apiUrl}/usuario/`, signup);
  }

}
