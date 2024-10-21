from django.contrib import admin
from .models import AlumnoT,Frase
# Register your models here.


class ComentarioInLine(admin.TabularInline):
    model=Frase
    extra=1
    
class AlumnoAdmin(admin.ModelAdmin):
    fields=["apaterno","amaterno","nombre","fecha_nacimiento","fecha_ingreso"]
    list_display=["apaterno","amaterno","nombre"]
    inlines=[ComentarioInLine]

admin.site.register(AlumnoT,AlumnoAdmin)

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    fields=["comentario","alumno_fk"]
    list_display=["comentario"]