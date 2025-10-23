from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from stdimage import StdImageField


# Criando um
class PublicadosManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publicado')


class New(models.Model):
    objects = models.Manager()
    publicados = PublicadosManager()
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    titulo = models.CharField(max_length=120)
    texto = models.TextField()
    slug = models.SlugField(max_length=120)
    criado = models.DateTimeField(auto_now_add=True)
    publicado = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL,
                              null=True, blank=True)
    status = models.CharField(max_length=9, choices=STATUS,
                              default='rascunho')


    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['-publicado']

    def __str__(self):
        return self.titulo


class ImgNew(models.Model):
    img = StdImageField(upload_to='imgNew',
                        variations={'thumb':{'width':280,
                                             'height': 280},
                                    'mini':{'width':28,
                                            'height':28}
                                    }
                        )
    main = models.BooleanField(default=False, unique=True)
    new = models.ForeignKey(New, on_delete=models.CASCADE,
                            related_name='imagensnotica')

    def __str__(self):
        return f'Imagem da notícia {self.new.id}'
