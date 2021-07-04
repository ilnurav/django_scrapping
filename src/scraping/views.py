from django.shortcuts import render
import datetime
# from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from .models import City


def home(request):
    date = datetime.datetime.now().date()
    name = request.session['member_id']
    date = {'date': date, 'name': name}
    return render(request, 'home.html', date)


def products(request, productid=21):
    output = "<h2>Product <br> № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id=1, name='Bob'):
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)


def products2(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Product № {0}  Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users2(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    del request.session['member_id']
    return HttpResponse(output)


def about(request):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def m304(request):
    return HttpResponseNotModified()


def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")


def m403(request):
    return HttpResponseForbidden("<h2>Forbidden</h2>")


def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")


def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")


def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")


def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")


# получение данных из бд
def index(request, id=00):
    citys = City.objects.all()
    #citys = City.objects.filter().first()
    request.session['member_id'] = 'Вы авторизованы'
    if id != 00:
        print(id)
    return render(request, "index.html", {"citys": citys, "id": id})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        city = City()
        city.name = request.POST.get("city")
        city.save()
        #print(city.id)

    return HttpResponseRedirect("/index/" + str(city.id))
        #date = {'id': city.id}
    #return render(request, "index.html", date)

def login(request):
    #try:
        '''
        m = Member.objects.get(username__exact=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponse("Вы авторизованы.")
    except Member.DoesNotExist:
        return HttpResponse("Ваши логин и пароль не соответствуют.")
        '''

