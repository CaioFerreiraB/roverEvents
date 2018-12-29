from django.contrib import admin
from home.models import Grupo, Participante


admin.site.site_header = 'Cultive-se Admin'

class ParticipanteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'grupo')
	search_fields = ('grupo__nome', 'nome')
	

# Register your models here.
admin.site.register(Grupo)
admin.site.register(Participante, ParticipanteAdmin)