from django.contrib import admin
from .models import *

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(ItemEstoque)
admin.site.register(Pedido)
admin.site.register(ItensPedido)
admin.site.register(Endereco)
admin.site.register(Cliente)

# Register your models here.
