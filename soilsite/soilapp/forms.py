from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SoilData

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class SoilDataForm(forms.ModelForm):
    class Meta:
        model = SoilData
        fields = ('soil_type', 'ph_level', 'nutrient_content')



class SoilPropertiesForm(forms.Form):
    pH = forms.CharField(label='pH', required=True)
    % Organic Carbon = forms.CharField(label='% Organic Carbon', required=True)
    %Total Nitrogen = forms.CharField(label='%Total Nitrogen', required=True)
    Available Phosphorus (mg/kg) = forms.CharField(label='Available Phosphorus (mg/kg)', required=True)
    Exch Acidity (/kg) = forms.CharField(label='Exch Acidity (/kg)', required=True)
    Ca (cmol/kg) = forms.CharField(label='Ca (cmol/kg)', required=True)
    Mg (cmol/kg) = forms.CharField(label='Mg (cmol/kg)', required=True)
    K (cmol/kg) = forms.CharField(label='K (cmol/kg)', required=True)
    Na(cmol/kg) = forms.CharField(label='Na(cmol/kg)', required=True)
    Mn (mg/kg) = forms.CharField(label='Mn (mg/kg)', required=True)
    Fe (mg/kg) = forms.CharField(label='Fe (mg/kg)', required=True)
    Cu(mg/kg) = forms.CharField(label='Cu(mg/kg)', required=True)
    Zn(mg/kg) = forms.CharField(label='Zn(mg/kg)', required=True)
    % Sand = forms.CharField(label='% Sand', required=True)
    % Silt = forms.CharField(label='% Silt', required=True)
    % Clay = forms.CharField(label='% Clay', required=True)




class ChatForm(forms.Form):
    prompt = forms.CharField(label='Type your message', max_length=255)

