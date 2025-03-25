from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    # profile = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

        self.fields['password1'].label = "password"
        self.fields['password2'].label = "Confirm password"


    class Meta:
        model = CustomUser
        fields = ['username','phone_number', 'password1', 'password2',]