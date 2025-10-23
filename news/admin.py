from django.contrib import admin
from .models import New, ImgNew


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display_padrao = ('titulo', 'criado', 'publicado', 'autor', 'status')
    fields_padrao = ('titulo','slug', 'texto', 'publicado')
    campo_restrito = ('status',)
    ordering = ['-status', '-publicado']
    prepopulated_fields = {'slug':('titulo',)}

    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'

    def get_list_display(self, request):
        if request.user.is_superuser:
            self.list_editable = ['status']
        else:
            self.list_editable = []
        return self.list_display_padrao

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.fields_padrao + self.campo_restrito
        else:
            return self.fields_padrao

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request,obj,form, change)

    def has_delete_permission(self, request, obj=None):
        # Verificando a permissão de exclusão geral. Um superusuário pode sempre excluir
        if obj is None or request.user.is_superuser:
            return super().has_delete_permission(request, obj)
        # Regra: Só pode excluir se for o autor E o status for RASCUNHO
        if obj.autor == request.user and obj.status == 'rascunho':
            return super().has_delete_permission(request, obj)
        # Sem permissão em todos os outros casos
        return False