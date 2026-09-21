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




def calculadora(request):
     dic = {
          "numero1": None,
          "numero2": None,
          "operador": None,
          "resultado": None
     }

     if request.method == "POST":
        dic["numero1"] = request.POST.get("numero1")
        dic["numero2"] = request.POST.get("numero2")
        dic["operador"] = request.POST.get("operador")

        if dic["operador"] == 'soma':
            dic["resultado"] = (int(dic["numero1"]) + int(dic["numero2"]))

        elif dic["operador"] == 'subtracao':
            dic["resultado"] = (int(dic["numero1"]) - int(dic["numero2"]))

        elif dic["operador"] == 'divisao':
            dic["resultado"] = (int(dic["numero1"]) / int(dic["numero2"]))

        elif dic["operador"] == 'multiplicacao':
            dic["resultado"] = (int(dic["numero1"]) * int(dic["numero2"]))

        return render(request, "calculadora.html", dic)

     if request.method == "GET":
          return render(request, "calculadora.html", dic)

