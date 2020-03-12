from django.contrib.auth.forms import UserCreationForm as UCF
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import login,authenticate
from django import forms

class UserCreationForm(UCF):
    class Meta(UCF.Meta):
        model = User
        fields = ('username','first_name','last_name','email')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(strip = False,widget=forms.PasswordInput)
    # We need to override the method __init__ to save the request, required to login the user
    def __init__(self,request=None,*args,**kwargs):
        self.request = request
        self.user = None
        super().__init__(*args,**kwargs)


    # We need to override the method clean to login the user
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(self.request,username = username, password = password)

        if user is not None:
            login(self.request,user)
        else:
            raise forms.ValidationError("El papito y la contrase;a no se parecen")

        return self.cleaned_data

    def get_user(self):
        return self.user