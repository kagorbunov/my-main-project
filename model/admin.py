from django.contrib import admin

from .models import  ModelTxt, Type, EnviromentalCondition, Diod, TransistorBP, TransistorPOLEV, TechologyTask,Order

# ModelTxtOnline

# class modAdmin(admin.ModelAdmin):
#     list_display_model = {'title','function','basicModel','structure','body'}

admin.site.register(ModelTxt)
admin.site.register(TechologyTask)
admin.site.register(Type)
admin.site.register(EnviromentalCondition)
admin.site.register(Diod)
admin.site.register(Order)
admin.site.register(TransistorBP)
admin.site.register(TransistorPOLEV)
# admin.site.register(ModelTxtOnline)
# Register your models here.
