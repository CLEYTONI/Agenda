from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'categoria', 'mostar')

    list_display_links = ('nome', 'sobrenome')

    # list_filter = ('nome', 'sobrenome')

    search_fields = ('nome', 'sobrenome', 'telefone')

    # Defini quantos dados vai mostrar por pagina
    list_per_page = 5

    list_editable = ('telefone', 'mostar')  # serve para condicionais


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
