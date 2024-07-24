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
