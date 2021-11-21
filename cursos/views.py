import math
from videos.models import Videos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from .models import Cursos

@login_required(login_url='accounts:login')
def cursos(request):

    cursos = Cursos.objects.all()
    template_name = 'cursos.html'
    context = {
        'cursos': cursos,
    }
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def details(request, slug):

    curso = get_object_or_404(Cursos,slug=slug)
    cursos = Cursos.objects.all()
    context = {
        'curso': curso,
        'cursos': cursos,
    }
    template_name = 'details_cursos.html'
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def videos_por_cursos(request, id):

    duration = 0

    curso = Cursos.objects.filter(id=id)
    videos = Videos.objects.filter(curso=id)
    segundos = Videos.objects.filter(curso=id).values('segundos')

    for i in range(videos.count()):
        duration += segundos[i]['segundos']

    if duration >= 3600:
        fracao_minutos = (duration / 3600) - int(duration / 3600)
        calc_horas = duration / 3600
        calc_minutos = int(fracao_minutos * 60)
        fracao_segundos = calc_minutos - int(calc_minutos)
        calc_segundos = fracao_segundos * 60
    else:
        calc_horas = 00
        fracao_segundos = (duration / 60) - int(duration / 60)
        calc_minutos = duration / 60
        calc_segundos = fracao_segundos * 60
    
    template_name = 'videos_por_cursos.html'
    context = {
        'videos': videos,
        'cursos': curso,
        'horas': int(calc_horas),
        'minutos': int(calc_minutos),
        'segundos': math.ceil(calc_segundos),
        'qtd_videos': videos.count()
    }
    return render(request, template_name, context)