import { AuthService } from './../../core/auth/auth.service';
import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  @ViewChild('usuarioInput') usuarioInput!: ElementRef<HTMLInputElement>;

  loginForm!: FormGroup;

  constructor(
    private authService: AuthService,
    private formBuilder: FormBuilder,
    private router: Router) { }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      usuario: ['', [Validators.required, Validators.minLength(3)]],
      senha: ['', [Validators.required, Validators.minLength(3)]]
    });

  }

  getErrorMessage(field: string): string {
    if (this.loginForm.get(field)?.hasError('required')) {
      return 'Campo obrigatório';
    }

    if (this.loginForm.get(field)?.hasError('minlength')) {
      return `Tamanho mínimo: ${this.loginForm.get(field)?.errors?.minlength.requiredLength}`;
    }

    return this.loginForm.get(field)?.invalid ? `Campo não válido ${field}` : '';

  }

  login(): void {
    const usuario: string = this.loginForm.get('usuario')?.value.toLowerCase().trim();
    const senha: string = this.loginForm.get('senha')?.value;

    this.authService
      .authenticate(usuario, senha)
      .subscribe(
        () => {
          this.router.navigate(['users', usuario]);
        },
        (error) => {
          this.loginForm.reset();
          alert('Usuário ou senha inválido');
          this.usuarioInput.nativeElement.focus();
        }
      );
  }

}
