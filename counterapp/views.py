from django.shortcuts import redirect, render
from . import models

# Create your views here.


def home(request):
    obj = models.CounterModel.objects.filter(id=1)[0]
    result = obj.num
    return render(request, 'home.html', {'result': result})


def increment(request):
    obj = models.CounterModel.objects.filter(id=1)[0]
    obj.num = int(obj.num)+1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])


def decrement(request):
    obj = models.CounterModel.objects.filter(id=1)[0]
    obj.num = int(obj.num)-1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])


def reset(request):
    obj = models.CounterModel.objects.filter(id=1)[0]
    obj.num = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])
