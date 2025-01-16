from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
  nome = models.CharField(max_length=200, null=True, blank=True)
  email = models.CharField(max_length=200, null=True, blank=True)
  telefone = models.CharField(max_length=200, null=True, blank=True)
  id_sessao = models.CharField(max_length=200, null=True, blank=True)
  usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

