from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404 
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from datetime import datetime
from forms import *
from models import *


"""
# El shortcut render_to_response equivale a todo esto
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
"""

def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.all()
	template = "index.html"

	#diccionario = {"categorias" : categorias, "enlaces" : enlaces}
	return render_to_response(template, locals())

def categoria(request, id_categoria):
	categorias = Categoria.objects.all()

	#sino existe la categoria
	cat = get_object_or_404(Categoria, pk = id_categoria)

	#este no evalua si existe o no
	#cat = Categoria.objects.get(pk = id_categoria)
	
	enlaces = Enlace.objects.filter(categoria = cat)
	template = "index.html"

	return render_to_response(template, locals())

@login_required
def add(request):
	if request.method == "POST":
		form = EnlaceForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
	else:
		form = EnlaceForm()

	template = "form.html"
	return render_to_response(template, 
					context_instance = RequestContext(request, locals()))

@login_required
def plus(request, id_enlace):
	enlace = Enlace.objects.get(pk = id_enlace)
	enlace.votos = enlace.votos + 1
	enlace.save()

	return HttpResponseRedirect("/")

@login_required
def minus(request, id_enlace):
	enlace = Enlace.objects.get(pk = id_enlace)
	enlace.votos = enlace.votos - 1
	enlace.save()

	return HttpResponseRedirect("/")

# Create your views here.
def hora_actual(request):
	""" Modo sin shortcut
	ahora = datetime.now()
	t = get_template("hora.html")
	c = Context({"hora":ahora,"usuario":"Freddier"})
	html = t.render(c)
	return HttpResponse(html)
	"""
	# Modo con shortcut
	now = datetime.now()
	return render_to_response('hora.html', {'hora':now, 'usuario':'Freddier'})