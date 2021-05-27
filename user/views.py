from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_(request):
    next = request.GET.get('next', '')
    if request.method == 'POST':
        email = request.POST['email']
        user = authenticate(request, email=email)

        if user is not None:

            login(request, user)
            if next:
                return redirect(next)
            else:
                return redirect('/')

    return render(request, template_name='user/login.html')


def logout_(request):
    logout(request)
    return redirect('/')
