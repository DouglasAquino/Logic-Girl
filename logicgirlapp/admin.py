from django.contrib import admin
from .models import Usuario, Publicacao, Cargo, RedeSocial

admin.site.register(Usuario)
admin.site.register(Publicacao)
admin.site.register(Cargo)
admin.site.register(RedeSocial)