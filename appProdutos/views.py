from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Produto
from .forms import ProdutoForm



def listar(request):
    produtos = Produto.objects.all() # -> Atribui os dados do model Produto, a variavel produtos
    return render(request, 'appProdutos/listar.html', {'produtos':produtos})



def criar(request):
    if request.method == 'POST':
        
        form = ProdutoForm(request.POST) # -> Atribui os dados do form ProdutoForm a variavel form

        if form.is_valid():
            form.save() # -> Momento que salva no banco

            return redirect('listar') # -> Redireciona o usuário ao template "listar"

    else:
        form = ProdutoForm()

    return render(request, 'appProdutos/formulario.html', {'form': form})





def editar(request, id):
    
    produto = get_object_or_404(
        produto,
        id=id
    )

    if request.method == 'POST':

        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            form.save()

    else:
        form = ProdutoForm(
            instance=produto
        )

        return render(request, 'appProdutos/formulario.html', {'form':form})




def excluir(request, id):

    produto = get_object_or_404(
        produto,
        id=id
    )

    if request.method == 'POST':
        produto.delete()
        return redirect('listar')

    return render(request, 'appProdutos/delete.html', {'produto':produto})