from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.


class Register(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phno = models.IntegerField()
    email = models.EmailField(null=False)
    password = models.CharField(null=False,max_length=15)


class Validate(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.cleaned_data = None

    def emailaddress(self):

        cleaned_data = super(Validate, self).clean()
        emailaddress = self.cleaned_data['emailadd']
        if User.objects.filter(username=emailaddress).exists():
            raise forms.ValidationError("This User is already registered!")
        return emailaddress

class AddItems():
    valuser=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE())