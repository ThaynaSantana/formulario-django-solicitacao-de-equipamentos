from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from gestaoAtivos.handle_excel import inserir_dados_solicitacao
from gestaoAtivos.forms import Solicitacao_Ativo


# Create your views here.
def index(request):
    if request.method == "POST":
        form = Solicitacao_Ativo(request.POST)
        if form.is_valid():
            # Pegando os dados inseridos do formulario
            solicitante = form.cleaned_data['solicitante']
            inicio_colaborador = form.cleaned_data['inicio_colaborador']
            nome = form.cleaned_data['nome']
            endereco = form.cleaned_data['endereco']
            criacao_email = form.cleaned_data['criacao_email']
            gestor_direto = form.cleaned_data['gestor_direto']
            cargo = form.cleaned_data['cargo']
            departamento = form.cleaned_data['departamento']
            cliente = form.cleaned_data['cliente']
            dispositivo = form.cleaned_data['dispositivo']
            codigo_ativo = form.cleaned_data['codigo_ativo']
            # Fazendo um array com os dados
            dados_formulario = [inicio_colaborador, nome, endereco, criacao_email, gestor_direto, cargo, departamento,
                                cliente, dispositivo, codigo_ativo, solicitante]
            # Inserindo a solicitação na planilha
            inserir_dados_solicitacao(dados_formulario)
            return sucesso(request)
    else:
        form = Solicitacao_Ativo()

    return render(request, "formulario.html", {"form": form})


def sucesso(request):
    return render(request, 'sucesso.html')
