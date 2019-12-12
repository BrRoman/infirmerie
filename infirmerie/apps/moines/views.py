from django.shortcuts import render


def list(request):
    return render(request, 'moines/list.html')


def create(request):
    return render(request, 'moines/form.html')


def detail(request):
    return render(request, 'moines/detail.html')


def update(request):
    return render(request, 'moines/form.html')
