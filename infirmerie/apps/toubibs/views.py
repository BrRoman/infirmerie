from django.shortcuts import render


def list(request):
    return render(request, 'toubibs/list.html')


def create(request):
    return render(request, 'toubibs/form.html')


def detail(request):
    return render(request, 'toubibs/detail.html')


def update(request):
    return render(request, 'toubibs/form.html')
