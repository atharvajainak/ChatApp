from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'position']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = User.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email '{email}' is already in use.")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username '{username}' is already in use.")

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.CharField(label='Email Id')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user_obj = User.objects.get(email=email)
        except Exception as e:
            raise forms.ValidationError('User does not exist')
        if not user_obj.check_password(password):
            raise forms.ValidationError('Incorrect Credentials')
        self.cleaned_data['user_obj'] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)