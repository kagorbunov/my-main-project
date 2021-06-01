from django.urls import path

from . import views

urlpatterns = [
    path('models_home', views.models_home, name='models_home'),
    path('trans_pole/', views.model_pole, name='model_pole'),
    path('trans_bipol/', views.model_bipol, name='model_bipol'),
    path('trans_diod/', views.model_diod, name='model_diod'),
    path('', views.main_page, name='home'),

]
