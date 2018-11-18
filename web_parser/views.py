from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import LoginForm
from django.views import View

@login_required()
def index(request):
    template = 'index.html'
    return render(request, template)

class Login(View):

    def get(self, request):
        error = ''
        form = LoginForm
        return render(request, "login.html", {'error': error, 'form': form})


    def post(self, request):
        form = LoginForm(request.POST or None)
        username = request.POST['username']
        password = request.POST['password']
        if username == 'Android':
            error = 'Доступ запрещен!'
            context = {
                'error': error,
                'form': form,
            }
            return render(request, "login.html", context)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = 'Аккаунт не активирован!'
                context = {
                    'error': error,
                    'form': form,
                }
                return render(request, "login.html", context)

        else:
            error = 'Неправильный логин или пароль'
            context = {
                'error': error,
                'form': form,
            }
            return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
