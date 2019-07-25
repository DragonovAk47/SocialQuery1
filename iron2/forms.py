from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from iron2.models import UserProfile,Document


class RegForm(UserCreationForm):
     email=forms.EmailField(required=True)
     class Meta:
         model=User
         fields=(
             'username',
             'first_name',
             'last_name',
             'email',
             'password1',
             'password2',

         )
     def save(self,commit=True):
         user=super(RegForm,self).save(commit=False)
         if commit:
             user.save()
         return user


class EditForm(UserChangeForm):

    class Meta:
        model=User

        fields=(
            'username',
            'email',
            'password',
        )


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control form-check-inline',
            'placeholder': "Username"


        }
    ))
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-check-inline',
            'placeholder': "Password"
        }
    ))

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('Filename','file', )

class UserProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=(
            'description',
            'Mobile',
            'Website',
            'image',
            'Email',
        )