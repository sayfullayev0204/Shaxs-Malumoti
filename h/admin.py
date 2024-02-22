from django.contrib import admin

# Register your models here.
from .models import Fuqoro,Hudud,Jinoyatchi,Qarindosh,Safarda
admin.site.register(Hudud)
admin.site.register(Fuqoro)
admin.site.register(Jinoyatchi)
admin.site.register(Qarindosh)
admin.site.register(Safarda)