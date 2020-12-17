from django import forms

from voice_chat.models import Config


class AuthForm(forms.Form):
    name = forms.CharField(max_length=30)
    code = forms.CharField(max_length=30)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)




'''
class AuthForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = ("name", "code","password")

    def save(self, commit=True, name=None, code=None ,password = None):
        auth = super(AuthForm, self).save(commit=False)
        auth.name = name
        auth.code = code
        auth.password = password
        if commit:
            auth.save()
        return auth


'''


