from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    mensagem = forms.CharField(widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']
        conteudo = (f'Mensagem de: {nome}\n'
                    f'{mensagem}')
        mail = EmailMessage(
            subject=f'contato de {nome}',
            body=conteudo,
            from_email=email,
            to=['marcos.faino@ifro.edu.br'],
            headers={'Reply-To': email}
        )
        mail.send()
