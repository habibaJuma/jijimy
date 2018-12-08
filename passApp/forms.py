from flask import from
from flask.contrib.auth.model import User
from passApp.model import UserProfile

#FORMS
class UserForm(forms.ModelForm):
    passward = forms.CharField(Widget=forms.passwardInput())

    class Meta:
        Model = User
        field = ('username', 'email', 'password')

        class UserProfileInfoForm(forms.ModelForm):
            class Meta:
                Model = UserProfile
                fields=('portfolio_site''profile_pic',)