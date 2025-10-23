from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200,
                                 blank=True, null=True)

    def __str__(self):
        return self.nome


class Funcionario(Base):
    nome = models.CharField(max_length=100)
    bio = models.TextField()
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL,
                              blank=True, null=True)
    foto = StdImageField(upload_to='equipe',
                         variations={'thumb':{'width': 60,
                                              'height': 60,
                                              'crop':True}})

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome

class RotinaTrabalho(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = StdImageField(upload_to='rotina',
                           variations={'thumb':{'width': 32,
                                              'height': 32,
                                              'crop':True}})

    class Meta:
        verbose_name = 'Rotina de Trabalho'
        verbose_name_plural = 'Rotinas de Trabalho'

    def __str__(self):
        return self.titulo
