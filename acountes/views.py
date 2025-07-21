from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)


            if user.is_authenticated:
                if user.role == 'formateur':
                    return redirect('dach_formater')
                elif user.role == 'administration':
                    return redirect('adinistration_dach')
                elif user.role == 'admin':
                    return redirect('admin:index')


            messages.error(request, 'Rôle utilisateur non autorisé.')
            return redirect('login')

        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')

    return render(request, 'acountes/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
