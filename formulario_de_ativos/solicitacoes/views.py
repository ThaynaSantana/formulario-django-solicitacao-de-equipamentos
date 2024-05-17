from django.shortcuts import render, redirect
from .forms import SolicitacaoForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = SolicitacaoForm()
    return render(request, 'solicitacoes/formulario.html', {'form': form})

def sucesso(request):
    return render(request, 'solicitacoes/sucesso.html')