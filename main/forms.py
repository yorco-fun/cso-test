from django import forms


class OrderForm(forms.ModelForm):
    firstname = forms.CharField(label="Ім'я", max_length=100, required=True)
    lastname = forms.CharField(label="Прізвище", max_length=100, required=True)
    surname = forms.CharField(label="По-батькові", max_length=100, required=False)
    adress = forms.CharField(label="Адреса", required=False)
    street = forms.CharField(required=False)
    building = forms.CharField(required=False)
    phone = forms.CharField(label="Контактний телефон", max_length=12, required=True)
    comment = forms.CharField(label="Коментар", required=False)