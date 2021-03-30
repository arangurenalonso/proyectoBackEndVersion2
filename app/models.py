from django.db import models
 
# Create your models here.
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.FileField()
    description_short = models.TextField()
    description_long = models.TextField()
    state = models.BooleanField(default=True)
    available = models.BooleanField(default=False)
    price = models.FloatField()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.name

class Inicio(models.Model):
    id = models.AutoField(primary_key=True)
    starting_date = models.DateField(max_length=200)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Inicio'
        verbose_name_plural = 'Inicios'

    def __str__(self):
        return str(self.starting_date)

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    frequency=models.CharField(max_length=200)
    schedule=models.CharField(max_length=200)
    inicio_id = models.ForeignKey(Inicio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return self.frequency

class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    unit_name=models.CharField(max_length=200)
    

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return self.unit_name

class Week(models.Model):
    id = models.AutoField(primary_key=True)
    week_name=models.CharField(max_length=200)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    unid_id = models.ForeignKey(Unit, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Semana'
        verbose_name_plural = 'Semanas'

    def __str__(self):
        return self.week_name

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    Lesson_name=models.CharField(max_length=200)
    week_id = models.ForeignKey(Week, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Leccion'
        verbose_name_plural = 'Lecciones'

    def __str__(self):
        return self.Lesson_name

