from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.shortcuts import render
from principal.mysql_config import conecta_no_banco_de_dados
from .forms import ContatoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.contrib import messages


def index(request):
     return render(request, 'index.html')
# Create your views here.

def template(request):
    return render(request, 'templates/template.html')

def sobre(request):
    if not request.session.get('usuario_id'):
            return redirect('login')
    else:
        return render(request, 'Sobre/sobre.html')




def pedido(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            try:
                # Estabelecer conexão com o banco de dados
                oracle = conecta_no_banco_de_dados()

                # Preparar consulta SQL e valores
                nome = form.cleaned_data['nome']
                email = form.cleaned_data['email']
                mensagem = form.cleaned_data['mensagem']
                sql = "INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)"
                values = (nome, email, mensagem)

                # Executar consulta SQL e confirmar alterações
                cursor = oracle.cursor()
                cursor.execute(sql, values)
                oracle.commit()

                # Mensagem de sucesso e redirecionamento
                print(f"Dados do formulário salvos com sucesso!")
                return HttpResponseRedirect('/')

            except Exception as err:
                # Manipular erros de banco de dados
                print(f"Erro ao salvar dados no banco de dados: {err}")
                mensagem_erro = "Ocorreu um erro ao processar o seu contato. Tente novamente mais tarde."
                return render(request, 'erro.html', mensagem_erro=mensagem_erro), 500

            finally:
                # Fechar conexão com o banco de dados se estiver aberta
                if oracle is not None:
                    oracle.close()

        else:
            # Manipular dados de formulário inválidos
            return render(request, 'pedido.html', {'form': form})

    else:
        # Renderizar formulário vazio
        form = ContatoForm()
        return render(request, 'pedido.html', {'form': form})
    