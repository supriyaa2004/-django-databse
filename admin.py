from django.contrib import admin
from .models import book

@admin.register(book)
class bookAdmin(admin.ModelAdmin):
    list_display = ('name', 'email' , 'tittle' , 'publisher' , 'year' , 'status' , 'roll')
