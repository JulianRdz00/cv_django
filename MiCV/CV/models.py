from django.db import models


class curriculum(models.Model):
	foto = models.ImageField(upload_to="fotos", null=True)
	nombre = models.CharField(max_length=50)
	nacimiento = models.CharField(max_length=10)
	celular = models.CharField(max_length=15)
	email = models.CharField(max_length=50)
	perfil = models.TextField()
	conocimientos = models.TextField()
	experiencia_laboral = models.TextField()
	objetivos = models.TextField()
	nivel_académico = (
	    ('Primario incompleto', 'Primario incompleto'),
	    ('Primario en curso', 'Primario en curso'),
	    ('Primario terminado', 'Primario terminado'),
	    ('Secundario incompleto', 'Secundario incompleto'),
	    ('Secundario en curso', 'Secundario en curso'),
	    ('Secundario terminado', 'Secundario terminado'),
	    ('Terciario incompleto', 'Terciario incompleto'),
	    ('Terciario en curso', 'Terciario en curso'),
	    ('Terciario terminado', 'Terciario terminado'),
	    ('Universitario incompleto', 'Universitario incompleto'),
	    ('Universitario en curso', 'Universitario en curso'),
	    ('Universitario terminado', 'Universitario terminado'), 
	)
	formacion_académica = models.CharField(max_length=100, choices=nivel_académico, null=True)
	carrera_e_institucion = models.CharField(max_length=50, null=True)
	años_cursados = (
		('1er año', '1er año'),
		('2do año', '2do año'),
		('3er año', '3er año'),
		('4to año', '4to año'),
		('5to año', '5to año'),
		('6to año', '6to año'),
		('7mo año', '7mo año'),
		('8vo año', '8vo año'),
		('9no año', '9no año'),
		('10mo año', '10mo año'),
	)
	año_en_curso = models.CharField(max_length=100, choices=años_cursados, null=True)
	hobbies = models.TextField(null=True)

	def __str__(self):
		return self.nombre