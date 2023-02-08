from django.urls import path, re_path

from . import views

app_name = 'videos'

urlpatterns = [
    path('', views.videos, name='index'),
    path('<slug:slug>', views.details, name='details'),
    path('<int:id>/<slug:slug>', views.details, name='details'),
    re_path(r'^<int:id>/(?P<title>[\w\-]+)/$', views.video_assistido, name='video_assistido')
]
