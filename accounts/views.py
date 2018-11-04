from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        # logic
        return
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        # logic
        return
    else:
        return render(request, 'accounts/register.html')


def logout():
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
