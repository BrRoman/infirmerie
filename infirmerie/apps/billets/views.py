from django.shortcuts import render


def list(request):
    return render(request, 'billets/list.html')


def create(request):
    return render(request, 'billets/form.html')


def detail(request):
    return render(request, 'billets/detail.html')


def update(request):
    return render(request, 'billets/form.html')
