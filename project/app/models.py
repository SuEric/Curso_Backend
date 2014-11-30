from django.db import models

# Create your models here.
class Categoria(models.Model):
	titulo = models.CharField(max_length = 140)

	def __unicode__(self):
		return self.titulo

class Enlace(models.Model):
	titulo = models.CharField(max_length = 140)
	enlace = models.URLField()
	votos = models.IntegerField(default=0)
	categoria = models.ForeignKey(Categoria)

	def __unicode__(self):
		return "%s - %s" % (self.enlace, self.titulo)