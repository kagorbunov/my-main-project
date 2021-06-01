from django.db import transaction
from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import OrderForm

# Create your views here.


def index(request):
    # allmodels = Diod.objects.all()
    data = {
        'title': 'Схемотехнические (SPICE) модели',
        'values': ['diod', 'Multimetr', '1000'],
        'linkhost': 'http://127.0.0.1:8000'
    }
    return render(request, 'main/index.html', data)


def models(request):
    data = {

    }
    return render(request, 'main/models.html', data)


def about(request):
    data = {
        'titleAbout': 'Информация про нас!'
    }
    return render(request, 'main/about.html', data)


def order_form(request):
    form = OrderForm(request.POST or None)
    data = {
        'titleOrder': 'Заказать модель',
        'form': form
    }
    return render(request, 'main/order_form.html', data)


def contacts(request):
    data = {
        'titleContacts': 'Контакты!'
    }
    return render(request, 'main/сontacts.html', data)


class MakeOrderView(View):

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.name = form.cleaned_data['name']
            new_order.email = form.cleaned_data['email']
            new_order.phonenumber = form.cleaned_data['phonenumber']
            new_order.description = form.cleaned_data['description']
            new_order.save()
            messages.add_message(request, messages.INFO, 'Спасибо за заказ! С вами свяжутся')
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/order/')

