from django.contrib import admin
from django.urls import path
from .views import home, download, avaliacao, equipe, publicacao, publicacoes
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',home,name="home"),
    path('download',download,name="download"),
    path('avaliacao',avaliacao,name="avaliacao"),
    path('equipe',equipe,name="equipe"),
    path('publicacao/<int:id>',publicacao,name="publicacao"),
    path('publicacoes',publicacoes,name="publicacoes"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
