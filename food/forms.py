from django import forms
from django.contrib.auth.models import User
from food.models import College, Consumer, Transaction, Driver


class CollegeForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = College
        fields = ('name',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ConsumerForm(forms.ModelForm):

    name=forms.CharField(max_length=128)
    addressline1=forms.CharField(max_length=128)
    city=forms.CharField(max_length=128)
    zipcode=forms.IntegerField()

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Consumer
        exclude = ('user',)

class DriverForm(forms.ModelForm):

    name=forms.CharField(max_length=128)
    phone=forms.CharField(max_length=128)

    SWAT = 'Swarthmore'
    HAVE = 'Haverford'
    SCHOOL_CHOICES = ((SWAT, 'Swarthmore'), (HAVE, 'Haverford'))
    school=forms.ChoiceField(SCHOOL_CHOICES)

    class Meta:
        model = Driver
        exclude = ('user',)


class TransactionForm(forms.ModelForm):
    drop_off = forms.CharField(max_length=128)
    city = forms.CharField(max_length=128)
    zipcode = forms.IntegerField()

    number_meals = forms.IntegerField()
    
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Transaction
        exclude = ('school','consumer','date', 'name')
