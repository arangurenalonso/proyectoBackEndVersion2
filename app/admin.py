from django.contrib import admin
from .models import Curso, Inicio, Horario, Unit, Week, Lesson
# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price','available']


@admin.register(Inicio)
class InicioAdmin(admin.ModelAdmin):
    list_display = ['starting_date', 'curso_id']


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ['frequency', 'schedule', 'inicio_id']


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['unit_name']


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ['week_name', 'unid_id','curso_id']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['Lesson_name', 'week_id']

