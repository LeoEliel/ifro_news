from django.db.transaction import commit
from django.shortcuts import render, redirect
from django.template.defaulttags import comment
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

# Create your views here.
from .forms import ImagensFormSet, NewForm
from .models import New, ImgNew

class NewListView(ListView):
    model = New
    template_name = 'noticias/listar.html'
    queryset = New.publicados.all()
    context_object_name = 'news'

class NewCreateView(CreateView):
    model = New
    template_name = 'noticias/cadastro.html'
    form_class = NewForm
    success_url = reverse_lazy('listarNews')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        cont = super().get_context_data(**kwargs)
        cont['formset']= ImagensFormSet()
        return cont

    def post(self, request, *args, **kwargs):
        self.object = obj
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        imagens_formset = ImagensFormSet(self.request.POST)
        if form.is_valid() and imagens_formset.is_valid():
            return self.form_valid(form, imagens_formset())
        else:
            return self.form_valid(form, imagens_formset)

    def form_valid(self, form, img_formset):
        self.object = form.save(commit=False)
        img_formset.instance = self.object
        imagens = img_formset.save()
        return redirect('listarNews')

    def form_invalid(self, form, img_formset):
        return self.render_to_response(self.get_context_data(
            form=form, formset=img_formset))

