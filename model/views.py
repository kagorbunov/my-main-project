from django.shortcuts import render

from .models import TransistorPOLEV, ModelTxt, TransistorBP, Diod


def models_home(request):
    mymodel = Diod.objects.all()
    LinkOnModel = ModelTxt.objects.all()

    return render(request, 'model/model_home.html', {
        'mymodel': mymodel,
        'link': LinkOnModel,
        'title': 'Схемотехнические (SPICE) модели',
        'values': ['diod', 'Multimetr', '1000']
    })


def model_pole(request):
    mymodel = TransistorPOLEV.objects.all()
    LinkOnModel = ModelTxt.objects.all()

    return render(request, 'model/model_pole.html', {
        'mymodel': mymodel,
        'link': LinkOnModel,
        'linkhost': 'http://127.0.0.1:8000'
    })


def model_bipol(request):
    mymodel = TransistorBP.objects.all()
    LinkOnModel = ModelTxt.objects.all()

    return render(request, 'model/model_bipol.html', {
        'mymodel': mymodel,
        'link': LinkOnModel,
        'linkhost': 'http://127.0.0.1:8000'
    })


def model_diod(request):
    mymodel = Diod.objects.all()
    LinkOnModel = ModelTxt.objects.all()

    return render(request, 'model/model_diod.html', {
        'mymodel': mymodel,
        'link': LinkOnModel,
        'linkhost': 'http://127.0.0.1:8000'
    })


def main_page(request):
    diod = Diod.objects.all()
    bp = TransistorBP.objects.all()
    polev = TransistorPOLEV.objects.all()
    LinkOnModel = ModelTxt.objects.all()
    return render(request, 'main/index.html', {
        'diod': diod,
        'bp': bp,
        'polev': polev,
        'link': LinkOnModel,
        'title': 'Схемотехнические (SPICE) модели',
        'linkhost': 'http://127.0.0.1:8000'
    })
