from rest_framework import serializers
from .models import Curso, Week, Unit, Lesson, Inicio, Horario
import simplejson
import json



class CursorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'name', 'image', 'description_short','description_long','price']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'unit_name']


class WeekSerializer(serializers.ModelSerializer):
    #curso_id=CursorSerializer(many=False, read_only=True)
    #unid_id=UnitSerializer(many=False, read_only=True)
    class Meta:
        model = Week
        fields = ['id', 'week_name', 'curso_id', 'unid_id']


class CursoWeekSerializar(serializers.ModelSerializer):
    semanas = serializers.SerializerMethodField()
    inicio=serializers.SerializerMethodField()
    def get_inicio(self, obj):
        try:
            ult_inicio=Inicio.objects.filter(curso_id__id=obj.id).order_by('starting_date').last()
            
            horarios=Horario.objects.filter(inicio_id__id=ult_inicio.id)
            lista_horario=[]
            for horario in horarios:
                dic_horario={
                    'frequency':horario.frequency,
                    'schedule':horario.schedule
                }
                lista_horario.append(dic_horario)
            dic_inicio={
                'id':ult_inicio.id,
                'starting_date':str(ult_inicio.starting_date),
                'horario':lista_horario
            }
            #Convierto la lista en un tipo string
            inicio_str=json.dumps(dic_inicio)
            #Deserializar un String 
            inicio_json=json.loads(inicio_str)
            return inicio_json
        except:
            return {
                'falta ingresar dato'
            }

    def get_semanas(self, obj):
        try:
            #Filtrar mediante un campo relacionado
            obj_unidades= Week.objects.filter(curso_id__id=obj.id).values('unid_id')
            
            lista_id_unidades=[]
            for obj_unid in obj_unidades:
                if obj_unid['unid_id'] not in lista_id_unidades:
                    lista_id_unidades.append(obj_unid['unid_id'])
            unidades=Unit.objects.filter(id__in=lista_id_unidades)
             
            lista_resultado=[]
            for unidad in unidades:
                semanas= Week.objects.filter(curso_id__id=obj.id,unid_id__id=unidad.id)
                lista_sem=[]
                for sem in semanas:
                    lista_lesson=[]
                    lecciones=Lesson.objects.filter(week_id__id=sem.id)
                    for leccion in lecciones:
                        lista_lesson.append(leccion.Lesson_name)
                    dic_sem={
                        'id':sem.id,
                        'tema':sem.week_name,
                        'sub-tema':lista_lesson
                    }
                    lista_sem.append(dic_sem)
                dic_unidad={
                    'id':unidad.id,
                    'unit_name':unidad.unit_name,
                    'plan de estudio':lista_sem
                }
                lista_resultado.append(dic_unidad)
            #Convierto la lista en un tipo string
            resultado_str=json.dumps(lista_resultado)
            #Deserializar un String 
            resultado_json=json.loads(resultado_str)
            return resultado_json
        except:
            return {
                'semana': 'no hay dato'
            }

    class Meta:
        model = Curso
        fields = ['id', 'name', 'image', 'description_short','description_long','price','inicio','semanas']
