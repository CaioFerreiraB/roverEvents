from django import forms


class SubmitForm(forms.ModelForm):
	nome = forms.CharField()
	numeral = forms.IntegerField()
	estado = forms.ChoiceField(choices=[('SP', 'SP'), ('MG', 'MG')])
	diretor = forms.CharField()
	email_diretor = forms.EmailField()