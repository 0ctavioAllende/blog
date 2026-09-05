from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'publicado')
    search_fields = ('titulo', 'contenido')
    list_filter = ('publicado',)
