from django.contrib import admin
from home.models import Grupo, Participante


admin.site.site_header = 'Cultive-se Admin'

	


class InputFilter(admin.SimpleListFilter):
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

class ParticpanteFilter(InputFilter):
    parameter_name = 'nome'
    title = 'Nome'
 
    def queryset(self, request, queryset):
        if self.value() is not None:
            nomes = self.value()
            return queryset.filter(
                Q(nome=nomes)
            )

class ParticipanteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'grupo')
	#search_fields = ('grupo__nome', 'nome')
	list_filters = (
        ParticpanteFilter,
    )



# Register your models here.
admin.site.register(Grupo)
admin.site.register(Participante, ParticipanteAdmin)
