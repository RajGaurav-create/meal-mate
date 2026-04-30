from django.contrib import admin

# Register your models here.
from .models import user,Restaurant,Item
from .models import Cart

admin.site.register(user)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Cart)