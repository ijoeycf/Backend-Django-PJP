from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sobre(request):
    dicionario = {
        "nome" : None,
        "idade": None
    }

    # Pega o retorno do input "InputNome" e inclui no dicionario
    if request.method == "POST":
        dicionario ['nome'] = request.POST.get("InputNome")
        dicionario ["idade"] = request.POST.get("InputIdade")
        return render(request, "index.html", dicionario)

    if request.method == "GET":
        return render (request, "index.html", dicionario)


def atividade(request):
    dic = {
        "numero": None,
        "tabuada":[]
    }

    if request.method == "POST":

        dic ["numero"] = request.POST.get("InputNumero")
        numero = request.POST.get("InputNumero")

        if numero:
             numero = int(numero)

        for i in range(0,11):
                valor = numero * i
                dic["tabuada"].append(valor)
                i+=1

        return render(request, "atividade.html", dic)

    if request.method == "GET":
        return render(request, "atividade.html", dic)

