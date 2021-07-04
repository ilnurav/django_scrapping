from django import forms


class UserForm(forms.Form):
    city = forms.CharField()
    '''
    name = forms.CharField()
    age = forms.IntegerField()
    comment = forms.CharField(label="Комментарий", widget=forms.PasswordInput)
    '''