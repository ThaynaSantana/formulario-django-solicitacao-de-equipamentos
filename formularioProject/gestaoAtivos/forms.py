from django import forms
from django.forms import CharField, ChoiceField, DateField
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
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Seu nome'}),
    ) # Char

    inicio_colaborador = DateField(
        label='Inicio Colaborador',
        required=True,
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
    ) # DATE

    nome = CharField(
        label='Nome Completo',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Nome e Sobrenome do Colaborador'}),
    ) # Char

    endereco = CharField(
        label='Endereco',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o endereço do Colaborador'}),
    ) # Char

    criacao_email = CharField(
        label='Email',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Insira para criação de email (nome.sobrenome), exemplo: joao.silva'}),
    ) # Char (porque é apenas usuario)

    gestor_direto = CharField(
        label='Gestor Direto',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Digite o nome do Gestor Direto do Colaborador'}),
    ) # Char

    grupo_email = ChoiceField(
        label='Grupo de Email',
        widget=forms.RadioSelect(),
        required=True,
        choices=GRUPOS_EMAIL_CHOICES)
    # CHOICES

    cargo = CharField(
        label='Cargo',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o cargo do Colaborador'}),
    ) # Char

    departamento = CharField(
        label='Departamento',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Digite o departamento que o Colaborador irá trabalhar'}),
    ) # Char

    cliente = CharField(
        label='Cliente',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do cliente'}),
    ) # Char

    dispositivo = ChoiceField(
        label='Tipo de Dispositivo',
        widget=forms.RadioSelect(),
        required=True,
        choices=DISPOSITIVOS_CHOICES
    ) # CHOICES

    codigo_ativo = ChoiceField(
        label='Selecione um Ativo Disponível',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        choices=CODIGO_ATIVO_CHOICES
    )
