from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SoilProperty
from django.forms import formset_factory

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

'''
class SoilDataForm(forms.ModelForm):
    class Meta:
        model = SoilData
        fields = ('soil_type', 'ph_level', 'nutrient_content')
'''


'''
class SoilPropertiesForm(forms.Form):
    particle_size = forms.CharField(label='Particle Size', required=True)
    soil_ph = forms.CharField(label='Soil pH', required=True)
    cec = forms.CharField(label='Cation Exchange Capacity (CEC)', required=True)
    calcium = forms.CharField(label='Calcium', required=True)
    magnesium = forms.CharField(label='Magnesium', required=True)
'''


class SoilPropertiesForm(forms.Form):
    name = forms.CharField(label='Property', max_length=100)
    value = forms.CharField(label='Value', max_length=100)

SoilPropertiesFormSet = formset_factory(SoilPropertiesForm, extra=1)


class ChatForm(forms.Form):
    prompt = forms.CharField(label='Enter a prompt', max_length=255)

