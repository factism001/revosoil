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
        """Save the new user"""
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
    ph = forms.CharField(label='pH', required=False)
    organic_carbon = forms.CharField(label='% Organic Carbon', required=False)
    total_nitrogen = forms.CharField(label='%Total Nitrogen', required=False)
    available_phosphorus_mg_kg = forms.CharField(label='Available Phosphorus (mg/kg)', required=False)
    exch_acidity_kg = forms.CharField(label='Exch Acidity (/kg)', required=False)
    ca_cmol_kg = forms.CharField(label='Ca (cmol/kg)', required=False)
    mg_cmol_kg = forms.CharField(label='Mg (cmol/kg)', required=False)
    k_cmol_kg = forms.CharField(label='K (cmol/kg)', required=False)
    na_cmol_kg = forms.CharField(label='Na(cmol/kg)', required=False)
    mn_mg_kg = forms.CharField(label='Mn (mg/kg)', required=False)
    fe_mg_kg = forms.CharField(label='Fe (mg/kg)', required=False)
    cu_mg_kg = forms.CharField(label='Cu(mg/kg)', required=False)
    zn_mg_kg = forms.CharField(label='Zn (mg/kg)', required=False)
    sand = forms.CharField(label='% Sand', required=False)
    silt = forms.CharField(label='% Silt', required=False)
    clay = forms.CharField(label='% Clay', required=False)




class ChatForm(forms.Form):
    prompt = forms.CharField(label='Type your message', max_length=255)

