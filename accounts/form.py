from django import forms



class LoginForm(forms.Form):
    usern = forms.CharField(max_length=100,label='username',widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'class2':'glyphicon glyphicon-user',
            'font-size':'10px',
        }
    ))
    pwd = forms.CharField(max_length=100,label='password',widget=forms.PasswordInput(
        attrs={
             'class':'form-control',
            
        }
    ))

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )