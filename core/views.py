from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from core.models import Funcionario, RotinaTrabalho
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['funcionarios'] = Funcionario.objects.order_by('?').all()
        contexto['rotinastrabalho'] = RotinaTrabalho.objects.order_by('?').all()
        return contexto

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request,
                         'E-mail enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,
                       'Não foi possível enviar o e-mail!')
        return super(IndexView, self).form_invalid(form)