from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [
    path('api/', include('model.api.urls')),
    path('', include('model.urls')),
    path('models/', views.models, name='models'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('order/', views.order_form, name='order_form'),
    path('make-order/', views.MakeOrderView.as_view(), name='make-order')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
