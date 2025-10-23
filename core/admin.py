from django.contrib import admin

from .models import Cargo, Funcionario, RotinaTrabalho

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'ativo', 'criado']
    list_editable = ['ativo']

@admin.register(RotinaTrabalho)
class RotinaTrabalhoAdmin(admin.ModelAdmin):
    list_display = ['titulo']
