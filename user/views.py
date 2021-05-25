from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic


# def home(request):

#     return render(request, template_name='index.html')


def login_(request):
    next = request.GET.get('next', '')
    if request.method == 'POST':
        email = request.POST['email']
        user = authenticate(request, email=email)

        if user is not None:
            print(user)
            login(request, user)
            if next:
                return redirect(next)
            else:
                return redirect('/')

    return render(request, template_name='user/login.html')
