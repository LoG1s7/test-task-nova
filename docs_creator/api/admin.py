from django.contrib import admin

from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    """Админка файлов"""

    list_display = ["id", "name", "data"]
