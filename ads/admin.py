from django.contrib import admin
from .models import Ad

# Register your models here.
class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created', 'postdate', 'posttime', 'category', 'text')

admin.site.register(Ad, AdAdmin)