from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

class RedeSocial(models.Model):
    redes_disponiveis = (("0","Instagram"),("1","twitter"),("2","Facebook"))
    rede = models.CharField("Rede social",max_length=50,choices=redes_disponiveis)
    tipo = models.CharField("codigo da rede",max_length=150,null=True,blank=True,editable=False)
    link = models.CharField("Link do perfil",max_length=1500,blank=True,null=True)

    def save(self, *args, **kwargs):
        tipos = ["fab fa-instagram","fab fa-twitter","fab fa-facebook-square"]
        self.tipo = tipos[int(self.rede)]
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.redes_disponiveis[int(self.rede)][1]

class Cargo(models.Model):
    tipo = models.CharField("Cargo",max_length=50)

    def __str__(self):
        return self.tipo

class Usuario(models.Model):
    nome = models.CharField("Nome do usuario",max_length=150)
    bio = models.CharField("Biografia",max_length=1500, null=True, blank=True)
    perfil = models.CharField("Imagem para o perfil",max_length=15000, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cargos = models.ManyToManyField(Cargo, blank=True)
    redes = models.ManyToManyField(RedeSocial)

    def __str__(self):
        return self.nome

class Publicacao(models.Model):
    capa = models.CharField("Capa da publicação",max_length=15000,null=True,blank=True)
    titulo = models.CharField("Titulo da publicação",max_length=500)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    corpo = models.TextField("Corpo da Publicação", max_length=15000)
    titulo_secao1 = models.CharField("Titulo da Seção 1",max_length=500,null=True,blank=True)
    secao1 = models.TextField("Corpo da Seção 1", max_length=15000,null=True,blank=True)
    capa_secao1 = models.CharField("Imagem da Seção 1",max_length=15000,null=True,blank=True)
    titulo_secao2 = models.CharField("Titulo da Seção 2",max_length=500,null=True,blank=True)
    secao2 = models.TextField("Corpo da Seção 2", max_length=15000,null=True,blank=True)
    capa_secao2 = models.CharField("Imagem da Seção 2",max_length=15000,null=True,blank=True)
    data_publicacao = models.DateField("Data de Publicação",null=True,blank=True)
    referencias = models.TextField("Referências", max_length=15000,null=True,blank=True)
    tipos_status = (("0","editando"),("1","revisão"),("2","publicado"))
    status = models.CharField("Status da Publicação",max_length=20,choices=tipos_status, default=tipos_status[0][1])

    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"
    
    def __str__(self):
        return self.titulo