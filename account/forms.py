from django import forms
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': '请填写用户名'})
    password = forms.CharField(required=True, error_messages={'required': '请填写密码'})


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='请输入密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='请再次输入密码', widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'name','mobile','email','city')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']