from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Hudud, Fuqoro, Qarindosh, Jinoyatchi,Safarda
from django.db.models import Q
from django.views.generic import DetailView
def home(request):
    hududlar = Hudud.objects.all()
    return render(request, 'home.html', {'hududlar': hududlar})

def fuqoro(request, hudud_id):
    hudud = Hudud.objects.get(pk=hudud_id)
    fuqorolar = Fuqoro.objects.filter(hudud=hudud)
    return render(request, 'fuqoro.html', {'hudud': hudud, 'fuqorolar': fuqorolar})

def detail(request, fuqoro_id):
    fuqoro = Fuqoro.objects.get(pk=fuqoro_id)
    qarindoshlar = Qarindosh.objects.filter(bogliq=fuqoro)
    jinoyatchilar = Jinoyatchi.objects.filter(hudud=fuqoro.hudud)
    return render(request, 'detail.html', {'fuqoro': fuqoro, 'qarindoshlar': qarindoshlar, 'jinoyatchilar': jinoyatchilar})

class QarindoshDetail(DetailView):
    model = Qarindosh
    def get(self, request, pk):
        clay={}
        clay['temp']=Qarindosh.objects.filter(id=pk)
        return render(request, 'qarindosh_detail.html', clay)

class JinoyatchiDetail(DetailView):
    model = Jinoyatchi
    def get(self, request, pk):
        clay={}
        clay['temp']=Qarindosh.objects.filter(id=pk)
        return render(request, 'qarindosh_detail.html', clay)



def search_fuqoro(request):
    query = request.GET.get('q')
    fuqorolar = Fuqoro.objects.filter(Ismi__icontains=query)
    return render(request, 'fuqoro.html', {'fuqorolar': fuqorolar})

from datetime import datetime

def check_time(request):
    if request.method == 'POST':
        vaqti_str = request.POST.get('vaqti')
        vaqti = datetime.strptime(vaqti_str, '%Y-%m-%dT%H:%M')  # Convert string to datetime
        current_time = datetime.now()
        if vaqti > current_time:
            shaxs_info = Safarda.objects.get(Vaqti=vaqti).Fuqoro
            return render(request, 'detail.html', {'shaxs_info': shaxs_info})
        else:
            return render(request, 'details.html', {'message': 'Entered time is not greater than current time'})
    return render(request, 'detail.html')

