from django import forms
from .models import Doador, Endereco

class FormDoador(forms.ModelForm):
	class Meta:
		model = Doador		
		fields = '__all__'
		exclude = ['endereco']

class FormEndereco(forms.ModelForm):
	class Meta:
		model = Endereco		
		fields = '__all__'
