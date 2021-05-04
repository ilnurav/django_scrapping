from django.shortcuts import render
import datetime
from django.http import HttpResponse


def home(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    date = {'date': date, 'name': name}
    return render(request, 'home.html', date)


def products(request, productid=21):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id=1, name='Bob'):
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)