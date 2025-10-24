from PIL.Image import Image
from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from .models import New, ImgNew

class NewForm(forms.ModelForm):

    class Meta:
        model = New

        exclude = {'autor', 'status', 'publicado', 'criado'}


class ImgNewForm(forms.ModelForm):
    class Meta:
        model = ImgNew
        fields = ['img', 'main']

ImagensFormSet = inlineformset_factory(New, ImgNew, form= ImgNewForm,
                                       extra=2, can_delete=True, exclude=[])

class Meta:
    model = ImgNew
    fields = ['img', 'main']