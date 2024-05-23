from django import forms
from django.forms import CharField, EmailField, ChoiceField, DateField, DateInput
from gestaoAtivos.handle_excel import listar_ativos_disponiveis

class Solicitacao_Ativo(forms.Form):

    GRUPOS_EMAIL_CHOICES = (
        ('Todos', 'Todos'),
        ('Prestadores', 'Prestadores'),
        ('CLT', 'CLT'),
        ('Estagiario', 'Estagiario'),
        ('Treinamentos', 'Treinamentos'),
        ('Gente & Gestão', 'Gente & Gestão'),
        ('Oportunidades', 'Oportunidades'),
        ('Contato', 'Contato'),
        ('Admgente', 'Admgente')
    )

    DISPOSITIVOS_CHOICES = (
        ('Notebook + Carregador', 'Notebook + Carregador'),
        ('Telefone Celular', 'Telefone Celular')
    )
    # Codigo do ativo e converção para tupla
    ativos_disponiveis = listar_ativos_disponiveis()
    ativos_tuplas = [(ativo, ativo) for ativo in ativos_disponiveis]
    CODIGO_ATIVO_CHOICES = tuple(ativos_tuplas)

    solicitante = CharField(
        label='Nome de quem esta solicitando',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    ) # Char

    inicio_colaborador = DateField(
        label='Inicio Colaborador',
        required=True,
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
    ) # DATE

    nome = CharField(
        label='Nome Completo',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    ) # Char

    endereco = CharField(
        label='Endereco',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    ) # Char

    criacao_email = CharField(
        label='Email',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'email'})
    ) # Char (porque é apenas usuario)

    gestor_direto = CharField(
        label='Diretor',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    ) # Char

    grupo_email = ChoiceField(
        label='Grupo de Email',
        widget=forms.RadioSelect(),
        choices=GRUPOS_EMAIL_CHOICES)
    # CHOICES

    cargo = CharField(
        label='Cargo',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    ) # Char

    departamento = CharField(
        label='Departamento'
        , max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    ) # Char

    cliente = CharField(
        label='Cliente',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    ) # Char

    dispositivo = ChoiceField(
        label='Tipo de Dispositivo',
        widget=forms.RadioSelect(),
        choices=DISPOSITIVOS_CHOICES
    ) # CHOICES

    codigo_ativo = ChoiceField(
        label='Selecione um Ativo Disponível',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=CODIGO_ATIVO_CHOICES
    )
