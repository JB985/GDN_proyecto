from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'tip_documento', 'num_documento', 'phone', 'role')
        witgets = {
            'email': forms.EmailInput()
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'role')

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['cod','name','desc']

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['cod_sub','name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cod_cat','name','sub_cat']

class MobForm(forms.ModelForm):
    class Meta:
        model = Moviliario
        fields = ['name', 'desc', 'ad_date', 'num_placa_almacen', 'price', 'cat']
        widgets = {
            'ad_date': forms.DateInput(attrs={'type': 'date'}),
        }

class RegionalForm(forms.ModelForm):
    class Meta:
        model = Regional
        fields = ['cod_reg','name']

class CentroForm(forms.ModelForm):
    class Meta:
        model = CentroFormacion
        fields = ['nit','name','reg']

class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ['cod_sede','name','city','direct','reg']

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa_Formacion
        fields = ['cod_prog','name','hours','version']

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = ['num_ficha','name','etapa','fecha_inicio','fecha_fin','prog']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'})
        }