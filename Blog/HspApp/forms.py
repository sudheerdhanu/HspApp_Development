from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(forms.ModelForm):
    mobile = forms.CharField(widget=forms.TextInput(attrs={'type': 'number','class':'form-control','placeholder':' Enter Mobile'}))
    address = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'type': 'text','class':'form-control','placeholder':' Enter address'}))
    conform_password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type': 'password','class':'form-control','placeholder':' Enter conform_password'}))
    # address=forms.CharField(label='addredd',max_length=40)
    # active=forms.BooleanField(label='active')
    # conform_password=forms.CharField(max_length=30)

    class Meta:

        model=User
        fields=('first_name','last_name','username','email','password')
        fields_required = ['first_name','last_name','username','email','password']
        help_texts = {
            'username': None,
        }

        widgets={

            'first_name':forms.TextInput(attrs={

                'class':'form-control',
                'placeholder': 'Enter First Name'
            }),

            'last_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Enter Last Name'
            }),

            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Username'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }),

            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Password'
            }),










        }

        def clean_password2(self):
            password1 = self.cleaned_data.get("password")
            password2 = self.cleaned_data.get("conform_password")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
            return password1

