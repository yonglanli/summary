from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse(u"欢迎光临!")


def system_manage(request):
    print("进入")
    return render(request, 'system/system_manage.html')