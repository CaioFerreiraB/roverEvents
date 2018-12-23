from django.db import models

# Create your models here.
class Grupo(models.Model):
	nome = models.CharField(max_length=100)
	numeral = models.IntegerField()
	estado = models.CharField(max_length=2)
	diretor = models.CharField(max_length=200)
	email_diretor = models.EmailField()

	class Meta:
		unique_together = (('nome', 'numeral', 'estado'),)

	def __str__(self):
		return self.nome + ' - ' + str(self.numeral) + ' - ' + self.estado

class Participante(models.Model):
	nome = models.CharField(max_length=200)
	idade = models.IntegerField()
	email = models.EmailField()
	grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE)
	ficha_medica = models.FileField() 
	autorizacao = models.FileField()

	class Meta:
		unique_together = (('nome', 'idade', 'email', 'grupo'),)

	def __str__(self):
		return self.nome + '	(' + self.grupo.nome + ' - ' + str(self.grupo.numeral) + ' - ' + self.grupo.estado + ')'
