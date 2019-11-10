from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, Djnago!!")

# 以下、追記

def call_template(request):

    template_name = "hello1.html"
    context = {'param1': 'これはパラメータです。'}
    return render(request, template_name, context)